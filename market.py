import random
from pokemon_db import pokemon_db

# ---------- Market Variables ----------
market_inventory = []  # Pokémon currently available in the market
market_day = 1         # Tracks the current market day

# ---------- Global Live Prices ----------
live_prices = {}

# ---------- Price Modifiers (Events) ----------
# These can be triggered based on game events or random occurrences
price_modifiers = {
    "fire_event": {"type": "Fire", "modifier": 1.2},
    "water_event": {"type": "Water", "modifier": 0.8},
    "grass_event": {"type": "Grass", "modifier": 1.1},
}

# ---------- Initialize Live Prices ----------
def initialize_prices():
    """
    Creates a global live price for every Pokémon in the game.
    This ensures all Pokémon always have a price regardless of market listing.
    """
    global live_prices
    for name, data in pokemon_db.items():
        live_prices[name] = data["base_price"]

# ---------- Helper: Filter Pokémon for Player ----------
def eligible_pokemon(player_balance):
    """
    Returns a list of Pokémon names the player can see based on their balance.
    Rare Pokémon only appear if player_balance >= 300.
    Maximum price cap = 8000 for ultra-expensive Pokémon.
    """
    eligible = []
    for name, data in pokemon_db.items():
        base_price = data['base_price']

        if base_price > 8000:
            continue  # Skip ultra-expensive Pokémon

        # Skip rare Pokémon if balance < 300
        if data['tier'] in ['pseudo_legendary', 'legendary', 'mythical'] and player_balance < 300:
            continue

        eligible.append(name)
    return eligible

# ---------- Generate Daily Market ----------
def generate_daily_market(player_balance):
    """
    Populate the market with 3-6 Pokémon based on player's balance.
    Each Pokémon gets a random quantity (1-3) and stays for 2 market days.
    Applies event-based price modifiers if applicable.
    """
    global market_inventory
    market_inventory = []  # Reset market each day

    eligible = eligible_pokemon(player_balance)
    if not eligible:
        print("No eligible Pokémon for your balance.")
        return

    num_pokemon = random.randint(3, 6)
    selected = random.sample(eligible, min(num_pokemon, len(eligible)))

    for name in selected:
        data = pokemon_db[name]

        # NEW: Use global live price instead of base price
        price = live_prices[name]

        # Apply type-based price modifiers
        for mod in price_modifiers.values():
            if any(t == mod['type'] for t in data['type']):
                price = int(price * mod['modifier'])

        market_inventory.append({
            "name": name,
            "type": data['type'],
            "tier": data['tier'],
            "quantity": random.randint(1, 3),
            "days_left": 2  # Pokémon remains for 2 market days
        })

# ---------- Advance Market Day ----------
def advance_day():
    """
    Progresses the market by one day.
    Reduces days_left for each Pokémon and removes expired ones.
    Increments market_day counter.
    """
    global market_inventory, market_day
    market_day += 1

    for pokemon in market_inventory:
        pokemon['days_left'] -= 1

    # Remove expired Pokémon
    market_inventory = [p for p in market_inventory if p['days_left'] > 0]

# ---------- Refresh Market ----------
def refresh_market(player_balance):
    """
    Player manually refreshes the market.
    Replaces all current Pokémon with a new random selection.
    Market day does not advance.
    """
    generate_daily_market(player_balance)

# ---------- View Market ----------
def view_market():
    """
    Prints the current Pokémon in the market.
    Displays name, type, tier, price, quantity, and days left.
    """
    print(f"\n--- Market Day {market_day} ---")
    for p in market_inventory:
        types_str = ", ".join(p['type'])

        # NEW: live price lookup
        price = live_prices[p["name"]]

        print(f"{p['name']} ({types_str}) - {p['tier'].capitalize()} - Price: {price} - Qty: {p['quantity']} - Days Left: {p['days_left']}")

# ---------- Optional: Simulate Market Price Fluctuation ----------
def random_price_fluctuations():
    """
    Randomly increases or decreases Pokémon prices daily by 5-15%.
    Makes the market feel more dynamic even without events.
    """
    for name in live_prices:
        fluctuation = random.uniform(0.85, 1.15)  # +/- 15%
        live_prices[name] = max(1, int(live_prices[name] * fluctuation))
