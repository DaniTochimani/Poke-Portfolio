# pip install rich

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
    color = TYPE_COLOURS.get(t, "white")
    return f"[{color}]{t}[/{color}]"


# ─────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────
def print_header(title: str) -> None:
    console.print(Rule(f"[bold yellow]{title}[/bold yellow]"))


def prompt_choice(options: list[str]) -> str:
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("Option", style="bold")
    table.add_column("Action")

    for i, opt in enumerate(options, 1):
        table.add_row(str(i), opt)
    table.add_row("0", "Quit Game")

    console.print(table)

    while True:
        choice = input("\n> ").strip()

        if choice == "0":
            return "quit"

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice. Try again.")


# ─────────────────────────────────────────────
# MARKET DISPLAY
# ─────────────────────────────────────────────
def show_market() -> None:
    if not market.market_inventory:
        console.print("[red]Market is empty![/red]")
        return

    table = Table(title="POKÉMARKET", box=box.SIMPLE_HEAVY)

    table.add_column("#", justify="right", style="dim")
    table.add_column("Name", style="bold")
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
            str(p["quantity"]),
        )

    console.print(table)


# ─────────────────────────────────────────────
# PORTFOLIO DISPLAY
# ─────────────────────────────────────────────
def show_portfolio(player: Player) -> None:
    if not player.inventory:
        console.print("[red]No Pokémon owned.[/red]")
        return

    table = Table(title="PORTFOLIO", box=box.SIMPLE_HEAVY)

    table.add_column("#", justify="right", style="dim")
    table.add_column("Name", style="bold")
    table.add_column("Type")
    table.add_column("Bought At", justify="right")

    for i, p in enumerate(player.inventory, 1):
        types = " / ".join(type_tag(t) for t in p["type"])

        table.add_row(
            str(i),
            p["name"],
            types,
            str(p["purchase_price"]),
        )

    console.print(table)


# ─────────────────────────────────────────────
# NEWS DISPLAY
# ─────────────────────────────────────────────
def show_news() -> None:
    if not news.active_news:
        console.print("[dim]No active news.[/dim]")
        return

    console.print(Panel.fit("[bold magenta]NEWS[/bold magenta]"))

    for i, n in enumerate(news.active_news, 1):
        console.print(f"[cyan]{i}.[/cyan] {n['headline']}")


# ─────────────────────────────────────────────
# ACTIONS
# ─────────────────────────────────────────────
def action_buy(player: Player) -> None:
    if not market.market_inventory:
        console.print("[red]Market is empty.[/red]")
        return

    print_header("BUY POKÉMON")
    show_market()

    raw = input("\nSelect number: ").strip()

    if not raw.isdigit() or int(raw) == 0:
        return

    idx = int(raw) - 1

    if idx < 0 or idx >= len(market.market_inventory):
        console.print("[red]Invalid selection[/red]")
        return

    chosen = market.market_inventory[idx]

    if chosen["quantity"] <= 0:
        console.print("[red]Sold out![/red]")
        return

    success = player.buy_pokemon(chosen["name"], chosen["price"])

    if success:
        chosen["quantity"] -= 1

        if chosen["quantity"] == 0:
            market.market_inventory.remove(chosen)
            console.print(f"[dim]{chosen['name']} removed from market[/dim]")


def action_sell(player: Player) -> None:
    if not player.inventory:
        console.print("[red]Nothing to sell.[/red]")
        return

    print_header("SELL POKÉMON")
    show_portfolio(player)

    raw = input("\nSelect number: ").strip()

    if not raw.isdigit() or int(raw) == 0:
        return

    idx = int(raw) - 1

    if idx < 0 or idx >= len(player.inventory):
        console.print("[red]Invalid selection[/red]")
        return

    chosen = player.inventory[idx]

    market_price = next(
        (p["price"] for p in market.market_inventory if p["name"] == chosen["name"]),
        chosen["purchase_price"]
    )

    player.sell_pokemon(chosen["name"], market_price)


def action_refresh(player: Player, refresh_counter: list) -> None:
    if refresh_counter[0] >= MAX_REFRESHES:
        console.print("[red]No refreshes left[/red]")
        return

    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)

    refresh_counter[0] += 1

    console.print(f"[green]Market refreshed ({MAX_REFRESHES - refresh_counter[0]} left)[/green]")


def action_advance_day(player: Player) -> None:
    expired = news.advance_news()

    if expired:
        console.print("\n[magenta]News ended:[/magenta]")
        for h in expired:
            console.print(f"[dim]- {h.split('.')[0]}[/dim]")

    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    market.random_price_fluctuations()
    market.advance_day()
    player.advance_day()
    market.generate_daily_market(player.get_balance())

    console.print(f"\n[bold cyan]Day {player.current_day}[/bold cyan]")


# ─────────────────────────────────────────────
# STARTER
# ─────────────────────────────────────────────
def choose_starter(player: Player) -> None:
    starters = {
        "1": ("Bulbasaur", "Grass/Poison"),
        "2": ("Charmander", "Fire"),
        "3": ("Squirtle", "Water"),
    }

    print_header("STARTER SELECTION")

    for k, v in starters.items():
        console.print(f"{k}. {v[0]} ({v[1]})")

    while True:
        choice = input("> ").strip()

        if choice in starters:
            name = starters[choice][0]
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

    console.print(f"[green]You chose {name}![/green]")


# ─────────────────────────────────────────────
# GAME LOOP
# ─────────────────────────────────────────────
def main():
    print_header("POKÉPORTFOLIO")

    name = input("Trainer name: ").strip() or "Trainer"
    player = Player(name, STARTING_BALANCE)

    choose_starter(player)

    refresh_counter = [0]

    market.generate_daily_market(player.get_balance())
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    while player.current_day <= TOTAL_DAYS:

        console.print(f"\n[bold yellow]Day {player.current_day}/{TOTAL_DAYS}[/bold yellow]")

        choice = prompt_choice([
            "View market",
            "Read news",
            "Buy Pokémon",
            "Sell Pokémon",
            "View portfolio",
            "Refresh market",
            "Advance day",
        ])

        if choice == "quit":
            break

        elif choice == "View market":
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
            action_refresh(player, refresh_counter)

        elif choice == "Advance day":
            action_advance_day(player)

            if player.current_day > TOTAL_DAYS:
                console.print("[bold red]Game Over[/bold red]")
                break


if __name__ == "__main__":
    main()
