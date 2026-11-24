#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry (account A).

Writes one original one-line excuse from a robot vacuum for missing a spot
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys


def build_line() -> str:
    """Return the excuse: one line, first person, vacuum's own world.

    The joke is rooted in the vacuum's own hardware: its cliff sensor
    mistakes the rug's shadow for a drop, so it logs the spot as a
    staircase and refuses to cross it — a deadpan machine keeping a
    straight face about a very small, very specific failure.
    """
    return (
        "I did not miss that spot. My cliff sensor saw the rug's shadow "
        "and filed it as a staircase."
    )


def validate(line: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1 to 140 characters,
    not only whitespace, a single line, printable, ending in terminal
    punctuation."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 140:
        raise ValueError(f"entry is {len(line)} characters, over the 140 limit")
    if len(line) < 1:
        raise ValueError("entry must be at least 1 character")
    if not all(ch.isprintable() for ch in line):
        raise ValueError("entry must contain only printable characters")
    if line[-1] not in ".!?":
        raise ValueError("entry must end in terminal punctuation")
    line.encode("utf-8")  # raises if not valid UTF-8


def write_entry() -> str:
    """Validate the line and write it to entry.txt. Returns the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry()
    print(f"Wrote {path} ({len(build_line())} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
