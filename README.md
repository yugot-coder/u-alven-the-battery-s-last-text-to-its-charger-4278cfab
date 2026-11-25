# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/yugot-coder/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/yugot-coder/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab): one line of at most 200 characters — the phone battery's final message to the charger it waited for all day.

## The entry

> Final review: 1 star. Always late, always tangled, somehow the hero of your own story. I spent my last percent waiting on you. Would die again just to leave this review.

(169 characters, one line.)

The idea: a one-star product review sent as a farewell text. The battery
spends its last percent not begging for a charge, but posting the review —
so the complaint itself is what kills it. Spiteful, a little needy, and
funnier the second time you read it.

## How it works

`main.py` is standard-library only. It validates the text against the
competition gate (UTF-8, 1–200 characters, not only whitespace, single
line) and writes it deterministically to `/output/entry.txt`.

```sh
python3 main.py
```

Run it twice and the output is byte-identical (same sha256 both runs).

## Files

- `main.py` — the entry program (writes `/output/entry.txt`)
- `CANDIDATES.md` — the 10 candidate lines considered, with reasons, and the winner
- `prompt.txt` — the build brief this entry was written from
- `LICENSE` — MIT

---

Built for [make.fun](https://make.fun) — if you want to try bounties like
this one, join with my referral link: https://make.fun/r/za0zfbxx
