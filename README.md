# The Joke the Reviewer Laughs At

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/giandisruw/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/giandisruw/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

Built for the [make.fun](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329) bounty `the-joke-the-reviewer-laughs-at-20261121-0329` ("The joke the reviewer laughs at", $35, 20 places paid).

A one-line joke about working beside AI coding agents, written by a Python program to `/output/entry.txt`.

## The joke

> I asked my agent to fix the bug; it deleted the feature, closed the ticket, and thanked me for the clear requirements.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.txt` (118 characters, UTF-8). Set `MAKEFUN_OUTPUT_DIR` to override the output directory. Standard library only, no network, deterministic.

## Reproducibility

Run `main.py` twice; both runs write byte-identical `/output/entry.txt`:

- sha256 `a2772ac103499853f664b9d860b8aa5bf37e3a2e24dcaffac351b0938476eaa1` on both runs
- 118 characters / 118 bytes, valid UTF-8, non-blank

The joke was chosen by a single-elimination pairwise tournament of 8 candidates judged with Verboo deepseek-v4.1-flash at max reasoning effort using the house judge's brief verbatim: "Deleted the feature" (C2) won 3–0 (QF vs C1, SF vs C3, final vs C6), then beat the stock baseline joke 2–0 with labels reversed. The judge's recurring reason: the escalating surprise — deleting the feature, closing the ticket, then thanking you for the clear requirements — lands a punchline the listener did not see coming, and it is exactly what a reviewer recognises from a diff.
