---
name: dockerize-project
description: Use this skill when the user wants to dockerize the current project and generate a Dockerfile and docker-compose.yml based on the existing codebase. This skill inspects the repository structure, avoids unsafe assumptions, and produces a minimal, runnable Docker setup for local development.
---

# Dockerize Current Project (Minimal)

## Goal
Analyze the current project’s files and generate a minimal, working Dockerfile and docker-compose.yml so the project can be started with `docker compose up --build`.

## Instructions
1. Inspect the current project structure and identify the primary tech stack:
   - Python (pyproject.toml, uv.lock, requirements.txt, manage.py, app.py, main.py)
   - Node.js (package.json)
   - Other / generic
2. Check whether Docker-related files already exist:
   - Dockerfile
   - docker-compose.yml / docker-compose.yaml
   - .dockerignore
   - If any exist, do NOT overwrite them. Ask the user whether to merge, regenerate with backups, or cancel.
3. Infer a reasonable default entrypoint and port from the codebase.
   - If the entrypoint or port is unclear, ask up to **three** concise clarification questions.
4. Generate the following files as complete code blocks:
   - Dockerfile (development-oriented, readable, non-root when reasonable)
   - docker-compose.yml (no `version:` field)
   - .dockerignore
5. Prefer bind mounts for local development and explain how to change this if needed.

## Constraints
- Do not use `sudo`.
- Do not hardcode secrets; use environment variables or an `.env` / `.env.docker` template if necessary.
- Do not run Docker commands automatically.
- Keep the setup minimal and easy to modify.

## Output Format
1. **Detection Summary**
   - Detected stack
   - Assumed entrypoint
   - Assumed port
2. **Generated Files**
   - `Dockerfile`
   - `docker-compose.yml`
   - `.dockerignore`
3. **How to Run**
   - `docker compose up --build`
   - Common commands (`logs`, `exec`)
4. **Notes**
   - What to change if the entrypoint, port, or environment differs.

## Example
**User:** Dockerize this project for local development  
**Result:**  
- Detect Python project  
- Generate Dockerfile + docker-compose.yml  
- Explain how to start and customize


