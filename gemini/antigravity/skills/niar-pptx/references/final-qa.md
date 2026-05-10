# NIAR PPTX Final QA

Use this checklist before delivering a NIAR-style `.pptx`. The goal is to catch failures that are easy to miss after staring at the deck: text collisions, blocked logos, low-contrast footers, and decks that look right as images but are not editable.

## Required Checks

1. **PowerPoint open check**
   - Open the final `.pptx` with PowerPoint COM when available.
   - Confirm the slide count matches the requested or intended count.
   - If COM is blocked, use `python-pptx` plus zip integrity as fallback and say COM was unavailable.

2. **Structure check**
   - Confirm zip integrity is OK.
   - Confirm every slide is inside the 16:9 page bounds.
   - Confirm there are no out-of-bounds shapes.
   - Confirm text is PowerPoint text boxes/shapes, not baked into a screenshot, except for the NIAR background PNGs.
   - Confirm titles, captions, source notes, table labels, and key numbers are editable PowerPoint text.
   - Confirm every non-cover slide has a clear title or purposeful headline.
   - Confirm tables are native PowerPoint tables or editable table-like shapes unless source limitations are documented.

3. **Placeholder and source-text check**
   - Search extracted text for `placeholder`, `lorem`, `ipsum`, `xxxx`, `Office 佈景`, and leftover template labels.
   - Check that slide titles and footer text match the new deck topic.
   - Check that the deck has no generic NIAR sample wording left behind.

4. **Visual render check**
   - Export slides to PNG or PDF-rendered images.
   - Inspect at least a contact sheet and any dense slides at full size.
   - Look specifically for overlapping text, clipped titles, text over the logo, content crossing footer/wave areas, and photo captions touching images.
   - Inspect dense table, timeline, diagram, and photo slides at full size.

5. **NIAR brand check**
   - Logo is visible and unobstructed on every slide.
   - Orange-red-gold gradient pages are used for cover/section/closing or high-impact pages.
   - White/cream pages are used for dense content.
   - Page number and footer placement are consistent.
   - Dark pages use light footer/page-number text.
   - Font is `Microsoft JhengHei` / `微軟正黑體` or documented fallback.
   - Each slide uses at least two NIAR identity signals beyond color alone, such as background, logo zone, kicker, navy panel, orange rule, footer, or wave ornament.

6. **Content and provenance check**
   - Deck answers the requested topic, not just a generic NIAR template.
   - Official or user-provided images are preferred and their provenance is clear.
   - If multiple source files were used, retain source filenames/sections in captions, notes, or a small source line when useful.
   - If many source files were used, check `evidence-table.md` or equivalent notes against the final slides.
   - Contradictions or missing evidence are marked as `待確認` rather than silently resolved.
   - Every slide has one primary goal; dense content is split into cards, tables, timelines, or additional slides instead of being shrunk unreadably.

## Suggested Validation Output

In the final response, include a compact status like:

```text
Validation:
- PowerPoint open-check: OK, slides=N
- Zip integrity: OK
- Out-of-bounds objects: 0
- Placeholder scan: no hits
- Structured editability: OK
- Visual QA: contact sheet/full-size dense pages checked
- Source trace: OK / not applicable
- Image provenance: official/user-provided/generated, as applicable
```

## Common Fixes

- **Title wraps into logo area:** reduce title width to end before `x=10.4 in`, lower font size, or split the title over two lines.
- **Footer unreadable on gradient slides:** switch page number and footer to cream/white.
- **Content collides with bottom wave:** move content up or use `white-footer-line-logo.png` for diagrams needing more vertical room.
- **Dense text looks off-brand:** split into cards, table rows, or a timeline instead of shrinking body text too much.
- **Claim lacks evidence:** add a source note/speaker note, soften wording, or mark `待確認`.
- **Table pasted as image:** rebuild as a native table or editable shapes unless extraction is impossible.
- **Photo page feels generic:** use a thin orange/gold/navy frame and a small gray caption; keep the photo aligned to the existing grid.
