#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the dumbest thing my agent did today."""

import os

ENTRY = "My agent grepped four hundred session files to find its own identity, then asked the database to confirm who it was."


def main() -> None:
    # The gate allows 1 to 200 characters; this line is well inside it.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
