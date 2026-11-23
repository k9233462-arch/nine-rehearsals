"""Write one one-line joke to /output/entry.txt.

The joke is the entry: a demo-day truth about working beside an
AI coding agent — flawless in every rehearsal, inventive exactly
once, in front of the live audience.
"""

from pathlib import Path

# One line, no newline: setup and punchline fused, nothing explained.
JOKE = (
    "After nine flawless rehearsals, my AI coding agent opened the live "
    "demo by confidently refactoring the only file that was live."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
