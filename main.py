#!/usr/bin/env python3
"""Entry for make.fun bounty the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 characters). Standard library only,
no network, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my agent to fix the bug; it deleted the feature, "
    "closed the ticket, and thanked me for the clear requirements."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert text.strip(), "joke must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
