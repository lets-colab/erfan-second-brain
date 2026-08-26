#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graphify-out"
ENTITIES_PATH = ROOT / "entities.json"
STRUCTURAL_GRAPH_PATH = GRAPH_DIR / "structural-graph.json"
REPORT_PATH = GRAPH_DIR / "STRUCTURAL_GRAPH_REPORT.md"
EXCLUDED_TOP_LEVEL = {".git", ".github", ".obsidian", "graphify-out"}
WORD_RE = re.compile(r"\b[\w’'-]+\b", re.UNICODE)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    result: dict[str, object] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            result[key] = [
                item.strip().strip("'\"")
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        else:
            result[key] = value.strip("'\"")
    return result


def title_for(path: Path, text: str, frontmatter: dict[str, object]) -> str:
    if isinstance(frontmatter.get("title"), str) and frontmatter["title"]:
        return str(frontmatter["title"])
    match = HEADING_RE.search(text)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def iter_markdown() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def resolve_internal_link(source: Path, raw: str) -> str | None:
    target = raw.strip()
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "notion://")):
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
            rel = variant.relative_to(ROOT)
        except ValueError:
            continue
        if variant.exists() and variant.is_file():
            return rel.as_posix()
    return None


def existing_people() -> list[str]:
    try:
        data = json.loads(ENTITIES_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    people = data.get("people", [])
    return sorted(
        {str(item).strip() for item in people if str(item).strip()},
        key=str.casefold,
    )


def build() -> tuple[dict[str, object], dict[str, object], str]:
    docs: list[dict[str, object]] = []
    edges: list[dict[str, str]] = []
    tags: set[str] = set()
    project_records: list[dict[str, str]] = []
    skill_records: list[dict[str, str]] = []
    total_words = 0

    markdown_files = iter_markdown()
    known_paths = {path.relative_to(ROOT).as_posix() for path in markdown_files}

    for path in markdown_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        title = title_for(path, text, fm)
        word_count = len(WORD_RE.findall(text))
        total_words += word_count
        raw_tags = fm.get("tags", [])
        if isinstance(raw_tags, list):
            tags.update(str(tag).strip() for tag in raw_tags if str(tag).strip())

        if rel.startswith("projects/"):
            project_records.append(
                {
                    "name": title,
                    "path": rel,
                    "status": str(fm.get("status", "unknown")),
                }
            )
        if rel.startswith("skills/") and rel.endswith("/SKILL.md") and "/_template/" not in f"/{rel}":
            parts = rel.split("/")
            skill_name = str(fm.get("name") or (parts[1] if len(parts) > 1 else title))
            skill_records.append(
                {
                    "name": skill_name,
                    "path": rel,
                    "status": str(fm.get("status", "unknown")),
                    "version": str(fm.get("version", "unversioned")),
                }
            )

        docs.append(
            {
                "id": rel,
                "title": title,
                "kind": str(fm.get("type") or (rel.split("/", 1)[0] if "/" in rel else "root")),
                "status": str(fm.get("status", "unknown")),
                "word_count": word_count,
            }
        )

        for raw_link in LINK_RE.findall(text):
            target = resolve_internal_link(path, raw_link)
            if target and target in known_paths:
                edges.append({"source": rel, "target": target, "type": "references"})

    docs.sort(key=lambda item: str(item["id"]))
    unique_edges = sorted({(e["source"], e["target"], e["type"]) for e in edges})
    edge_dicts = [
        {"source": source, "target": target, "type": edge_type}
        for source, target, edge_type in unique_edges
    ]
    project_records.sort(key=lambda item: item["name"].casefold())
    skill_records.sort(key=lambda item: item["name"].casefold())

    incoming: dict[str, int] = {str(doc["id"]): 0 for doc in docs}
    outgoing: dict[str, int] = {str(doc["id"]): 0 for doc in docs}
    for edge in edge_dicts:
        incoming[edge["target"]] = incoming.get(edge["target"], 0) + 1
        outgoing[edge["source"]] = outgoing.get(edge["source"], 0) + 1
    isolated = sorted(
        doc_id
        for doc_id in incoming
        if incoming.get(doc_id, 0) == 0 and outgoing.get(doc_id, 0) == 0
    )

    graph = {
        "schema_version": 1,
        "generated_by": "scripts/rebuild_knowledge_index.py",
        "graph_type": "deterministic_structural_reference_graph",
        "documents": docs,
        "edges": edge_dicts,
        "summary": {
            "documents": len(docs),
            "edges": len(edge_dicts),
            "words": total_words,
            "isolated_documents": len(isolated),
        },
    }

    entities = {
        "schema_version": 2,
        "generated_by": "scripts/rebuild_knowledge_index.py",
        "people": existing_people(),
        "projects": sorted({item["name"] for item in project_records}, key=str.casefold),
        "skills": sorted({item["name"] for item in skill_records}, key=str.casefold),
        "topics": sorted(tags, key=str.casefold),
        "project_records": project_records,
        "skill_records": skill_records,
        "source_documents": len(docs),
    }

    isolated_lines = "\n".join(f"- `{item}`" for item in isolated[:25]) or "- None"
    if len(isolated) > 25:
        isolated_lines += f"\n- ... plus {len(isolated) - 25} more"

    report = f"""# Current Structural Knowledge Graph

This report is generated deterministically from the current repository by `scripts/rebuild_knowledge_index.py`.

It is a **structural reference graph**, not a semantic Graphify run. An edge means one Markdown document explicitly links to another. It must not be interpreted as causality, endorsement, similarity, or inferred truth.

## Current corpus

- Documents indexed: **{len(docs)}**
- Approximate words: **{total_words:,}**
- Explicit internal reference edges: **{len(edge_dicts)}**
- Structurally isolated documents: **{len(isolated)}**
- Project records: **{len(project_records)}**
- Skill records: **{len(skill_records)}**
- Topics from frontmatter tags: **{len(tags)}**

## Provenance rules

- Nodes are repository Markdown files outside generated/output folders.
- Edges exist only when a resolvable relative Markdown link is present.
- `entities.json` is regenerated from current project files, skill contracts, frontmatter tags, and the previously approved people list.
- No inferred semantic edge is created by this script.
- The historical semantic Graphify output remains preserved in Git history; a fresh semantic Graphify run requires the actual Graphify runtime and must be verified separately.

## Structurally isolated documents

{isolated_lines}

## Maintenance

Run:

```bash
python scripts/rebuild_knowledge_index.py --write
python scripts/rebuild_knowledge_index.py --check
```

CI verifies that committed generated files match the current repository state.
"""
    return graph, entities, report


def serialize_json(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def expected_outputs() -> dict[Path, str]:
    graph, entities, report = build()
    return {
        STRUCTURAL_GRAPH_PATH: serialize_json(graph),
        ENTITIES_PATH: serialize_json(entities),
        REPORT_PATH: report,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rebuild deterministic structural knowledge indexes."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write generated index files.")
    mode.add_argument("--check", action="store_true", help="Fail if generated index files are stale.")
    args = parser.parse_args()

    outputs = expected_outputs()
    if args.write:
        GRAPH_DIR.mkdir(parents=True, exist_ok=True)
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")
        return 0

    stale: list[str] = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            stale.append(path.relative_to(ROOT).as_posix())
    if stale:
        print(
            "stale generated knowledge index: " + ", ".join(stale),
            file=sys.stderr,
        )
        return 1
    print("knowledge index is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
