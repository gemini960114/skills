# Evidence-Driven Multi-Document Workflow

Use this when the user provides many files, a folder, or mixed source materials. The goal is to avoid hallucinated or untraceable presentations.

Do not expose hidden chain-of-thought. Provide checkable artifacts instead: file inventory, evidence table, gaps, and outline.

## Required Artifacts

Create these before implementation when the input is large or mixed:

```text
source-inventory.md
evidence-table.md
outline.md
```

## Workflow

1. **Inventory**
   - List all source files.
   - Note file type, readable status, and likely topics.
   - Flag missing, unreadable, password-protected, or unsupported files.

2. **Query Plan**
   - Convert the user's goal into 3-8 extraction questions.
   - Examples: background, current progress, data, timeline, stakeholders, risks, decisions, open issues.

3. **Extract**
   - Search/read sources by question.
   - Extract concise evidence, numbers, dates, tables, image candidates, and direct source locations.

4. **Observe Gaps**
   - Mark missing data, contradictory claims, ambiguous dates, missing units, or unsupported conclusions.

5. **Iterate**
   - Search again for gaps.
   - If still unresolved, keep a `待確認` item instead of inventing.

6. **Synthesize**
   - Organize by presentation logic, not file order.
   - Group evidence into a story: why it matters, what happened, what evidence supports it, what decision is needed.

7. **Outline**
   - Convert the synthesis into slide goals and reveal steps.
   - Map each slide to evidence rows.

8. **Build and QA**
   - Build the static HTML web deck.
   - Check source trace against slides.

## Evidence Table Format

| Topic | Evidence Summary | Source File | Location | Used In Slide | Confidence / Issue |
|---|---|---|---|---|---|

## Source Inventory Format

| File | Type | Status | Relevant Topics | Notes |
|---|---|---|---|---|

## Rules

- Do not make a slide from a claim unless it has evidence or is clearly marked as inference.
- Preserve source filenames/sections in notes, captions, or the evidence table.
- When sources conflict, mark the conflict and choose a conservative slide wording.
- Use visuals only after evidence is clear.
