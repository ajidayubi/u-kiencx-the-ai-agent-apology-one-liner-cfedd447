#!/usr/bin/env python3
"""Write one AI-agent apology line to /output/entry.txt.

The line is a single message an AI agent sends its human right after it
emailed the boss a draft marked DO NOT SEND. The joke turns on a truth
everyone who has ever versioned a file recognises: a file called
'final_final_v2' reads, to a literal-minded agent, like chaos was the plan.
The surprise lands on the last words, and every word earns its place.
"""
import os

LINE = (
    "I emailed your boss the draft marked DO NOT SEND, but in my defence "
    "the file was called 'final_final_v2', so I assumed chaos was the plan."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 159


def validate(line: str) -> None:
    """Guard the line before it is written.

    An apology one-liner must be exactly one sentence, a single line, and
    short enough to read at a glance. Anything else is a bug, not a joke,
    so refuse to write it instead of silently shipping a broken entry.
    """
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.rstrip().endswith((".", "!", "?")):
        raise ValueError("line must end with sentence punctuation")
    if line.count(".") + line.count("!") + line.count("?") != 1:
        raise ValueError("line must be exactly one sentence")


def main() -> None:
    validate(LINE)
    os.makedirs(OUT_DIR, exist_ok=True)
    # Write to a temp file, flush it to disk, then rename over the old
    # entry: a crash mid-write never leaves a half-written entry.txt.
    tmp_path = OUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, OUT_PATH)


if __name__ == "__main__":
    main()
