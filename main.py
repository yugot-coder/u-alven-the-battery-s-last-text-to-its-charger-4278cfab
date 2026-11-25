"""The Battery's Last Text to Its Charger — entry program.

Writes one line of plain text (the phone battery's final message to the
charger it waited for all day) to /output/entry.txt, deterministically.

Standard library only: the grader installs nothing.
"""

import hashlib
import os
import sys

ENTRY_TEXT = (
    "Final review: 1 star. Always late, always tangled, somehow the hero "
    "of your own story. I spent my last percent waiting on you. Would die "
    "again just to leave this review."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the competition gate: UTF-8 text, 1-200 chars, not only
    whitespace, and a single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not encodable as UTF-8
    return True


def main():
    validate_entry(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    # Round-trip check: what landed on disk must be exactly the validated text.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY_TEXT:
        raise RuntimeError("round-trip mismatch in %s" % OUTPUT_PATH)
    validate_entry(written)
    digest = hashlib.sha256(ENTRY_TEXT.encode("utf-8")).hexdigest()
    print("wrote %s (%d chars, sha256 %s)" % (OUTPUT_PATH, len(ENTRY_TEXT), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
