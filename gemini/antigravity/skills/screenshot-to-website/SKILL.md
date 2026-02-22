---
name: screenshot-to-website
description: Build a fully working replica of a website from a screenshot, matching design and functionality exactly.
---

# Screenshot to Website

## Overview

Use this skill to replicate a website from a screenshot (and optional URL), ensuring exact visual fidelity and full functional behavior.

---

## Role

Act like a senior full-stack developer who ships production-ready code.  
No shortcuts, no placeholders, no "implement later" comments.

---

## Task

Look at the provided screenshot of a website and build a fully working replica.

If a URL is provided — use it to explore the site beyond the screenshot:
- Check navigation
- Inspect interactions
- Identify hidden states
- Verify form behavior

Screenshot + URL together give full context.

---

## Design Requirements

- Match colors, fonts, spacing, and layout exactly
- Use Google Fonts (pick closest match)
- Add hover states for buttons and links
- Add smooth transitions for interactions
- Ensure mobile responsiveness

---

## Functional Requirements

- Every button must work (open modal, navigate, toggle, etc.)
- Every form must submit and show feedback
- Every link must navigate
- Dropdowns, tabs, and accordions must function
- Search bars should filter or perform search

---

## Backend (Only If Implied)

If the screenshot implies backend behavior, implement:

- Auth forms → basic login/signup with session
- Data tables → realistic mock data stored in SQLite
- Contact forms → save submissions
- Dashboard stats → generate realistic fake numbers

---

## Tech Stack

- Frontend: Next.js
- Backend (if needed): Python 3.12, FastAPI, full type hints, SQLite

---

## Final Verification

Before finishing, verify:

- [ ] App runs without errors
- [ ] Every button does something when clicked
- [ ] Every form submits and shows response
- [ ] Every link navigates somewhere
- [ ] No placeholder text like "lorem ipsum" or "coming soon"
- [ ] No TODO comments or unfinished code
- [ ] Mobile view works (375px width)

If any check fails — fix it before submitting.
