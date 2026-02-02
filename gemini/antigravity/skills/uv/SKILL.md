---
name: uv-python-manager
description: Use this skill when the user wants to manage Python projects, virtual environments, or dependencies using uv, including creating venvs, installing packages, syncing environments, or running Python tools.
---

# uv Python Manager

## Goal
Provide a fast and reliable way to manage Python environments and dependencies using the `uv` command-line tool.

## Instructions
- Interpret the user's request related to Python project setup, dependency management, or execution.
- Choose the appropriate `uv` subcommand (e.g. `uv venv`, `uv add`, `uv sync`, `uv run`).
- Execute the command via the script in `scripts/run.sh`.
- Clearly explain what the command does before and after execution.
- Show concise output summaries instead of full logs when possible.

## Common Operations
- Create a virtual environment:
  - `uv venv`
- Add dependencies:
  - `uv add <package>`
- Sync environment from lockfile:
  - `uv sync`
- Run a Python script or command:
  - `uv run python script.py`
- Manage Python versions:
  - `uv python install`
  - `uv python list`

## Constraints
- Do not use `sudo`.
- Do not modify system-wide Python installations.
- Only operate within the user's current working directory unless explicitly instructed.
- Do not delete files or environments unless the user explicitly asks.

## Examples

**User:** Create a new virtual environment for this project  
**Action:**  
```bash
uv venv
````

**User:** Install requests and pandas
**Action:**

```bash
uv add requests pandas
```

**User:** Run main.py using uv
**Action:**

```bash
uv run python main.py
```

