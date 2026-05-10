---
name: niar-web-presentation
description: Build NIAR / 國家實驗研究院 style static HTML web slide presentations for live browser playback and screen recording. Use when Codex needs to create a no-npm 16:9 NIAR-branded HTML presentation with next/previous slide navigation, per-slide reveal steps, hidden/hover presentation controls, reusable NIAR PNG backgrounds, and evidence-driven handling of articles or many uploaded source files.
---

# NIAR Web Presentation

Use this skill to build a NIAR-style **web slide presentation**: a static HTML presentation folder that can be opened directly in a browser for clients or recorded with desktop screen recording tools.

The default deliverable is `index.html` plus an `assets/` folder. End users should not need `npm install`, `npm run dev`, a local server, or a build step. DOM, Canvas, plain JavaScript, or bundled/minified libraries are acceptable when they remain directly openable as local HTML. Vite / React / TypeScript is an advanced developer-only option when the user explicitly asks for a source app.

It is not a PPTX generator. For PowerPoint output, use `niar-pptx` plus the project `pptx` skill.

## Quick Workflow

1. Identify the input type: simple topic, article, existing script, single document, many documents, or existing deck.
2. If the user provides many files, read `references/multi-document-workflow.md` and create source/evidence notes before writing slides.
3. Read `references/visual-system.md`, `references/asset-manifest.md`, and `references/structured-html.md`; the output must look NIAR at first glance while remaining readable, selectable, and maintainable.
4. Read `references/outline-format.md`; create or update `outline.md` before implementation unless the user asks for immediate coding from an already clear outline.
5. Build a static HTML presentation. Use `scripts/scaffold-niar-web-presentation.py` for the starting folder when useful.
6. Implement slide navigation as `slideIndex + revealIndex`: click/keyboard advances reveal first, then next slide.
7. Keep controls hidden by default and available on hover; support clean playback/recording mode.
8. Before delivery, follow `references/final-qa.md` and report the validation results.

## Core Rules

- Use a fixed `1920 x 1080` stage scaled to the viewport.
- Center the scaled stage with absolute positioning plus `translate(-50%, -50%) scale(...)`; do not rely on CSS Grid centering for the stage.
- Support live presentation: previous/next, keyboard navigation, and per-slide reveal steps.
- Support screen-recording-friendly playback: clean stage, hidden chrome, stable 16:9 framing.
- Use the bundled backgrounds in `assets/backgrounds/`; do not rely only on text descriptions.
- Preserve NIAR identity: right-top logo/brand area, orange-red-gold backgrounds, white content pages, dark navy panels, small section labels, orange accent lines, and Microsoft JhengHei typography.
- Do not make a landing page. The first screen is the presentation.
- Prefer one portable `index.html` for the deck; multi-page HTML is acceptable only when it improves organization and still works by opening local files.
- Do not make npm, Vite, React, TypeScript, or a dev server part of the normal user workflow.
- Keep the presentation as structured HTML: use semantic sections, real text, real tables/lists, and accessible labels. Do not flatten slide content into images or canvas.
- Treat standard coordinates as layout starting points, not hard locks. If content is long, split it across slides/reveals or adjust panel size within the safe area instead of forcing overlap.
- Avoid one-shot bullet dumps. Reveal elements in meaningful steps.
- Do not expose hidden chain-of-thought. For many documents, provide source inventory, evidence table, gaps, and outline instead.

## Bundled Resources

- `assets/backgrounds/`: NIAR PNG backgrounds copied from the NIAR PPTX visual system.
- `references/visual-system.md`: NIAR web visual rules and brand identity checks.
- `references/asset-manifest.md`: background image descriptions and use cases.
- `references/interaction-model.md`: slide/reveal cursor, keyboard, mouse, clean mode, persistence.
- `references/structured-html.md`: semantic HTML, selectable text, real tables, accessibility labels, and canvas/SVG guardrails.
- `references/multi-document-workflow.md`: evidence-driven workflow for many uploaded files.
- `references/outline-format.md`: required `outline.md` structure.
- `references/scene-patterns.md`: NIAR-style slide and reveal patterns.
- `references/final-qa.md`: required static HTML, browser, visual, and evidence checks.
- `references/usage-examples.md`: copy-paste user prompt examples.
- `scripts/scaffold-niar-web-presentation.py`: create a starter static HTML deck and copy NIAR backgrounds.

## Common User Requests

- "用 NIAR 風格做一份網頁投影片，可以播放給客戶看"
- "把這份文件做成可點擊播放的 web slide，每頁元素依序出現"
- "從一堆文件整理成 NIAR 風格網頁簡報"
- "做一份可以現場展示，也適合桌面錄影的 NIAR web presentation"
