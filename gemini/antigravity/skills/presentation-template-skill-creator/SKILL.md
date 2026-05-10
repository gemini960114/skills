---
name: presentation-template-skill-creator
description: Create reusable presentation-production skills from user-provided PPTX or PDF presentation templates. Use when Codex needs to analyze a deck template, extract its visual system and reusable assets, then build a new skill for either static HTML/web presentations, editable PPTX decks, or both, using skill-creator conventions and template-specific references.
---

# Presentation Template Skill Creator

Use this skill to create a new presentation skill from a user-provided `.pptx` or `.pdf` presentation template.

The output is not a finished presentation. The output is a reusable skill folder that lets future agents reproduce the template style without repeatedly loading the original template.

## Output Modes

Choose the mode from the user's goal:

- `web-presentation`: creates a skill for static HTML web presentations with slide/reveal navigation.
- `pptx`: creates a skill for editable PowerPoint decks.
- `both`: creates either two coordinated skills or one skill with clearly separated web and PPTX references.

If the user is unsure, prefer separate skills: one for web presentation output and one for PPTX output. This keeps playback rules, QA, and scaffolds clean.

## Quick Workflow

1. Confirm the template input: PPTX template, PDF presentation template, or both.
2. Read `references/template-analysis.md` and inspect the template.
3. Extract reusable assets into the new skill's `assets/` folder.
4. Record the visual system in text: colors, fonts, logo zones, backgrounds, layouts, spacing, footer, and content rhythm.
5. For web output, read `references/web-presentation-skill-plan.md`.
6. For PPTX output, read `references/pptx-skill-plan.md`.
7. Use `scripts/bootstrap-template-skill.py` when useful to create the target skill skeleton.
8. Write the target skill's `SKILL.md`, `agents/openai.yaml`, references, scripts, and asset manifest.
9. Validate the target skill with `skill-creator`'s `quick_validate.py`.
10. Forward-test the target skill with a realistic request when practical.

## Core Rules

- Keep the target skill generic to the user's template, not to this helper skill.
- Do not leave the target skill dependent on the original PPTX/PDF template unless the user explicitly wants the original file bundled as reference-only material.
- Store reusable extracted assets in the target skill's `assets/` folder.
- Store design facts in text references so future agents can reproduce the style without rereading the template.
- Use progressive disclosure: keep the target `SKILL.md` short and put detailed visual rules, QA, examples, and workflows in `references/`.
- For PPTX template input, inspect editable objects when possible.
- For PDF template input, treat it as a visual template: infer style from rendered pages and extracted assets, and document uncertainty.
- Separate web-only concepts from PPTX-only concepts. Do not put HTML stage scaling rules into a PPTX skill, and do not put PowerPoint COM validation rules into a web skill.

## Bundled Resources

- `references/template-analysis.md`: how to analyze PPTX/PDF templates and extract reusable style facts.
- `references/web-presentation-skill-plan.md`: implementation plan for a static HTML web-presentation skill.
- `references/pptx-skill-plan.md`: implementation plan for an editable PPTX skill.
- `references/shared-workflows.md`: common evidence, outline, asset, usage example, and validation workflows.
- `scripts/bootstrap-template-skill.py`: creates a starter skill folder for `web-presentation`, `pptx`, or `both` mode.

## Common User Requests

- "Use this PPTX template to create a reusable web presentation skill."
- "Use this PDF slide template to create a PPTX generation skill."
- "Create both web and PowerPoint skills from this corporate deck template."
- "Analyze this presentation sample and make a skill that can reproduce its style without reloading the sample."
