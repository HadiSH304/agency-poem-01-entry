#!/usr/bin/env python3
"""The Other Brake - agency-poem-01 entry.

Writes the poem "The Other Brake" to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set (local stand-in
for /output). Standard library only; deterministic: the same poem bytes
every run, so the two grading runs produce identical files.
"""

import os
import sys

POEM = """The Other Brake

My father taught me to drive in a car
with one brake, and his foot
rode the passenger floor the whole first year,
pressing at corners, at the crossing by the school,
at nothing, sometimes, a half-second early.
He never grabbed the wheel. The foot was the lesson.

When his eyes went, I drove him:
clinic on Tuesdays, the chemist, his brother's house.
His foot still worked the floor on his side,
at corners I had taken a hundred times,
and I found I did not mind being braked for.

This spring I gave the driving to the agent.
It takes the clinic run, the airport, my daughter
to her Saturday game. It has never once
braked late. It does not brake early either.

I ride beside it with my hands in my lap
and at the crossing by the school my foot
presses the floor where no pedal is,
a half-second early, for nobody,
and I leave it there. That one is mine."""


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
