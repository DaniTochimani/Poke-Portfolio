import market
import news
from player import Player

STARTING_BALANCE = 500
TOTAL_DAYS = 10
DIVIDER = "-" * 55
MAX_REFRESHES = 3

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
        matches = [o for o in options if o.lower().startswith(raw.lower())]

        if len(matches) == 1:
            return matches[0]
        print("Invalid choice - Try again.")

#Actions
def action_view_market() -> None:
    market.view_market()


def action_buy(player: Player) -> None:
    """Let the player pick a Pokémon from the market and buy it."""
    if not market.market_inventory:
        print("\n  The market is empty! Try refreshing or advancing the day.")
        return

    print_header("Buy a Pokémon")
    for i, p in enumerate(market.market_inventory, 1):
        types_str = "/".join(p["type"])
        print(f"  {i}. {p['name']} ({types_str}) [{p['tier']}]"
              f"  — {p['price']} PokéDollars  (Qty: {p['quantity']})")
    print("  0. Cancel")

    raw = input("\n  Pick a number: ").strip()
    if not raw.isdigit() or int(raw) == 0:
        print("  Cancelled.")
        return

    idx = int(raw) - 1
    if idx < 0 or idx >= len(market.market_inventory):
        print("  Invalid selection.")
        return

    chosen = market.market_inventory[idx]

    if chosen["quantity"] == 0:
        print(f"  {chosen['name']} is sold out!")
        return

    success = player.buy_pokemon(chosen["name"], chosen["price"])
    if success:
        chosen["quantity"] -= 1
        if chosen["quantity"] == 0:
            market.market_inventory.remove(chosen)
            print(f"  (Last {chosen['name']} sold — removed from market.)")


def action_sell(player: Player) -> None:
    """Let the player pick a Pokémon from their inventory to sell."""
    owned = player.inventory
    if not owned:
        print("\n  You don't own any Pokémon to sell.")
        return

    print_header("Sell a Pokémon")
    for i, p in enumerate(owned, 1):
        from pokemon_db import pokemon_db
        current_price = pokemon_db[p["name"]]["base_price"]
        for mp in market.market_inventory:
            if mp["name"] == p["name"]:
                current_price = mp["price"]
                break
        types_str = "/".join(p["type"])
        pnl = current_price - p["purchase_price"]
        pnl_label = f"+{pnl}" if pnl >= 0 else str(pnl)
        print(f"  {i}. {p['name']} ({types_str}) — Bought @ {p['purchase_price']}"
              f"  Current: {current_price}  P/L: {pnl_label}")
    print("  0. Cancel")

    raw = input("\n  Pick a number: ").strip()
    if not raw.isdigit() or int(raw) == 0:
        print("  Cancelled.")
        return

    idx = int(raw) - 1
    if idx < 0 or idx >= len(owned):
        print("  Invalid selection.")
        return

    chosen = owned[idx]
    from pokemon_db import pokemon_db
    sell_price = pokemon_db[chosen["name"]]["base_price"]
    for mp in market.market_inventory:
        if mp["name"] == chosen["name"]:
            sell_price = mp["price"]
            break

    player.sell_pokemon(chosen["name"], sell_price)


def action_refresh(player: Player, refresh_counter: list) -> None:
    """Manually refresh the market. Limited to MAX_REFRESHES times per game."""
    if refresh_counter[0] >= MAX_REFRESHES:
        print(f"\n  You've used all {MAX_REFRESHES} market refreshes for this run.")
        return
    market.refresh_market(player.get_balance())
    news.apply_news_to_market(market.market_inventory)  # keep news multipliers applied
    refresh_counter[0] += 1
    remaining = MAX_REFRESHES - refresh_counter[0]
    print(f"\n  Market refreshed! ({remaining} refresh{'es' if remaining != 1 else ''} remaining)")
    market.view_market()


def action_advance_day(player: Player) -> None:
    """
    End the current day in the correct order:
      1. Age + expire old news events (show any that just ended)
      2. Generate fresh news events for the new day
      3. Apply random base price fluctuations
      4. Age the market (remove listings that have expired)
      5. Generate new market listings
      6. Apply active news multipliers to the fresh market prices
      7. Increment counters and show the results
    """
    expired_headlines = news.advance_news()
    if expired_headlines:
        print("\n  📰 The following stories have concluded:")
        for h in expired_headlines:
            first_sentence = h.split(".")[0] + "."
            print(f"    • [ENDED] {first_sentence}")

    news.generate_new_events(n=2)

    market.random_price_fluctuations()

    market.advance_day()
    player.advance_day()
    market.generate_daily_market(player.get_balance())

    news.apply_news_to_market(market.market_inventory)

    print(f"\n  ⏩  Day advanced → Day {player.current_day}")

    news.display_news()
    market.view_market()

#News
def seed_opening_news() -> None:
    news.generate_new_events(n=2)
    news.apply_news_to_market(market.market_inventory)
    news.display_news()

#Game Over
def game_over(player: Player) -> None:
    from pokemon_db import pokemon_db

    print_header(f"GAME OVER — Day {player.current_day}")

    # Liquidate remaining portfolio at base prices
    portfolio_value = sum(
        pokemon_db[p["name"]]["base_price"] for p in player.inventory
    )
    final_net_worth = player.poke_dollars + portfolio_value

    print(f"\n  Player        : {player.name}")
    print(f"  Cash balance  : {player.poke_dollars} PokéDollars")
    print(f"  Portfolio     : {portfolio_value} PokéDollars")
    print(f"  ── NET WORTH  : {final_net_worth} PokéDollars ──")

    # Simple rank
    if final_net_worth >= 2000:
        rank = "🏆 Pokémon Master Investor"
    elif final_net_worth >= 1200:
        rank = "⭐ Elite Trader"
    elif final_net_worth >= 800:
        rank = "📈 Rising Trainer"
    elif final_net_worth >= 500:
        rank = "😐 Broke Even"
    else:
        rank = "📉 Better luck next time..."

    print(f"\n  Rank: {rank}\n")

#Starter Selection
def choose_starter(player: Player) -> None:
    """
    Present the three Kanto starters and gift the chosen one to the player.
    Added directly to inventory at purchase_price 0 — it's a gift, not a purchase.
    """
    starters = {
        "1": ("Bulbasaur",  "the calm, strategic choice — Grass/Poison type"),
        "2": ("Charmander", "the bold, high-risk choice — Fire type"),
        "3": ("Squirtle",   "the steady, defensive choice — Water type"),
    }

    print(f"\n{'─' * 55}")
    print("  Professor Oak steps forward and clears his throat.\n")
    print("  'The world of Pokémon trading is not so different")
    print("   from the world of Pokémon training. You must read")
    print("   the market, manage your risk, and above all —")
    print("   trust your instincts.'\n")
    print("  'Now then — every trainer needs a partner.")
    print("   Choose your starter Pokémon.'\n")

    for key, (name, desc) in starters.items():
        print(f"    {key}.  {name} — {desc}")

    while True:
        raw = input("\n  > ").strip()
        if raw in starters:
            chosen_name, _ = starters[raw]
            break
        match = [k for k, (n, _) in starters.items() if n.lower().startswith(raw.lower())]
        if len(match) == 1:
            chosen_name, _ = starters[match[0]]
            break
        print("  Please enter 1, 2, or 3 (or type the Pokémon's name).")

    from pokemon_db import pokemon_db
    data = pokemon_db[chosen_name]
    player.inventory.append({
        "name":           chosen_name,
        "tier":           data["tier"],
        "type":           data["type"],
        "purchase_price": 0,
        "day_bought":     player.current_day,
    })
    print(f"\n  You chose {chosen_name}! It's been added to your portfolio.")
    print("  (Starter Pokémon are gifted — purchase price recorded as 0.)\n")

#Main Game
def main() -> None:
    print_header("Welcome to PokéPortfolio!")
    print(f"""
  In a world where Pokémon aren't just partners — they're assets.

  Rare sightings drive prices up. New regulations crash entire types
  overnight. A single viral clip can send Magikarp soaring.

  You have {TOTAL_DAYS} days and {STARTING_BALANCE} PokéDollars to build a fortune.
  Read the news. Time the market. Buy low, sell high.

  Good luck, Trainer.
          """)
    name = input("  Enter your trainer name: ").strip() or "IamABot"

    player = Player(name, starting_balance=STARTING_BALANCE)

    choose_starter(player)

    refresh_counter = [0]
    market.generate_daily_market(player.get_balance())
    print(f"\n  Good luck, {player.name}! You have {TOTAL_DAYS} days to build your fortune.")
    seed_opening_news()
    market.view_market()

    while player.current_day <= TOTAL_DAYS:
        refreshes_left = MAX_REFRESHES - refresh_counter[0]
        print(f"\n{DIVIDER}")
        print(f"  Day {player.current_day} / {TOTAL_DAYS}   |   "
              f"Balance: {player.poke_dollars} PokéDollars   |   "
              f"Holdings: {len(player.inventory)}")
        print(DIVIDER)

        choice = prompt_choice([
            "View market",
            "Read news",
            "Buy Pokémon",
            "Sell Pokémon",
            "View portfolio",
            f"Refresh Market ({refreshes_left} left)",
            "Advance day",
        ])

        if choice == "quit":
            print("\n  Thanks for playing — see you next time!")
            break
        elif choice == "View market":
            action_view_market()
        elif choice == "Read news":
            news.display_news()
        elif choice == "Buy Pokémon":
            action_buy(player)
        elif choice == "Sell Pokémon":
            action_sell(player)
        elif choice == "View portfolio":
            player.view_portfolio()
        elif choice.startswith("Refresh Market"):
            action_refresh(player, refresh_counter)
        elif choice == "Advance day":
            if player.current_day == TOTAL_DAYS:
                print(f"\n  This is the last day! Advancing ends the game.")
            action_advance_day(player)

            if player.current_day > TOTAL_DAYS:
                game_over(player)
                break


if __name__ == "__main__":
    main()

