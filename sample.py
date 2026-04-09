import market
from player import Player

# Create a player with 500 starting balance
player = Player("Ash", starting_balance=500)

# Generate the market based on player's balance
market.generate_daily_market(player.get_balance())

# See what's available
market.view_market()

# Buy a Pokémon
print()
player.buy_pokemon("Magikarp", 20)

# Try to buy something too expensive
player.buy_pokemon("Mewtwo", 1200)

# Try to buy something that doesn't exist
player.buy_pokemon("Pikapool", 100)

# View portfolio after buying
player.view_portfolio()

# Advance to day 2
player.advance_day()
market.advance_day()

# Sell Magikarp at a profit
print()
player.sell_pokemon("Magikarp", 45)

# Try to sell something you don't own
player.sell_pokemon("Charizard", 600)

# Final portfolio
player.view_portfolio()
