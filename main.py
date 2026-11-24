#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = (
    "I hit reply all to say 'please don't reply all.' Four people asked to be "
    "removed; one asked who please was."
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"

    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    target = output_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
