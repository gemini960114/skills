# Structured PPTX Rules

Use this reference when building the final `.pptx`. The deck should look polished and still remain editable, searchable, and maintainable in PowerPoint.

## Editable Object Rules

- Keep all titles, body text, captions, source notes, labels, and numbers as PowerPoint text.
- Do not bake slide text into screenshots or raster images.
- Use the bundled NIAR background PNGs as backgrounds only; place editable content above them.
- Keep decorative shapes separate from content shapes when possible.
- Group related diagram parts only after ensuring individual text elements remain editable.

## Slide Structure

Every slide should have:

- A title or purposeful cover/closing headline.
- A clear content hierarchy: title, key sentence, supporting cards/table/photo/diagram, source/caption when needed.
- A consistent footer/page number unless the user explicitly asks for a cover without footer.
- An intentional reading order from top-left to main content to takeaway.

## Tables And Data

- Prefer native PowerPoint tables for tabular data when practical.
- Editable table-like shapes are acceptable when they better match the NIAR visual style.
- Do not paste a table as an image unless the user supplied an image-only table and no reliable extraction is possible.
- Keep units, dates, and data sources visible or in speaker notes.
- Highlight key rows/columns with NIAR orange, gold, teal, or navy accents.

## Charts And Diagrams

- Prefer editable shapes, connectors, labels, and chart elements.
- If using a chart image from a source document, add editable labels/captions around it and document provenance.
- Diagrams should preserve editable labels and connectors.
- Keep important numbers and labels as text even when the visual anchor is an image.

## Images

- Use official, user-provided, or clearly sourced imagery where possible.
- Place photos in clean rectangular frames with thin orange, gold, teal, or navy borders.
- Add a small editable caption or source note when provenance matters.
- Do not let photos, captions, or icons cover the top-right NIAR logo zone.

## Optional Animation

PowerPoint animation is optional, not the default. The deck must read correctly with all objects visible.

Use animations only when:

- The user asks for animation.
- A live explanation benefits from staged build-up.
- The animation does not break PDF export or handout readability.

When animation is used, keep the build order simple and aligned with `outline.md`.

## Validation Hints

- Extract text from the PPTX package or use PowerPoint automation to confirm text is present.
- Render slides to images to catch overlaps, but do not treat rendered images as proof of editability.
- Inspect dense table, chart, and diagram slides at full size.
