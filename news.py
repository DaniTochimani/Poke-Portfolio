import random

# ---------- News Event Pool ----------
# Each entry:
#   headline       : paragraph shown to the player — written to imply direction, no numbers
#   target         : {"kind": "type"|"tier"|"name"|"all", "value": ...}
#   effect_range   : (min_multiplier, max_multiplier) — rolled ONCE when the event activates
#   duration_range : (min_days, max_days)             — rolled ONCE when the event activates
#   weight         : relative likelihood of selection (positive ≈ negative ≈ 3, mild-neg ≈ 4, crash ≈ 0.5)

NEWS_POOL = [

    # ===== FIRE TYPE =====
    {
        "headline": (
            "The annual Cinnabar Island Fire Trainer Tournament has drawn its largest crowd yet, "
            "with thousands of spectators traveling from across Kanto. Demand for Fire-type Pokémon "
            "has spiked dramatically in the weeks leading up to the event, as aspiring competitors "
            "scramble to assemble competitive rosters. Vendors report inventory running low as collectors "
            "and trainers alike compete for the same pool of available Pokémon."
        ),
        "target": {"kind": "type", "value": "Fire"},
        "effect_range": (1.12, 1.28),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Seismic activity near Mt. Ember has driven large numbers of Fire-type Pokémon out of "
            "their cave habitats and into surrounding routes. Trainers report encountering Fire-types "
            "at rates far above seasonal norms, and several breeding sanctuaries have noted an unusual "
            "intake of displaced individuals. Market analysts expect the increased availability to "
            "push valuations down in the short term."
        ),
        "target": {"kind": "type", "value": "Fire"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== WATER TYPE =====
    {
        "headline": (
            "Cerulean City has announced the return of its biennial Sailing and Water Pokémon Festival, "
            "drawing thousands of enthusiasts from across the region. Historically, the event has "
            "correlated with a sharp uptick in Water-type Pokémon acquisitions, as trainers look to "
            "participate in the festival's exhibition battles. Pre-festival demand already appears to "
            "be building, with traders noting increased buy-side activity."
        ),
        "target": {"kind": "type", "value": "Water"},
        "effect_range": (1.08, 1.22),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "Weeks of unseasonable rainfall have caused widespread flooding across multiple water routes, "
            "pushing Water-type Pokémon out of their natural habitats in enormous numbers. Trainers are "
            "reporting Water-types appearing in areas where they have never been seen before. The sudden "
            "surplus has already begun to weigh on prices, with sellers struggling to find buyers at "
            "previous valuations."
        ),
        "target": {"kind": "type", "value": "Water"},
        "effect_range": (0.82, 0.93),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== ELECTRIC TYPE =====
    {
        "headline": (
            "A series of unexplained failures across Kanto's power grid has prompted regional authorities "
            "to explore alternative energy sources. Several municipalities have begun contracting with "
            "Electric-type Pokémon trainers to supplement conventional power generation. The government "
            "contracts have driven significant institutional demand, with multiple large buyers entering "
            "the market simultaneously."
        ),
        "target": {"kind": "type", "value": "Electric"},
        "effect_range": (1.10, 1.25),
        "duration_range": (3, 5),
        "weight": 3,
    },
    {
        "headline": (
            "New urban safety ordinances passed in Vermilion City and Saffron City will significantly "
            "restrict the ownership and use of Electric-type Pokémon within city limits, citing a rise "
            "in accidental discharge incidents. Legal experts expect the regulations to spread to other "
            "municipalities. Collectors are already reporting difficulty reselling Electric-types to "
            "urban buyers, dampening demand across the board."
        ),
        "target": {"kind": "type", "value": "Electric"},
        "effect_range": (0.78, 0.90),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== PSYCHIC TYPE =====
    {
        "headline": (
            "The Saffron City Institute for Advanced Pokémon Research has published a landmark study "
            "on the cognitive capabilities of Psychic-type Pokémon, suggesting their potential "
            "applications in fields ranging from medicine to urban planning are vastly underexplored. "
            "The paper has generated significant interest from academic institutions and private "
            "collectors alike, with early trading sessions showing strong buy-side momentum."
        ),
        "target": {"kind": "type", "value": "Psychic"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A series of highly publicized failures by Psychic-type Pokémon in major tournament "
            "prediction events has shaken public confidence in the tier. Several prominent trainers "
            "have publicly moved away from Psychic-types in their competitive rosters, and social "
            "sentiment trackers show a sharp decline in positive mentions. Analysts are advising "
            "caution for holders of Psychic-type positions."
        ),
        "target": {"kind": "type", "value": "Psychic"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== DRAGON TYPE =====
    {
        "headline": (
            "Following a series of disturbances near Dragon's Den in Blackthorn City, Dragon-type "
            "Pokémon have retreated to deeper, more inaccessible areas of their habitat. Field "
            "researchers confirm that encounter rates have dropped to historic lows, with experienced "
            "trainers reporting weeks of fruitless searching. The sudden scarcity has already begun "
            "driving prices upward among serious collectors."
        ),
        "target": {"kind": "type", "value": "Dragon"},
        "effect_range": (1.15, 1.35),
        "duration_range": (2, 5),
        "weight": 3,
    },
    {
        "headline": (
            "The International Pokémon Battle Commission has issued sweeping restrictions on Dragon-type "
            "Pokémon usage in sanctioned competitive play, citing balance concerns after a dominant "
            "tournament season. The ruling is expected to significantly reduce demand from competitive "
            "trainers, who represent a major segment of the Dragon-type buyer market. Several dealers "
            "have already begun marking down inventory in anticipation."
        ),
        "target": {"kind": "type", "value": "Dragon"},
        "effect_range": (0.78, 0.88),
        "duration_range": (3, 5),
        "weight": 3,
    },

    # ===== GRASS TYPE =====
    {
        "headline": (
            "A consortium of herbal medicine researchers in Celadon City has announced a multi-year "
            "study into the medicinal properties of plants cultivated by Grass-type Pokémon. "
            "The project has attracted substantial funding, and participating researchers are actively "
            "acquiring Grass-types for controlled study environments. Demand from the academic sector "
            "has been particularly strong over the past week."
        ),
        "target": {"kind": "type", "value": "Grass"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Unusually warm and wet spring conditions have triggered a mass seasonal bloom across "
            "Kanto's forest routes, with Grass-type Pokémon reproducing at rates well above historical "
            "averages. Rangers are reporting overcrowding in several protected areas, and a number of "
            "breeding sanctuaries have begun offloading surplus individuals onto the open market. "
            "Prices are expected to soften through the season."
        ),
        "target": {"kind": "type", "value": "Grass"},
        "effect_range": (0.83, 0.93),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== GHOST TYPE =====
    {
        "headline": (
            "A surge in paranormal tourism following a widely-shared documentary on Lavender Town's "
            "history has driven unprecedented interest in Ghost-type Pokémon. Tour operators report "
            "fully booked expeditions weeks in advance, and souvenir traders note that Ghost-type "
            "Pokémon are among the most requested items by visiting collectors. The trend shows no "
            "sign of slowing, with a follow-up documentary already confirmed to be in production."
        ),
        "target": {"kind": "type", "value": "Ghost"},
        "effect_range": (1.10, 1.25),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A series of reports linking Ghost-type Pokémon habitation to declining property values "
            "in residential neighborhoods has prompted several local governments to consider relocation "
            "programs. The negative press has dampened enthusiasm among casual collectors, and several "
            "prominent traders report increased difficulty moving Ghost-type inventory at previously "
            "standard prices."
        ),
        "target": {"kind": "type", "value": "Ghost"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== FIGHTING TYPE =====
    {
        "headline": (
            "The Saffron City Fighting Dojo has announced the return of its legendary open invitational "
            "tournament, drawing competitors from every corner of Kanto. Pre-registration numbers have "
            "broken records, and demand for Fighting-type Pokémon has climbed steadily as participants "
            "look to strengthen their rosters. Seasoned traders are recommending positions ahead of "
            "the event, which historically correlates with sustained price increases."
        ),
        "target": {"kind": "type", "value": "Fighting"},
        "effect_range": (1.08, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Several major cities, including Celadon and Saffron, have passed ordinances restricting "
            "the training and public use of Fighting-type Pokémon following a string of incidents near "
            "urban gyms. Legal experts anticipate the restrictions spreading to Vermilion and Pewter. "
            "The regulatory headwind has visibly dampened buyer interest, with market activity for "
            "Fighting-types falling sharply over the past several sessions."
        ),
        "target": {"kind": "type", "value": "Fighting"},
        "effect_range": (0.80, 0.90),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ICE TYPE =====
    {
        "headline": (
            "An unexpected summer heat wave sweeping across the Seafoam Islands has forced Ice-type "
            "Pokémon to migrate to much deeper, colder cave systems where temperatures remain survivable. "
            "Field researchers report near-zero encounter rates in previously reliable habitats, and "
            "several traders who typically source directly from the islands have halted operations "
            "entirely. Supply disruptions are expected to persist until temperatures normalize."
        ),
        "target": {"kind": "type", "value": "Ice"},
        "effect_range": (1.12, 1.30),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A cold snap of unusual severity has pushed Ice-type Pokémon out of mountain habitats and "
            "into lower-altitude routes in large numbers. Trainers in the northern routes report "
            "Ice-type encounter rates several times above seasonal norms, and several large batches of "
            "recently caught individuals have entered the market simultaneously, pushing prices "
            "noticeably lower."
        ),
        "target": {"kind": "type", "value": "Ice"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== DARK TYPE =====
    {
        "headline": (
            "Following the recent closure of several key mountain passes due to rockslides, Dark-type "
            "Pokémon habitats have become increasingly difficult for trainers to access. Expedition "
            "leaders report turning back empty-handed after days of searching, and several established "
            "supply chains for Dark-types have been disrupted indefinitely. Scarcity is beginning "
            "to reflect in asking prices across major trading hubs."
        ),
        "target": {"kind": "type", "value": "Dark"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Authorities have confirmed a crackdown on illegal Dark-type Pokémon trafficking rings "
            "operating out of Mahogany Town, resulting in the seizure and subsequent market release "
            "of a large number of confiscated individuals. The influx of inventory has arrived at "
            "an inopportune time, as buyer appetite for Dark-types was already showing signs of "
            "fatigue following a slow tournament season."
        ),
        "target": {"kind": "type", "value": "Dark"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== POISON TYPE =====
    {
        "headline": (
            "Pharmaceutical researchers at the Fuchsia City Institute have announced promising early "
            "results from trials using Poison-type Pokémon venom compounds as the basis for a new "
            "class of antitoxins. The announcement has attracted venture funding and drawn institutional "
            "buyers into the market who had previously shown little interest in the type. Prices at "
            "several major trading hubs have moved meaningfully higher on the news."
        ),
        "target": {"kind": "type", "value": "Poison"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A public health advisory issued by Kanto's Ministry of Safety has warned against keeping "
            "Poison-type Pokémon in residential areas without specialized containment equipment, "
            "following a spike in accidental exposure incidents in Celadon. The advisory has prompted "
            "a wave of voluntary surrenders to shelters, which are now struggling to absorb the sudden "
            "increase in available Poison-type Pokémon."
        ),
        "target": {"kind": "type", "value": "Poison"},
        "effect_range": (0.80, 0.90),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== LEGENDARY TIER =====
    {
        "headline": (
            "Multiple credible sightings of what researchers believe to be a legendary Pokémon have "
            "been reported near the northern coast of Kanto. Photographs circulating among collector "
            "communities, while unverified, have sent enthusiasm to fever pitch. Auction houses are "
            "reporting a dramatic spike in inquiries for legendary-tier Pokémon, and several high-value "
            "trades have already been completed at prices well above recent norms."
        ),
        "target": {"kind": "tier", "value": "legendary"},
        "effect_range": (1.20, 1.45),
        "duration_range": (1, 3),
        "weight": 3,
    },
    {
        "headline": (
            "Kanto's legislature has passed the Legendary Pokémon Conservation Act, placing strict "
            "limits on the private trading and ownership of legendary-tier Pokémon pending a full "
            "ecological review. Legal experts warn that existing holders may face compliance costs, "
            "and several institutional buyers have paused acquisition activity until the regulatory "
            "picture becomes clearer. Market liquidity for legendaries has thinned considerably."
        ),
        "target": {"kind": "tier", "value": "legendary"},
        "effect_range": (0.72, 0.85),
        "duration_range": (3, 5),
        "weight": 2,
    },

    # ===== STARTER TIER =====
    {
        "headline": (
            "Kanto's Department of Education has announced a major expansion of its new trainer "
            "enrollment program, with the incoming class expected to be the largest in regional history. "
            "Professor Oak's office has confirmed that starter Pokémon distributions will begin shortly, "
            "and secondary demand from trainers supplementing their rosters has already begun to lift "
            "prices for starter-tier Pokémon across the board."
        ),
        "target": {"kind": "tier", "value": "starter"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "Professor Oak's laboratory has completed a years-long captive breeding initiative and "
            "announced the release of a large number of starter Pokémon into the open market at "
            "subsidized prices, citing a desire to lower barriers to entry for new trainers. The "
            "program has flooded the market with supply, and independent dealers are struggling "
            "to compete with the institutional pricing."
        ),
        "target": {"kind": "tier", "value": "starter"},
        "effect_range": (0.80, 0.90),
        "duration_range": (2, 3),
        "weight": 3,
    },

    # ===== PSEUDO-LEGENDARY TIER =====
    {
        "headline": (
            "A sweeping update to the competitive battle meta has elevated pseudo-legendary Pokémon "
            "to the top of most tier lists, with analysts crediting their stat profiles as uniquely "
            "well-suited to the current format. Tournament registrations show a marked shift toward "
            "pseudo-legendary-heavy rosters, and dealer buy-side pressure has intensified as "
            "competitors race to assemble competitive teams."
        ),
        "target": {"kind": "tier", "value": "pseudo_legendary"},
        "effect_range": (1.12, 1.28),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A string of high-profile upsets at last weekend's regional championships, in which "
            "pseudo-legendary Pokémon performed well below expectations, has triggered a reassessment "
            "among competitive trainers. Several prominent coaches have publicly announced roster "
            "overhauls moving away from the tier, and resale demand has softened noticeably in "
            "the days since the tournament concluded."
        ),
        "target": {"kind": "tier", "value": "pseudo_legendary"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: MAGIKARP =====
    {
        "headline": (
            "In what commentators are calling the upset of the decade, a Magikarp entered by a "
            "rookie trainer managed to outlast a full field of far more powerful opponents at the "
            "Cerulean City invitational, eventually evolving mid-match in a moment that has since "
            "gone viral across every major Pokémon forum. The 'underdog arc' narrative has driven "
            "a surprising surge in Magikarp acquisitions among collectors looking to replicate the story."
        ),
        "target": {"kind": "name", "value": "Magikarp"},
        "effect_range": (1.15, 1.35),
        "duration_range": (1, 2),
        "weight": 3,
    },
    {
        "headline": (
            "Fishing guilds across Kanto are reporting historic Magikarp catches this season, with "
            "several rivers and lakes yielding numbers that have overwhelmed local processing and "
            "holding facilities. The abundance has pushed the open-market price for Magikarp to "
            "multi-year lows, and several dealers have suspended new purchases entirely until "
            "existing inventory can be moved."
        ),
        "target": {"kind": "name", "value": "Magikarp"},
        "effect_range": (0.65, 0.80),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== SPECIFIC: EEVEE =====
    {
        "headline": (
            "Researchers at the Pokémon Evolution Institute have published a paper describing a "
            "previously unknown evolutionary pathway for Eevee, suggesting the species' genetic "
            "plasticity may be even broader than previously understood. The announcement has reignited "
            "collector interest in Eevee at a level not seen in years, with buyers citing both "
            "intrinsic research value and the potential for further discoveries down the line."
        ),
        "target": {"kind": "name", "value": "Eevee"},
        "effect_range": (1.18, 1.38),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "An ambitious Eevee breeding cooperative operating out of Celadon City has announced "
            "the successful completion of its expansion program, dramatically increasing the number "
            "of Eevee available on the open market. The cooperative's stated mission is to make "
            "Eevee accessible to all trainers, and their bulk pricing has already begun undercutting "
            "individual sellers across major trading hubs."
        ),
        "target": {"kind": "name", "value": "Eevee"},
        "effect_range": (0.75, 0.88),
        "duration_range": (2, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: SNORLAX =====
    {
        "headline": (
            "Sleep researchers at Saffron University have partnered with Snorlax trainers for a "
            "landmark study on restorative hibernation patterns, attracting substantial grant funding "
            "from both academic and private sources. The project requires a significant number of "
            "Snorlax subjects, and institutional acquisition has driven a notable uptick in "
            "market demand over the past week."
        ),
        "target": {"kind": "name", "value": "Snorlax"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Transportation authorities have reported at least a dozen Snorlax blocking major trade "
            "routes across Kanto this week, causing significant logistical disruptions and drawing "
            "unflattering media coverage. The incidents have generated a wave of negative public "
            "sentiment toward Snorlax owners, and several traders report that buyer enthusiasm "
            "has cooled sharply in response to the ongoing coverage."
        ),
        "target": {"kind": "name", "value": "Snorlax"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== SPECIFIC: GYARADOS =====
    {
        "headline": (
            "An unprecedented Gyarados sighting in the waters just off Cinnabar Island drew enormous "
            "crowds of spectators over the weekend, reigniting collector obsession with the species. "
            "Video footage of the encounter has spread rapidly across trainer networks, and several "
            "major dealers report fielding more inquiries about Gyarados in the past 48 hours than "
            "in the previous month combined."
        ),
        "target": {"kind": "name", "value": "Gyarados"},
        "effect_range": (1.12, 1.30),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: DITTO =====
    {
        "headline": (
            "A widespread counterfeiting scandal has emerged involving Ditto being sold as rare "
            "Pokémon, with several prominent traders under investigation for deliberate misrepresentation. "
            "The revelations have severely damaged buyer confidence in Ditto as a legitimate asset, "
            "and the resulting reputational fallout has pushed prices sharply lower even among "
            "sellers with no connection to the alleged misconduct."
        ),
        "target": {"kind": "name", "value": "Ditto"},
        "effect_range": (0.60, 0.78),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ALL MARKET — POSITIVE =====
    {
        "headline": (
            "The biennial Kanto Pokémon Trading Expo has broken all previous attendance records, "
            "with collectors, dealers, and institutional buyers converging on Celadon City from "
            "across the region. Trading volumes in the days surrounding the event historically reach "
            "annual highs, and early floor reports suggest this year is no exception. Sentiment "
            "across all tiers and types appears broadly positive heading into the main sessions."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (1.05, 1.15),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "The Kanto Regional Economic Council has released its quarterly outlook, projecting "
            "above-trend growth for the coming season driven by strong consumer spending and "
            "rising trainer enrollment. Economists expect disposable income for Pokémon-related "
            "purchases to climb across all demographic segments. The report has lifted broad "
            "market sentiment, with buyers returning to categories that had seen recent softness."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (1.05, 1.12),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ALL MARKET — MILD NEGATIVE =====
    {
        "headline": (
            "The Kanto Currency Exchange has reported a modest weakening of the PokéDollar against "
            "several regional currencies, attributed to softer-than-expected trade data for the "
            "quarter. Analysts describe the movement as within normal ranges, but the report has "
            "introduced a note of caution into market sessions, with some buyers pulling back "
            "pending clearer economic signals in the coming weeks."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.90, 0.97),
        "duration_range": (1, 2),
        "weight": 4,
    },
    {
        "headline": (
            "Newly proposed trading regulations under review by the Pokémon Commerce Authority "
            "would introduce additional documentation and compliance requirements for all Pokémon "
            "transactions above a certain value threshold. While the rules have not yet been "
            "finalized, the uncertainty has prompted some market participants to reduce activity "
            "until the regulatory picture becomes clearer."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.88, 0.95),
        "duration_range": (2, 4),
        "weight": 4,
    },

    # ===== ALL MARKET — CRASH =====
    {
        "headline": (
            "Authorities have confirmed an ongoing investigation into a coordinated price manipulation "
            "scheme allegedly involving several of Kanto's largest Pokémon trading houses. The probe, "
            "which sources describe as the most serious in the market's history, has triggered a wave "
            "of panic selling across all tiers and types as participants rush to reduce exposure. "
            "Several major dealers have temporarily suspended operations pending legal review, and "
            "no clear floor has yet been established."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.55, 0.72),
        "duration_range": (1, 3),
        "weight": 0.5,
    },
    {
        "headline": (
            "A sudden and severe economic contraction in the greater Kanto region, triggered by the "
            "collapse of a major financial institution with deep ties to the Pokémon trading sector, "
            "has sent shockwaves through all asset classes. Consumer confidence has fallen to its "
            "lowest recorded level, and discretionary spending on Pokémon has dropped precipitously. "
            "Market participants describe conditions as the worst in recent memory."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.55, 0.70),
        "duration_range": (2, 4),
        "weight": 0.5,
    },
]

# ---------- Active News State ----------
active_news = []  # List of live events: {headline, target, multiplier, days_left}


def generate_new_events(n=2):
    """
    Selects n distinct headlines from NEWS_POOL (weighted) and adds them to active_news.
    Each event's multiplier and duration are rolled once at activation and locked in.
    Already-active headlines are excluded from selection.
    """
    active_headlines = {e["headline"] for e in active_news}
    pool = [h for h in NEWS_POOL if h["headline"] not in active_headlines]
    if not pool:
        return

    weights = [h["weight"] for h in pool]
    n = min(n, len(pool))

    # random.choices can return duplicates; deduplicate while preserving weighted selection
    seen = set()
    selected = []
    for event in random.choices(pool, weights=weights, k=n * 3):
        if event["headline"] not in seen:
            seen.add(event["headline"])
            selected.append(event)
        if len(selected) == n:
            break

    for event in selected:
        active_news.append({
            "headline": event["headline"],
            "target": event["target"],
            "multiplier": round(random.uniform(*event["effect_range"]), 4),
            "days_left": random.randint(*event["duration_range"]),
        })


def advance_news():
    """
    Ages all active events by one day and removes expired ones.
    Returns a list of headlines that expired this tick (caller can display them as 'story over').
    """
    global active_news
    for event in active_news:
        event["days_left"] -= 1

    expired = [e["headline"] for e in active_news if e["days_left"] <= 0]
    active_news = [e for e in active_news if e["days_left"] > 0]
    return expired


def apply_news_to_market(market_inventory):
    """
    Applies all active news multipliers to matching Pokémon in market_inventory in-place.
    Multiple active events stack multiplicatively.
    """
    for event in active_news:
        kind = event["target"]["kind"]
        value = event["target"]["value"]
        mult = event["multiplier"]

        for pokemon in market_inventory:
            if kind == "all":
                pokemon["price"] = max(1, int(pokemon["price"] * mult))
            elif kind == "type" and value in pokemon["type"]:
                pokemon["price"] = max(1, int(pokemon["price"] * mult))
            elif kind == "tier" and pokemon["tier"] == value:
                pokemon["price"] = max(1, int(pokemon["price"] * mult))
            elif kind == "name" and pokemon["name"] == value:
                pokemon["price"] = max(1, int(pokemon["price"] * mult))


def display_news():
    """
    Prints all currently active news as paragraphs.
    Shows days remaining; multipliers are never revealed to the player.
    """
    if not active_news:
        print("\n[No current news.]")
        return

    print("\n===== TODAY'S POKEMON MARKET NEWS =====")
    for i, event in enumerate(active_news, 1):
        tag = "BREAKING" if event["days_left"] == 1 else f"ONGOING ({event['days_left']} days)"
        print(f"\n[{i}] {tag}")
        print(event["headline"])
    print("\n========================================")
