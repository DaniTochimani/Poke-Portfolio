import market
from player import Player

STARTING_BALANCE = 500
TOTAL_DAYS = 10
DIVIDER = "-" * 55

#Helpers
def print_header(title: str) -> None:
    print(f"\n{'=' * 55}")
    print(f" {title}")
    print(f"{'=' * 55}")

def prompt_choice(options: list[str]) -> str:
    for i, opt in enumerate(options, 1):
        print(f"    {i}.  {opt}")
    print(f"    0. Quit Game")

    while True:
        raw = input("\n  > ").strip()
        if raw.isdigit():
            idx = int(raw)
            if idx == 0:
                return "quit"
            if 1 <= idx <= len(options):
                return options[idx - 1]
        matches = [o for o in options if o.lower().startwith(raw.lower())]
        if len(matches) == 1:
            return matches[0]
        print("Invalid choice - Try again.")
