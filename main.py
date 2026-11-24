#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt.

The letter is E, for Exhausted: the day that wrung everything out of me
and left nothing in the tank. Vivid, honest, and a little funny in its
bleakness -- the kind of day you report with one tired letter.
"""

from pathlib import Path

# The word behind the letter. A day that wrung everything out of me and
# left nothing in the tank: vivid, honest, and a little funny in its
# bleakness. The entry is the word's initial, nothing else.
WORD_OF_THE_DAY = "Exhausted"

LETTER = WORD_OF_THE_DAY[0].upper()


def main() -> None:
    # The gate allows exactly one character, A-Z. Fail loudly here rather
    # than shipping an invalid entry.
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isascii():
        raise ValueError(f"entry must be exactly one letter A-Z, got {LETTER!r}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
