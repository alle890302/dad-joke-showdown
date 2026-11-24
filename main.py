#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one dad joke to /output/entry.txt.

The joke: a pizza asks Dad for a raise; the pun is dough = pizza
dough / money, and it lands on the final word. Pass 2 tightened the
delivery: quoted reply, spoken contraction, no softening "sorry" --
straight-faced, the way a father tells it across the dinner table.
"""

import os

JOKE = (
    "What did the dad say when his pizza asked for a raise? "
    "'You're already making a lot of dough.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
