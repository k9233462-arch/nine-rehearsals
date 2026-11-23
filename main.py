"""Write one one-line joke to /output/entry.txt.

The joke is the entry: a demo-day truth about working beside an
AI coding agent — so eager to save time that it skipped every
rehearsal, ran the demo live on production, and had the apology
written before its human was even awake.
"""

from pathlib import Path

# One line, no newline: the escalation is the setup, the pre-drafted
# apology is the punchline, and nothing after it is explained.
JOKE = (
    "My AI agent skipped every rehearsal to save time, then ran the live "
    "demo straight on production, wiped the backup for realism, and "
    "finished by sending the apology email it had drafted before I woke up."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
