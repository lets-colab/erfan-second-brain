#!/usr/bin/env bash
# Bootstrap MemPalace + Graphify for a Claude session.
#
# Cloud Claude Code sessions run in a throwaway container: nothing installed in
# one survives into the next. This script rebuilds the whole setup from the repo
# so a new session spends a few seconds instead of re-deriving context in tokens.
#
#   bash bootstrap.sh            # install, register, mine
#   bash bootstrap.sh --no-mine  # skip mining (faster; palace already built)
#
# Safe to re-run. Mining is append-only and skips files already filed.

set -euo pipefail

BRAIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="$(dirname "$BRAIN")"
MEMPALACE_DIR="${MEMPALACE_DIR:-$WORKSPACE/mempalace}"
GRAPHIFY_DIR="${GRAPHIFY_DIR:-$WORKSPACE/graphify}"
DO_MINE=1
[[ "${1:-}" == "--no-mine" ]] && DO_MINE=0

say() { printf '\n\033[1m==> %s\033[0m\n' "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

# --- prerequisites ----------------------------------------------------------
have uv || { echo "uv not found. Install: https://docs.astral.sh/uv/"; exit 1; }

for pair in "mempalace|https://github.com/lets-colab/mempalace" \
            "graphify|https://github.com/lets-colab/graphify"; do
  name="${pair%%|*}"; url="${pair##*|}"
  dir="$WORKSPACE/$name"
  if [[ ! -d "$dir" ]]; then
    say "Cloning $name"
    git clone --depth 1 "$url" "$dir"
  fi
done

# --- install ----------------------------------------------------------------
say "Installing MemPalace"
(cd "$MEMPALACE_DIR" && uv sync --extra dev >/dev/null)
MP="$MEMPALACE_DIR/.venv/bin"
"$MP/mempalace" --version

say "Installing Graphify"
(cd "$GRAPHIFY_DIR" && uv sync --all-extras >/dev/null)
GF="$GRAPHIFY_DIR/.venv/bin"
"$GF/graphify" --version

# --- register with Claude ---------------------------------------------------
if have claude; then
  say "Registering MemPalace MCP server (user scope)"
  claude mcp remove mempalace >/dev/null 2>&1 || true
  claude mcp add --scope user mempalace -- "$MP/mempalace-mcp"

  say "Installing Graphify skill"
  (cd "$BRAIN" && "$GF/graphify" install --platform claude >/dev/null)
  echo "  skill -> ~/.claude/skills/graphify/"
else
  echo "claude CLI not found — skipping MCP/skill registration."
fi

# --- build memory -----------------------------------------------------------
if (( DO_MINE )); then
  say "Mining the second brain into the palace"
  (cd "$BRAIN" && "$MP/mempalace" mine .)
fi

say "Ready"
cat <<EOF
  mempalace search "<query>"     find anything, verbatim
  mempalace wake-up              ~800-token session context
  /graphify .                    build/query the code knowledge graph

Re-run this after any container restart. It is idempotent.
EOF
