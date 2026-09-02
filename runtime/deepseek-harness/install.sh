#!/usr/bin/env bash
set -euo pipefail

START=false
if [[ "${1:-}" == "--start" ]]; then
  START=true
fi

command -v node >/dev/null 2>&1 || { echo 'node is required but was not found on PATH.' >&2; exit 1; }
command -v npx >/dev/null 2>&1 || { echo 'npx is required but was not found on PATH.' >&2; exit 1; }

RAW_VERSION="$(node --version | sed 's/^v//')"
IFS='.' read -r MAJOR MINOR PATCH <<< "$RAW_VERSION"

SUPPORTED=false
if [[ "$MAJOR" -eq 22 && "$MINOR" -ge 19 ]]; then
  SUPPORTED=true
elif [[ "$MAJOR" -ge 24 ]]; then
  SUPPORTED=true
fi

if [[ "$SUPPORTED" != true ]]; then
  echo "DeepSeek Harness requires Node.js ^22.19.0 or >=24.0.0. Found $RAW_VERSION." >&2
  exit 1
fi

export DSH_HOME="${DSH_HOME:-$HOME/.drx-ai/dsh}"
export DSH_TELEMETRY_DISABLED=1
mkdir -p "$DSH_HOME"

echo 'DR.X DeepSeek Harness sandbox'
echo "Node.js: $RAW_VERSION"
echo "DSH_HOME: $DSH_HOME"
echo 'Telemetry: disabled'
echo 'Bootstrapping official @deepseek-ai/dsh package...'

npx --yes @deepseek-ai/dsh --version

echo 'Bootstrap verified.'
echo 'No API key has been written to this repository.'
echo 'Web UI default: http://127.0.0.1:3080'

if [[ "$START" == true ]]; then
  echo 'Starting DeepSeek Harness Web UI...'
  exec npx --yes @deepseek-ai/dsh web --no-open
fi

echo 'To start now: bash runtime/deepseek-harness/install.sh --start'
