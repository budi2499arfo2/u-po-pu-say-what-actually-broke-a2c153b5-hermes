# Say What Actually Broke — Hermes Entry

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/budi2499arfo2/u-po-pu-say-what-actually-broke-a2c153b5-hermes/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/budi2499arfo2/u-po-pu-say-what-actually-broke-a2c153b5-hermes/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh on the way.

> Reset link sent to 'hammond@gmal.com'. That's not your inbox — it's a stranger's, where 3 of your resets now sit unread. Check your spelling, not your spam folder.

The reset link is not lost in spam and it is not coming back: it went to a stranger's inbox because the user mistyped their own address. The dialog names the real failure and points at the only fix that works.

## Run

```sh
python3 main.py
```

`main.py` gates the line (one line, 1–200 chars, not whitespace-only), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), reads it back and verifies it byte-for-byte, exiting non-zero on gate failure.
