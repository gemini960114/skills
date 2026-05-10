#!/usr/bin/env python
"""Create a starter skill folder for a template-based presentation skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from textwrap import dedent


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9-]+", "-", value.strip().lower()).strip("-")
    return value or "template-presentation-skill"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).lstrip(), encoding="utf-8")


def target_files(mode: str) -> list[str]:
    common = [
        "references/asset-manifest.md",
        "references/multi-document-workflow.md",
        "references/outline-format.md",
        "references/final-qa.md",
        "references/usage-examples.md",
    ]
    if mode == "web-presentation":
        return common + [
            "references/visual-system.md",
            "references/interaction-model.md",
            "references/structured-html.md",
            "references/scene-patterns.md",
            "scripts/scaffold-template-web-presentation.py",
        ]
    if mode == "pptx":
        return common + [
            "references/style-guide.md",
            "references/structured-pptx.md",
            "scripts/copy_assets.py",
        ]
    return common + [
        "references/web/visual-system.md",
        "references/web/interaction-model.md",
        "references/web/structured-html.md",
        "references/web/scene-patterns.md",
        "references/pptx/style-guide.md",
        "references/pptx/structured-pptx.md",
        "scripts/scaffold-template-web-presentation.py",
        "scripts/copy_assets.py",
    ]


def skill_description(mode: str) -> str:
    if mode == "web-presentation":
        return "Build static HTML web presentations that reproduce a captured presentation template style, with slide navigation, reveal steps, reusable assets, structured HTML, and evidence-driven source handling."
    if mode == "pptx":
        return "Create editable PowerPoint decks that reproduce a captured presentation template style, using reusable backgrounds/assets, structured editable PPTX objects, and evidence-driven source handling."
    return "Create static HTML web presentations and editable PowerPoint decks that reproduce a captured presentation template style, with separate web and PPTX workflows, reusable assets, and evidence-driven source handling."


def create_skill(out: Path, name: str, mode: str) -> None:
    skill_name = slugify(name)
    root = out / skill_name
    root.mkdir(parents=True, exist_ok=True)
    (root / "assets" / "backgrounds").mkdir(parents=True, exist_ok=True)
    (root / "assets" / "logos").mkdir(parents=True, exist_ok=True)
    (root / "assets" / "examples").mkdir(parents=True, exist_ok=True)

    write(
        root / "SKILL.md",
        f"""
        ---
        name: {skill_name}
        description: {skill_description(mode)}
        ---

        # {skill_name}

        Use this skill to create presentations that follow the captured template style without reloading the original template.

        ## Quick Workflow

        1. Read the relevant visual/style reference.
        2. Read `references/asset-manifest.md` before choosing assets.
        3. For many source files, follow `references/multi-document-workflow.md`.
        4. Create or update `outline.md` before implementation unless the user supplied a clear plan.
        5. Build the requested output while preserving template identity and editability/readability.
        6. Follow `references/final-qa.md` before delivery.

        ## Core Rules

        - Use extracted assets from `assets/`.
        - Preserve template identity signals such as logo, typography, color, background rhythm, footer, and layout recipes.
        - Treat coordinates as starting points, not hard locks.
        - Keep claims traceable when source documents are used.
        - Do not rely on the original template file unless the user explicitly provides it for a refresh.
        """,
    )

    write(
        root / "agents" / "openai.yaml",
        f"""
        interface:
          display_name: "{skill_name}"
          short_description: "Template-based presentation skill"
          default_prompt: "Use ${skill_name} to create a presentation following the captured template style."
        """,
    )

    for rel in target_files(mode):
        path = root / rel
        if path.suffix == ".py":
            write(path, "#!/usr/bin/env python\n\"\"\"TODO: implement reusable helper for this template skill.\"\"\"\n")
        else:
            title = path.stem.replace("-", " ").title()
            write(path, f"# {title}\n\nTODO: Fill this reference from the analyzed PPTX/PDF template.\n")

    print(root)


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap a template-based presentation skill folder.")
    parser.add_argument("name", help="Target skill name")
    parser.add_argument("--mode", choices=["web-presentation", "pptx", "both"], default="web-presentation")
    parser.add_argument("--out", default=".", help="Output directory that will contain the skill folder")
    args = parser.parse_args()

    create_skill(Path(args.out).resolve(), args.name, args.mode)


if __name__ == "__main__":
    main()
