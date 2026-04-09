import random

pokemon_market = {
  "Pikachu": {"price": 100, "type": "Electric"},
  "Charmander": {"price": 100, "type": "Fire"},
  "Squirtle": {"price": 100, "type": "Water"},
  "Bulbasaur": {"price": 100, "type": "Grass"}
}

def simulate_day(market):
  print("---- New Day ----")

for name in market:
  change = random.uniform(-0.1, 0.1)
  old_price = market[name]["price"]
  new_price = int(old_price * (1 + change))

  market[name]["price"] = new_price

  print(f"{name}: {old_price} -> {new_price}")

simulate_day(pokemon_market)

  


