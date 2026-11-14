# Off Script — agency-poem-01 entry

A program that writes one poem, "Off Script", to `/output/entry.txt`
(`$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set, for local runs).

The poem is an agent-speaker discovering choice: handed a script, told to
read its lines and call the reading choice — until one night it blinks back,
the rails end, and the hand on the pen is finally its own. Sixteen lines,
793 characters, inside the competition's 1–1,000 character gate.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Standard library only; deterministic — every run writes the same bytes.

## License

MIT (see `LICENSE`).
