# Claude Code prompt — sync Claude Design into the shared DR.X source of truth

Use this prompt from Claude Code while working in a repository that has access to the `claude_design` MCP.

---

Synchronize the currently approved Claude Design project/design system into the DR.X shared design-system mirror.

Requirements:

1. Use the connected `claude_design` MCP. If it is not authenticated, use Claude Design's supported login flow; do not inspect or copy raw credential files.
2. First call the read tools needed to identify the exact design system/project and inventory its files. Do not guess an id.
3. Read the current design-system rules, project metadata, relevant files, and design conversation/rationale.
4. Write a durable snapshot under:
   `integrations/claude-design/snapshots/<project-or-design-system-slug>/`
5. Produce at minimum:
   - `manifest.json`
   - `DESIGN_SYSTEM.md`
   - `components.md`
   - `screens.md`
   - `tokens.json` when exact tokens are available
6. In `manifest.json`, record exact source identifiers, source paths, sync timestamp, and whether each artifact is exact export or interpretation.
7. Preserve exact tokens/text/components where available. Clearly label any interpretation.
8. Do not create fake design tokens or missing component states.
9. Do not commit OAuth tokens, cookies, credentials, private auth URLs, or secrets.
10. Do not redraw or reinterpret locked brand assets. Reference the canonical source instead.
11. Compare the snapshot against the current production repository when relevant and record conflicts instead of silently resolving them.
12. Commit with message:
   `design-sync: <design-system/project name>`
13. Return the commit SHA, snapshot path, source design/project id, files synchronized, unresolved gaps, and conflicts.

Goal: ChatGPT, Codex, Claude Code, and other approved agents must be able to reconstruct the current approved design system from GitHub without depending on memory or cross-vendor chat history.

---
