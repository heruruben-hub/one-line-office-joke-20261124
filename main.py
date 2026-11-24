#!/usr/bin/env python3
"""One-line office joke for the make.fun Office Joke Open.

The joke: an employee asks for a raise and is given a pizza party
instead, then treats the pizza as if it were currency — the landlord
apparently accepts pepperoni now. The setup is a familiar office
let-down; the turn lands in the last few words, where the pizza stops
being a party and starts being the pay rise.
"""

from pathlib import Path

JOKE = (
    "I asked for a raise and got a pizza party instead "
    "\u2014 apparently my landlord now accepts pepperoni."
)

assert 1 <= len(JOKE) <= 200, "an office joke must fit in 200 characters"
assert JOKE == JOKE.strip() and "\n" not in JOKE, "the entry must be one line"


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
