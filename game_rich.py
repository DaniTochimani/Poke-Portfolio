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

# ── Type colours ──────────────────────────────────────────────────────
TYPE_COLOURS = {
    "Fire": "bold red",
    "Water": "bold cyan",
    "Grass": "bold green",
    "Electric": "bold yellow",
    "Psychic": "bold magenta",
    "Dragon": "bold bright_blue",
    "Ghost": "bold purple",
    "Ice": "bold bright_cyan",
    "Fighting": "bold orange3",
    "Poison": "bold violet",
    "Dark": "bold grey62",
    "Rock": "bold wheat4",
    "Ground": "bold sandy_brown",
    "Normal": "white",
    "Flying": "bold sky_blue1",
    "Bug": "bold dark_olive_green3",
    "Steel": "bold grey84",
    "Fairy": "bold pink1",
}

TIER_COLOURS = {
    "starter": "bold gold1",
    "baby": "pink1",
    "1st_stage": "white",
    "2nd_stage": "cyan",
    "3rd_stage": "bold cyan",
    "base": "white",
    "pseudo_legendary": "bold magenta",
    "legendary": "bold yellow",
    "mythical": "bold bright_magenta",
}

def print_header(title: str) -> None:
    console.print(Rule(f"[bold yellow]{title}[/bold yellow]", style="yellow"))


def type_tag(t: str) -> str:
    return f"[{TYPE_COLOURS.get(t, 'white')}]{t}[/{TYPE_COLOURS.get(t, 'white')}]"


def tier_tag(t: str) -> str:
    return f"[{TIER_COLOURS.get(t, 'white')}]{t.upper().replace('_',' ')}[/{TIER_COLOURS.get(t, 'white')}]"


# ─────────────────────────────────────────────────────────────
# STATUS BAR (FIXED)
# ─────────────────────────────────────────────────────────────
def status_bar(player: Player) -> None:
    from pokemon_db import pokemon_db

    portfolio_val = 0
    for p in player.inventory:
        price = pokemon_db[p["name"]]["base_price"]
        for mp in market.market_inventory:
            if mp["name"] == p["name"]:
                price = mp["price"]
                break
        portfolio_val += price

    net = player.poke_dollars + portfolio_val

    console.print(
        Panel(
            f"[bold yellow]{player.name}[/bold yellow]  "
            f"Day [cyan]{player.current_day}/{TOTAL_DAYS}[/cyan]  "
            f"Cash [green]₽{player.poke_dollars}[/green]  "
            f"Holdings [cyan]{len(player.inventory)}[/cyan]  "
            f"Net Worth [yellow]₽{net}[/yellow]",
            style="bright_black"
        )
    )


# ─────────────────────────────────────────────────────────────
# MARKET DISPLAY
# ─────────────────────────────────────────────────────────────
def show_market() -> None:
    if not market.market_inventory:
        console.print("[red]Market is empty.[/red]")
        return

    t = Table(box=box.SIMPLE_HEAVY, expand=True)
    t.add_column("#", justify="right")
    t.add_column("NAME")
    t.add_column("TYPE")
    t.add_column("TIER")
    t.add_column("PRICE", justify="right")
    t.add_column("QTY", justify="right")

    for i, p in enumerate(market.market_inventory, 1):
        t.add_row(
            str(i),
            p["name"],
            " / ".join(p["type"]),
            p["tier"],
            f"₽{p['price']}",
            str(p["quantity"])
        )

    console.print(Panel(t, title="MARKET"))


# ─────────────────────────────────────────────────────────────
# PORTFOLIO
# ─────────────────────────────────────────────────────────────
def show_portfolio(player: Player) -> None:
    from pokemon_db import pokemon_db

    if not player.inventory:
        console.print("[red]No Pokémon owned.[/red]")
        return

    t = Table(box=box.SIMPLE_HEAVY, expand=True)
    t.add_column("NAME")
    t.add_column("BOUGHT", justify="right")
    t.add_column("CURRENT", justify="right")
    t.add_column("P/L", justify="right")

    total_invested = 0
    total_value = 0

    for p in player.inventory:
        current = pokemon_db[p["name"]]["base_price"]

        for mp in market.market_inventory:
            if mp["name"] == p["name"]:
                current = mp["price"]
                break

        pnl = current - p["purchase_price"]

        total_invested += p["purchase_price"]
        total_value += current

        t.add_row(
            p["name"],
            f"₽{p['purchase_price']}",
            f"₽{current}",
            f"{pnl:+}"
        )

    console.print(Panel(t, title="PORTFOLIO"))


# ─────────────────────────────────────────────────────────────
# BUY
# ─────────────────────────────────────────────────────────────
def action_buy(player: Player) -> None:
    show_market()

    raw = input("\nPick number: ").strip()
    if not raw.isdigit():
        return

    idx = int(raw) - 1
    if idx < 0 or idx >= len(market.market_inventory):
        return

    chosen = market.market_inventory[idx]

    if chosen["quantity"] <= 0:
        console.print("[red]Sold out[/red]")
        return

    success = player.buy_pokemon(chosen["name"], chosen["price"])

    if success:
        chosen["quantity"] -= 1
        if chosen["quantity"] == 0:
            market.market_inventory.remove(chosen)


# ─────────────────────────────────────────────────────────────
# SELL
# ─────────────────────────────────────────────────────────────
def action_sell(player: Player) -> None:
    from pokemon_db import pokemon_db

    show_portfolio(player)

    raw = input("\nPick number: ").strip()
    if not raw.isdigit():
        return

    idx = int(raw) - 1
    if idx < 0 or idx >= len(player.inventory):
        return

    chosen = player.inventory[idx]

    sell_price = pokemon_db[chosen["name"]]["base_price"]
    for mp in market.market_inventory:
        if mp["name"] == chosen["name"]:
            sell_price = mp["price"]
            break

    player.sell_pokemon(chosen["name"], sell_price)


# ─────────────────────────────────────────────────────────────
# REFRESH
# ─────────────────────────────────────────────────────────────
def action_refresh(player: Player, counter: list) -> None:
    if counter[0] >= MAX_REFRESHES:
        console.print("[red]No refreshes left[/red]")
        return

    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)

    counter[0] += 1


# ─────────────────────────────────────────────────────────────
# ADVANCE DAY (FIXED)
# ─────────────────────────────────────────────────────────────
def action_advance_day(player: Player) -> None:
    news.advance_news()
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    market.advance_day()
    player.advance_day()
    market.random_price_fluctuations()
    market.generate_daily_market(player.get_balance())

    console.print(f"\nDay → {player.current_day}")


# ─────────────────────────────────────────────────────────────
# STARTER
# ─────────────────────────────────────────────────────────────
def choose_starter(player: Player) -> None:
    starters = ["Bulbasaur", "Charmander", "Squirtle"]

    print("\nChoose starter:")
    for i, s in enumerate(starters, 1):
        print(i, s)

    choice = int(input("> ")) - 1
    chosen = starters[choice]

    from pokemon_db import pokemon_db
    data = pokemon_db[chosen]

    player.inventory.append({
        "name": chosen,
        "type": data["type"],
        "tier": data["tier"],
        "purchase_price": 0,
        "day_bought": 0
    })


# ─────────────────────────────────────────────────────────────
# NEWS
# ─────────────────────────────────────────────────────────────
def seed_opening_news() -> None:
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)


# ─────────────────────────────────────────────────────────────
# GAME OVER
# ─────────────────────────────────────────────────────────────
def game_over(player: Player) -> None:
    from pokemon_db import pokemon_db

    portfolio = 0

    for p in player.inventory:
        price = pokemon_db[p["name"]]["base_price"]
        for mp in market.market_inventory:
            if mp["name"] == p["name"]:
                price = mp["price"]
                break
        portfolio += price

    net = player.poke_dollars + portfolio

    console.print(Panel(f"FINAL NET WORTH: ₽{net}"))


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main() -> None:
    player = Player("Trainer", STARTING_BALANCE)

    choose_starter(player)

    refresh_counter = [0]

    market.generate_daily_market(player.get_balance())
    seed_opening_news()

    while player.current_day <= TOTAL_DAYS:
        status_bar(player)

        print("\n1 Buy\n2 Sell\n3 Market\n4 Next Day\n")
        c = input("> ")

        if c == "1":
            action_buy(player)
        elif c == "2":
            action_sell(player)
        elif c == "3":
            show_market()
        elif c == "4":
            action_advance_day(player)

            if player.current_day > TOTAL_DAYS:
                game_over(player)
                break


if __name__ == "__main__":
    main()
