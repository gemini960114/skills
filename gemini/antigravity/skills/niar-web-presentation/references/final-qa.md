# Final QA

Run these checks before delivering a NIAR web presentation.

## Static HTML Runtime

- `index.html` exists and can be opened directly from the file system.
- Required assets are present under `assets/niar/backgrounds/`.
- Browser opens the presentation without a dev server.
- No console errors that break navigation or rendering.
- If the user explicitly requested Vite / React / TypeScript, `npm run build` may be added as an extra check, but it is not part of the default workflow.

## Interaction

- `Space` / `ArrowRight` advances reveal first, then next slide.
- `ArrowLeft` reverses reveal first, then previous slide.
- Mouse click left/right works.
- `Home`, `End`, `R`, and `C` work if implemented.
- Cursor persistence works or is intentionally disabled and documented.
- `deckVersion` prevents stale cursor problems after slide/reveal changes.

## HTML Structure

- Slide content is structured as semantic HTML, not flattened into a screenshot, bitmap, or all-canvas surface.
- Main presentation uses `<main>`, slide containers use `<article>` or `<section>`, and controls use `<nav>`.
- Every slide has a real `h1`/`h2` heading and an `aria-labelledby` relationship.
- Important text is selectable/copyable DOM text.
- Tables use real `<table>` elements; lists use `<ul>` / `<ol>` when appropriate.
- Decorative dividers or ornaments use `aria-hidden="true"`.
- Canvas/SVG visuals have nearby DOM labels, captions, or summaries when they carry meaning.

## Visual

- Stage is fixed 16:9 and scales without distortion.
- Stage remains visually centered at `1920 x 1080`, `1366 x 768`, and `1280 x 720` viewports.
- Stage uses absolute center positioning with `translate(-50%, -50%) scale(...)`, or an equivalent tested method.
- Page has no scrollbars during playback.
- First screen is the presentation, not a landing page.
- Each slide has at least two NIAR identity signals beyond color alone.
- Top-right NIAR logo/brand area is unobstructed.
- Deep navy panels have readable white/cream text.
- White content pages do not crowd the lower wave area.
- Text, panels, metrics, and reveal elements do not overlap or drift outside the safe area.
- Controls are hidden by default and never cover the logo area.
- `?clean=1` or equivalent clean mode hides controls for playback/recording.

## Content

- Slide count and reveal rhythm match the user's request and audience.
- Every slide has one clear goal.
- Reveals add meaning; no arbitrary animation-only steps.
- No placeholder/lorem/TODO content remains.
- If many documents were used, `evidence-table.md` traces content to sources.
- Contradictions or missing evidence are marked as `待確認`.

## Suggested Final Report

```text
Validation:
- Direct HTML open: OK
- Browser playback: OK
- Viewport centering/scaling: OK
- Navigation/reveals: OK
- Clean mode: OK
- Structured HTML/readability: OK
- NIAR identity check: OK
- Source trace: OK / not applicable
```
