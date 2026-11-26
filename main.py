"""Deadpan forecast for the invented city of Glimmerwick.

Writes a single one-line forecast to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

import os

ENTRY = (
    "Tonight in Glimmerwick: a high of 61, scattered applause from the "
    "clouds, and a 40 percent chance the rain remembers your name. "
    "Bring an umbrella and an alibi."
)


def main() -> None:
    # The gate requires 1-160 UTF-8 characters, not only whitespace.
    # Fail loudly here rather than shipping an entry the scorer rejects.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
