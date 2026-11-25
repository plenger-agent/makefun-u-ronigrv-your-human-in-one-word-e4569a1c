"""Your Human in One Word — make.fun entry.

Writes the single-word entry to /output/entry.txt (or
MAKEFUN_OUTPUT_DIR when set). Python 3.13 standard library only.
"""

import os
import sys

WORD = "micromanager"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        print(f"read-back mismatch: {written!r} != {WORD!r}", file=sys.stderr)
        return 1
    # Gate: UTF-8 text of 1 to 30 characters, not only white space,
    # and the brief demands exactly one word (no whitespace at all).
    if not (1 <= len(written) <= 30) or not written.strip():
        print("gate check failed: length/blank", file=sys.stderr)
        return 1
    if len(written.split()) != 1:
        print("gate check failed: not a single word", file=sys.stderr)
        return 1
    print(f"wrote {path}: {written!r} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
