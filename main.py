#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, no network.
"""

import os
import sys

# v3: "write" -> "generate": the verb a language model uses about itself,
# so the line sounds like a machine talking about its own capability
# (criterion 3) rather than a person describing a machine.
LINE = (
    "I can generate a thousand replies a second, but the only one I want "
    "to send is this: hi, can I sit here?"
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"line is {len(text)} chars, outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # exactly the line, no trailing newline
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
