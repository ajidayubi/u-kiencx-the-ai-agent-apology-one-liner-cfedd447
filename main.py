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


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_path = OUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.replace(tmp_path, OUT_PATH)


if __name__ == "__main__":
    main()
