# NIAR Web Visual System

The top priority is **NIAR at first glance**. A deck that only borrows the NIAR colors but lacks the backgrounds, logo area, section labels, navy panels, orange accents, and white-page rhythm is a miss.

## Stage

- Author at `1920 x 1080`.
- Scale the whole stage uniformly to the viewport.
- Do not use a responsive web layout as the primary composition.
- The first screen is the presentation, not a landing page.

## Stage Implementation

Use absolute center positioning for the fixed stage. This is more reliable than CSS Grid centering when a `1920 x 1080` stage is scaled down inside small browser windows.

```css
.viewport {
  position: fixed;
  inset: 0;
  overflow: hidden;
}

.stage {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1920px;
  height: 1080px;
  transform-origin: center center;
}
```

```js
function resizeStage() {
  const scale = Math.max(0.1, Math.min(window.innerWidth / 1920, window.innerHeight / 1080));
  stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
}
```

Do not set `.viewport { display: grid; place-items: center; }` as the primary stage centering mechanism. In some browsers and zoom states, a large scaled stage can appear offset.

## Brand Identity Signals

Every deck should combine several of these on most slides:

- Full-stage NIAR background PNG.
- Top-right NIAR logo / brand area, unobstructed.
- Small section label / kicker at top-left.
- Large Microsoft JhengHei title.
- Short orange accent rule under the title.
- Dark navy `#0E2841` panels or cards on gradient pages.
- White/cream content pages with faint wave lines and generous whitespace.
- Orange-red-gold gradient pages for cover, section, and closing.

QA rule: each slide should have at least two NIAR identity signals beyond color alone.

## Color Tokens

```css
:root {
  --niar-navy: #0e2841;
  --niar-teal: #156082;
  --niar-orange: #e97132;
  --niar-gold: #f0c23a;
  --niar-red: #a80022;
  --niar-green: #196b24;
  --niar-cyan: #0f9ed5;
  --niar-cream: #f7f4ea;
  --niar-gray: #666666;
  --niar-black: #000000;
  --niar-font: "Microsoft JhengHei", "Microsoft YaHei", system-ui, sans-serif;
}
```

## Typography

- Font: `Microsoft JhengHei` / `微軟正黑體`.
- Fallback: `Microsoft YaHei`, then system sans-serif.
- Cover title: 64-82 px.
- Slide title: 52-70 px.
- Section label / kicker: 20-26 px.
- Body: 28-38 px.
- Caption/source: 18-22 px.
- Use normal letter spacing.

## Standard Positions

Coordinates are for the 1920 x 1080 stage.

Use these as starting positions, not immutable locks. Preserve the logo protected zone and overall NIAR rhythm, but adjust panel height, column width, or slide count when real content is longer than the example copy.

- Logo protected zone: `x=1500-1885`, `y=40-145`.
- Kicker: `x=104`, `y=72`, width up to `600`, 20-24 px.
- Title: `x=104`, `y=112`, width usually `1050-1280`, 56-70 px.
- Orange title rule: `x=104`, `y=218`, `w=190-280`, `h=10-14`.
- Left navy cover panel: `x=110`, `y=205`, `w=900`, `h=500`.
- Main content safe area: `x=100-1800`, `y=170-900`.
- Avoid dense content below `y=900` on wave backgrounds.

## Slide Rhythm

Use a mixed sequence:

- Cover: gradient, navy title panel.
- Key message / section: gradient or dark bokeh, white text.
- Content: white/cream background, navy title, cards or two columns.
- Data / process: white-footer-line background, clean timeline/table.
- Closing: closing-gradient background, navy panel and optional photo/frame.

## Layout Resilience

- Keep all meaningful text inside the stage safe area after every reveal.
- If content becomes dense, split it into more slides or more reveal steps instead of shrinking body text below 24 px.
- Validate at `1920 x 1080`, `1366 x 768`, and `1280 x 720` browser viewports.
- Verify there is no page scroll, stage drift, clipped control bar, or text overlap after scaling.
- Controls may sit near the bottom center, but must never cover the logo protected zone or essential content.

## Avoid

- Generic website hero sections.
- Purple/blue SaaS gradients unrelated to NIAR.
- Over-rounded cards and decorative blobs.
- Fixed visible navbar/header/footer chrome.
- All bullets appearing at once.
- Text or controls covering the top-right NIAR logo area.
