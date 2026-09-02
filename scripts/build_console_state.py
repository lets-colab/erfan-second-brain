#!/usr/bin/env python3
"""Extract the repository's live state for the DR.X Console.

Reads the repository's own contract files and emits a single state document that
the console renders. The console authors no data of its own: every figure it
displays originates here and names the file it came from.

Stdlib only, matching the other scripts in this directory and the CI workflow,
which provisions Python without installing dependencies.

Usage:
    python3 scripts/build_console_state.py            # write console/state.{json,js}
    python3 scripts/build_console_state.py --check    # verify on-disk state is current
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "console"

# Proof states, in the order the console displays them. Exhaustive: every value
# the console renders resolves to exactly one of these.
STATES = ("proven", "partial", "unproven", "failed", "stale")

# Raw status vocabulary used across the evaluation contracts, mapped onto the
# console's proof-state axis. Unrecognized values fall back to "unproven" and are
# reported, so a new status word surfaces rather than being silently absorbed.
STATUS_MAP = {
    "pass": "proven",
    "passed": "proven",
    "verified": "proven",
    "complete": "proven",
    "partial": "partial",
    "in_progress": "partial",
    "not_run": "unproven",
    "pending": "unproven",
    "fail": "failed",
    "failed": "failed",
    "blocked": "failed",
    "stale": "stale",
    "invalidated": "stale",
}

UNKNOWN_STATUSES: set[str] = set()


# --------------------------------------------------------------------------
# Minimal YAML subset reader
# --------------------------------------------------------------------------
# Handles the shapes actually present in evaluations/*.yaml: nested block
# mappings, block sequences of scalars and of mappings, inline empty lists,
# quoted scalars, folded block scalars (>- and |-), and comments. It is not a
# general YAML implementation; it raises on input it does not understand rather
# than guessing, so a contract file that outgrows it fails loudly.


def _scalar(raw: str):
    text = raw.strip()
    if not text:
        return ""
    if text[0] in "\"'" and text[-1] == text[0] and len(text) >= 2:
        return text[1:-1]
    if text in ("[]", "{}"):
        return [] if text == "[]" else {}
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        return [_scalar(p) for p in inner.split(",")] if inner else []
    low = text.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "~", "none"):
        return None
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    return text


def _strip_comment(line: str) -> str:
    out, quote = [], None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            out.append(ch)
            continue
        if ch == "#":
            break
        out.append(ch)
    return "".join(out).rstrip()


def _lines(text: str):
    result = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = _strip_comment(raw)
        if not stripped.strip():
            continue
        result.append((len(stripped) - len(stripped.lstrip(" ")), stripped.strip()))
    return result


def _parse_block(rows, idx, indent):
    """Parse one block at the given indent. Returns (value, next_index)."""
    if idx >= len(rows):
        return None, idx

    if rows[idx][1].startswith("- "):
        items = []
        while idx < len(rows) and rows[idx][0] == indent and rows[idx][1].startswith("- "):
            body = rows[idx][1][2:].strip()
            if ":" in body and not body.startswith(("\"", "'")):
                # Sequence of mappings: re-read the item's first key inline, then
                # continue with any deeper keys belonging to the same item.
                key, _, rest = body.partition(":")
                item = {}
                child_indent = indent + 2
                if rest.strip():
                    item[key.strip()] = _scalar(rest)
                    idx += 1
                else:
                    idx += 1
                    value, idx = _parse_block(rows, idx, child_indent)
                    item[key.strip()] = value
                while idx < len(rows) and rows[idx][0] >= child_indent and not rows[idx][1].startswith("- "):
                    sub, idx = _parse_mapping_entry(rows, idx, child_indent)
                    item.update(sub)
                items.append(item)
            else:
                items.append(_scalar(body))
                idx += 1
        return items, idx

    mapping = {}
    while idx < len(rows) and rows[idx][0] == indent:
        entry, idx = _parse_mapping_entry(rows, idx, indent)
        mapping.update(entry)
    return mapping, idx


def _parse_mapping_entry(rows, idx, indent):
    _, content = rows[idx]
    if ":" not in content:
        raise ValueError(f"unsupported YAML line: {content!r}")
    key, _, rest = content.partition(":")
    key = key.strip()
    rest = rest.strip()
    idx += 1

    if rest in (">-", ">", "|", "|-"):
        parts = []
        while idx < len(rows) and rows[idx][0] > indent:
            parts.append(rows[idx][1])
            idx += 1
        joined = " ".join(parts) if rest.startswith(">") else "\n".join(parts)
        return {key: joined}, idx

    if rest:
        return {key: _scalar(rest)}, idx

    if idx < len(rows) and rows[idx][0] > indent:
        value, idx = _parse_block(rows, idx, rows[idx][0])
        return {key: value}, idx

    return {key: None}, idx


def read_yaml(path: Path) -> dict:
    rows = _lines(path.read_text(encoding="utf-8"))
    if not rows:
        return {}
    value, _ = _parse_block(rows, 0, rows[0][0])
    return value if isinstance(value, dict) else {"_root": value}


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def map_status(raw) -> str:
    if raw is None:
        return "unproven"
    key = str(raw).strip().lower()
    mapped = STATUS_MAP.get(key)
    if mapped is None:
        UNKNOWN_STATUSES.add(key)
        return "unproven"
    return mapped


def tally(values) -> dict:
    counts = {state: 0 for state in STATES}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


# --------------------------------------------------------------------------
# Collectors
# --------------------------------------------------------------------------


def collect_repo() -> dict:
    return {
        "commit": git("rev-parse", "HEAD"),
        "short": git("rev-parse", "--short", "HEAD"),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "committed_at": git("log", "-1", "--format=%cI"),
        "subject": git("log", "-1", "--format=%s"),
        "dirty": bool(git("status", "--porcelain")),
    }


def collect_verification() -> dict:
    script = ROOT / "scripts" / "verify_second_brain.py"
    if not script.exists():
        return {"state": "unproven", "summary": "verify_second_brain.py not present", "source": None}
    proc = subprocess.run(
        [sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True
    )
    output = (proc.stdout + proc.stderr).strip()
    warnings = 0
    match = re.search(r"(\d+)\s+warning", output)
    if match:
        warnings = int(match.group(1))
    if proc.returncode != 0:
        state = "failed"
    elif warnings:
        state = "partial"
    else:
        state = "proven"
    return {
        "state": state,
        "summary": output.splitlines()[0] if output else "no output",
        "warnings": warnings,
        "exit_code": proc.returncode,
        "source": rel(script),
    }


def collect_acceptance() -> dict:
    tests_path = ROOT / "evaluations" / "acceptance-tests.yaml"
    evidence_path = ROOT / "evaluations" / "acceptance-evidence.yaml"
    contract = read_yaml(tests_path) if tests_path.exists() else {}
    evidence = read_yaml(evidence_path) if evidence_path.exists() else {}

    results = evidence.get("results") or {}
    suite = evidence.get("suite_state") or {}
    items = []

    for test in contract.get("tests") or []:
        if not isinstance(test, dict):
            continue
        test_id = test.get("id")
        record = results.get(test_id) or {}
        raw_status = record.get("status") if isinstance(record, dict) else None
        state = map_status(raw_status)
        ev = record.get("evidence") if isinstance(record, dict) else None
        invalidated = bool(isinstance(record, dict) and record.get("invalidated_evidence"))
        # Evidence that predates a material change is stale, not merely absent.
        if invalidated and state == "unproven":
            state = "stale"
        items.append(
            {
                "id": test_id,
                "critical": bool(test.get("critical")),
                "objective": test.get("objective") or "",
                "raw_status": raw_status if raw_status is not None else "not recorded",
                "state": state,
                "evidence_count": len(ev) if isinstance(ev, list) else 0,
                "invalidated": invalidated,
            }
        )

    # A test named in evidence but absent from the contract is still real state.
    known = {item["id"] for item in items}
    for test_id, record in results.items():
        if test_id in known:
            continue
        raw_status = record.get("status") if isinstance(record, dict) else None
        items.append(
            {
                "id": test_id,
                "critical": False,
                "objective": "",
                "raw_status": raw_status if raw_status is not None else "not recorded",
                "state": map_status(raw_status),
                "evidence_count": 0,
                "invalidated": False,
                "note": "present in evidence, absent from acceptance-tests.yaml",
            }
        )

    critical = [i for i in items if i["critical"]]
    return {
        "production_certified": bool(suite.get("production_certified")),
        "human_owner_signoff": bool(suite.get("human_owner_signoff")),
        "reason": suite.get("reason") or "",
        "release_gate": contract.get("release_gate") or "",
        "total": len(items),
        "critical_total": len(critical),
        "critical_proven": sum(1 for i in critical if i["state"] == "proven"),
        "executed": sum(1 for i in items if i["state"] in ("proven", "partial", "failed")),
        "counts": tally(i["state"] for i in items),
        "tests": items,
        "sources": [rel(tests_path), rel(evidence_path)],
    }


def collect_skills() -> dict:
    fitness_path = ROOT / "evaluations" / "skill-fitness.yaml"
    fitness = read_yaml(fitness_path) if fitness_path.exists() else {}
    registry = fitness.get("skills") or {}

    on_disk = set()
    skills_dir = ROOT / "skills"
    if skills_dir.is_dir():
        for entry in sorted(skills_dir.iterdir()):
            if entry.is_dir() and not entry.name.startswith("_") and (entry / "SKILL.md").exists():
                on_disk.add(entry.name)

    items = []
    for name in sorted(set(registry) | on_disk):
        record = registry.get(name) or {}
        if not isinstance(record, dict):
            record = {}
        runs = record.get("runs")
        run_count = len(runs) if isinstance(runs, list) else 0
        state = map_status(record.get("benchmark_status"))
        # A contract file with no registry entry is defined but unmeasured.
        if name not in registry:
            state = "unproven"
        items.append(
            {
                "name": name,
                "version": record.get("version") or "unversioned",
                "previous_version": record.get("previous_version"),
                "benchmark_status": record.get("benchmark_status") or "not registered",
                "state": state,
                "runs": run_count,
                "has_contract": name in on_disk,
                "registered": name in registry,
                "limitation": record.get("limitation") or "",
            }
        )

    promotion = fitness.get("promotion_rule") or {}
    return {
        "total": len(items),
        "counts": tally(i["state"] for i in items),
        "benchmarked": sum(1 for i in items if i["runs"] > 0),
        "minimum_runs_for_promotion": promotion.get("minimum_repeated_runs"),
        "items": items,
        "sources": [rel(fitness_path), "skills/"],
    }


READINESS_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([0-9.]+)\s*\|\s*([^|]*?)\s*\|")
READINESS_OVERALL = re.compile(r"\*\*Overall readiness:\s*([0-9.]+)\s*/\s*([0-9.]+)\*\*")
READINESS_DATE = re.compile(r"##\s*Current assessment\s*[—-]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")


def collect_readiness() -> dict:
    path = ROOT / "areas" / "knowledge-readiness.md"
    if not path.exists():
        return {"available": False, "source": None}
    text = path.read_text(encoding="utf-8")

    dimensions = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        match = READINESS_ROW.match(line)
        if not match:
            continue
        label = match.group(1).strip()
        if label.lower() in ("dimension",) or set(label) <= set("-: "):
            continue
        dimensions.append(
            {
                "name": label,
                "score": float(match.group(2)),
                "confidence": match.group(3).strip(),
            }
        )

    overall = READINESS_OVERALL.search(text)
    scale = float(overall.group(2)) if overall else 10.5
    score = float(overall.group(1)) if overall else None
    if score is None and dimensions:
        # The document governs by lowest material dimension; mirror that rather
        # than averaging, which would read better than the evidence supports.
        score = min(d["score"] for d in dimensions)

    lowest = min(dimensions, key=lambda d: d["score"]) if dimensions else None
    date = READINESS_DATE.search(text)
    return {
        "available": True,
        "score": score,
        "scale": scale,
        "assessed_on": date.group(1) if date else None,
        "governing_dimension": lowest["name"] if lowest else None,
        "governing_rule": "overall score uses the lowest material dimension",
        "dimensions": sorted(dimensions, key=lambda d: d["score"]),
        "source": rel(path),
    }


def collect_knowledge() -> dict:
    entities_path = ROOT / "entities.json"
    entities = {}
    if entities_path.exists():
        entities = json.loads(entities_path.read_text(encoding="utf-8"))

    tracked = ("architecture", "areas", "decisions", "evaluations", "governance",
               "notes", "observability", "projects", "reviews", "routing", "skills")
    corpus = []
    for name in tracked:
        directory = ROOT / name
        if not directory.is_dir():
            continue
        files = [p for p in directory.rglob("*") if p.is_file()]
        corpus.append({"directory": name, "files": len(files)})

    return {
        "people": len(entities.get("people") or []),
        "projects": entities.get("projects") or [],
        "skills_indexed": len(entities.get("skills") or []),
        "topics": len(entities.get("topics") or []),
        "schema_version": entities.get("schema_version"),
        "corpus": corpus,
        "total_files": sum(c["files"] for c in corpus),
        "sources": [rel(entities_path)],
    }


def collect_graph() -> dict:
    graph_path = ROOT / "graphify-out" / "graph.json"
    manifest_path = ROOT / "graphify-out" / "manifest.json"
    if not graph_path.exists():
        return {"available": False, "state": "unproven", "source": None}

    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = graph.get("nodes") or []
    links = graph.get("links") or []
    hyperedges = graph.get("hyperedges") or (graph.get("graph") or {}).get("hyperedges") or []
    communities = {n.get("community") for n in nodes if isinstance(n, dict) and n.get("community") is not None}

    # Coverage, not file mtimes: a git checkout rewrites mtimes, so freshness is
    # measured by which repository files the graph actually indexed.
    covered, missing = set(), []
    if manifest_path.exists():
        covered = set(json.loads(manifest_path.read_text(encoding="utf-8")).keys())
    indexable = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(ROOT).parts
        if parts[0] in (".git", ".github", "graphify-out", "console", "scripts"):
            continue
        if path.suffix in (".md", ".json", ".yaml", ".yml"):
            indexable.append(rel(path))
    missing = sorted(p for p in indexable if p not in covered)

    state = "proven" if not missing else "stale"
    return {
        "available": True,
        "state": state,
        "nodes": len(nodes),
        "links": len(links),
        "hyperedges": len(hyperedges),
        "communities": len(communities),
        "indexed_files": len(covered),
        "repository_files": len(indexable),
        "unindexed": missing[:20],
        "unindexed_total": len(missing),
        "sources": [rel(graph_path), rel(manifest_path)],
    }


def collect_decisions() -> list:
    records = []
    for name in ("decisions", "reviews"):
        directory = ROOT / name
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            date = None
            match = re.search(r"^updated:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.M)
            if not match:
                match = re.search(r"^created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.M)
            if not match:
                match = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", path.name)
            if match:
                date = match.group(1)
            title = None
            for line in text.splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            records.append(
                {
                    "kind": name[:-1],
                    "title": title or path.stem.replace("-", " "),
                    "date": date,
                    "path": rel(path),
                }
            )
    records.sort(key=lambda r: (r["date"] or "", r["path"]), reverse=True)
    return records


def build_state() -> dict:
    acceptance = collect_acceptance()
    skills = collect_skills()
    readiness = collect_readiness()
    graph = collect_graph()
    verification = collect_verification()

    # The headline verdict is governed by the worst material input, never by an
    # average and never by file presence. AGENTS.md rules 15, 17 and 20.
    blocking = []
    if not acceptance["production_certified"]:
        blocking.append("acceptance suite is not production certified")
    if acceptance["critical_proven"] < acceptance["critical_total"]:
        blocking.append(
            f"{acceptance['critical_total'] - acceptance['critical_proven']} of "
            f"{acceptance['critical_total']} critical acceptance tests lack pass evidence"
        )
    if skills["benchmarked"] == 0 and skills["total"]:
        blocking.append("no production skill has recorded benchmark runs")
    if graph.get("state") == "stale":
        blocking.append("knowledge graph does not cover the current repository")
    if verification["state"] == "failed":
        blocking.append("repository contract verification is failing")

    verdict_state = "unproven"
    if verification["state"] == "failed":
        verdict_state = "failed"
    elif not blocking:
        verdict_state = "proven"
    elif acceptance["executed"]:
        verdict_state = "partial"

    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "generator": "scripts/build_console_state.py",
        "contract": "Values are read from repository files. The console authors none of them.",
        "verdict": {
            "state": verdict_state,
            "headline": "Built, not yet verified" if verdict_state in ("unproven", "partial")
            else ("Verification failing" if verdict_state == "failed" else "Verified"),
            "blocking": blocking,
            "governed_by": "worst material input (AGENTS.md rules 15, 17, 20)",
        },
        "repo": collect_repo(),
        "verification": verification,
        "readiness": readiness,
        "acceptance": acceptance,
        "skills": skills,
        "knowledge": collect_knowledge(),
        "graph": graph,
        "history": collect_decisions(),
        "unmapped_statuses": sorted(UNKNOWN_STATUSES),
        "states": list(STATES),
    }


def render(state: dict) -> tuple[str, str]:
    payload = json.dumps(state, indent=2, ensure_ascii=False, sort_keys=False)
    # state.js lets the console open straight from the filesystem, where fetch()
    # of a local JSON file is blocked by the browser's origin rules.
    script = (
        "/* Generated by scripts/build_console_state.py. Do not edit by hand. */\n"
        f"window.__DRX_STATE__ = {payload};\n"
    )
    return payload + "\n", script


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if on-disk state is not current")
    args = parser.parse_args()

    state = build_state()
    payload, script = render(state)

    json_path = OUT_DIR / "state.json"
    js_path = OUT_DIR / "state.js"

    if args.check:
        if not json_path.exists():
            print("console/state.json is missing; run scripts/build_console_state.py", file=sys.stderr)
            return 1
        current = json.loads(json_path.read_text(encoding="utf-8"))
        volatile = ("generated_at",)
        a = {k: v for k, v in current.items() if k not in volatile}
        b = {k: v for k, v in state.items() if k not in volatile}
        if a != b:
            print("console/state.json is stale; run scripts/build_console_state.py", file=sys.stderr)
            return 1
        print("Console state is current.")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    json_path.write_text(payload, encoding="utf-8")
    js_path.write_text(script, encoding="utf-8")

    verdict = state["verdict"]
    print(f"Wrote {rel(json_path)} and {rel(js_path)}")
    print(f"Verdict: {verdict['state']} — {verdict['headline']}")
    for reason in verdict["blocking"]:
        print(f"  blocking: {reason}")
    if state["unmapped_statuses"]:
        print(f"  unmapped status values: {', '.join(state['unmapped_statuses'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
