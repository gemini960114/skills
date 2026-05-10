# NIAR PPTX Outline Format

Create `outline.md` before building unless the user already supplied a clear slide plan. This outline is a production blueprint for an editable PowerPoint deck, not a script for web-style interaction.

## Minimal Structure

```markdown
# <Presentation Title>

Audience:
Purpose:
Playback mode: PowerPoint live presentation / PDF handout / both
Requested slide count:
Source files:

## Slide 01 - <Title>
- Background: cover-gradient-wave-logo.png
- Recipe: cover / section / white two-column / photo / strategy cards / timeline / table / closing
- Goal:
- NIAR signals: background, logo, kicker, navy panel, orange rule, footer
- Content structure:
  - Title:
  - Main message:
  - Supporting points/data:
- Build/read order:
  1. <first thing audience should read>
  2. <second thing>
- Source / evidence:
- Notes:

## Slide 02 - <Title>
...
```

## Slide Fields

- `Background`: choose a bundled background PNG.
- `Recipe`: choose a NIAR layout recipe from `style-guide.md`.
- `Goal`: one sentence explaining what the slide should accomplish.
- `NIAR signals`: list the brand signals used.
- `Content structure`: title, key sentence, cards, table, photo, diagram, source note, or conclusion.
- `Build/read order`: the intended audience reading sequence. This is not mandatory animation.
- `Source / evidence`: source file, section, evidence row, or `inference`.
- `Notes`: optional speaker notes, image provenance, table caveats, or unresolved gaps.

## Build Order Guidance

Use build order to design the slide rhythm:

- Cover: title -> subtitle/date.
- Standard content: title -> key sentence -> cards/table/photo -> takeaway.
- Table/data: title -> data groups -> highlighted row/number -> takeaway.
- Timeline/process: title -> phases in order -> conclusion bar.
- Closing: title -> closing sentence -> contact/source if needed.

Do not add PowerPoint animations by default. Use animations only when explicitly requested or when they improve live explanation.

## Content Density

- One slide should have one primary goal.
- Split the slide when the audience needs to read more than one dense paragraph.
- Avoid shrinking body text below 10.5 pt to force content onto one slide.
- Prefer cards, rows, timelines, or follow-up slides over crowded bullet dumps.
- Use `white-footer-line-logo.png` when diagrams or tables need extra vertical room.

## Slide Count

Do not force a fixed slide count unless the user specified one. Choose slide count by content, audience, and presentation purpose.
