# PokéPortfolio

A strategy-based terminal finance game where players manage a dynamic portfolio of Pokémon using PokéDollars in an ever-changing market.

## How to Play

**Plain terminal (no dependencies):**
```
python game.py
```

**Rich UI — colored tables, panels, and type highlighting:**
```
pip install rich
python game_rich.py
```

Enter your trainer name, choose a starter Pokémon (gifted for free), then trade over 10 in-game days to maximize your net worth.

## Gameplay

- **Starting balance:** 500 PokéDollars
- **Game length:** 10 days
- **Win condition:** Highest net worth (cash + portfolio value) at game end

Each day you can:
- View the market and buy/sell Pokémon
- Read the news to anticipate price movements
- Refresh the market (limited to 3 refreshes per game)
- Advance to the next day

Prices fluctuate ±15% daily. Active news events apply additional multipliers on top of base fluctuations.

### Ranking (end of game)
| Net Worth | Rank |
|-----------|------|
| ≥ 2000 | Pokémon Master Investor |
| ≥ 1200 | Elite Trader |
| ≥ 800 | Rising Trainer |
| ≥ 500 | Broke Even |
| < 500 | Better luck next time... |

## Dividends

Every Pokémon you hold pays a small daily dividend when the day advances. Higher-tier Pokémon pay more. Dividends are automatically added to your balance and displayed in the Rich UI variant. The market table shows the dividend range for each listing so you can factor passive income into buying decisions. Your cumulative **Total Dividends Earned** is shown in the portfolio footer and the end-of-game summary.

| Tier | Daily Payout Range |
|------|--------------------|
| Baby | 2–5 |
| 1st stage | 3–7 |
| Starter | 5–10 |
| Base (single-stage) | 5–12 |
| 2nd stage | 10–22 |
| 3rd stage | 15–30 |
| Pseudo-legendary | 22–45 |
| Legendary | 35–65 |
| Mythical | 55–85 |

## Market

- Each listing shows its **Dividend/day** range so you can compare passive income potential at a glance
- 3–6 Pokémon appear daily; each listing expires after 2 days
- Rare/legendary Pokémon only appear once your balance reaches 300+ PokéDollars
- Prices cap at 8,000 PokéDollars (ultra-expensive Pokémon excluded)

## News System

Events drawn from a pool of 30+ headlines affect prices for 1–5 days via a locked-in multiplier. Events target:
- Specific types (Fire, Water, Electric, Psychic, Dragon, Grass, Ghost, Fighting, Ice, Dark, Poison)
- Tiers (starter, pseudo-legendary, legendary)
- Named Pokémon (Magikarp, Eevee, Snorlax, Gyarados, Ditto)
- The entire market (bull runs, crashes, regulatory reviews)

Two events seed at game start; roughly one new event generates each day.

## Pokémon Database

Covers Generation I and II with regional variants (Alolan, Galarian, Hisuian, Paldean forms).

| Tier | Price Range | Examples |
|------|-------------|---------|
| Baby | 80–90 | Pichu, Cleffa, Elekid |
| 1st stage | 30–200 | Bulbasaur, Dratini |
| 2nd stage | 150–600 | Charizard line mid-evos |
| 3rd stage | 250–800 | Venusaur, Tyranitar |
| Starter | 100 | Bulbasaur, Charmander, Squirtle, Johto starters |
| Base (single-stage) | 150–500 | Eevee, Snorlax, Ditto |
| Pseudo-legendary | 800 | Dragonite |
| Legendary | 1000–1200 | Articuno, Mewtwo, Lugia |
| Mythical | 1500 | Mew, Celebi |

## External Contributors

AI — Used as a development aid throughout the project. Assisted with debugging logic errors, suggesting fixes for edge cases in the buy/sell flow, helping write and refine news headlines, formatting and cleaning up code comments, and generating this README documentation based on the existing codebase.

## File Structure

```
Poke-Portfolio/
 ├─ game.py          # Main game loop — plain terminal UI
 ├─ game_rich.py     # Rich terminal UI — colored tables, panels, dividend display
 ├─ market.py        # Market generation, live price tracking, daily fluctuations
 ├─ news.py          # News event pool, activation, aging, and price multiplier application
 ├─ player.py        # Player state: balance, inventory, buy/sell, dividends, portfolio view
 ├─ pokemon_db.py    # Full Pokémon database with types, tiers, and base prices
 └─ sample.py        # Scratch/testing file
```
