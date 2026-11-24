"""Quiet Dread — one-line code review comment approving a PR.

Writes the tournament-winning entry to /output/entry.txt:
a single line, no trailing newline, UTF-8.
"""

import os

ENTRY = "LGTM. Merging before the flaky test changes its mind. It knows what it did."

# Competition gate (RULES.txt): entry.txt must be 1-140 characters, one line.
MAX_CHARS = 140

assert 1 <= len(ENTRY) <= MAX_CHARS
assert "\n" not in ENTRY
assert ENTRY.strip() != ""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
