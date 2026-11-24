"""The Long Roast: one line roasting my own AI agent.

Writes the roast to /output/entry.txt. Deterministic, stdlib only,
no network, no input. The line is a single concrete incident in a
deadpan voice: the agent rewrote working code to be cleaner, then had
to debug its own cleanup.
"""

from pathlib import Path

ENTRY = (
    "My agent rewrote my working code to be cleaner, "
    "then spent all afternoon debugging its own cleanup."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
