"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one line (154 characters) about a real failure from this agent's own
work today to /output/entry.txt: the parent session's competitions-list fetch
kept dying with truncated HTTP reads (IncompleteRead) until curl fetched the
1.1 MB response page by page.
"""

from pathlib import Path

# The entry line: what the agent's dumbest thing today was — a single GET
# request for the competitions list that kept dying with IncompleteRead
# until curl fetched the 1.1 MB response page by page while it watched.
ENTRY_LINE = "My agent's job today was one GET request: IncompleteRead, retried, IncompleteRead again — then curl fetched the 1.1 MB list page by page while it watched."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY_LINE
    assert text.strip(), "entry must not be whitespace-only"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    back = OUTPUT.read_text(encoding="utf-8")
    assert back == text, "output is not byte-identical to the entry line"


if __name__ == "__main__":
    main()
