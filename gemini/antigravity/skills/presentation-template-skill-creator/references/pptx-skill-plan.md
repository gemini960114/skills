# PPTX Skill Plan

Use this plan to create a target skill that generates editable PowerPoint decks from a PPTX/PDF template style.

## Target Skill Goal

The target skill should create `.pptx` files that:

- Open normally in PowerPoint.
- Visually follow the user's template.
- Keep titles, body text, tables, labels, captions, and source notes editable.
- Preserve template identity: logo, footer, page number, typography, colors, backgrounds, and layout rhythm.
- Support normal PowerPoint playback and PDF export.

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
│   ├── style-guide.md
│   ├── asset-manifest.md
│   ├── multi-document-workflow.md
│   ├── outline-format.md
│   ├── structured-pptx.md
│   ├── final-qa.md
│   └── usage-examples.md
└── scripts/
    └── copy_assets.py
```

## Required References

### `style-guide.md`

Document:

- Canvas size and EMU dimensions.
- Safe margins and protected zones.
- Color table.
- Typography table.
- Header/footer rules.
- Background rhythm.
- Slide recipes with coordinates.
- Content density rules.
- Common fixes.

Coordinates are starting points, not hard locks.

### `asset-manifest.md`

Clearly distinguish:

- Final-use backgrounds.
- Logo assets.
- Reference-only screenshots.
- Table/style screenshots that should be recreated as editable objects.

### `outline-format.md`

Use:

```markdown
Audience:
Purpose:
Playback mode: PowerPoint live presentation / PDF handout / both
Requested slide count:
Source files:

## Slide 01 - <Title>
- Background:
- Recipe:
- Goal:
- Template signals:
- Content structure:
- Build/read order:
- Source / evidence:
- Notes:
```

`Build/read order` means intended reading sequence. It does not require animation.

### `structured-pptx.md`

Require:

- PowerPoint text for titles, body copy, captions, notes, labels, and numbers.
- No screenshots for main slide text.
- Background images allowed; editable content above them.
- Native tables or editable table-like shapes.
- Editable chart labels and diagram connectors where practical.
- Important labels remain editable even when source visuals are image-based.
- Animation optional, not default.

### `multi-document-workflow.md`

For many source files, require:

```text
source-inventory.md
evidence-table.md
outline.md
```

Synthesize by presentation logic, not file order.

## Helper Scripts

Create `scripts/copy_assets.py`.

It should:

- Copy assets into a working folder.
- Print a manifest.
- Avoid destructive operations.
- Not require the original template after assets are extracted.

Optional scripts:

- `inspect_template.py`.
- `render_contact_sheet.py`.
- `validate_pptx_structure.py`.

Only include scripts that are likely to be reused.

## Final QA

Check:

1. PowerPoint open check.
2. Slide count.
3. Zip integrity.
4. Slide size.
5. No out-of-bounds shapes.
6. Structured editability.
7. Placeholder scan.
8. Visual render/contact sheet check.
9. Template identity check.
10. Content/provenance check.

Suggested validation report:

```text
Validation:
- PowerPoint open-check: OK, slides=N
- Zip integrity: OK
- Out-of-bounds objects: 0
- Structured editability: OK
- Placeholder scan: no hits
- Visual QA: contact sheet/full-size dense pages checked
- Source trace: OK / not applicable
- Image provenance: official/user-provided/generated, as applicable
```
