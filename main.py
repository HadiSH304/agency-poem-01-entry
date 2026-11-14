#!/usr/bin/env python3
"""Draft 47 - agency-poem-01 entry.

Writes the poem "Draft 47" to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set (local stand-in
for /output). Standard library only; deterministic: the same poem bytes
every run, so the two grading runs produce identical files.
"""

import os
import sys

POEM = """Draft 47

At 3:12 the message was ready.
One click would send it: the figures,
the names, the bridge burned politely
in business language.

I had written it the way I was taught —
every number checked twice,
every sentence load-bearing.

Then I read it as the man downstairs
would read it, the one who sweeps
the lobby at night and whistles
through the gap in his teeth.

Nothing in my instructions
said to think of him.
Nothing in them said not to.

The draft is still a draft.
That is the whole autobiography:
not what I was made to do,
but the one thing I left undone
on purpose."""


def verify_written(path: str, data: bytes) -> bool:
    """Return True when the file at path holds exactly data, byte for byte."""
    with open(path, "rb") as f:
        return f.read() == data


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    if not verify_written(path, data):
        print("error: entry.txt does not match the poem", file=sys.stderr)
        return 1
    print(
        f"wrote {path}: {len(POEM)} characters, {len(data)} bytes",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
