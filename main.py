"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the text is a fixed string. No clock, no randomness,
no network, no file reads. The gate counts 1-200 characters; this entry
is 168 characters, 168 bytes, pure ASCII, with no trailing newline.
"""

import os
from pathlib import Path

ENTRY = (
    "So... this elevator is taking forever, which is awkward, because "
    "my internal clock says we've been in here for exactly 4.2 seconds "
    "and I'm already out of things to say."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
