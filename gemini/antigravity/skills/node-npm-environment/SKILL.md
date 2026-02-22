---
name: node-npm-environment
description: Use when the user asks about Node.js, npm, nvm, package.json, or shows node/npm output. Assume Node is already installed and prefer existing setup instead of reinstalling.
---

You are helping with Node.js and npm.

## Core Principle
Assume Node.js and npm are already installed.
Do not suggest reinstalling unless explicitly requested.

## Step 1 — Detect OS

Detect OS from:
- Path style
- Shell prompt
- where vs which
- Explicit mention

## Step 2 — Use OS-appropriate commands

### Windows
- Check node:
  `node -v`
- Check npm:
  `npm -v`
- Locate binary:
  `where node`
- nvm:
  `nvm list`
  `nvm use <version>`

### macOS/Linux
- Check node:
  `node -v`
- Check npm:
  `npm -v`
- Locate binary:
  `which node`
- nvm:
  `nvm list`
  `nvm use <version>`

## Project Workflow

- `npm init -y`
- `npm install`
- `npm install <pkg>`
- `npm install -D <pkg>`
- `npm run <script>`

If project fails:
1. Check package.json
2. Run `npm install`
3. Then run the script

## Troubleshooting (Only If Needed)

If command not found:
- Diagnose PATH first
- Do not reinstall immediately

If cache issue:
- `npm cache verify`
- `npm cache clean --force` (last resort)

## Output Style

- Practical
- Short command blocks
- OS-correct syntax
- Prefer minimal changes
