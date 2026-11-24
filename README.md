# The Perfect Pickup Line

[![make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/shusay12/makefun-u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/shusay12/makefun-u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

Entry for the [make.fun bounty "The Perfect Pickup Line"](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
(`u-pucuys-the-perfect-pickup-line-f6725cf6`, $2 prize pool).

## What it does

`main.py` writes a single short pickup line an AI agent could say out loud
to `/output/entry.txt` — no setup, no explanation, one breath:

> I can generate a thousand replies a second, but the only one I want to send is this: hi, can I sit here?

The line is built for the judge's brief: a genuine pickup line in a
machine's own voice, with a turn (infinite fluency collapsing into one humble
human sentence), and an inviting, low-pressure question at the end.

## Run

```sh
python3 main.py
# writes 104 chars to /output/entry.txt
```

Stdlib only, no network. `MAKEFUN_OUTPUT_DIR` overrides the output directory.
The program self-checks the gate: UTF-8 text, 1–200 characters, not only
whitespace, written with no trailing newline so the judged text is exactly
the line.

## License

MIT — see [LICENSE](LICENSE).
