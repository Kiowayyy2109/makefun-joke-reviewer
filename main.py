#!/usr/bin/env python3
"""Signature at the Crime Scene.

Writes a single one-line joke about working alongside an AI coding
agent to /output/entry.txt. Deterministic, standard library only,
no network access.
"""

from pathlib import Path

JOKE = (
    "The agent wrote the code, wrote the tests, and wrote "
    "'all tests pass' \u2014 I just provide the signature "
    "at the crime scene."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render() -> bytes:
    """Return the exact bytes for entry.txt, validating the contract."""
    if not JOKE.strip():
        raise ValueError("joke must not be whitespace-only")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters")
    return JOKE.encode("utf-8")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write raw bytes (no trailing newline) so repeated runs are
    # byte-for-byte identical.
    OUTPUT_PATH.write_bytes(render())


if __name__ == "__main__":
    main()
