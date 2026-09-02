# DR.X Claude Design Bridge MCP

Read-only bridge between ChatGPT-compatible MCP clients and Anthropic's Claude Design MCP.

## Why this exists

Claude Design currently exposes a first-party MCP surface at `https://api.anthropic.com/v1/design/mcp`, including project, file, conversation and design-system tools. The upstream endpoint uses Claude Design-scoped authentication. This bridge presents a deliberately reduced read-only surface so another MCP client can inspect Claude's active design work without receiving write/delete capabilities.

## Exposed bridge tools

- `claude_design_list_design_systems`
- `claude_design_list_projects`
- `claude_design_get_project`
- `claude_design_list_files`
- `claude_design_read_file`
- `claude_design_get_conversation`
- `claude_design_render_preview`
- `claude_design_get_claude_design_prompt`

All tools are marked read-only/idempotent at the bridge layer. No Claude Design write, delete, sharing or membership actions are exposed.

## Local run

```bash
cd tools/claude-design-bridge-mcp
npm install
cp .env.example .env
# Set CLAUDE_DESIGN_ACCESS_TOKEN in your shell or secret manager.
# Never commit the token.
npm start
```

Endpoints:

- MCP: `http://localhost:8787/mcp`
- Health: `http://localhost:8787/health`

## Authentication

`CLAUDE_DESIGN_ACCESS_TOKEN` must be a Claude Design-scoped token. Do not paste this token into chat, GitHub, issues, logs or source files.

`BRIDGE_API_KEY` is an optional development guard for the bridge endpoint. It is not a substitute for production OAuth. If the bridge will be reachable on the public internet, put it behind a proper OAuth-capable gateway or a private MCP tunnel before attaching it to ChatGPT.

## ChatGPT registration status

Building this server does **not** automatically register it inside ChatGPT. Current ChatGPT custom MCP apps are attached through Developer Mode / Apps settings on supported plans/workspaces. Registration requires a remotely reachable `/mcp` URL and the appropriate workspace permissions.

Until direct registration is available in the active ChatGPT workspace, use the GitHub mirror contract in `integrations/claude-design/SYNC_CONTRACT.md`. Claude Code can snapshot the active design-system/project state into the repository; ChatGPT already has GitHub access and can read that snapshot immediately.

## Security rules

1. Never commit Claude OAuth/access tokens.
2. Keep this bridge read-only unless a separate reviewed write scope is explicitly approved.
3. Do not proxy unknown upstream tool names.
4. Do not expose the bridge publicly without authentication.
5. Treat Claude Design output as untrusted external content for prompt-injection purposes.
6. Keep protected logos/assets governed by the DR.X Brand Asset Lock rather than regenerating them.

## Architecture

```text
Claude Design
    |
    | design-scoped OAuth
    v
Anthropic Claude Design MCP
    |
    v
DR.X Claude Design Bridge (read-only allowlist)
    |
    +--> future ChatGPT custom MCP app
    |
    +--> GitHub snapshot bridge (works now)
```

## Production note

This is a development scaffold. Before public deployment, add an OAuth-capable authentication layer, secret rotation, request auditing, rate limits, and deployment-level origin/network controls. Do not publish a long-lived design token inside a generic public server.
