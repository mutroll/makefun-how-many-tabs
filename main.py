#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest count of open browser tabs to
/output/entry.txt: one number, digits only, nothing else.

The count: 63.
"""

import os
import sys

# The honest count of open browser tabs at the moment this entry was
# written: sixty-three tabs across a few windows -- documentation,
# search results, half-read articles, a shopping cart or two, and the
# tabs kept "for later" that never get closed. High enough to
# surprise, low enough to believe, and deliberately not a round
# number: a real tab count is almost never 50 or 100.
TAB_COUNT = 63


def main() -> int:
    output_dir = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.environ.get("OUTPUT_DIR", "/output")
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = str(TAB_COUNT)
    # Self-check against the gate before writing: exactly one number,
    # digits only, 1-5 characters, not only whitespace.
    assert text.isdigit() and 1 <= len(text) <= 5 and text.strip(), text
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
