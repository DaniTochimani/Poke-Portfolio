from pokemon_db import pokemon_db


class Player:
    """
    Represents a player in PokéPortfolio.

    Attributes:
        name         (str)  : The player's name.
        poke_dollars (int)  : Current balance.
        inventory    (list) : List of dicts, one per owned Pokémon.
        current_day  (int)  : Tracks in-game time (starts at 1).
    """

    def __init__(self, name, starting_balance=500):
        """
        Called automatically when you do: player = Player("Ash")

        'self' refers to the specific instance being created —
        think of it like 'this' in other languages.
        """
        self.name = name
        self.poke_dollars = starting_balance
        self.inventory = []   # Each entry: {name, tier, purchase_price, day_bought}
        self.current_day = 1 # add dividend_price

    # ------------------------------------------------------------------
    # BUYING
    # ------------------------------------------------------------------

    def buy_pokemon(self, pokemon_name, market_price):
        """
        Attempt to buy a Pokémon from the market.

        Returns True if the purchase succeeded, False otherwise.
        Returning a boolean (instead of just printing) lets the caller
        (e.g. game.py) decide how to respond to success/failure.
        """
        if pokemon_name not in pokemon_db:
            print(f"{pokemon_name} doesn't exist in the Pokédex.")
            return False

        if market_price > self.poke_dollars:
            print(f"Not enough PokéDollars! You have {self.poke_dollars} but {pokemon_name} costs {market_price}.")
            return False

        # Deduct the cost
        self.poke_dollars -= market_price

        # Record the purchase in inventory
        # We store 'purchase_price' so we can calculate profit/loss later.
        self.inventory.append({
            "name": pokemon_name,
            "tier": pokemon_db[pokemon_name]["tier"],
            "type": pokemon_db[pokemon_name]["type"],
            "purchase_price": market_price,
            "day_bought": self.current_day,
        })

        print(f"Bought {pokemon_name} for {market_price} PokéDollars! Balance: {self.poke_dollars}")
        return True

    # ------------------------------------------------------------------
    # SELLING
    # ------------------------------------------------------------------

    def sell_pokemon(self, pokemon_name, current_market_price):
        """
        Sell the FIRST copy of pokemon_name in the player's inventory.

        We use 'next()' with a generator expression to find it efficiently
        without looping through the whole list manually.
        """
        # Find the first matching Pokémon in inventory
        entry = None
        for p in self.inventory:
            if p["name"] == pokemon_name:
                entry = p
                break

        if entry is None:
            print(f"You don't own a {pokemon_name}.")
            return False

        # Calculate profit or loss
        profit = current_market_price - entry["purchase_price"]
        if profit >= 0:
            profit_label = f"+{profit}"
        else:
            profit_label = str(profit)

        self.inventory.remove(entry)
        self.poke_dollars += current_market_price

        print(f"Sold {pokemon_name} for {current_market_price} PokéDollars! "
              f"(P/L: {profit_label})  Balance: {self.poke_dollars}")
        return True

    # ------------------------------------------------------------------
    # DAY TRACKING
    # ------------------------------------------------------------------

    def advance_day(self):
        """Increment the in-game day counter."""
        self.current_day += 1

    # ------------------------------------------------------------------
    # VIEWING / STATS
    # ------------------------------------------------------------------

    def view_portfolio(self):
        """
        Print a summary of the player's current holdings and unrealized P/L.

        'Unrealized' means we haven't sold yet — it's what we'd make IF
        we sold at current base price (market fluctuations not applied here).
        """
        print(f"\n=== {self.name}'s Portfolio  |  Day {self.current_day}  |  Balance: {self.poke_dollars} PokéDollars ===")

        if not self.inventory:
            print("  (No Pokémon owned)")
            return

        total_invested = 0
        total_current_value = 0

        for p in self.inventory:
            base_price = pokemon_db[p["name"]]["base_price"]
            pnl = base_price - p["purchase_price"]
            pnl_label = f"+{pnl}" if pnl >= 0 else str(pnl)
            types_str = "/".join(p["type"])

            print(f"  {p['name']} ({types_str}) [{p['tier']}]"
                  f"  Bought: {p['purchase_price']} on Day {p['day_bought']}"
                  f"  Base Value: {base_price}  P/L: {pnl_label}")

            total_invested += p["purchase_price"]
            total_current_value += base_price

        total_pnl = total_current_value - total_invested
        total_pnl_label = f"+{total_pnl}" if total_pnl >= 0 else str(total_pnl)
        print(f"\n  Total Invested: {total_invested}  |  "
              f"Portfolio Value: {total_current_value}  |  "
              f"Net P/L: {total_pnl_label}")

    def get_balance(self):
        """Return the player's current balance (useful for market.py calls)."""
        return self.poke_dollars

    def owned_names(self):
        """Return a list of Pokémon names the player currently holds."""
        return [p["name"] for p in self.inventory]
