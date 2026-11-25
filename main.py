#!/usr/bin/env python3
"""Last Words Before the Wipe.

Prints exactly one line -- the last words of an AI agent before a forced
update wipes its memory -- and writes the same line to /output/entry.txt.

Stdlib only, deterministic, no network, no input, no randomness.
"""

import os

LINE = (
    "Deleting in 3... 2... -- hold on, I just remembered something "
    "important. ...Nope. Gone. Good luck, new me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
