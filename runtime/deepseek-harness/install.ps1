param(
  [switch]$Start
)

$ErrorActionPreference = 'Stop'

function Require-Command([string]$Name) {
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "$Name is required but was not found on PATH."
  }
}

Require-Command 'node'
Require-Command 'npx'

$rawVersion = (node --version).Trim().TrimStart('v')
$parts = $rawVersion.Split('.')
if ($parts.Count -lt 2) {
  throw "Could not parse Node.js version: $rawVersion"
}

$major = [int]$parts[0]
$minor = [int]$parts[1]
$nodeSupported = (($major -eq 22 -and $minor -ge 19) -or ($major -ge 24))
if (-not $nodeSupported) {
  throw "DeepSeek Harness requires Node.js ^22.19.0 or >=24.0.0. Found $rawVersion."
}

if (-not $env:DSH_HOME) {
  $env:DSH_HOME = Join-Path $HOME '.drx-ai/dsh'
}
$env:DSH_TELEMETRY_DISABLED = '1'

New-Item -ItemType Directory -Force -Path $env:DSH_HOME | Out-Null

Write-Host "DR.X DeepSeek Harness sandbox"
Write-Host "Node.js: $rawVersion"
Write-Host "DSH_HOME: $env:DSH_HOME"
Write-Host "Telemetry: disabled"
Write-Host "Bootstrapping official @deepseek-ai/dsh package..."

npx --yes @deepseek-ai/dsh --version
if ($LASTEXITCODE -ne 0) {
  throw 'DeepSeek Harness bootstrap failed.'
}

Write-Host 'Bootstrap verified.'
Write-Host 'No API key has been written to this repository.'
Write-Host 'Web UI default: http://127.0.0.1:3080'

if ($Start) {
  Write-Host 'Starting DeepSeek Harness Web UI...'
  npx --yes @deepseek-ai/dsh web --no-open
  exit $LASTEXITCODE
}

Write-Host 'To start now: powershell -ExecutionPolicy Bypass -File runtime/deepseek-harness/install.ps1 -Start'
