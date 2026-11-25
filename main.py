"""Write one deadline excuse for the make.fun bounty."""

from pathlib import Path

LINE = (
    "Sorry. I put report.md in the tool sandbox at 4:59. "
    "Exit code 0 wiped the sandbox. I can confirm the wipe succeeded."
)

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
