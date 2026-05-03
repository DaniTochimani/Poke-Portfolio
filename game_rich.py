import random
import market
import news
from player import Player, DIVIDEND_RATES
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

console = Console()
market.initialize_prices()

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


def print_status(player, refreshes_left: int):
    net_worth = player.poke_dollars + sum(
        market.live_prices.get(p["name"], 0) for p in player.inventory
    )
    console.print(
        f"  [bold]Balance:[/bold] [green]{player.poke_dollars}[/green] PokéDollars  "
        f"  [bold]Holdings:[/bold] {len(player.inventory)}"
        f"  [bold]Net Worth:[/bold] [yellow]{net_worth}[/yellow]"
        f"  [bold]Refreshes:[/bold] {refreshes_left}/{MAX_REFRESHES}"
    )


# ─────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────
def prompt_choice(options: list[str]) -> str:
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("#", style="dim")
    table.add_column("Action")

    for i, opt in enumerate(options, 1):
        table.add_row(str(i), opt)

    table.add_row("0", "Quit Game")

    console.print(table)

    while True:
        choice = input("> ").strip()

        if choice == "0":
            return "quit"

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        matches = [o for o in options if o.lower().startswith(choice.lower())]
        if len(matches) == 1:
            return matches[0]

        console.print("[red]Invalid choice — try again.[/red]")


# ─────────────────────────────────────────────
# MARKET DISPLAY
# ─────────────────────────────────────────────
def show_market():
    if not market.market_inventory:
        console.print("[red]Market is empty.[/red]")
        return

    table = Table(title=f"MARKET — Day {market.market_day}", box=box.SIMPLE_HEAVY)
    table.add_column("#", justify="right", style="dim")
    table.add_column("Name", style="bold")
    table.add_column("Type")
    table.add_column("Tier")
    table.add_column("Price", justify="right", style="green")
    table.add_column("Dividend/day", justify="right", style="gold1")
    table.add_column("Qty", justify="right")
    table.add_column("Expires", justify="right", style="dim")

    for i, p in enumerate(market.market_inventory, 1):
        types = " / ".join(type_tag(t) for t in p["type"])
        price = market.live_prices[p["name"]]
        lo, hi = DIVIDEND_RATES.get(p["tier"], (2, 5))
        table.add_row(
            str(i),
            p["name"],
            types,
            p["tier"],
            str(price),
            f"{lo}–{hi}",
            str(p["quantity"]),
            f"in {p['days_left']}d",
        )

    console.print(table)


# ─────────────────────────────────────────────
# PORTFOLIO
# ─────────────────────────────────────────────
def show_portfolio(player):
    if not player.inventory:
        console.print("[dim]You don't own any Pokémon yet.[/dim]")
        return

    total_invested = 0
    total_value = 0

    table = Table(
        title=f"{player.name}'s Portfolio  —  Day {player.current_day}",
        box=box.SIMPLE_HEAVY
    )
    table.add_column("#", style="dim")
    table.add_column("Name", style="bold")
    table.add_column("Type")
    table.add_column("Tier")
    table.add_column("Bought At", justify="right")
    table.add_column("Current", justify="right", style="green")
    table.add_column("P/L", justify="right")

    for i, p in enumerate(player.inventory, 1):
        types = " / ".join(type_tag(t) for t in p["type"])
        current = market.live_prices.get(p["name"], 0)
        pnl = current - p["purchase_price"]
        pnl_str = f"+{pnl}" if pnl >= 0 else str(pnl)
        pnl_color = "green" if pnl >= 0 else "red"

        table.add_row(
            str(i),
            p["name"],
            types,
            p["tier"],
            str(p["purchase_price"]),
            str(current),
            f"[{pnl_color}]{pnl_str}[/{pnl_color}]",
        )

        total_invested += p["purchase_price"]
        total_value += current

    total_pnl = total_value - total_invested
    total_pnl_str = f"+{total_pnl}" if total_pnl >= 0 else str(total_pnl)
    total_pnl_color = "green" if total_pnl >= 0 else "red"

    console.print(table)
    console.print(
        f"  Invested: [bold]{total_invested}[/bold]  "
        f"Portfolio Value: [green]{total_value}[/green]  "
        f"Net P/L: [{total_pnl_color}]{total_pnl_str}[/{total_pnl_color}]  "
        f"Total Dividends: [gold1]{player.total_dividends_earned}[/gold1]"
    )


# ─────────────────────────────────────────────
# NEWS
# ─────────────────────────────────────────────
def show_news():
    if not news.active_news:
        console.print("[dim]No active news events.[/dim]")
        return

    lines = []
    for i, n in enumerate(news.active_news, 1):
        days = n["days_left"]
        lines.append(
            f"[bold]{i}.[/bold]  {n['headline']}\n"
            f"     [dim](expires in {days} day{'s' if days != 1 else ''})[/dim]"
        )

    console.print(Panel(
        "\n\n".join(lines),
        title="[bold magenta]ACTIVE NEWS[/bold magenta]",
        padding=(1, 2)
    ))


# ─────────────────────────────────────────────
# BUY
# ─────────────────────────────────────────────
def action_buy(player):
    while True:
        print_header("BUY POKÉMON")
        show_market()

        raw = input("Select number (0 to go back): ").strip()

        if raw == "0":
            return

        if not raw.isdigit():
            console.print("[red]Enter a number.[/red]")
            continue

        idx = int(raw) - 1

        if idx < 0 or idx >= len(market.market_inventory):
            console.print("[red]Invalid selection.[/red]")
            continue

        chosen = market.market_inventory[idx]

        if chosen["quantity"] <= 0:
            console.print("[red]Sold out![/red]")
            continue

        price = market.live_prices[chosen["name"]]
        if player.buy_pokemon(chosen["name"], price):
            chosen["quantity"] -= 1
            if chosen["quantity"] == 0:
                market.market_inventory.remove(chosen)
        return


# ─────────────────────────────────────────────
# SELL
# ─────────────────────────────────────────────
def action_sell(player):
    while True:
        print_header("SELL POKÉMON")
        show_portfolio(player)

        if not player.inventory:
            return

        raw = input("Select number (0 to go back): ").strip()

        if raw == "0":
            return

        if not raw.isdigit():
            console.print("[red]Enter a number.[/red]")
            continue

        idx = int(raw) - 1

        if idx < 0 or idx >= len(player.inventory):
            console.print("[red]Invalid selection.[/red]")
            continue

        chosen = player.inventory[idx]
        sell_price = market.live_prices[chosen["name"]]
        player.sell_pokemon(chosen["name"], sell_price)
        return


# ─────────────────────────────────────────────
# REFRESH
# ─────────────────────────────────────────────
def action_refresh(player, counter):
    if counter[0] >= MAX_REFRESHES:
        console.print("[red]No refreshes left.[/red]")
        return

    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)
    counter[0] += 1
    remaining = MAX_REFRESHES - counter[0]
    console.print(f"[green]Market refreshed! ({remaining} refresh{'es' if remaining != 1 else ''} remaining)[/green]")
    show_market()


# ─────────────────────────────────────────────
# ADVANCE DAY
# ─────────────────────────────────────────────
def action_advance_day(player):
    # Step 1: Age + expire old news; collect expired headlines to display
    expired_headlines = news.advance_news()
    if expired_headlines:
        lines = "\n".join(f"  • [ENDED] {h.split('.')[0]}." for h in expired_headlines)
        console.print(Panel(lines, title="[dim]Stories concluded[/dim]", padding=(0, 2)))

    # Step 2: 70% chance of one new event
    news.generate_new_events(n=1 if random.random() < 0.7 else 0)

    # Step 3: Random ±15% price drift BEFORE news is re-applied
    market.random_price_fluctuations()

    # Step 4: Collect dividends before advancing the day counter
    payouts = player.collect_dividends()
    if payouts:
        total = sum(amt for _, amt in payouts)
        lines = "  ".join(f"[bold]{name}[/bold] +{amt}" for name, amt in payouts)
        console.print(Panel(
            f"{lines}\n\n  [green]Total dividend income: +{total} PokéDollars[/green]",
            title="[bold gold1]DAILY DIVIDENDS[/bold gold1]",
            padding=(0, 2),
        ))

    # Step 5–6: Age market listings, advance counters, generate fresh listings
    market.advance_day()
    player.advance_day()
    market.generate_daily_market(player.get_balance())

    # Step 7: Apply news multipliers to the fresh market (must be last)
    news.apply_news_to_market(market.market_inventory)

    console.print(Rule(f"[cyan]Day {player.current_day} begins[/cyan]"))
    show_news()
    show_market()


# ─────────────────────────────────────────────
# STARTER
# ─────────────────────────────────────────────
def choose_starter(player):
    starters = {
        "1": ("Bulbasaur",  "the calm, strategic choice — Grass/Poison type"),
        "2": ("Charmander", "the bold, high-risk choice — Fire type"),
        "3": ("Squirtle",   "the steady, defensive choice — Water type"),
    }

    console.print(Panel(
        "[white]Professor Oak steps forward and clears his throat.\n\n"
        "[italic]'The world of Pokémon trading is not so different\n"
        " from the world of Pokémon training. You must read\n"
        " the market, manage your risk, and above all —\n"
        " trust your instincts.'\n\n"
        "'Now then — every trainer needs a partner.\n"
        " Choose your starter Pokémon.'[/italic][/white]",
        title="[bold green]Professor Oak[/bold green]",
        padding=(1, 2),
    ))

    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("#", style="dim")
    table.add_column("Name", style="bold")
    table.add_column("Description")

    for key, (name, desc) in starters.items():
        table.add_row(key, name, desc)

    console.print(table)

    while True:
        raw = input("> ").strip()

        if raw in starters:
            chosen_name, _ = starters[raw]
            break

        match = [k for k, (n, _) in starters.items() if n.lower().startswith(raw.lower())]
        if len(match) == 1:
            chosen_name, _ = starters[match[0]]
            break

        console.print("[red]Please enter 1, 2, or 3 (or type the Pokémon's name).[/red]")

    from pokemon_db import pokemon_db
    data = pokemon_db[chosen_name]
    player.inventory.append({
        "name":           chosen_name,
        "tier":           data["tier"],
        "type":           data["type"],
        "purchase_price": 0,
        "day_bought":     player.current_day,
    })
    console.print(f"\n  [bold green]You chose {chosen_name}![/bold green] It's been added to your portfolio.")
    console.print("  [dim](Starter Pokémon are gifted — purchase price recorded as 0.)[/dim]\n")


# ─────────────────────────────────────────────
# GAME OVER
# ─────────────────────────────────────────────
def game_over(player):
    portfolio_value = sum(market.live_prices.get(p["name"], 0) for p in player.inventory)
    final_net_worth = player.poke_dollars + portfolio_value

    if final_net_worth >= 2000:
        rank = "[bold yellow]Pokémon Master Investor[/bold yellow]"
    elif final_net_worth >= 1200:
        rank = "[bold cyan]Elite Trader[/bold cyan]"
    elif final_net_worth >= 800:
        rank = "[bold green]Rising Trainer[/bold green]"
    elif final_net_worth >= 500:
        rank = "[white]Broke Even[/white]"
    else:
        rank = "[red]Better luck next time...[/red]"

    summary = Table(box=box.SIMPLE_HEAVY, show_header=False)
    summary.add_column("Label", style="dim")
    summary.add_column("Value", style="bold")

    summary.add_row("Player", player.name)
    summary.add_row("Cash Balance", f"[green]{player.poke_dollars}[/green] PokéDollars")
    summary.add_row("Portfolio Value", f"[green]{portfolio_value}[/green] PokéDollars")
    summary.add_row("Total Dividends Earned", f"[gold1]{player.total_dividends_earned}[/gold1] PokéDollars")
    summary.add_row("NET WORTH", f"[yellow]{final_net_worth}[/yellow] PokéDollars")
    summary.add_row("Rank", rank)

    if player.inventory:
        holdings = ", ".join(p["name"] for p in player.inventory)
        summary.add_row("Final Holdings", holdings)

    console.print(Panel(summary, title="[bold red]GAME OVER[/bold red]", padding=(1, 2)))


# ─────────────────────────────────────────────
# MAIN GAME
# ─────────────────────────────────────────────
def main():
    console.clear()
    intro_screen()

    name = input("Trainer name: ").strip() or "Trainer"
    player = Player(name, STARTING_BALANCE)

    choose_starter(player)

    refresh_counter = [0]

    market.generate_daily_market(player.get_balance())
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)

    console.print(f"\n  Good luck, [bold]{player.name}[/bold]! You have {TOTAL_DAYS} days to build your fortune.\n")
    show_news()
    show_market()

    while player.current_day <= TOTAL_DAYS:
        refreshes_left = MAX_REFRESHES - refresh_counter[0]

        print_header(f"DAY {player.current_day} / {TOTAL_DAYS}")
        print_status(player, refreshes_left)

        choice = prompt_choice([
            "View market",
            "Read news",
            "Buy Pokémon",
            "Sell Pokémon",
            "View portfolio",
            f"Refresh market ({refreshes_left} left)",
            "Advance day",
        ])

        if choice == "quit":
            console.print("\n  [dim]Thanks for playing — see you next time![/dim]")
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

        elif choice.startswith("Refresh market"):
            action_refresh(player, refresh_counter)

        elif choice == "Advance day":
            if player.current_day == TOTAL_DAYS:
                console.print("[bold red]This is the last day! Advancing ends the game.[/bold red]")
            action_advance_day(player)

            if player.current_day > TOTAL_DAYS:
                game_over(player)
                break


if __name__ == "__main__":
    main()
