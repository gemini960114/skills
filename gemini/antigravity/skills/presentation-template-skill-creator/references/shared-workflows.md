# Shared Workflows

These workflows apply to both web-presentation and PPTX target skills.

## Evidence Workflow

Use when the final presentation is built from many files.

Required artifacts:

```text
source-inventory.md
evidence-table.md
outline.md
```

Steps:

1. Inventory source files.
2. Convert the user's goal into extraction questions.
3. Extract evidence, numbers, dates, tables, image candidates, and source locations.
4. Mark contradictions and gaps.
5. Synthesize by presentation logic.
6. Build an outline.
7. Build the final output.
8. Check slides against evidence.

## Usage Examples

Each target skill should include examples for:

- Simple topic.
- Single document.
- Many documents.
- Data/table extraction.
- Existing deck restyle.
- Executive briefing.
- Client or public presentation.

## Target Skill Validation

Always run:

```powershell
python C:\Users\c00cjz00\.codex\skills\.system\skill-creator\scripts\quick_validate.py <skill-folder>
```

Also verify:

- `SKILL.md` routes to all references.
- `agents/openai.yaml` matches the target skill.
- Assets exist and match `asset-manifest.md`.
- The target skill can work without reloading the original PPTX/PDF template.

## Forward Test Prompt

Use a realistic request:

```text
Use $<target-skill-name> at <target-skill-path> to create a presentation from <source-file>.
Follow the captured template style. Keep the output editable/readable and report validation results.
```

Review whether the output:

- Looks like the template.
- Preserves editability or structured HTML as appropriate.
- Handles evidence and sources.
- Passes final QA.
