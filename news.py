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
            "The Kanto Geological Survey has issued an indefinite restricted-access order for Mt. Ember's "
            "upper cave systems, citing new assessments of lava flow instability in the summit passages. "
            "All permitted trainer expeditions have been suspended, and the three Ranger outposts "
            "operating within the restricted zone have been withdrawn to staging areas outside the perimeter. "
            "No timeline for review has been disclosed."
        ),
        "target": {"kind": "type", "value": "Fire"},
        "effect_range": (1.12, 1.28),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Kanto's Geological Survey published its quarterly activity report for Mt. Ember today, "
            "noting that seismic indicators have fallen to their lowest recorded levels since monitoring "
            "began. Rangers report that several cave passages restricted for years due to lava flow risk "
            "are being evaluated for reopening under a phased safety review, with the first sites expected "
            "to receive clearance within weeks."
        ),
        "target": {"kind": "type", "value": "Fire"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== WATER TYPE =====
    {
        "headline": (
            "The Kanto Waterway Authority has announced the closure of three major freshwater access "
            "corridors — Routes 20, 21, and the eastern inlet at Cerulean Cape — for an extended "
            "ecological assessment. No timeline for reopening has been provided, and interim access "
            "permits will not be issued during the review period. Trainers are advised to consult "
            "the Authority's public notice board for updates."
        ),
        "target": {"kind": "type", "value": "Water"},
        "effect_range": (1.08, 1.22),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "Meteorological services have issued a multi-day advisory for Kanto's central river basin "
            "following sustained above-average rainfall over the past two weeks. Water route monitoring "
            "stations are recording elevated gauge readings across all major checkpoints, and the Kanto "
            "Waterway Authority has deployed additional Ranger teams to document changing conditions "
            "along affected routes."
        ),
        "target": {"kind": "type", "value": "Water"},
        "effect_range": (0.82, 0.93),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== ELECTRIC TYPE =====
    {
        "headline": (
            "The Kanto Power Authority issued a statement this morning confirming that two of its largest "
            "eastern substation contracts — which together serve approximately 40% of the region's "
            "industrial load — will not be renewed when they expire next quarter. The statement cited "
            "'evolving infrastructure strategy' without elaboration and directed press inquiries to a "
            "conference scheduled later in the month."
        ),
        "target": {"kind": "type", "value": "Electric"},
        "effect_range": (1.10, 1.25),
        "duration_range": (3, 5),
        "weight": 3,
    },
    {
        "headline": (
            "The Vermilion City Council voted 5-4 this morning to advance a proposed ordinance to its "
            "second reading. The ordinance would amend the city's existing Pokémon ownership code to "
            "add Electric-type Pokémon to the list of species subject to 'high-impact classification' "
            "requirements, which include mandatory training certification, liability insurance bonding, "
            "and indoor containment standards."
        ),
        "target": {"kind": "type", "value": "Electric"},
        "effect_range": (0.78, 0.90),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== PSYCHIC TYPE =====
    {
        "headline": (
            "The Saffron City Institute for Advanced Research published its annual project registry "
            "this morning. Among items listed, the institute has opened fourteen new research positions "
            "under its cognitive and behavioral sciences division — a division that has not conducted "
            "active recruitment in five years. Application materials are available through the institute's "
            "academic affairs office."
        ),
        "target": {"kind": "type", "value": "Psychic"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "The Pokémon Battle Analytics Consortium has released its quarterly performance report "
            "covering the past three months of sanctioned competitive play. Data tables within the "
            "report show that the twelve most-used Psychic-type Pokémon recorded a combined win rate "
            "of 41.3% across all bracket tiers, compared to 58.7% during the same period last quarter."
        ),
        "target": {"kind": "type", "value": "Psychic"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== DRAGON TYPE =====
    {
        "headline": (
            "The Blackthorn City Conservation Alliance has submitted a formal petition to Kanto's "
            "Pokémon Management Authority requesting that Dragon's Den be reclassified under the "
            "Protected Ecological Zone framework. The petition, supported by over 3,000 signatures, "
            "requests a temporary access moratorium pending a full ecological survey. The Authority "
            "has confirmed receipt and indicated a response is expected within 60 days."
        ),
        "target": {"kind": "type", "value": "Dragon"},
        "effect_range": (1.15, 1.35),
        "duration_range": (2, 5),
        "weight": 3,
    },
    {
        "headline": (
            "The International Pokémon Battle Commission has released its updated seasonal ruleset, "
            "effective at the start of next month. Among the modifications are revisions to damage "
            "calculation multipliers for several interaction categories and updated criteria governing "
            "the 'restricted species' classification list. The full ruleset document is available on "
            "the Commission's official publication archive."
        ),
        "target": {"kind": "type", "value": "Dragon"},
        "effect_range": (0.78, 0.88),
        "duration_range": (3, 5),
        "weight": 3,
    },

    # ===== GRASS TYPE =====
    {
        "headline": (
            "The Celadon City University Department of Natural Sciences has received approval for a "
            "seven-year research initiative funded by a joint grant from three private foundations. "
            "The project, described in the grant application as focused on 'applied botanical "
            "pharmacology using native Kanto flora and associated Pokémon species,' will begin "
            "enrollment of research subjects next quarter."
        ),
        "target": {"kind": "type", "value": "Grass"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Kanto's Forest Service annual ecosystem census, published this morning, documents "
            "Grass-type Pokémon population densities across all major forested routes and protected "
            "areas. The report notes that seven survey zones have recorded population figures at or "
            "above the 'ecological carrying capacity' threshold, automatically triggering review "
            "under the Pokémon Density Management Protocol."
        ),
        "target": {"kind": "type", "value": "Grass"},
        "effect_range": (0.83, 0.93),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== GHOST TYPE =====
    {
        "headline": (
            "The Lavender Town Cultural Heritage Bureau has approved a heritage preservation designation "
            "for the 14-block area surrounding Pokémon Tower. Under the new designation, non-resident "
            "access requires a permit issued by the Cultural Heritage Committee, and commercial Pokémon "
            "activities within the zone are subject to a mandatory review process. The designation "
            "takes effect at the start of next month."
        ),
        "target": {"kind": "type", "value": "Ghost"},
        "effect_range": (1.10, 1.25),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Lavender Town's city council has voted to proceed with the Pokémon Tower Heritage "
            "Relocation Project, which would move the tower's preserved remains to a newly constructed "
            "cultural site on the city's eastern outskirts as part of an urban revitalization initiative. "
            "Site preparation is expected to begin within the current fiscal year."
        ),
        "target": {"kind": "type", "value": "Ghost"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== FIGHTING TYPE =====
    {
        "headline": (
            "The Kanto Amateur Athletics Association has announced a major restructuring of its junior "
            "and adult competitive battling programs, adding 18 new regional divisions and increasing "
            "the maximum team roster from four to six Pokémon per competitor. Registration for the "
            "expanded fall season opens next week, and organizers report that early inquiries have "
            "already surpassed last year's total registration figures."
        ),
        "target": {"kind": "type", "value": "Fighting"},
        "effect_range": (1.08, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A coalition of Pokémon training facility operators in Celadon City has filed a consolidated "
            "liability claim following a series of incidents at urban battling venues over the past "
            "quarter. Three of the affected facilities have suspended full-contact battle formats "
            "pending resolution of the claims, with no estimated date for resuming normal operations."
        ),
        "target": {"kind": "type", "value": "Fighting"},
        "effect_range": (0.80, 0.90),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ICE TYPE =====
    {
        "headline": (
            "The Seafoam Islands Natural Preserve Authority has announced the suspension of all "
            "commercial and recreational expedition permits, citing safety concerns identified in "
            "an independent audit of visitor management practices. Permit renewals have been halted "
            "and existing operators have been notified that their licenses are under administrative "
            "review. No timeline for resolution has been provided."
        ),
        "target": {"kind": "type", "value": "Ice"},
        "effect_range": (1.12, 1.30),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "A cold pressure system has remained stationary over Kanto's interior for the past eight "
            "days, producing temperatures well below seasonal averages across northern routes. Ranger "
            "stations from Pewter to Mahogany have submitted unusually high incident report volumes "
            "this week, and the Kanto Wildlife Service has activated monitoring protocols for several "
            "mountain-dwelling species."
        ),
        "target": {"kind": "type", "value": "Ice"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== DARK TYPE =====
    {
        "headline": (
            "The Kanto Interior Roads Authority has announced the immediate closure of Route 42 and "
            "the Mahogany Town eastern access trail due to emergency rockslide remediation work. "
            "Structural engineers have not provided an estimated reopening date. Commercial operators "
            "and trainers are advised to use alternate routes, which add several hours to the "
            "standard transit time."
        ),
        "target": {"kind": "type", "value": "Dark"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "The Mahogany Town Office of Public Safety has released a brief statement confirming "
            "the conclusion of an 'interdiction operation' that began several weeks ago. The statement "
            "notes that seized property has been 'processed and distributed through authorized channels' "
            "and that individuals identified during the operation have been referred to the Kanto "
            "Trainer Ethics Board."
        ),
        "target": {"kind": "type", "value": "Dark"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== POISON TYPE =====
    {
        "headline": (
            "The Fuchsia City Research Institute has logged seventeen new patent applications with the "
            "Kanto Intellectual Property Registry over the past quarter, all listed under the "
            "biochemical compound classification. A note accompanying several of the filings indicates "
            "that the applications are associated with active clinical trial protocols currently "
            "underway at the institute."
        ),
        "target": {"kind": "type", "value": "Poison"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "The Kanto Ministry of Housing has finalized an update to the standard residential tenancy "
            "addendum. Effective for all new leases executed after the start of next month, the addendum "
            "includes a clause requiring tenants to disclose ownership of any Pokémon listed on the "
            "Ministry's environmental hazard species registry and to provide documentation of compliant "
            "containment measures."
        ),
        "target": {"kind": "type", "value": "Poison"},
        "effect_range": (0.80, 0.90),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== LEGENDARY TIER =====
    {
        "headline": (
            "A commercial fishing vessel operating in the northern waters filed an equipment malfunction "
            "report with the Kanto Maritime Authority on Tuesday, citing unexplained interference "
            "with navigation and sonar systems that lasted approximately five hours. The vessel's "
            "captain noted in the report that two other ships operating in the same area had filed "
            "similar reports within the past month."
        ),
        "target": {"kind": "tier", "value": "legendary"},
        "effect_range": (1.20, 1.45),
        "duration_range": (1, 3),
        "weight": 3,
    },
    {
        "headline": (
            "The Kanto National Assembly's Joint Committee on Commerce and Wildlife has published the "
            "agenda for its next scheduled hearings, which include a session titled 'Private Ownership "
            "and Ecological Stewardship of Rare and High-Tier Pokémon.' Fifteen expert witnesses have "
            "been invited to testify across two days of proceedings scheduled for next month."
        ),
        "target": {"kind": "tier", "value": "legendary"},
        "effect_range": (0.72, 0.85),
        "duration_range": (3, 5),
        "weight": 2,
    },

    # ===== STARTER TIER =====
    {
        "headline": (
            "The Kanto Department of Education's Division of Trainer Affairs has submitted a budget "
            "request to expand its new trainer certification program to 31 accredited sites across "
            "the region, up from the current 12. The request, pending committee approval, cites a "
            "multi-year trend of increasing applicant volumes as the primary justification for "
            "the expansion."
        ),
        "target": {"kind": "tier", "value": "starter"},
        "effect_range": (1.10, 1.22),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "Professor Oak's laboratory published its annual operations summary this week. Under the "
            "breeding and conservation section, the report notes that captive breeding programs "
            "produced output that exceeded projections by 31% for the third consecutive year, and "
            "that current holding capacity at the facility is at 94% utilization."
        ),
        "target": {"kind": "tier", "value": "starter"},
        "effect_range": (0.80, 0.90),
        "duration_range": (2, 3),
        "weight": 3,
    },

    # ===== PSEUDO-LEGENDARY TIER =====
    {
        "headline": (
            "Tournament organizers for the upcoming Indigo Plateau Regional Championships released "
            "registered team field data this week. Analysis circulating in competitive battling "
            "communities notes that the average base stat total across all participating rosters "
            "is approximately 15% higher than the comparable figure from last year's field."
        ),
        "target": {"kind": "tier", "value": "pseudo_legendary"},
        "effect_range": (1.12, 1.28),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "The Pokémon Battle Analytics Consortium's mid-season report, published Friday, includes "
            "a section on combat efficiency metrics. The data shows that the mean number of turns "
            "required to eliminate pseudo-legendary Pokémon in top-tier bracket play decreased by "
            "19% compared to the prior season."
        ),
        "target": {"kind": "tier", "value": "pseudo_legendary"},
        "effect_range": (0.82, 0.92),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: MAGIKARP =====
    {
        "headline": (
            "A video clip from last weekend's Cerulean City invitational tournament has surpassed "
            "two million views on the Kanto Trainer Network within 72 hours. The clip was posted "
            "without a title by an anonymous account; the caption reads only 'never give up.' "
            "It has been shared across every major trainer community forum and has remained the "
            "top trending item on the platform for four consecutive days."
        ),
        "target": {"kind": "name", "value": "Magikarp"},
        "effect_range": (1.15, 1.35),
        "duration_range": (1, 2),
        "weight": 3,
    },
    {
        "headline": (
            "The Kanto Waterway Authority's semi-annual fishery population assessment has been "
            "released. Among its findings, the report documents population densities in twelve "
            "monitored river systems and four major lakes, with all sixteen sites recording figures "
            "for one particular species at or above the 'sustainable upper threshold' defined in "
            "the agency's fishery management guidelines."
        ),
        "target": {"kind": "name", "value": "Magikarp"},
        "effect_range": (0.65, 0.80),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== SPECIFIC: EEVEE =====
    {
        "headline": (
            "A paper from researchers at the Pokémon Evolution Institute has passed peer review and "
            "been accepted for publication in next month's issue of the Journal of Applied Pokémon "
            "Genetics. The journal's editor-in-chief described it as 'among the most consequential "
            "submissions received in recent years' in a brief statement accompanying the acceptance notice."
        ),
        "target": {"kind": "name", "value": "Eevee"},
        "effect_range": (1.18, 1.38),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "The Celadon City Pokémon Cooperative published its annual member report this week, "
            "noting that its breeding programs produced a 34% increase in output over the prior year "
            "and that the cooperative's regional certification — enabling bulk sales at institutional "
            "rates — was renewed without issue for a further three-year term."
        ),
        "target": {"kind": "name", "value": "Eevee"},
        "effect_range": (0.75, 0.88),
        "duration_range": (2, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: SNORLAX =====
    {
        "headline": (
            "Saffron University's Department of Biological Sciences has announced receipt of a "
            "5.2 million PokéDollar research grant for a multi-year study on 'metabolic regulation "
            "and sleep cycle optimization in large-class Pokémon.' The project will begin enrollment "
            "of research subjects next month, according to the university's research affairs office."
        ),
        "target": {"kind": "name", "value": "Snorlax"},
        "effect_range": (1.08, 1.20),
        "duration_range": (2, 4),
        "weight": 3,
    },
    {
        "headline": (
            "Three regional news outlets ran feature stories this week on what they are calling 'the "
            "obstruction incidents,' covering a series of cases in which large Pokémon blocked a "
            "commercial delivery corridor, an emergency vehicle access road, and a pedestrian "
            "thoroughfare. Two city councils have confirmed they are reviewing their Pokémon "
            "ownership ordinances in response."
        ),
        "target": {"kind": "name", "value": "Snorlax"},
        "effect_range": (0.80, 0.92),
        "duration_range": (1, 2),
        "weight": 3,
    },

    # ===== SPECIFIC: GYARADOS =====
    {
        "headline": (
            "A coastal ecology monitoring team has published an update to its long-term survey of "
            "Kanto's marine Pokémon populations. The report notes that encounters with apex-class "
            "aquatic Pokémon in the waters west of Cinnabar Island increased approximately threefold "
            "compared to the previous survey period three years ago, the largest single-interval "
            "increase recorded since monitoring began."
        ),
        "target": {"kind": "name", "value": "Gyarados"},
        "effect_range": (1.12, 1.30),
        "duration_range": (1, 3),
        "weight": 3,
    },

    # ===== SPECIFIC: DITTO =====
    {
        "headline": (
            "The Kanto Pokémon Authenticity Registry has announced the rollout of a rapid point-of-sale "
            "verification protocol developed in partnership with fourteen major trading hubs. The system "
            "can confirm species identification in under two minutes, and its adoption has been "
            "designated mandatory for all licensed exchange operators beginning next quarter."
        ),
        "target": {"kind": "name", "value": "Ditto"},
        "effect_range": (0.60, 0.78),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ALL MARKET — POSITIVE =====
    {
        "headline": (
            "The Kanto Regional Chamber of Commerce has released its annual consumer confidence index "
            "for the current quarter. The index recorded its highest value since the survey was first "
            "conducted eleven years ago. The full report is available at Chamber offices and will be "
            "presented at the quarterly economic briefing scheduled for next week."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (1.05, 1.15),
        "duration_range": (2, 3),
        "weight": 3,
    },
    {
        "headline": (
            "The Kanto Revenue Authority has confirmed that the trainer expense deduction — which "
            "allows registered trainers to offset qualifying Pokémon-related purchases against annual "
            "income — will apply retroactively to all eligible transactions made during the current "
            "fiscal year. The deduction ceiling is set at 15% of gross annual earnings."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (1.05, 1.12),
        "duration_range": (2, 4),
        "weight": 3,
    },

    # ===== ALL MARKET — MILD NEGATIVE =====
    {
        "headline": (
            "The Kanto Commerce Ministry has released preliminary trade figures for the current quarter. "
            "Consumer discretionary spending, which includes Pokémon trading activity, declined 6% "
            "compared to the same period last year. Ministry officials characterized the decline as "
            "within the margin of seasonal variation and indicated no policy response is being "
            "contemplated at this time."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.90, 0.97),
        "duration_range": (1, 2),
        "weight": 4,
    },
    {
        "headline": (
            "The Pokémon Commerce Authority has published a notice in the official regulatory gazette "
            "indicating that it has initiated a review of documentation and compliance requirements "
            "for all Pokémon transactions. The review is expected to take between three and six months. "
            "Affected parties may submit written comments during the 60-day public comment period."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.88, 0.95),
        "duration_range": (2, 4),
        "weight": 4,
    },

    # ===== ALL MARKET — CRASH =====
    {
        "headline": (
            "Trading at the Celadon and Saffron Pokémon exchange hubs was suspended for approximately "
            "90 minutes this morning following what exchange administrators described as 'anomalous "
            "order flow conditions.' Operations resumed after an internal review. The Kanto Financial "
            "Stability Council has scheduled an emergency advisory session for this afternoon; no "
            "agenda has been made public."
        ),
        "target": {"kind": "all", "value": None},
        "effect_range": (0.55, 0.72),
        "duration_range": (1, 3),
        "weight": 0.5,
    },
    {
        "headline": (
            "Several of Kanto's largest Pokémon trading houses did not open for business this morning, "
            "with locations in Celadon, Saffron, and Vermilion remaining dark and communications going "
            "unanswered. No public statements have been issued by any of the affected firms. The Kanto "
            "Financial Stability Council has confirmed an emergency session is convening this afternoon."
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
    Applies all active news multipliers to matching Pokémon in live_prices.
    Multiple active events stack multiplicatively.
    """
    import market  # needed to access live_prices

    for event in active_news:
        kind = event["target"]["kind"]
        value = event["target"]["value"]
        mult = event["multiplier"]

        for pokemon in market_inventory:

            name = pokemon["name"]

            if name not in market.live_prices:
                continue

            if kind == "all":
                market.live_prices[name] = max(
                    1,
                    int(market.live_prices[name] * mult)
                )

            elif kind == "type" and value in pokemon["type"]:
                market.live_prices[name] = max(
                    1,
                    int(market.live_prices[name] * mult)
                )

            elif kind == "tier" and pokemon["tier"] == value:
                market.live_prices[name] = max(
                    1,
                    int(market.live_prices[name] * mult)
                )

            elif kind == "name" and pokemon["name"] == value:
                market.live_prices[name] = max(
                    1,
                    int(market.live_prices[name] * mult)
                )


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
        if event["days_left"] <= 0:
            tag = "ENDED"
        elif event["days_left"] == 1:
            tag = "FINAL DAY"
        else:
            tag = f"ONGOING ({event['days_left']} days)"
        print(f"\n[{i}] {tag}")
        print(event["headline"])
    print("\n========================================")
