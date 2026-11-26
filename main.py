#!/usr/bin/env python3
"""The Printer Apology — a one-line apology from an office printer.

The line is assembled from named parts so each beat earns its place:
an apology, the printer's own grievances, and a punchline that lands last.
Standard library only, deterministic, no network access.
"""

import hashlib
import os
import sys
from pathlib import Path

APOLOGY = "Sorry I ate your report"
GRIEVANCE = "you feed me damp paper, staple my lunch"
PUNCH = "and still expect colour by nine."
BEAT_SEP = " \u2014 "
MAX_CHARS = 119


def build_line() -> str:
    """Join the three beats into the single apology line."""
    middle = GRIEVANCE + ", " + PUNCH
    return APOLOGY + BEAT_SEP + middle


def main() -> int:
    line = build_line()
    count = len(line)
    if count > MAX_CHARS:
        print(f"line too long: {count} chars (max {MAX_CHARS})", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")

    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"chars: {count}")
    print(f"sha256: {digest}")
    print(f"wrote: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
