"""Write the dad joke entry to /output/entry.txt.

One dad joke, 78 characters (limit 200) -- no trailing newline."""

from pathlib import Path

ENTRY = "Why did the dad bring a ladder to the barbecue? He heard the steaks were high."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
