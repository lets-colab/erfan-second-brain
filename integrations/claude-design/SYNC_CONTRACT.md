# Claude Design ↔ DR.X Shared Design-System Sync Contract

Purpose: make Claude Design work legible to every approved agent through a durable source of truth, even when direct cross-vendor MCP attachment is unavailable.

## Canonical flow

```text
Claude Design project/design system
        ↓
Claude Code + claude_design MCP
        ↓
verified snapshot/export
        ↓
GitHub repository
        ↓
ChatGPT / Codex / other approved agents
```

## Snapshot location

Claude Code should write exported design-system state under:

`integrations/claude-design/snapshots/<design-system-or-project-slug>/`

Recommended files:

- `manifest.json` — project/design-system id, name, source, last sync time, upstream file inventory, commit source.
- `DESIGN_SYSTEM.md` — human-readable design principles and rules.
- `tokens.json` — colors, typography, spacing, radius, motion and other machine-readable tokens when available.
- `components.md` — component families, variants and behavior.
- `screens.md` — screen/page inventory and intent.
- `conversation.md` — relevant design rationale/conversation when appropriate.
- `files/` — exported Claude Design source files that are safe to persist.
- `previews/` — approved preview images only when licensing/privacy permits.

## Mandatory provenance

Every snapshot must record:

- Claude Design project/design-system identifier;
- upstream source file/path for every derived artifact;
- sync timestamp;
- whether content is exact export, transformed export, or human-authored interpretation;
- unresolved conflicts with the production codebase;
- protected brand assets referenced but not copied/rebuilt.

## Sync rule for Claude Code

When asked to synchronize Claude Design:

1. Authenticate using Claude Design's own supported login flow.
2. Use the upstream `claude_design` MCP tools; never scrape credentials from local config.
3. Identify the requested design system/project explicitly.
4. Read the upstream project/file inventory before writing anything locally.
5. Export or snapshot only material needed for cross-agent design implementation/review.
6. Never commit OAuth tokens, cookies, API credentials, private review links or user secrets.
7. Preserve exact text/tokens/components where available; label interpretations.
8. Commit the snapshot with a message beginning `design-sync:`.
9. Report the commit SHA and snapshot path.

## ChatGPT read rule

When ChatGPT is asked to use Claude's current design system:

1. Read the latest snapshot in this directory from GitHub before designing or coding.
2. Treat exact exported tokens/components as stronger evidence than recollection.
3. Treat `DESIGN_SYSTEM.md` interpretation as supporting context unless backed by exact source.
4. If the snapshot is stale or missing a required screen/component, say so rather than inventing it.
5. Preserve DR.X Brand Asset Lock rules for protected logos/identity assets.
6. Use DR.X execution QC before claiming a production implementation matches Claude Design.

## Conflict order

When sources disagree:

1. Current explicit user instruction.
2. Locked canonical brand asset/source-of-truth rule.
3. Current production code if it reflects an approved shipped state.
4. Latest exact Claude Design export.
5. Latest interpreted Claude Design notes.
6. Older snapshots/history.

Never silently merge contradictory design systems.

## Why GitHub is the immediate bridge

ChatGPT already has authorized GitHub access in this workspace. Therefore a verified Claude Design snapshot committed here is immediately retrievable by ChatGPT without exposing Anthropic credentials or waiting for a custom MCP app to be registered.
