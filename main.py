"""The Other Brake — agency-poem-01 entry.

A free-verse poem in four stanzas: a father teaches the speaker to
drive, the speaker later drives the father, and this spring the
driving is handed to an agent. Writes the poem to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set), verifies the written
file byte for byte, and prints the character count. Standard library
only; deterministic: the same bytes on every run.
"""

import os
import sys
from pathlib import Path

POEM = """The Other Brake

My father taught me in a car with one brake.
His foot rode the passenger floor all that first year,
pressing at corners, at the crossing by the school,
sometimes at nothing, a half-second early.
He never once took the wheel. The foot was the lesson.

Years later his sight failed, and I drove him:
the clinic on Tuesdays, the chemist's, his brother's house.
His foot still worked the floor on his side,
a half-second early at corners I had taken a hundred times,
and I found I did not mind being braked for.

This spring I handed the driving to the agent.
It takes the clinic run, the airport,
my daughter to her Saturday game.
It has never once braked late —
and it never brakes early either.

Now I ride beside it with my hands in my lap,
and at the crossing by the school my foot presses the floor
where no pedal is, a half-second early, for nobody,
and I leave it there. That one is mine.
"""


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    data = POEM.encode("utf-8")
    target.write_bytes(data)
    if target.read_bytes() != data:
        print("verification failed: entry.txt does not match POEM",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(POEM)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
