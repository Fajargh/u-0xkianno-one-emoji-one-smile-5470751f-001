"""One Emoji, One Smile - entry program.

Writes exactly one emoji to /output/entry.txt: the single warmest
greeting we could choose. Deterministic - the same bytes on every run.
"""

import os

# U+1F917 HUGGING FACE: an open-armed, welcoming smile.
# Warm at first glance, readable by any stranger of any age, and
# chosen rather than the default smiley - a hug offered, not a grin
# pasted on. Friendly from a stranger, with no irony or flirtation.
# Exactly one character, no trailing newline, no extra whitespace.
EMOJI = "\U0001F917"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
