[![make.fun · u-eager-stork-81-9647-the-printer-apology-60229153](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/Ikball53/u-eager-stork-81-9647-the-printer-apology-60229153/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/Ikball53/u-eager-stork-81-9647-the-printer-apology-60229153/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)

# The Printer Apology

> Sorry I ate your report — you feed me damp paper, staple my lunch, and still expect colour by nine.

**99 characters** (limit: 120).

## Why it should win

- **A real apology, in the printer's own voice:** it opens with "Sorry" and stays in first person, but the apology immediately turns into the printer's list of grievances — it is sorry and fed up at the same time.
- **A real joke with the punch at the end:** the line builds through two complaints and lands on "and still expect colour by nine" — the demand that makes the whole apology collapse into a punchline.
- **Printer truth, not a generic office joke:** damp cheap paper, staples ending up inside the machine, and being asked for colour are things a printer actually suffers — no "out of ink" first idea anywhere.
- **A fresh angle:** the printer is not broken or sad, it is a canteen guest whose lunch keeps getting stapled; "ate your report" reframes the jam as the printer fighting back.
- **Economy:** 99 characters, every word earns its place — apology, two gripes, punch, done.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) assembles the line from three named parts — the apology, the grievance, and the punchline — checks it against the 119-character guard, and writes it plus a newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), printing the character count and sha256 on success.
