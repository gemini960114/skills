#!/usr/bin/env python
"""Copy bundled NIAR PPTX visual assets into a working directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
BACKGROUND_DIR = SKILL_DIR / "assets" / "backgrounds"
MANIFEST = SKILL_DIR / "references" / "asset-manifest.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy NIAR background PNG assets.")
    parser.add_argument("output_dir", help="Directory to receive the NIAR background assets")
    parser.add_argument("--manifest", action="store_true", help="Also copy asset-manifest.md")
    args = parser.parse_args()

    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    copied = []
    for src in sorted(BACKGROUND_DIR.glob("*.png")):
        dst = out / src.name
        shutil.copy2(src, dst)
        copied.append(dst)

    if args.manifest:
        shutil.copy2(MANIFEST, out / MANIFEST.name)

    print(f"copied {len(copied)} NIAR background assets to {out}")
    for path in copied:
        print(path)


if __name__ == "__main__":
    main()
