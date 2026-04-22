#pip install rich

import market
import news
from player import Player

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console()

STARTING_BALANCE = 500
TOTAL_DAYS       = 10
MAX_REFRESHES    = 3

# ── Type colours ──────────────────────────────────────────────────────
TYPE_COLOURS = {
    "Fire":     "bold red",
    "Water":    "bold cyan",
    "Grass":    "bold green",
    "Electric": "bold yellow",
    "Psychic":  "bold magenta",
    "Dragon":   "bold bright_blue",
    "Ghost":    "bold purple",
    "Ice":      "bold bright_cyan",
    "Fighting": "bold orange3",
    "Poison":   "bold violet",
    "Dark":     "bold grey62",
    "Rock":     "bold wheat4",
    "Ground":   "bold sandy_brown",
    "Normal":   "white",
    "Flying":   "bold sky_blue1",
    "Bug":      "bold dark_olive_green3",
    "Steel":    "bold grey84",
    "Fairy":    "bold pink1",
}

TIER_COLOURS = {
    "starter":          "bold gold1",
    "baby":             "pink1",
    "1st_stage":        "white",
    "2nd_stage":        "cyan",
    "3rd_stage":        "bold cyan",
    "base":             "white",
    "pseudo_legendary": "bold magenta",
    "legendary":        "bold yellow",
    "mythical":         "bold bright_magenta",
}

def type_tag(t: str) -> str:
    col = TYPE_COLOURS.get(t, "white")
    return f"[{col}]{t}[/{col}]"

def tier_tag(t: str) -> str:
    col = TIER_COLOURS.get(t, "white")
    label = t.replace("_", " ").upper()
    return f"[{col}]{label}[/{col}]"


# ══════════════════════════════════════════════════════════════════════
#  DISPLAY HELPERS
# ══════════════════════════════════════════════════════════════════════

def print_header(title: str) -> None:
    console.print()
    console.print(Rule(f"[bold yellow]★  {title}  ★[/bold yellow]", style="yellow"))


def status_bar(player: Player) -> None:
    from pokemon_db import pokemon_db
    portfolio_val = sum(
        market.current_prices.get(p["name"], pokemon_db[p["name"]]["base_price"])
        for p in player.inventory
    )
    net = player.poke_dollars + portfolio_val
    txt = (
        f"[bold white]TRAINER[/bold white] [bold yellow]{player.name}[/bold yellow]"
        f"   [bold white]DAY[/bold white] [bold cyan]{player.current_day}[/bold cyan][white]/{TOTAL_DAYS}[/white]"
        f"   [bold white]BALANCE[/bold white] [bold green]₽{player.poke_dollars:,}[/bold green]"
        f"   [bold white]HOLDINGS[/bold white] [bold cyan]{len(player.inventory)}[/bold cyan]"
        f"   [bold white]NET WORTH[/bold white] [bold yellow]₽{net:,}[/bold yellow]"
    )
    console.print(Panel(txt, style="bright_black", padding=(0, 1)))


def show_market() -> None:
    if not market.market_inventory:
        console.print(Panel("[dim]Market is empty — refresh or advance the day.[/dim]",
                            title="[bold cyan]MARKET[/bold cyan]", style="bright_black"))
        return

    t = Table(box=box.SIMPLE_HEAVY, header_style="bold cyan",
              show_edge=False, padding=(0, 1), expand=True)
    t.add_column("#",      style="dim",        width=3, justify="right")
    t.add_column("NAME",   style="bold white", min_width=16)
    t.add_column("TYPE",   min_width=22)
    t.add_column("TIER",   min_width=14)
    t.add_column("PRICE",  justify="right", style="bold yellow")
    t.add_column("QTY",    justify="right", style="dim")
    t.add_column("DAYS",   justify="right", style="dim")

    for i, p in enumerate(market.market_inventory, 1):
        types_str = " [dim]|[/dim] ".join(type_tag(tp) for tp in p["type"])
        t.add_row(str(i), p["name"], types_str, tier_tag(p["tier"]),
                  f"₽{p['price']:,}", str(p["quantity"]), str(p["days_left"]))

    console.print(Panel(t, title=f"[bold cyan]MARKET[/bold cyan]  [dim]Day {market.market_day}[/dim]",
                        style="bright_black"))


def show_portfolio(player: Player) -> None:
    from pokemon_db import pokemon_db
    if not player.inventory:
        console.print(Panel("[dim]No Pokémon owned yet.[/dim]",
                            title="[bold green]PORTFOLIO[/bold green]", style="bright_black"))
        return

    t = Table(box=box.SIMPLE_HEAVY, header_style="bold green",
              show_edge=False, padding=(0, 1), expand=True)
    t.add_column("#",       style="dim",        width=3,  justify="right")
    t.add_column("NAME",    style="bold white", min_width=16)
    t.add_column("TYPE",    min_width=22)
    t.add_column("BOUGHT",  justify="right", style="dim")
    t.add_column("CURRENT", justify="right", style="bold yellow")
    t.add_column("P / L",   justify="right", min_width=10)

    total_invested, total_value = 0, 0
    for i, p in enumerate(player.inventory, 1):
        cur = market.current_prices.get(p["name"], pokemon_db[p["name"]]["base_price"])
        pnl = cur - p["purchase_price"]
        pnl_str = (f"[bold green]+₽{pnl:,}[/bold green]" if pnl > 0
                   else f"[bold red]₽{pnl:,}[/bold red]" if pnl < 0
                   else "[dim]₽0[/dim]")
        types_str = " [dim]|[/dim] ".join(type_tag(tp) for tp in p["type"])
        total_invested += p["purchase_price"]
        total_value    += cur
        t.add_row(str(i), p["name"], types_str,
                  f"₽{p['purchase_price']:,}", f"₽{cur:,}", pnl_str)

    net_pnl = total_value - total_invested
    net_str = (f"[bold green]+₽{net_pnl:,}[/bold green]" if net_pnl > 0
               else f"[bold red]₽{net_pnl:,}[/bold red]" if net_pnl < 0
               else "[dim]₽0[/dim]")
    summary = (f"[dim]INVESTED[/dim] [yellow]₽{total_invested:,}[/yellow]"
               f"   [dim]VALUE[/dim] [yellow]₽{total_value:,}[/yellow]"
               f"   [dim]NET P/L[/dim] {net_str}")
    console.print(Panel(t, title="[bold green]PORTFOLIO[/bold green]",
                        subtitle=summary, style="bright_black"))


def show_news() -> None:
    if not news.active_news:
        console.print(Panel("[dim]No active news stories.[/dim]",
                            title="[bold magenta]NEWS FEED[/bold magenta]", style="bright_black"))
        return
    lines = []
    for i, event in enumerate(news.active_news, 1):
        tag = ("[bold red]● BREAKING[/bold red]" if event["days_left"] == 1
               else f"[bold cyan]● ONGOING[/bold cyan] [dim]({event['days_left']} days left)[/dim]")
        lines.append(f"[dim][{i}][/dim]  {tag}")
        lines.append(f"[white]{event['headline']}[/white]")
        lines.append("")
    console.print(Panel("\n".join(lines).strip(),
                        title="[bold magenta]NEWS FEED[/bold magenta]",
                        style="bright_black", padding=(1, 2)))


def prompt_choice(options: list[str]) -> str:
    console.print()
    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="dim",        width=4, justify="right")
    t.add_column(style="bold white", min_width=30)
    for i, opt in enumerate(options, 1):
        t.add_row(f"[cyan]{i}[/cyan]", opt)
    t.add_row("[red]0[/red]", "[dim]Quit Game[/dim]")
    console.print(t)

    while True:
        raw = console.input("\n  [bold cyan]>[/bold cyan] ").strip()
        if raw.isdigit():
            idx = int(raw)
            if idx == 0:
                return "quit"
            if 1 <= idx <= len(options):
                return options[idx - 1]
        matches = [o for o in options if o.lower().startswith(raw.lower())]
        if len(matches) == 1:
            return matches[0]
        console.print("  [red]Invalid choice — try again.[/red]")


# ══════════════════════════════════════════════════════════════════════
#  ACTIONS
# ══════════════════════════════════════════════════════════════════════

def action_buy(player: Player) -> None:
    if not market.market_inventory:
        console.print("[red]  Market is empty![/red]")
        return
    print_header("BUY A POKÉMON")
    show_market()
    console.print("  [dim]Enter number to buy, or 0 to cancel.[/dim]")
    raw = console.input("\n  [bold cyan]>[/bold cyan] ").strip()
    if not raw.isdigit() or int(raw) == 0:
        console.print("  [dim]Cancelled.[/dim]")
        return
    idx = int(raw) - 1
    if idx < 0 or idx >= len(market.market_inventory):
        console.print("  [red]Invalid selection.[/red]")
        return
    chosen = market.market_inventory[idx]
    if chosen["quantity"] == 0:
        console.print(f"  [red]{chosen['name']} is sold out![/red]")
        return
    success = player.buy_pokemon(chosen["name"], chosen["price"])
    if success:
        chosen["quantity"] -= 1
        if chosen["quantity"] == 0:
            market.market_inventory.remove(chosen)
            console.print(f"  [dim](Last {chosen['name']} sold — removed from market.)[/dim]")


def action_sell(player: Player) -> None:
    from pokemon_db import pokemon_db
    if not player.inventory:
        console.print("[red]  You don't own any Pokémon to sell.[/red]")
        return
    print_header("SELL A POKÉMON")
    show_portfolio(player)
    console.print("  [dim]Enter number to sell, or 0 to cancel.[/dim]")
    raw = console.input("\n  [bold cyan]>[/bold cyan] ").strip()
    if not raw.isdigit() or int(raw) == 0:
        console.print("  [dim]Cancelled.[/dim]")
        return
    idx = int(raw) - 1
    if idx < 0 or idx >= len(player.inventory):
        console.print("  [red]Invalid selection.[/red]")
        return
    chosen = player.inventory[idx]
    sell_price = market.current_prices.get(chosen["name"], pokemon_db[chosen["name"]]["base_price"])
    player.sell_pokemon(chosen["name"], sell_price)


def action_refresh(player: Player, refresh_counter: list) -> None:
    if refresh_counter[0] >= MAX_REFRESHES:
        console.print(f"  [red]You've used all {MAX_REFRESHES} refreshes.[/red]")
        return
    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)
    market.sync_market_prices()
    refresh_counter[0] += 1
    remaining = MAX_REFRESHES - refresh_counter[0]
    console.print(f"\n  [green]Market refreshed![/green] [dim]({remaining} refresh{'es' if remaining != 1 else ''} remaining)[/dim]")
    show_market()


def action_advance_day(player: Player) -> None:
    expired = news.advance_news()
    if expired:
        console.print("\n  [magenta]📰 Stories concluded:[/magenta]")
        for h in expired:
            console.print(f"    [dim]• [ENDED] {h.split('.')[0]}.[/dim]")
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)
    market.advance_day()
    player.advance_day()
    market.random_price_fluctuations()
    market.generate_daily_market(player.get_balance())
    console.print(f"\n  [bold cyan]⏩  Day advanced → Day {player.current_day}[/bold cyan]")
    show_news()
    show_market()


# ══════════════════════════════════════════════════════════════════════
#  STARTER / NEWS / GAME OVER
# ══════════════════════════════════════════════════════════════════════

def choose_starter(player: Player) -> None:
    starters = {
        "1": ("Bulbasaur",  "Grass / Poison", "Calm, strategic"),
        "2": ("Charmander", "Fire",           "Bold, high-risk"),
        "3": ("Squirtle",   "Water",          "Steady, defensive"),
    }
    console.print()
    console.print(Panel(
        "[italic white]'The world of Pokémon trading is not so different from the world of Pokémon training.\n"
        "You must read the market, manage your risk, and above all — trust your instincts.\n\n"
        "Now then — every trainer needs a partner.  Choose your starter Pokémon.'[/italic white]",
        title="[bold yellow]PROFESSOR OAK[/bold yellow]", style="bright_black", padding=(1, 3)))

    t = Table(box=box.SIMPLE_HEAVY, header_style="bold yellow", show_edge=False, padding=(0, 2))
    t.add_column("#",     style="dim",        width=3, justify="right")
    t.add_column("NAME",  style="bold white", min_width=14)
    t.add_column("TYPE",  min_width=18)
    t.add_column("STYLE", style="dim")
    for key, (name, types, style) in starters.items():
        type_parts = " [dim]/[/dim] ".join(type_tag(tp.strip()) for tp in types.split("/"))
        t.add_row(f"[cyan]{key}[/cyan]", name, type_parts, style)
    console.print(t)

    while True:
        raw = console.input("\n  [bold cyan]>[/bold cyan] ").strip()
        if raw in starters:
            chosen_name = starters[raw][0]; break
        match = [k for k, (n, _, _) in starters.items() if n.lower().startswith(raw.lower())]
        if len(match) == 1:
            chosen_name = starters[match[0]][0]; break
        console.print("  [red]Please enter 1, 2, or 3.[/red]")

    from pokemon_db import pokemon_db
    data = pokemon_db[chosen_name]
    player.inventory.append({"name": chosen_name, "tier": data["tier"],
                              "type": data["type"], "purchase_price": 0,
                              "day_bought": player.current_day})
    console.print(f"\n  [bold green]You chose {chosen_name}![/bold green] [dim]Added to portfolio at no cost.[/dim]")


def seed_opening_news() -> None:
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)
    market.sync_market_prices()
    show_news()


def game_over(player: Player) -> None:
    from pokemon_db import pokemon_db
    portfolio_value = sum(
        market.current_prices.get(p["name"], pokemon_db[p["name"]]["base_price"])
        for p in player.inventory)
    final_net_worth = player.poke_dollars + portfolio_value

    if final_net_worth >= 2000:
        rank, rs = "🏆  POKÉMON MASTER INVESTOR", "bold gold1"
    elif final_net_worth >= 1200:
        rank, rs = "⭐  ELITE TRADER",             "bold cyan"
    elif final_net_worth >= 800:
        rank, rs = "📈  RISING TRAINER",            "bold green"
    elif final_net_worth >= 500:
        rank, rs = "😐  BROKE EVEN",                "white"
    else:
        rank, rs = "📉  BETTER LUCK NEXT TIME",     "bold red"

    print_header("GAME OVER")
    t = Table(box=box.SIMPLE_HEAVY, show_header=False, show_edge=False, padding=(0, 2))
    t.add_column(style="dim",        min_width=20)
    t.add_column(style="bold white", justify="right")
    t.add_row("Trainer",         f"[yellow]{player.name}[/yellow]")
    t.add_row("Cash balance",    f"[green]₽{player.poke_dollars:,}[/green]")
    t.add_row("Portfolio value", f"[green]₽{portfolio_value:,}[/green]")
    t.add_row("──────────────", "──────────")
    t.add_row("[bold]FINAL NET WORTH[/bold]", f"[bold yellow]₽{final_net_worth:,}[/bold yellow]")
    console.print(Panel(t, title="[bold yellow]FINAL LEDGER[/bold yellow]", style="bright_black"))
    console.print(Panel(f"[{rs}]{rank}[/{rs}]", style="bright_black", padding=(1, 4)))


# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════

def main() -> None:
    console.clear()
    print_header("WELCOME TO POKÉPORTFOLIO")
    console.print(Panel(
        "[white]In a world where Pokémon aren't just partners — they're [bold yellow]assets[/bold yellow].\n\n"
        "[red]Rare sightings[/red] drive prices up.  New regulations [red]crash[/red] entire types overnight.\n"
        "A single viral clip can send [bold green]Magikarp soaring[/bold green].\n\n"
        "You have [bold cyan]10 days[/bold cyan] and [bold yellow]₽500[/bold yellow] to build a fortune.\n"
        "Read the news.  Time the market.  Buy low, sell high.[/white]",
        style="bright_black", padding=(1, 3)))

    name = console.input("\n  [bold cyan]Enter your trainer name:[/bold cyan] ").strip() or "Trainer"
    player = Player(name, starting_balance=STARTING_BALANCE)

    choose_starter(player)

    refresh_counter = [0]
    market.generate_daily_market(player.get_balance())
    market.generate_daily_market(player.get_balance())
    console.print(f"\n  [bold green]Good luck, {player.name}![/bold green] [dim]{TOTAL_DAYS} days on the clock.[/dim]")
    seed_opening_news()
    show_market()

    while player.current_day <= TOTAL_DAYS:
        refreshes_left = MAX_REFRESHES - refresh_counter[0]
        console.print()
        status_bar(player)

        choice = prompt_choice([
            "View market",
            "Read news",
            "Buy Pokémon",
            "Sell Pokémon",
            "View portfolio",
            f"Refresh market  [{refreshes_left} left]",
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
                console.print("\n  [bold red]This is the last day! Advancing ends the game.[/bold red]")
            action_advance_day(player)
            if player.current_day > TOTAL_DAYS:
                game_over(player)
                break


if __name__ == "__main__":
    main()
