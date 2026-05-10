---
name: niar-pptx
description: Create editable PowerPoint decks that reproduce the NIAR / 國家實驗研究院 visual style without loading niar.pptx. Use when Codex needs to build or restyle evidence-grounded .pptx slides using the NIAR orange-red-gold wave backgrounds, fixed top-right NIAR logo area, Microsoft JhengHei typography, white/dark slide rhythm, page footer system, structured editable PowerPoint objects, and bundled reusable PNG backgrounds.
---

# NIAR PPTX

Use this skill to make a new editable PowerPoint that looks like the `niar.pptx` brand deck without reading that original PPTX.

## Required Companion Skill

When creating or editing a `.pptx`, also use the project `pptx` skill for PPTX mechanics and validation. This skill only supplies the NIAR visual system, reusable backgrounds, and layout recipes.

## Quick Workflow

1. Read `references/style-guide.md` before designing slides.
2. Read `references/asset-manifest.md` when choosing a background PNG.
3. If the user provides many files or a folder, read `references/multi-document-workflow.md` and create source/evidence notes before writing slides.
4. Read `references/outline-format.md`; create a slide map/outline unless the user already supplied a clear slide plan.
5. Read `references/structured-pptx.md`; build all content as editable PowerPoint objects above the background image.
6. Use the bundled PNG files in `assets/backgrounds/` as full-slide backgrounds whenever possible.
7. Before final delivery, follow `references/final-qa.md` and report the validation results.

## Core Rules

- Use 16:9 widescreen at `13.333 x 7.5 in`.
- Use `Microsoft JhengHei` / `微軟正黑體`; fallback to `Microsoft YaHei` only if needed.
- Preserve the top-right NIAR logo area. Most bundled backgrounds already contain the logo; do not draw text over it.
- Use the NIAR rhythm: orange-red-gold full-bleed pages for cover, section, and closing; white/cream pages with faint wave ornaments for dense content.
- Put page numbers at bottom-left and a small footer label beside them.
- Keep text editable. Do not rasterize slide text into images.
- Keep each slide purposeful: one primary goal, readable density, and a clear reading/build order.
- For data and source-heavy decks, keep claims traceable to source files, captions, notes, or an evidence table.
- Use structured editable PowerPoint objects: real text boxes, table objects or editable table-like shapes, chart labels, captions, and grouped diagram parts.
- Prefer official/event imagery for photos. Place photos inside clean rectangular frames with thin orange, gold, or navy borders.

## Bundled Resources

- `assets/backgrounds/`: reusable PNG backgrounds extracted from `niar.pptx`.
- `references/style-guide.md`: detailed style system, dimensions, typography, colors, and layout recipes.
- `references/asset-manifest.md`: text description of each background PNG and when to use it.
- `references/multi-document-workflow.md`: evidence-driven workflow for many uploaded files.
- `references/outline-format.md`: required slide map fields, content density rules, and build-order guidance.
- `references/structured-pptx.md`: editable PowerPoint object rules for text, tables, charts, diagrams, sources, and optional animations.
- `references/usage-examples.md`: user-facing usage guide with 10 copy-paste prompt examples.
- `references/final-qa.md`: required final validation checks for NIAR-style PPTX delivery.
- `scripts/copy_assets.py`: copy NIAR assets into a working folder and print the manifest.

## Common User Requests

- "用 NIAR / 國研院風格做一份簡報"
- "不要讀 niar.pptx，直接套用既有 NIAR 樣式"
- "沿用 niar.pptx 的 Logo、底圖、配色、字型、頁碼和版面節奏"
- "把這份內容做成可編輯 PowerPoint，像 niar.pptx 那套品牌簡報"
