# Template Analysis

Use this reference before writing the target skill. The goal is to convert a user-provided PPTX or PDF presentation template into reusable, text-described design knowledge plus reusable assets.

## Input Types

### PPTX Template

Prefer PPTX when available because it may contain editable objects, theme colors, fonts, layouts, masters, notes, and embedded images.

Inspect:

- Slide size and aspect ratio.
- Slide masters and layout names.
- Theme colors and font theme.
- Logo position and protected zones.
- Header, footer, page number, section label, date, confidentiality label.
- Title hierarchy and text styles.
- Background images and decorative layers.
- Shape styles: fills, borders, line widths, shadows, opacity, corner radius.
- Tables, charts, diagrams, icons, and image frames.
- Animation/build order if relevant.

### PDF Presentation Template

Use PDF when the user only has a rendered deck. A PDF is a visual source, not a full editable-template source.

Inspect:

- Page size and aspect ratio.
- Rendered pages as images.
- Visible logo position and protected zones.
- Colors, typography, footer/page number, layout rhythm.
- Reusable backgrounds or decorative regions.
- Repeated slide patterns.
- Approximate coordinates and spacing.

Document uncertainty when the PDF does not reveal original fonts, editable objects, or master layouts.

## Extract Reusable Assets

Export or save:

- Full-slide backgrounds.
- Logo variants.
- Decorative layers.
- Icon examples if reusable.
- Reference screenshots for documentation only.

Recommended target skill structure:

```text
assets/
├── backgrounds/
├── logos/
└── examples/
```

Do not use reference screenshots as final slide content unless the user explicitly accepts image-only reproduction.

## Record Design Facts

Create a style reference that includes:

- Canvas/stage size.
- Coordinate system.
- Safe margins.
- Logo protected zone.
- Color tokens.
- Typography table.
- Title/body/caption/footer hierarchy.
- Layout recipes.
- Image treatment.
- Table/chart style.
- Content density limits.
- Common mistakes to avoid.

Coordinates are starting points, not hard locks. Preserve the template identity and protected zones, but adjust within safe areas when real content is longer than the sample copy.

## Decide Output Mode

Use `web-presentation` when the final target is browser playback, recording, client demos, or interactive reveal-by-click.

Use `pptx` when the final target is editable PowerPoint, official deck delivery, normal PowerPoint playback, or PDF export from PowerPoint.

Use `both` only when the user clearly wants reusable skill support for both formats.

## Minimum Analysis Output

Before creating the target skill, produce or internally maintain:

```text
template-analysis-notes.md
asset-manifest.md
visual-system.md or style-guide.md
layout-recipes.md
final-qa.md draft
```
