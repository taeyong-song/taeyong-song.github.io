param(
    [switch]$GenerateOnly
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$toolDir = Join-Path $repoRoot '.cv-tools'
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'

if (Test-Path -LiteralPath $bundledPython) {
    $pythonExe = $bundledPython
} else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonCommand) {
        throw 'Python was not found. Install Python 3 or run this command inside Codex.'
    }
    $pythonExe = $pythonCommand.Source
}

New-Item -ItemType Directory -Force -Path $toolDir | Out-Null
$previousPythonPath = $env:PYTHONPATH
$env:PYTHONPATH = if ($previousPythonPath) { "$toolDir;$previousPythonPath" } else { $toolDir }

try {
    $localYaml = Join-Path $toolDir 'yaml\__init__.py'
    if (-not (Test-Path -LiteralPath $localYaml)) {
        Write-Host 'Installing the local CV parser dependency (PyYAML)...'
        & $pythonExe -m pip install --disable-pip-version-check --target $toolDir PyYAML
        if ($LASTEXITCODE -ne 0) {
            throw 'Could not install PyYAML.'
        }
    }

    $arguments = @((Join-Path $PSScriptRoot 'build_cv.py'))
    if ($GenerateOnly) {
        $arguments += '--generate-only'
    }
    & $pythonExe @arguments
    if ($LASTEXITCODE -ne 0) {
        throw 'CV generation failed.'
    }
} finally {
    $env:PYTHONPATH = $previousPythonPath
}
