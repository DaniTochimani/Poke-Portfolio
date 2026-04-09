#Pokemon List: https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number#Generation_I

# Baby Pokémon
# Tier: Baby
# Base Price: 50-90
# Notes: First stage in evolution lines, weak stats, cheap, examples: Pichu, Cleffa, Igglybuff, Tyrogue, Smoochum, Elekid, Magby

# 1st Stage / Base Pokémon
# Tier: Base
# Base Price: 50-200
# Notes: Can evolve, moderate price, examples: Bulbasaur, Chikorita, Teddiursa, Shuckle

# 2nd Stage / Mid Evolutions
# Tier: Mid Evolution
# Base Price: 200-500
# Notes: Stronger, good battle potential, examples: Ivysaur, Bayleef, Piloswine, Octillery

# 3rd Stage / Final Evolutions
# Tier: Final Evolution
# Base Price: 400-800
# Notes: High stats and utility, examples: Venusaur, Meganium, Tyranitar, Blissey

# Pseudo-Legendary
# Tier: Pseudo-Legendary
# Base Price: 600-800
# Notes: High combat potential, usually final evolutions with 3-stage lines, examples: Dragonite, Tyranitar

# Legendary
# Tier: Legendary
# Base Price: 1000-1200
# Notes: Rare, single-stage, examples: Raikou, Entei, Suicune, Lugia, Ho-Oh

# Mythical
# Tier: Mythical
# Base Price: 1500
# Notes: Extremely rare, event-exclusive, examples: Mew, Celebi

# Regional / Alternate Forms
# Tier: Regional Form
# Base Price: +20-100 compared to base form
# Notes: Alolan, Galarian, Hisuian forms, examples: Qwilfish_Hisuian, Corsola_Galarian, Typhlosion_Hisuian

pokemon_db = {
  "Bulbasaur": {"type": ["Grass", "Poison"], "tier": "starter", "base_price": 100},
  "Ivysaur": {"type": ["Grass", "Poison"], "tier": "2nd_stage", "base_price": 300},
  "Venusaur": {"type": ["Grass", "Poison"], "tier": "3rd_stage", "base_price": 600},

  "Charmander": {"type": ["Fire"], "tier": "starter", "base_price": 100},
  "Charmeleon": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 300},
  "Charizard": {"type": ["Fire", "Flying"], "tier": "3rd_stage", "base_price": 600},

  "Squirtle": {"type": ["Water"], "tier": "starter", "base_price": 100},
  "Wartortle": {"type": ["Water"], "tier": "2nd_stage", "base_price": 300},
  "Blastoise": {"type": ["Water"], "tier": "3rd_stage", "base_price": 600},

  "Caterpie": {"type": ["Bug"], "tier": "1st_stage", "base_price": 50},
  "Metapod": {"type": ["Bug"], "tier": "2nd_stage", "base_price": 150},
  "Butterfree": {"type": ["Bug", "Flying"], "tier": "3rd_stage", "base_price": 250},

  "Weedle": {"type": ["Bug", "Poison"], "tier": "1st_stage", "base_price": 50},
  "Kakuna": {"type": ["Bug", "Poison"], "tier": "2nd_stage", "base_price": 150},
  "Beedrill": {"type": ["Bug", "Poison"], "tier": "3rd_stage", "base_price": 250},

  "Pidgey": {"type": ["Normal", "Flying"], "tier": "1st_stage", "base_price": 50},
  "Pidgeotto": {"type": ["Normal", "Flying"], "tier": "2nd_stage", "base_price": 200},
  "Pidgeot": {"type": ["Normal", "Flying"], "tier": "3rd_stage", "base_price": 400},

  "Rattata": {"type": ["Normal"], "tier": "1st_stage", "base_price": 30},
  "Raticate": {"type": ["Normal"], "tier": "2nd_stage", "base_price": 150},

  "Spearow": {"type": ["Normal", "Flying"], "tier": "1st_stage", "base_price": 50},
  "Fearow": {"type": ["Normal", "Flying"], "tier": "2nd_stage", "base_price": 200},

  "Ekans": {"type": ["Poison"], "tier": "1st_stage", "base_price": 50},
  "Arbok": {"type": ["Poison"], "tier": "2nd_stage", "base_price": 200},

  "Pikachu": {"type": ["Electric"], "tier": "2nd_stage", "base_price": 200},
  "Raichu": {"type": ["Electric"], "tier": "3rd_stage", "base_price": 400},

  "Sandshrew": {"type": ["Ground"], "tier": "1st_stage", "base_price": 50},
  "Sandslash": {"type": ["Ground"], "tier": "2nd_stage", "base_price": 200},

  "Nidoran♀": {"type": ["Poison"], "tier": "1st_stage", "base_price": 50},
  "Nidorina": {"type": ["Poison"], "tier": "2nd_stage", "base_price": 200},
  "Nidoqueen": {"type": ["Poison", "Ground"], "tier": "3rd_stage", "base_price": 500},

  "Nidoran♂": {"type": ["Poison"], "tier": "1st_stage", "base_price": 50},
  "Nidorino": {"type": ["Poison"], "tier": "2nd_stage", "base_price": 200},
  "Nidoking": {"type": ["Poison", "Ground"], "tier": "3rd_stage", "base_price": 500},

  "Clefairy": {"type": ["Fairy"], "tier": "2nd_stage", "base_price": 150},
  "Clefable": {"type": ["Fairy"], "tier": "3rd_stage", "base_price": 400},

  "Vulpix": {"type": ["Fire"], "tier": "1st_stage", "base_price": 100},
  "Ninetales": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 400},

  "Jigglypuff": {"type": ["Normal", "Fairy"], "tier": "2nd_stage", "base_price": 150},
  "Wigglytuff": {"type": ["Normal", "Fairy"], "tier": "3rd_stage", "base_price": 400},

  "Zubat": {"type": ["Poison", "Flying"], "tier": "1st_stage", "base_price": 30},
  "Golbat": {"type": ["Poison", "Flying"], "tier": "2nd_stage", "base_price": 150},

  "Oddish": {"type": ["Grass", "Poison"], "tier": "1st_stage", "base_price": 50},
  "Gloom": {"type": ["Grass", "Poison"], "tier": "2nd_stage", "base_price": 200},
  "Vileplume": {"type": ["Grass", "Poison"], "tier": "3rd_stage", "base_price": 450}
  "Paras": {"type": ["Bug", "Grass"], "tier": "1st_stage", "base_price": 50},
  "Parasect": {"type": ["Bug", "Grass"], "tier": "2nd_stage", "base_price": 200},

  "Venonat": {"type": ["Bug", "Poison"], "tier": "1st_stage", "base_price": 50},
  "Venomoth": {"type": ["Bug", "Poison"], "tier": "2nd_stage", "base_price": 200},

  "Diglett": {"type": ["Ground"], "tier": "1st_stage", "base_price": 50},
  "Diglett_Alolan": {"type": ["Ground", "Steel"], "tier": "1st_stage", "base_price": 70},
  "Dugtrio": {"type": ["Ground"], "tier": "2nd_stage", "base_price": 200},
  "Dugtrio_Alolan": {"type": ["Ground", "Steel"], "tier": "2nd_stage", "base_price": 250},

  "Meowth": {"type": ["Normal"], "tier": "1st_stage", "base_price": 50},
  "Meowth_Alolan": {"type": ["Dark"], "tier": "1st_stage", "base_price": 70},
  "Meowth_Galarian": {"type": ["Steel"], "tier": "1st_stage", "base_price": 80},
  "Persian": {"type": ["Normal"], "tier": "2nd_stage", "base_price": 200},
  "Persian_Alolan": {"type": ["Dark"], "tier": "2nd_stage", "base_price": 250},

  "Psyduck": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Golduck": {"type": ["Water"], "tier": "2nd_stage", "base_price": 250},

  "Mankey": {"type": ["Fighting"], "tier": "1st_stage", "base_price": 60},
  "Primeape": {"type": ["Fighting"], "tier": "2nd_stage", "base_price": 250},

  "Growlithe": {"type": ["Fire"], "tier": "1st_stage", "base_price": 100},
  "Growlithe_Hisuian": {"type": ["Fire", "Rock"], "tier": "1st_stage", "base_price": 120},
  "Arcanine": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 400},
  "Arcanine_Hisuian": {"type": ["Fire", "Rock"], "tier": "2nd_stage", "base_price": 450},

  "Poliwag": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Poliwhirl": {"type": ["Water"], "tier": "2nd_stage", "base_price": 200},
  "Poliwrath": {"type": ["Water", "Fighting"], "tier": "3rd_stage", "base_price": 450},

  "Abra": {"type": ["Psychic"], "tier": "1st_stage", "base_price": 120},
  "Kadabra": {"type": ["Psychic"], "tier": "2nd_stage", "base_price": 300},
  "Alakazam": {"type": ["Psychic"], "tier": "3rd_stage", "base_price": 600},

  "Machop": {"type": ["Fighting"], "tier": "1st_stage", "base_price": 80},
  "Machoke": {"type": ["Fighting"], "tier": "2nd_stage", "base_price": 250},
  "Machamp": {"type": ["Fighting"], "tier": "3rd_stage", "base_price": 500},

  "Bellsprout": {"type": ["Grass", "Poison"], "tier": "1st_stage", "base_price": 50},
  "Weepinbell": {"type": ["Grass", "Poison"], "tier": "2nd_stage", "base_price": 200},
  "Victreebel": {"type": ["Grass", "Poison"], "tier": "3rd_stage", "base_price": 450},

  "Tentacool": {"type": ["Water", "Poison"], "tier": "1st_stage", "base_price": 80},
  "Tentacruel": {"type": ["Water", "Poison"], "tier": "2nd_stage", "base_price": 300},

  "Geodude": {"type": ["Rock", "Ground"], "tier": "1st_stage", "base_price": 60},
  "Geodude_Alolan": {"type": ["Rock", "Electric"], "tier": "1st_stage", "base_price": 80},
  "Graveler": {"type": ["Rock", "Ground"], "tier": "2nd_stage", "base_price": 200},
  "Graveler_Alolan": {"type": ["Rock", "Electric"], "tier": "2nd_stage", "base_price": 250},
  "Golem": {"type": ["Rock", "Ground"], "tier": "3rd_stage", "base_price": 450},
  "Golem_Alolan": {"type": ["Rock", "Electric"], "tier": "3rd_stage", "base_price": 500},

  "Ponyta": {"type": ["Fire"], "tier": "1st_stage", "base_price": 100},
  "Ponyta_Galarian": {"type": ["Psychic"], "tier": "1st_stage", "base_price": 120},
  "Rapidash": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 400},
  "Rapidash_Galarian": {"type": ["Psychic", "Fairy"], "tier": "2nd_stage", "base_price": 450},

  "Slowpoke": {"type": ["Water", "Psychic"], "tier": "1st_stage", "base_price": 100},
  "Slowpoke_Galarian": {"type": ["Psychic"], "tier": "1st_stage", "base_price": 120},
  "Slowbro": {"type": ["Water", "Psychic"], "tier": "2nd_stage", "base_price": 400},
  "Slowbro_Galarian": {"type": ["Poison", "Psychic"], "tier": "2nd_stage", "base_price": 450},

  "Magnemite": {"type": ["Electric", "Steel"], "tier": "1st_stage", "base_price": 100},
  "Magneton": {"type": ["Electric", "Steel"], "tier": "2nd_stage", "base_price": 300},

  "Farfetch'd": {"type": ["Normal", "Flying"], "tier": "1st_stage", "base_price": 120},
  "Farfetch'd_Galarian": {"type": ["Fighting"], "tier": "1st_stage", "base_price": 150},

  "Doduo": {"type": ["Normal", "Flying"], "tier": "1st_stage", "base_price": 50},
  "Dodrio": {"type": ["Normal", "Flying"], "tier": "2nd_stage", "base_price": 200},

  "Seel": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Dewgong": {"type": ["Water", "Ice"], "tier": "2nd_stage", "base_price": 300},

  "Grimer": {"type": ["Poison"], "tier": "1st_stage", "base_price": 60},
  "Grimer_Alolan": {"type": ["Poison", "Dark"], "tier": "1st_stage", "base_price": 80},
  "Muk": {"type": ["Poison"], "tier": "2nd_stage", "base_price": 300},
  "Muk_Alolan": {"type": ["Poison", "Dark"], "tier": "2nd_stage", "base_price": 350},

  "Shellder": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Cloyster": {"type": ["Water", "Ice"], "tier": "2nd_stage", "base_price": 350},

  "Gastly": {"type": ["Ghost", "Poison"], "tier": "1st_stage", "base_price": 100},
  "Haunter": {"type": ["Ghost", "Poison"], "tier": "2nd_stage", "base_price": 300},
  "Gengar": {"type": ["Ghost", "Poison"], "tier": "3rd_stage", "base_price": 600},

  "Onix": {"type": ["Rock", "Ground"], "tier": "1st_stage", "base_price": 150},

  "Drowzee": {"type": ["Psychic"], "tier": "1st_stage", "base_price": 80},
  "Hypno": {"type": ["Psychic"], "tier": "2nd_stage", "base_price": 250},

  "Krabby": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Kingler": {"type": ["Water"], "tier": "2nd_stage", "base_price": 250},

  "Voltorb": {"type": ["Electric"], "tier": "1st_stage", "base_price": 80},
  "Voltorb_Hisuian": {"type": ["Electric", "Grass"], "tier": "1st_stage", "base_price": 100},
  "Electrode": {"type": ["Electric"], "tier": "2nd_stage", "base_price": 250},
  "Electrode_Hisuian": {"type": ["Electric", "Grass"], "tier": "2nd_stage", "base_price": 300},

  "Exeggcute": {"type": ["Grass", "Psychic"], "tier": "1st_stage", "base_price": 100},
  "Exeggutor": {"type": ["Grass", "Psychic"], "tier": "2nd_stage", "base_price": 350},
  "Exeggutor_Alolan": {"type": ["Grass", "Dragon"], "tier": "2nd_stage", "base_price": 400},

  "Cubone": {"type": ["Ground"], "tier": "1st_stage", "base_price": 80},
  "Marowak": {"type": ["Ground"], "tier": "2nd_stage", "base_price": 300},
  "Marowak_Alolan": {"type": ["Fire", "Ghost"], "tier": "2nd_stage", "base_price": 350},

  "Hitmonlee": {"type": ["Fighting"], "tier": "base", "base_price": 300},
  "Hitmonchan": {"type": ["Fighting"], "tier": "base", "base_price": 300},

  "Lickitung": {"type": ["Normal"], "tier": "base", "base_price": 200},

  "Koffing": {"type": ["Poison"], "tier": "1st_stage", "base_price": 80},
  "Weezing": {"type": ["Poison"], "tier": "2nd_stage", "base_price": 300},
  "Weezing_Galarian": {"type": ["Poison", "Fairy"], "tier": "2nd_stage", "base_price": 350},

  "Rhyhorn": {"type": ["Ground", "Rock"], "tier": "1st_stage", "base_price": 100},
  "Rhydon": {"type": ["Ground", "Rock"], "tier": "2nd_stage", "base_price": 350},

  "Chansey": {"type": ["Normal"], "tier": "base", "base_price": 400},

  "Tangela": {"type": ["Grass"], "tier": "base", "base_price": 200},

  "Kangaskhan": {"type": ["Normal"], "tier": "base", "base_price": 400},

  "Horsea": {"type": ["Water"], "tier": "1st_stage", "base_price": 80},
  "Seadra": {"type": ["Water"], "tier": "2nd_stage", "base_price": 250},

  "Goldeen": {"type": ["Water"], "tier": "1st_stage", "base_price": 60},
  "Seaking": {"type": ["Water"], "tier": "2nd_stage", "base_price": 200},

  "Staryu": {"type": ["Water"], "tier": "base", "base_price": 100},
  "Starmie": {"type": ["Water", "Psychic"], "tier": "2nd_stage", "base_price": 400},

  "Mr. Mime": {"type": ["Psychic", "Fairy"], "tier": "base", "base_price": 300},
  "Mr. Mime_Galarian": {"type": ["Ice", "Psychic"], "tier": "base", "base_price": 320},

  "Scyther": {"type": ["Bug", "Flying"], "tier": "base", "base_price": 300},
  "Jynx": {"type": ["Ice", "Psychic"], "tier": "base", "base_price": 300},
  "Electabuzz": {"type": ["Electric"], "tier": "base", "base_price": 300},
  "Magmar": {"type": ["Fire"], "tier": "base", "base_price": 300},
  "Pinsir": {"type": ["Bug"], "tier": "base", "base_price": 300},

  "Tauros": {"type": ["Normal"], "tier": "base", "base_price": 300},
  "Tauros_Paldean_Combat": {"type": ["Fighting"], "tier": "base", "base_price": 320},
  "Tauros_Paldean_Blaze": {"type": ["Fighting", "Fire"], "tier": "base", "base_price": 350},
  "Tauros_Paldean_Aqua": {"type": ["Fighting", "Water"], "tier": "base", "base_price": 350},

  "Magikarp": {"type": ["Water"], "tier": "1st_stage", "base_price": 20},
  "Gyarados": {"type": ["Water", "Flying"], "tier": "2nd_stage", "base_price": 500},

  "Lapras": {"type": ["Water", "Ice"], "tier": "base", "base_price": 400},

  "Ditto": {"type": ["Normal"], "tier": "base", "base_price": 300},

  "Eevee": {"type": ["Normal"], "tier": "base", "base_price": 200},
  "Vaporeon": {"type": ["Water"], "tier": "2nd_stage", "base_price": 400},
  "Jolteon": {"type": ["Electric"], "tier": "2nd_stage", "base_price": 400},
  "Flareon": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 400},

  "Porygon": {"type": ["Normal"], "tier": "base", "base_price": 300},

  "Omanyte": {"type": ["Rock", "Water"], "tier": "1st_stage", "base_price": 120},
  "Omastar": {"type": ["Rock", "Water"], "tier": "2nd_stage", "base_price": 400},

  "Kabuto": {"type": ["Rock", "Water"], "tier": "1st_stage", "base_price": 120},
  "Kabutops": {"type": ["Rock", "Water"], "tier": "2nd_stage", "base_price": 400},

  "Aerodactyl": {"type": ["Rock", "Flying"], "tier": "base", "base_price": 500},

  "Snorlax": {"type": ["Normal"], "tier": "base", "base_price": 500},

  "Articuno": {"type": ["Ice", "Flying"], "tier": "legendary", "base_price": 1000},
  "Articuno_Galarian": {"type": ["Psychic", "Flying"], "tier": "legendary", "base_price": 1000},

  "Zapdos": {"type": ["Electric", "Flying"], "tier": "legendary", "base_price": 1000},
  "Zapdos_Galarian": {"type": ["Fighting", "Flying"], "tier": "legendary", "base_price": 1000},

  "Moltres": {"type": ["Fire", "Flying"], "tier": "legendary", "base_price": 1000},
  "Moltres_Galarian": {"type": ["Dark", "Flying"], "tier": "legendary", "base_price": 1000},

  "Dratini": {"type": ["Dragon"], "tier": "1st_stage", "base_price": 200},
  "Dragonair": {"type": ["Dragon"], "tier": "2nd_stage", "base_price": 400},
  "Dragonite": {"type": ["Dragon", "Flying"], "tier": "pseudo_legendary", "base_price": 800},

  "Mewtwo": {"type": ["Psychic"], "tier": "legendary", "base_price": 1200},

  "Mew": {"type": ["Psychic"], "tier": "mythical", "base_price": 1500},
  
  "Chikorita": {"type": ["Grass"], "tier": "starter", "base_price": 100},
  "Bayleef": {"type": ["Grass"], "tier": "2nd_stage", "base_price": 300},
  "Meganium": {"type": ["Grass"], "tier": "3rd_stage", "base_price": 600},

  "Cyndaquil": {"type": ["Fire"], "tier": "starter", "base_price": 100},
  "Quilava": {"type": ["Fire"], "tier": "2nd_stage", "base_price": 300},
  "Typhlosion": {"type": ["Fire"], "tier": "3rd_stage", "base_price": 600},
  "Typhlosion_Hisuian": {"type": ["Fire", "Ghost"], "tier": "3rd_stage", "base_price": 650},

  "Totodile": {"type": ["Water"], "tier": "starter", "base_price": 100},
  "Croconaw": {"type": ["Water"], "tier": "2nd_stage", "base_price": 300},
  "Feraligatr": {"type": ["Water"], "tier": "3rd_stage", "base_price": 600},

  "Sentret": {"type": ["Normal"], "tier": "1st_stage", "base_price": 40},
  "Furret": {"type": ["Normal"], "tier": "2nd_stage", "base_price": 180},

  "Hoothoot": {"type": ["Normal", "Flying"], "tier": "1st_stage", "base_price": 50},
  "Noctowl": {"type": ["Normal", "Flying"], "tier": "2nd_stage", "base_price": 200},

  "Ledyba": {"type": ["Bug", "Flying"], "tier": "1st_stage", "base_price": 40},
  "Ledian": {"type": ["Bug", "Flying"], "tier": "2nd_stage", "base_price": 180},

  "Spinarak": {"type": ["Bug", "Poison"], "tier": "1st_stage", "base_price": 40},
  "Ariados": {"type": ["Bug", "Poison"], "tier": "2nd_stage", "base_price": 180},

  "Crobat": {"type": ["Poison", "Flying"], "tier": "3rd_stage", "base_price": 400},

  "Chinchou": {"type": ["Water", "Electric"], "tier": "1st_stage", "base_price": 80},
  "Lanturn": {"type": ["Water", "Electric"], "tier": "2nd_stage", "base_price": 250},

  "Pichu": {"type": ["Electric"], "tier": "baby", "base_price": 80},
  "Cleffa": {"type": ["Fairy"], "tier": "baby", "base_price": 80},
  "Igglybuff": {"type": ["Normal", "Fairy"], "tier": "baby", "base_price": 80},

  "Togepi": {"type": ["Fairy"], "tier": "baby", "base_price": 100},
  "Togetic": {"type": ["Fairy", "Flying"], "tier": "2nd_stage", "base_price": 300},

  "Natu": {"type": ["Psychic", "Flying"], "tier": "1st_stage", "base_price": 80},
  "Xatu": {"type": ["Psychic", "Flying"], "tier": "2nd_stage", "base_price": 250},

  "Mareep": {"type": ["Electric"], "tier": "1st_stage", "base_price": 80},
  "Flaaffy": {"type": ["Electric"], "tier": "2nd_stage", "base_price": 250},
  "Ampharos": {"type": ["Electric"], "tier": "3rd_stage", "base_price": 500},

  "Bellossom": {"type": ["Grass"], "tier": "3rd_stage", "base_price": 450},

  "Marill": {"type": ["Water", "Fairy"], "tier": "1st_stage", "base_price": 80},
  "Azumarill": {"type": ["Water", "Fairy"], "tier": "2nd_stage", "base_price": 300},

  "Sudowoodo": {"type": ["Rock"], "tier": "base", "base_price": 200},

  "Politoed": {"type": ["Water"], "tier": "3rd_stage", "base_price": 450},

  "Hoppip": {"type": ["Grass", "Flying"], "tier": "1st_stage", "base_price": 40},
  "Skiploom": {"type": ["Grass", "Flying"], "tier": "2nd_stage", "base_price": 180},
  "Jumpluff": {"type": ["Grass", "Flying"], "tier": "3rd_stage", "base_price": 350},

  "Aipom": {"type": ["Normal"], "tier": "base", "base_price": 200},

  "Sunkern": {"type": ["Grass"], "tier": "1st_stage", "base_price": 30},
  "Sunflora": {"type": ["Grass"], "tier": "2nd_stage", "base_price": 200},

  "Yanma": {"type": ["Bug", "Flying"], "tier": "base", "base_price": 200},

  "Wooper": {"type": ["Water", "Ground"], "tier": "1st_stage", "base_price": 80},
  "Wooper_Paldean": {"type": ["Poison", "Ground"], "tier": "1st_stage", "base_price": 100},
  "Quagsire": {"type": ["Water", "Ground"], "tier": "2nd_stage", "base_price": 300},

  "Espeon": {"type": ["Psychic"], "tier": "2nd_stage", "base_price": 400},
  "Umbreon": {"type": ["Dark"], "tier": "2nd_stage", "base_price": 400},

  "Murkrow": {"type": ["Dark", "Flying"], "tier": "base", "base_price": 200},

  "Slowking": {"type": ["Water", "Psychic"], "tier": "3rd_stage", "base_price": 500},
  "Slowking_Galarian": {"type": ["Poison", "Psychic"], "tier": "3rd_stage", "base_price": 550},

  "Misdreavus": {"type": ["Ghost"], "tier": "base", "base_price": 250},

  "Unown": {"type": ["Psychic"], "tier": "base", "base_price": 150},

  "Wobbuffet": {"type": ["Psychic"], "tier": "base", "base_price": 250},

  "Girafarig": {"type": ["Normal", "Psychic"], "tier": "base", "base_price": 250},

  "Pineco": {"type": ["Bug"], "tier": "1st_stage", "base_price": 60},
  "Forretress": {"type": ["Bug", "Steel"], "tier": "2nd_stage", "base_price": 300},

  "Dunsparce": {"type": ["Normal"], "tier": "base", "base_price": 200},

  "Gligar": {"type": ["Ground", "Flying"], "tier": "base", "base_price": 250},

  "Steelix": {"type": ["Steel", "Ground"], "tier": "2nd_stage", "base_price": 500},

  "Snubbull": {"type": ["Fairy"], "tier": "1st_stage", "base_price": 80},
  "Granbull": {"type": ["Fairy"], "tier": "2nd_stage", "base_price": 250},
  "Qwilfish": {"type": ["Water", "Poison"], "tier": "base", "base_price": 200},
  "Qwilfish_Hisuian": {"type": ["Dark", "Poison"], "tier": "base", "base_price": 250},

  "Scizor": {"type": ["Bug", "Steel"], "tier": "2nd_stage", "base_price": 500},

  "Shuckle": {"type": ["Bug", "Rock"], "tier": "base", "base_price": 200},

  "Heracross": {"type": ["Bug", "Fighting"], "tier": "base", "base_price": 400},

  "Sneasel": {"type": ["Dark", "Ice"], "tier": "base", "base_price": 180},
  "Sneasel_Hisuian": {"type": ["Fighting", "Poison"], "tier": "base", "base_price": 220},

  "Teddiursa": {"type": ["Normal"], "tier": "1st_stage", "base_price": 50},
  "Ursaring": {"type": ["Normal"], "tier": "2nd_stage", "base_price": 300},

  "Slugma": {"type": ["Fire"], "tier": "1st_stage", "base_price": 60},
  "Magcargo": {"type": ["Fire", "Rock"], "tier": "2nd_stage", "base_price": 300},

  "Swinub": {"type": ["Ice", "Ground"], "tier": "1st_stage", "base_price": 50},
  "Piloswine": {"type": ["Ice", "Ground"], "tier": "2nd_stage", "base_price": 250},

  "Corsola": {"type": ["Water", "Rock"], "tier": "base", "base_price": 200},
  "Corsola_Galarian": {"type": ["Ghost"], "tier": "base", "base_price": 220},

  "Remoraid": {"type": ["Water"], "tier": "1st_stage", "base_price": 40},
  "Octillery": {"type": ["Water"], "tier": "2nd_stage", "base_price": 200},

  "Delibird": {"type": ["Ice", "Flying"], "tier": "base", "base_price": 180},
  "Mantine": {"type": ["Water", "Flying"], "tier": "base", "base_price": 300},
  "Skarmory": {"type": ["Steel", "Flying"], "tier": "base", "base_price": 400},

  "Houndour": {"type": ["Dark", "Fire"], "tier": "1st_stage", "base_price": 80},
  "Houndoom": {"type": ["Dark", "Fire"], "tier": "2nd_stage", "base_price": 400},

  "Kingdra": {"type": ["Water", "Dragon"], "tier": "2nd_stage", "base_price": 600},

  "Phanpy": {"type": ["Ground"], "tier": "1st_stage", "base_price": 60},
  "Donphan": {"type": ["Ground"], "tier": "2nd_stage", "base_price": 400},

  "Porygon2": {"type": ["Normal"], "tier": "2nd_stage", "base_price": 400},
  "Stantler": {"type": ["Normal"], "tier": "base", "base_price": 200},
  "Smeargle": {"type": ["Normal"], "tier": "base", "base_price": 250},

  "Tyrogue": {"type": ["Fighting"], "tier": "baby", "base_price": 80},
  "Hitmontop": {"type": ["Fighting"], "tier": "2nd_stage", "base_price": 350},

  "Smoochum": {"type": ["Ice", "Psychic"], "tier": "baby", "base_price": 90},
  "Elekid": {"type": ["Electric"], "tier": "baby", "base_price": 90},
  "Magby": {"type": ["Fire"], "tier": "baby", "base_price": 90},

  "Miltank": {"type": ["Normal"], "tier": "base", "base_price": 350},
  "Blissey": {"type": ["Normal"], "tier": "3rd_stage", "base_price": 600},

  "Raikou": {"type": ["Electric"], "tier": "legendary", "base_price": 1000},
  "Entei": {"type": ["Fire"], "tier": "legendary", "base_price": 1000},
  "Suicune": {"type": ["Water"], "tier": "legendary", "base_price": 1000},

  "Larvitar": {"type": ["Rock", "Ground"], "tier": "1st_stage", "base_price": 100},
  "Pupitar": {"type": ["Rock", "Ground"], "tier": "2nd_stage", "base_price": 400},
  "Tyranitar": {"type": ["Rock", "Dark"], "tier": "3rd_stage", "base_price": 800},

  "Lugia": {"type": ["Psychic", "Flying"], "tier": "legendary", "base_price": 1200},
  "Ho-Oh": {"type": ["Fire", "Flying"], "tier": "legendary", "base_price": 1200},

  "Celebi": {"type": ["Psychic", "Grass"], "tier": "mythical", "base_price": 1500}
}
