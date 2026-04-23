import market
import news
from player import Player
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

console = Console()

STARTING_BALANCE = 500
TOTAL_DAYS = 10
MAX_REFRESHES = 3

# ─────────────────────────────────────────────
# TYPE COLORS
# ─────────────────────────────────────────────
TYPE_COLOURS = {
    "Fire": "red",
    "Water": "cyan",
    "Grass": "green",
    "Electric": "yellow",
    "Psychic": "magenta",
    "Dragon": "bright_blue",
    "Ghost": "purple",
    "Ice": "bright_cyan",
    "Fighting": "orange3",
    "Poison": "violet",
    "Dark": "grey62",
    "Rock": "wheat4",
    "Ground": "sandy_brown",
    "Normal": "white",
    "Flying": "sky_blue1",
    "Bug": "dark_olive_green3",
    "Steel": "grey84",
    "Fairy": "pink1",
}

def type_tag(t: str) -> str:
    return f"[{TYPE_COLOURS.get(t, 'white')}]{t}[/{TYPE_COLOURS.get(t, 'white')}]"


# ─────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────
def print_header(title: str):
    console.print(Rule(f"[bold yellow]{title}[/bold yellow]"))


def intro_screen():
    console.print(Panel(
        "[white]In a world where Pokémon aren't just partners — they're assets.\n\n"
        "Rare sightings drive prices up. News crashes markets. Timing is everything.\n\n"
        "You have 10 days and 500 PokéDollars to build your fortune.\n"
        "Buy low. Sell high. Read the market.[/white]",
        title="[bold cyan]POKÉPORTFOLIO[/bold cyan]",
        style="black",
        padding=(1, 2)
    ))


# ─────────────────────────────────────────────
# MENU (WITH BACK SUPPORT FIXED)
# ─────────────────────────────────────────────
def prompt_choice(options: list[str]) -> str:
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("#", style="dim")
    table.add_column("Action")

    for i, opt in enumerate(options, 1):
        table.add_row(str(i), opt)

    table.add_row("0", "Back / Cancel / Quit")

    console.print(table)

    while True:
        choice = input("> ").strip()

        if choice == "0":
            return "back"

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice")


# ─────────────────────────────────────────────
# MARKET DISPLAY (SHOWS UPDATED PRICES)
# ─────────────────────────────────────────────
def show_market():
    if not market.market_inventory:
        console.print("[red]Market empty[/red]")
        return

    table = Table(title="MARKET", box=box.SIMPLE_HEAVY)

    table.add_column("#", justify="right")
    table.add_column("Name")
    table.add_column("Type")
    table.add_column("Tier")
    table.add_column("Price", justify="right")
    table.add_column("Qty", justify="right")

    for i, p in enumerate(market.market_inventory, 1):
        types = " / ".join(type_tag(t) for t in p["type"])

        table.add_row(
            str(i),
            p["name"],
            types,
            p["tier"],
            str(p["price"]),
            str(p["quantity"])
        )

    console.print(table)


# ─────────────────────────────────────────────
# PORTFOLIO
# ─────────────────────────────────────────────
def show_portfolio(player):
    if not player.inventory:
        console.print("[red]No Pokémon owned[/red]")
        return

    table = Table(title="PORTFOLIO", box=box.SIMPLE_HEAVY)

    table.add_column("#")
    table.add_column("Name")
    table.add_column("Type")
    table.add_column("Bought At")

    for i, p in enumerate(player.inventory, 1):
        types = " / ".join(type_tag(t) for t in p["type"])

        table.add_row(
            str(i),
            p["name"],
            types,
            str(p["purchase_price"])
        )

    console.print(table)


# ─────────────────────────────────────────────
# NEWS
# ─────────────────────────────────────────────
def show_news():
    if not news.active_news:
        console.print("[dim]No news[/dim]")
        return

    console.print(Panel("[bold magenta]NEWS[/bold magenta]"))

    for n in news.active_news:
        console.print(f"- {n['headline']}")


# ─────────────────────────────────────────────
# BUY (BACK WORKS)
# ─────────────────────────────────────────────
def action_buy(player):
    while True:
        print_header("BUY POKÉMON")
        show_market()

        raw = input("Select number (0 to go back): ").strip()

        if raw == "0":
            return

        if not raw.isdigit():
            continue

        idx = int(raw) - 1

        if idx < 0 or idx >= len(market.market_inventory):
            continue

        chosen = market.market_inventory[idx]

        if chosen["quantity"] <= 0:
            console.print("[red]Sold out[/red]")
            continue

        if player.buy_pokemon(chosen["name"], chosen["price"]):
            chosen["quantity"] -= 1
            if chosen["quantity"] == 0:
                market.market_inventory.remove(chosen)
        return


# ─────────────────────────────────────────────
# SELL (BACK WORKS)
# ─────────────────────────────────────────────
def action_sell(player):
    while True:
        print_header("SELL POKÉMON")
        show_portfolio(player)

        raw = input("Select number (0 to go back): ").strip()

        if raw == "0":
            return

        if not raw.isdigit():
            continue

        idx = int(raw) - 1

        if idx < 0 or idx >= len(player.inventory):
            continue

        chosen = player.inventory[idx]

        market_price = next(
            (p["price"] for p in market.market_inventory if p["name"] == chosen["name"]),
            chosen["purchase_price"]
        )

        player.sell_pokemon(chosen["name"], market_price)
        return


# ─────────────────────────────────────────────
# REFRESH (PRICE UPDATE STILL WORKS)
# ─────────────────────────────────────────────
def action_refresh(player, counter):
    if counter[0] >= MAX_REFRESHES:
        console.print("[red]No refreshes left[/red]")
        return

    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)

    counter[0] += 1

    console.print(f"[green]Market refreshed ({MAX_REFRESHES - counter[0]} left)[/green]")


# ─────────────────────────────────────────────
# ADVANCE DAY (UNCHANGED LOGIC)
# ─────────────────────────────────────────────
def action_advance_day(player):
    news.advance_news()
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    market.random_price_fluctuations()
    market.advance_day()
    player.advance_day()
    market.generate_daily_market(player.get_balance())

    console.print(f"[cyan]Day {player.current_day}[/cyan]")


# ─────────────────────────────────────────────
# STARTER
# ─────────────────────────────────────────────
def choose_starter(player):
    starters = {
        "1": "Bulbasaur",
        "2": "Charmander",
        "3": "Squirtle",
    }

    print_header("STARTER")

    for k, v in starters.items():
        print(k, v)

    while True:
        choice = input("> ").strip()

        if choice in starters:
            name = starters[choice]
            break

    from pokemon_db import pokemon_db
    data = pokemon_db[name]

    player.inventory.append({
        "name": name,
        "type": data["type"],
        "tier": data["tier"],
        "purchase_price": 0,
        "day_bought": player.current_day,
    })


# ─────────────────────────────────────────────
# MAIN GAME
# ─────────────────────────────────────────────
def main():
    console.clear()
    intro_screen()

    name = input("Trainer name: ").strip() or "Trainer"
    player = Player(name, STARTING_BALANCE)

    choose_starter(player)

    counter = [0]

    market.generate_daily_market(player.get_balance())
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    while player.current_day <= TOTAL_DAYS:

        print_header(f"DAY {player.current_day}/{TOTAL_DAYS}")

        choice = prompt_choice([
            "View market",
            "Read news",
            "Buy Pokémon",
            "Sell Pokémon",
            "View portfolio",
            "Refresh market",
            "Advance day",
        ])

        if choice == "back":
            continue

        if choice == "View market":
            show_market()

        elif choice == "Read news":
            show_news()

        elif choice == "Buy Pokémon":
            action_buy(player)

        elif choice == "Sell Pokémon":
            action_sell(player)

        elif choice == "View portfolio":
            show_portfolio(player)

        elif choice == "Refresh market":
            action_refresh(player, counter)

        elif choice == "Advance day":
            action_advance_day(player)

            if player.current_day > TOTAL_DAYS:
                console.print("[bold red]GAME OVER[/bold red]")
                break


if __name__ == "__main__":
    main()
