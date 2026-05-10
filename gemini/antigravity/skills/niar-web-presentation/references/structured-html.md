# Structured HTML Rules

Use this reference when building the final `index.html`. The deck should be visually polished, interactive, and still readable as normal HTML.

## Required Structure

- Use one top-level `<main>` for the presentation viewport.
- Use one fixed stage container, usually `<section id="stage" class="stage">`.
- Use one semantic slide container per slide, usually `<article class="slide">` or `<section class="slide">`.
- Give every slide a real heading: `h1` for the cover, `h2` for normal slides, `h3` for cards or subsections.
- Connect slides to their heading with `aria-labelledby`.
- Use `<nav>` for controls.
- Mark decorative lines, background-only elements, and visual ornaments with `aria-hidden="true"`.

## Real Text

- Keep titles, body copy, captions, source notes, numbers, and labels as DOM text.
- Do not render main slide text into a bitmap, full-slide screenshot, or canvas.
- Do not use images for tables, bullet lists, or key numeric evidence.
- Text must be selectable and copyable in the browser.

## Data And Evidence

- Use real `<table>` for tabular data.
- Use `<ul>` / `<ol>` for lists when the content is actually list-like.
- Use `<figure>` and `<figcaption>` for charts, diagrams, photos, screenshots, or important visuals.
- If a chart uses SVG or Canvas, include visible DOM labels or a concise DOM text summary nearby.
- Preserve source notes in DOM text when the task depends on evidence.

## Canvas, SVG, And Motion

- Canvas is allowed for motion, particles, dynamic backgrounds, or specialized diagrams.
- SVG is allowed for icons, lines, maps, and diagrams.
- Canvas or SVG should not be the only copy of important narrative text.
- If a visual is decorative, mark it with `aria-hidden="true"`.

## Reveal Semantics

- Use `data-reveal` on the element that appears.
- Keep hidden reveal content in the DOM; do not inject all important content only after a click unless there is a good reason.
- The DOM order should match the reading order and narration order.

## Minimal Slide Pattern

```html
<article class="slide bg-white-wave" aria-labelledby="slide-02-title" data-title="核心訊息">
  <p class="page-label">02 / 核心訊息</p>
  <h2 id="slide-02-title">標題文字</h2>
  <div class="orange-rule" aria-hidden="true"></div>
  <section class="navy-panel" data-reveal="1">
    <h3>小標題</h3>
    <p>正文保留為可選取的 DOM 文字。</p>
  </section>
</article>
```
