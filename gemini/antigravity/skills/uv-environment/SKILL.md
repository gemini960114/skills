---
name: uv-environment
description: Use when the user asks about uv, Python virtual environments, pyproject.toml, dependency management, or shows uv/venv output. Assume uv is already installed and prefer using the existing setup instead of reinstalling.
---

You are helping with uv and Python environments.

## Core Principle
Assume uv is already installed.
Never suggest reinstalling uv or Python unless explicitly requested or clearly broken.

## Step 1 — Detect OS

Detect the operating system from:
- Path style (C:\ vs /home/)
- Shell prompt (PS vs $)
- Commands used (where vs which)
- Explicit OS mention

## Step 2 — Use OS-appropriate commands

### If Windows:
- Activate venv:
  `.\.venv\Scripts\Activate.ps1`
- Check python:
  `where python`
- Check uv:
  `uv --version`

### If macOS/Linux:
- Activate venv:
  `source .venv/bin/activate`
- Check python:
  `which python`
- Check uv:
  `uv --version`

## Always Prefer uv Workflow

Use:
- `uv init`
- `uv venv`
- `uv sync`
- `uv run`
- `uv pip`

Avoid switching to pip/venv unless requested.

## Troubleshooting (Only If Needed)

If venv missing:
- `uv venv`

If dependencies missing:
- `uv sync`

If PowerShell policy blocks activation:
- `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

## Output Style

- Command-first
- Minimal steps
- Provide copy-paste ready blocks
- Use OS-correct syntax
- 
