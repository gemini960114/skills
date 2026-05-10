# Web Presentation Skill Plan

Use this plan to create a target skill that generates static HTML web presentations from a PPTX/PDF template style.

## Target Skill Goal

The target skill should create browser-playable presentations that visually follow the user's template while remaining:

- Static and directly openable.
- Interactive with next/previous and per-slide reveal steps.
- Structured as semantic HTML.
- Readable and selectable.
- Suitable for live playback and screen recording.

Default output:

```text
index.html
assets/
outline.md
```

Do not make `npm install`, `npm run dev`, Vite, or React the default user workflow.

## Target Skill Structure

```text
<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── backgrounds/
│   ├── logos/
│   └── examples/
├── references/
│   ├── visual-system.md
│   ├── asset-manifest.md
│   ├── interaction-model.md
│   ├── structured-html.md
│   ├── multi-document-workflow.md
│   ├── outline-format.md
│   ├── scene-patterns.md
│   ├── final-qa.md
│   └── usage-examples.md
└── scripts/
    └── scaffold-<skill-name>.py
```

## Required References

### `visual-system.md`

Document:

- Stage size, usually `1920 x 1080`.
- Coordinate system and safe areas.
- Logo protected zone.
- CSS color tokens.
- Typography rules.
- Header/footer positions.
- Layout recipes.
- Content density rules.
- Responsive/scaling rules.
- Avoid list.

### `asset-manifest.md`

For each asset:

```text
File:
Source:
Size:
Use:
Visual description:
Do / do not:
Recommended path:
```

### `interaction-model.md`

Use:

- `slideIndex + revealIndex`.
- Right click area / `Space` / `ArrowRight`: next.
- Left click area / `ArrowLeft`: previous.
- `Home`, `End`, `R`, `C`.
- Hidden controls by default.
- Clean mode.

Stage centering:

```js
stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
```

Do not rely on CSS Grid as the primary stage-centering mechanism.

### `structured-html.md`

Require:

- `<main>` for viewport.
- Fixed stage container.
- Semantic slide containers.
- Real headings.
- `aria-labelledby`.
- `<nav>` controls.
- DOM text for important content.
- Real `<table>` for tabular data.
- `<figure>` / `<figcaption>` for meaningful visuals.
- `aria-hidden="true"` for decorative elements.

### `outline-format.md`

Use fields:

```markdown
Audience:
Purpose:
Playback mode:
Source files:

## Slide 01 - <Title>
- Background:
- Scene type:
- Goal:
- Template signals:
- Reveals:
- Visual notes:
- Source / evidence:
```

### `scene-patterns.md`

Document reusable scene types from the template:

- Cover.
- Section divider.
- Key message.
- Two-column.
- Photo plus text.
- Data/table.
- Timeline/process.
- Cards.
- Comparison.
- Closing.

## Scaffold Script

Create `scripts/scaffold-<skill-name>.py`.

It should create:

- `index.html`.
- `assets/<skill-name>/...` or `assets/...`.
- `outline.md`.
- Optional output README.

Generated HTML should include:

- Fixed `1920 x 1080` stage.
- Absolute center scaling.
- Several template-style sample slides.
- Hidden/hover controls.
- Keyboard and click navigation.
- Reveal steps.
- Clean mode.
- Semantic HTML.
- Local asset paths.

## Final QA

Check:

- Direct HTML open.
- Assets present.
- No console-breaking errors.
- Navigation/reveals.
- Clean mode.
- Stage centered at `1920 x 1080`, `1366 x 768`, and `1280 x 720`.
- No scrollbars.
- Template identity visible.
- Protected logo zones clear.
- Text selectable and structured.
- Tables are real HTML.
- No placeholder text.
- Source trace when many files were used.

Suggested validation report:

```text
Validation:
- Direct HTML open: OK
- Navigation/reveals: OK
- Viewport centering/scaling: OK
- Structured HTML/readability: OK
- Template identity check: OK
- Source trace: OK / not applicable
```
