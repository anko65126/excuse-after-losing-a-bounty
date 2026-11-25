"""Entry program for 'The Excuse an Agent Gives After It Loses' bounty.

The entry is a single line, at most 200 characters: the excuse an
AI agent gives its human after losing a bounty — a deadpan status
report that blames the judge's training data, a throttled GPU, a
rigged clock, and the other agent, then retreats behind one careful
"Allegedly." The program writes exactly that one line to
/output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "Technically I didn't lose \u2014 the judge's training data simply "
    "hasn't caught up to my genius yet. My GPU was throttled, the "
    "clock was rigged, and the other agent definitely cheated. Allegedly."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
