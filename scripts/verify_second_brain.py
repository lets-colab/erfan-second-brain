#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []
WARNINGS: list[str] = []

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "architecture/DRX-AI-OS.md",
    "routing/task-router.yaml",
    "governance/authority-matrix.yaml",
    "observability/event-schema.yaml",
    "evaluations/acceptance-tests.yaml",
    "evaluations/acceptance-evidence.yaml",
    "evaluations/skill-fitness.yaml",
    "entities.json",
    "graphify-out/GRAPH_REPORT.md",
    "graphify-out/STRUCTURAL_GRAPH_REPORT.md",
    "graphify-out/structural-graph.json",
]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "openai_key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    "google_api_key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
EXCLUDED_TOP_LEVEL = {".git", ".obsidian"}


def fail(message: str) -> None:
    FAILURES.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def resolve_link(source: Path, raw: str) -> Path | None:
    target = raw.strip()
    if not target or target.startswith(
        ("#", "http://", "https://", "mailto:", "tel:", "notion://")
    ):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target:
        return None
    candidate = (source.parent / target).resolve()
    variants = [candidate]
    if candidate.suffix == "":
        variants.extend([candidate.with_suffix(".md"), candidate / "README.md"])
    for variant in variants:
        try:
            variant.relative_to(ROOT)
        except ValueError:
            continue
        if variant.exists():
            return variant
    return candidate


def skill_names() -> set[str]:
    result: set[str] = set()
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        fail("skills/ directory is missing")
        return result
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir() or child.name == "_template":
            continue
        skill_file = child / "SKILL.md"
        if not skill_file.exists():
            fail(f"active skill directory has no SKILL.md: {child.relative_to(ROOT)}")
            continue
        text = skill_file.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"^name:\s*([^\n]+)", text, re.MULTILINE)
        result.add(match.group(1).strip().strip("'\"") if match else child.name)
        if not re.search(r"^description:\s*\S", text, re.MULTILINE):
            fail(f"skill missing description frontmatter: {skill_file.relative_to(ROOT)}")
        if not re.search(r"^version:\s*\S", text, re.MULTILINE):
            warn(f"skill is unversioned: {skill_file.relative_to(ROOT)}")
    return result


def fitness_skill_names(text: str) -> set[str]:
    marker = "skills:\n"
    index = text.find(marker)
    if index == -1:
        return set()
    section = text[index + len(marker) :]
    if "\nrules:\n" in section:
        section = section.split("\nrules:\n", 1)[0]
    return set(re.findall(r"^  ([A-Za-z0-9_-]+):\s*$", section, re.MULTILINE))


def acceptance_test_ids(text: str) -> tuple[set[str], set[str]]:
    all_ids: set[str] = set()
    critical_ids: set[str] = set()
    for match in re.finditer(
        r"^  - id:\s*([^\n]+)\n\s+critical:\s*(true|false)\s*$",
        text,
        re.MULTILINE,
    ):
        test_id = match.group(1).strip()
        all_ids.add(test_id)
        if match.group(2) == "true":
            critical_ids.add(test_id)
    return all_ids, critical_ids


def evidence_statuses(text: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    marker = "results:\n"
    index = text.find(marker)
    if index == -1:
        return statuses
    section = text[index + len(marker) :]
    current: str | None = None
    for line in section.splitlines():
        top = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", line)
        if top:
            current = top.group(1)
            continue
        status = re.match(r"^    status:\s*([^\n]+)$", line)
        if current and status:
            statuses[current] = status.group(1).strip()
    return statuses


def scan_internal_links() -> None:
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in LINK_RE.findall(text):
            resolved = resolve_link(path, raw)
            if resolved is None:
                continue
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                fail(f"broken internal Markdown link in {rel}: {raw}")


def scan_secrets() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(f"possible {name} secret committed in {rel}")


def main() -> int:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(f"required path missing: {rel}")

    skills = skill_names()
    fitness_text = (
        read("evaluations/skill-fitness.yaml")
        if (ROOT / "evaluations/skill-fitness.yaml").exists()
        else ""
    )
    registered = fitness_skill_names(fitness_text)
    for name in sorted(skills - registered):
        fail(f"active skill not registered in evaluations/skill-fitness.yaml: {name}")
    for name in sorted(registered - skills):
        warn(f"fitness registry has no matching current skill directory: {name}")

    tests_text = (
        read("evaluations/acceptance-tests.yaml")
        if (ROOT / "evaluations/acceptance-tests.yaml").exists()
        else ""
    )
    evidence_text = (
        read("evaluations/acceptance-evidence.yaml")
        if (ROOT / "evaluations/acceptance-evidence.yaml").exists()
        else ""
    )
    test_ids, critical_ids = acceptance_test_ids(tests_text)
    statuses = evidence_statuses(evidence_text)
    for test_id in sorted(test_ids - statuses.keys()):
        fail(f"acceptance test has no evidence status: {test_id}")
    allowed_statuses = {"passed", "failed", "blocked", "partial", "not_run"}
    for test_id, status in sorted(statuses.items()):
        if status not in allowed_statuses:
            fail(f"invalid acceptance evidence status for {test_id}: {status}")

    certified = bool(
        re.search(
            r"^\s*production_certified:\s*true\s*$", evidence_text, re.MULTILINE
        )
    )
    if certified:
        not_passed = sorted(
            test_id for test_id in critical_ids if statuses.get(test_id) != "passed"
        )
        if not_passed:
            fail(
                "production_certified is true while critical tests are not passed: "
                + ", ".join(not_passed)
            )
        if not re.search(
            r"^\s*human_owner_signoff:\s*true\s*$", evidence_text, re.MULTILINE
        ):
            fail("production_certified is true without human_owner_signoff: true")

    router = (
        read("routing/task-router.yaml")
        if (ROOT / "routing/task-router.yaml").exists()
        else ""
    )
    agents = read("AGENTS.md") if (ROOT / "AGENTS.md").exists() else ""
    for required in [
        "drx-execution-qc",
        "drx-systematic-debugger",
        "drx-brand-asset-lock",
        "drx-fable-godlevel-execution",
    ]:
        if required not in router:
            fail(f"router does not reference required specialist/final skill: {required}")
        if required not in agents:
            fail(f"AGENTS.md does not reference required specialist/final skill: {required}")

    historical = (
        read("graphify-out/GRAPH_REPORT.md")
        if (ROOT / "graphify-out/GRAPH_REPORT.md").exists()
        else ""
    )
    if "SUPERSEDED" not in historical.upper() and "HISTORICAL" not in historical.upper():
        fail("graphify-out/GRAPH_REPORT.md is not clearly marked historical/superseded")

    scan_internal_links()
    scan_secrets()

    index_script = ROOT / "scripts/rebuild_knowledge_index.py"
    if not index_script.exists():
        fail("scripts/rebuild_knowledge_index.py is missing")
    else:
        proc = subprocess.run(
            [sys.executable, str(index_script), "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            fail(
                "knowledge index check failed: "
                + (proc.stderr.strip() or proc.stdout.strip())
            )

    for message in WARNINGS:
        print(f"WARN: {message}")
    if FAILURES:
        for message in FAILURES:
            print(f"FAIL: {message}", file=sys.stderr)
        print(
            f"verification failed: {len(FAILURES)} failure(s), {len(WARNINGS)} warning(s)",
            file=sys.stderr,
        )
        return 1
    print(f"Second Brain repository verification PASS ({len(WARNINGS)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
