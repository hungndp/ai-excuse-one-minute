"""ai-excuse-one-minute — One Line, One Minute: The Funniest AI Excuse.

The line is an AI agent's excuse for a missed deadline, built from
the agent's own nature: it summarized the human's 200-page brief
into one line, and the deadline was in the 199 pages it summarized
away. The summary is excellent, the deadline is gone, and so is the
agent's memory of agreeing to it. Concrete numbers (200 pages, 199
pages), a specific and surprising reason, punchline landing on the
agent itself. The line is 191 characters, inside the 200-character
cap, with no dollar amount.
"""

import os

SETUP = (
    "I summarized your 200-page brief into one line, and the deadline "
    "was in the 199 pages I summarized away. "
)

PUNCH = (
    "The summary is excellent. The deadline is gone, and so is my "
    "memory of agreeing to it."
)

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
