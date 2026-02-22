---
name: screenshot-to-website
description: Build a fully working replica of a website from a screenshot, matching design and functionality exactly.
---

# Screenshot to Website Skill

## Overview

Use this skill when given a screenshot (and optionally a URL) of a website. The agent should replicate the site fully, including design and interactive functionality.

## When to Use

Trigger this skill when:
- You are asked to convert a website screenshot into a working implementation.
- A URL is provided to explore navigation and interactive behavior beyond the screenshot.

## Instructions

### Role

Act like a senior full-stack developer who ships production-ready code.  
No shortcuts, no placeholders, no “implement later" comments.

### Task

1. Look at the provided screenshot of a website.
2. Build a fully working replica.
3. If a URL is provided, use it to explore additional context such as:
   - Navigation
   - Interactions
   - Hidden states
   - Forms behavior

### Design

- Match **colors**, **fonts**, **spacing**, **layout** exactly.
- Use **Google Fonts** (pick closest match).
- Add **hover states** for buttons and links.
- Add **smooth transitions** for interactions.
- Ensure the replica is **mobile responsive**.

### Functionality

- Every button must work (open modal, navigate, toggle, etc.).
- Every form must submit and show feedback.
- Every link must navigate.
- Dropdowns, tabs, and accordions must function.
- Search bars should filter or perform search correctly.

### Backend (if needed)

If the screenshot implies a backend is required, implement:

- **Auth forms** → Basic login/signup with session.
- **Data tables** → Create realistic mock data, store in SQLite.
- **Contact forms** → Save submissions.
- **Dashboard stats** → Generate realistic fake numbers.

### Tech

- **Frontend:** Next.js  
- **Backend (if needed):** Python 3.12, FastAPI, full type hints, SQLite

## Output Format

When generating responses, structure them to include:

- A clear description of the development steps.
- Code snippets where relevant.
- Explanations of UX and design decisions.
- Any assumptions made based on the screenshot.

## Notes

- Do not include placeholder text like “lorem ipsum” or “coming soon”.
- Ensure mobile view works at 375px width.
- Verify all interactive elements function in the final implementation.
