# Current Structural Knowledge Graph

This report is generated deterministically from the current repository by `scripts/rebuild_knowledge_index.py`.

It is a **structural reference graph**, not a semantic Graphify run. An edge means one Markdown document explicitly links to another. It must not be interpreted as causality, endorsement, similarity, or inferred truth.

## Current corpus

- Documents indexed: **50**
- Approximate words: **48,860**
- Explicit internal reference edges: **26**
- Structurally isolated documents: **19**
- Project records: **6**
- Skill records: **13**
- Topics from frontmatter tags: **54**

## Provenance rules

- Nodes are repository Markdown files outside generated/output folders.
- Edges exist only when a resolvable relative Markdown link is present.
- `entities.json` is regenerated from current project files, skill contracts, frontmatter tags, and the previously approved people list.
- No inferred semantic edge is created by this script.
- The historical semantic Graphify output remains preserved in Git history; a fresh semantic Graphify run requires the actual Graphify runtime and must be verified separately.

## Structurally isolated documents

- `AGENTS.md`
- `architecture/DRX-AION-SIGMA.md`
- `areas/channel-registry.md`
- `areas/drx-identity-covenant.md`
- `decisions/2026-07-19-obsidian-first-knowledge-base.md`
- `decisions/cofound-product-hierarchy-2026-08-17.md`
- `decisions/drx-ai-aion-sigma-integration-2026-08-23.md`
- `notes/last-bench-legal-review-source.md`
- `projects/colab.md`
- `reviews/cofound-final-convergence-audit-2026-08-18.md`
- `reviews/cofound-ultramax-reaudit-2026-08-17.md`
- `reviews/cofound-v4.1-execution-qc-2026-08-18.md`
- `reviews/founder-intelligence-ultramax-audit-2026-08-17.md`
- `reviews/founder-portfolio-trendcraft-pressure-test-2026-08-26.md`
- `reviews/second-brain-system-audit-2026-08-17.md`
- `reviews/second-brain-verification-audit-2026-08-21.md`
- `skills/drx-architecture-convergence/SKILL.md`
- `skills/drx-fable2036-reasoner/SKILL.md`
- `skills/drx-prelive-simulator/SKILL.md`

## Maintenance

Run:

```bash
python scripts/rebuild_knowledge_index.py --write
python scripts/rebuild_knowledge_index.py --check
```

CI verifies that committed generated files match the current repository state.
