"""Rejected Olympic Sports — make.fun entry.

Writes one fixed funny line, a rejected Olympic sport, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt). Deterministic:
no randomness, no time, no network, Python 3.13 stdlib only.

The line: a made-up event plausible enough that a broadcaster
would have to explain it, with the twist landing in one read.
"""

import os
from pathlib import Path

ENTRY = (
    "Synchronized drowning: two swimmers, one pool, "
    "and judges scoring their panic in perfect unison."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    out_path = Path(output_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
