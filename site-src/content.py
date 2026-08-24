SITE = {
    "name": "Marrow Notes",
    "tagline": "Mortal Shell II guides that show their sources",
    "base": "https://kevin-wei-sudo.github.io/marrow-notes",
    "updated": "24 August 2026",
}

# tier: t1 = official, t2 = tested guide site, t3 = needs cross-checking, ugc = players
PAGES = [
# ---------------------------------------------------------------- home
{
 "slug": "index",
 "kind": "home",
 "title": "Marrow Notes — Mortal Shell II guides",
 "desc": "Mortal Shell II guides that label where every fact came from. Boss strategies, Shell picks, Hardening, PC stutter fixes and beta carry-over rules.",
 "h1": "Mortal Shell II, with the sources left in",
 "eyebrow": "Launched 20 August 2026",
 "lede": "Most guides for this game were written during the open beta and never updated. Some contradict each other about where bosses are. One of the top-ranking sites invents boss names outright. Every page here marks which claims come from Cold Symmetry, which come from someone who actually played the retail build, and which are still in dispute.",
 "body": """
## Start here

If you are stuck right now, go straight to the fight. If you have not launched yet, the two pages worth reading first are the beta carry-over rules and the PC setup notes — both save you time you cannot get back.

- [[Magdalena, the Lady of the Woods|/bosses/magdalena.html]] — the first major boss, and the one most players lose to
- [[Which Shell to take on your first run|/shells/best-first-shell.html]] — the decision you make before you know what any of it means
- [[Does beta progress carry over?|/systems/beta-carry-over.html]] — short answer: almost none of it
- [[Stutter and frame drops on PC|/systems/stuttering-fix.html]] — what is confirmed, and what the community is arguing about

## How we mark things

Every factual claim on this site carries a marker. Hover it, or read the source list at the foot of each page.

| Marker | Means |
| Official | Stated by Cold Symmetry, Playstack, or a platform store listing |
| Tested | Reported by a guide site working from the retail build |
| Unconfirmed | Single source, or a claim we could not cross-check |
| Disputed | Two credible sources say different things — we print both |

## Where the guides disagree

These are live disagreements as of 24 August 2026. We would rather show you the fork in the road than pick one and hope.

- **Magdalena's location** has four published routes. At least one is a beta route that no longer applies.
- **Forcing DirectX 11** via launch options is called the single most effective stutter fix by one guide and a guaranteed crash by another.
- **The Slayer Seal** is recommended without caveat for the Magdalena fight, while a separate beginner guide says it locks you out of some achievements.

Each of those has its own page. None of them is settled.
""",
 "sources": [],
},

# ---------------------------------------------------------------- hubs
{
 "slug": "bosses/index",
 "kind": "hub",
 "parent": None,
 "title": "All Mortal Shell II bosses in order | Marrow Notes",
 "desc": "The ten major bosses of Mortal Shell II, the region each one sits in, and which fights are optional. Includes the six Corrupted Gate dungeons.",
 "h1": "All Mortal Shell II bosses in order",
 "eyebrow": "Boss guides",
 "lede": "Ten major bosses, spread across Fainweald, Mammon and the final dungeon. Six of them sit at the end of a Corrupted Gate; the rest are story-critical or hidden.",
 "body": """
## The shape of the run

The overworld holds six Corrupted Gate dungeons. Three are in Fainweald — the Glutted Mire, the Sanguine Caverns and the Prisoners' Domain. Three are in Mammon — the Conquered Temple, the Withered Shoals and the Faded Citadel. Each ends in a major boss. The remaining fights are in the final dungeon.{{t2}}

There is also a boss in the prologue whose outcome is fixed, so it does not count toward the ten.{{t2}}

## Confirmed bosses

| Boss | Where | Notes |
| Tar Golem | Prologue | Outcome is predetermined |
| The Wandering Shepherd | Glutted Mire | Mini-boss before Magdalena |
| Magdalena, the Lady of the Woods | Glutted Mire | Usually the first major boss |
| Solnir Stillblade | Overworld | First boss shown in preview footage |
| Vellen, High Lord of Mammon | Underground, Mammon | A Shell sits in the room behind him |
| Lucian, the Thirsting Knight | The Hidden Keep | Optional Beacon dungeon |
| Sir Isaac, the Scholar-Prince | — | Region unconfirmed |
| Malborn Offspring | Late game | Compare with Zmey before committing |
| Zmey, the Unbidden | Unfound Path | Final boss |

## Fights with a guide here

- [[Magdalena, the Lady of the Woods|/bosses/magdalena.html]] — loadout, the Fly Storm phase, and why the four published routes disagree
- [[Zmey or Malborn Offspring first?|/bosses/zmey-or-malborn.html]] — the answer depends on your Shell, and the one source that answered it said so

## General approach

Break damage is the throughline. Most fights are built around filling a boss's Break meter with skills or parries, then landing a riposte, rather than out-damaging them with raw hits.{{t2}} The exception is any boss whose main attacks are unblockable — Magdalena is the clearest case — where dodging is simply more reliable than testing parry timing.{{t2}}
""",
 "sources": [
   ("t2", "Game8 — All Mortal Shell 2 Bosses in Order", "Count of ten major bosses, recommended order, Break-damage approach"),
   ("t2", "GameSpot — All bosses and how to beat them", "Region breakdown, the six Corrupted Gate names, the predetermined prologue fight"),
   ("t2", "Fextralife — Bosses", "Mandatory versus optional split, individual boss pages"),
   ("t3", "GameTyrant", "Existing pages for Malborn Offspring and Sir Isaac, the Scholar-Prince"),
 ],
},
{
 "slug": "shells/index",
 "kind": "hub",
 "title": "Mortal Shell II Shells: locations and picks | Marrow Notes",
 "desc": "All eight Shells in Mortal Shell II, where they are, and how to spend Glimpses on Bond levels instead of wasting them on map markers.",
 "h1": "Shells, Bonds and Glimpses",
 "eyebrow": "Shell guides",
 "lede": "Your Shell is both your class and your armour. There are eight, none of them are missable, and the currency you use to deepen them is scarcer than it looks.",
 "body": """
## Eight, not nine

The official site says eight playable Shells.{{t1}} The open beta build contained nine Shell records including Harros, and nobody has publicly mapped those nine records onto the retail eight.{{t3}} Treat eight as the number and ignore the beta data unless Cold Symmetry says otherwise.

## Nothing is missable

You can find every Shell after the final boss during free roam, before you choose to enter New Game Plus.{{t2}} The first two are marked on your map automatically at the start.{{t2}} That means there is no reason to rush Shell hunting and no reason to panic about a locked gate.

## Do not pay to mark them

You can spend Glimpses in the Shellkeeper's room to reveal the location of the remaining Shells. This is a bad trade. Glimpses are also what raise Shell Bond, and Bond level is what unlocks Shell Memories.{{t2}} Watching every Memory is required for one achievement, and there are not enough Glimpses in a single playthrough to get there.{{t2}}

## Guides here

- [[Which Shell to take on your first run|/shells/best-first-shell.html]]
- [[What to spend Glimpses on|/shells/glimpses.html]]

## What a build is made of

Five slots: Shell, Weapon, Sidearm, Seal and Tarstones. All five are scattered through the open world and have to be found before you can use them.{{t3}} Tarstones come in four types — Support, Combat, Infusion and Ability — and are upgraded through Franz.{{t3}}
""",
 "sources": [
   ("t1", "Official Mortal Shell II site", "Eight playable Shells"),
   ("t2", "PowerPyx — All Shell Locations", "No Shells are missable; the first two are auto-marked; why paying Glimpses to mark Shells is a bad trade"),
   ("t2", "Game8 — Shells Tier List", "Relative ranking of the eight Shells"),
   ("t2", "GameRant — New Game Plus", "Seeking the Past needs more Glimpses than one playthrough provides"),
   ("t3", "games.gg — Beginner's guide", "The five build slots, Tarstone types, upgrading through Franz"),
   ("t3", "mortalshell2.org", "Nine Shell records in the open beta build, mapping unverified"),
 ],
},
{
 "slug": "systems/index",
 "kind": "hub",
 "title": "Mortal Shell II systems and PC fixes | Marrow Notes",
 "desc": "Hardening, Gloom recovery, Beacons, beta carry-over and PC stutter fixes for Mortal Shell II — with the contradictory advice flagged.",
 "h1": "Systems, currencies and PC problems",
 "eyebrow": "Systems",
 "lede": "The mechanics that cost people the most time, plus the launch-window PC issues. This is also where the worst misinformation lives, so the markers matter more here than anywhere else.",
 "body": """
## Combat and progression

- [[Hardening: when it works and when it does not|/systems/hardening.html]]
- [[Recovering Gloom after you die|/systems/gloom-recovery.html]]

## Launch-window problems

- [[Stutter and frame drops on PC|/systems/stuttering-fix.html]]
- [[Does beta progress carry over?|/systems/beta-carry-over.html]]

## Beacons do two jobs

Beacons are checkpoints and fast travel nodes. Some also have a dungeon underneath that can be cleansed for Ova — the primary objective currency — plus resources and Glimpse.{{t3}} Not every Beacon has one.

Fast travel does not unlock until you have siphoned six Ova back at the Marrow Keep.{{t3}} Until then the Beacon network is your route map, so light every one you walk past.

## A warning about this corner of the internet

One site currently ranking for several of these queries publishes fabricated content. It lists boss names that appear in no other source, and its own pages contradict each other on whether forcing DirectX 11 fixes stutter or causes crashes. We are not linking it. If a guide gives you a boss name you cannot find on Game8, Fextralife or GameSpot, close the tab.
""",
 "sources": [
   ("t3", "games.gg — Beginner's guide", "Beacon dual role, Ova as objective currency, six-Ova fast travel unlock"),
   ("t2", "TheGamer — Beginner tips", "Combat pacing, Gloom recovery as a core early skill"),
 ],
},

# ---------------------------------------------------------------- P0 pages
{
 "slug": "bosses/magdalena",
 "kind": "page",
 "title": "How to beat Magdalena in Mortal Shell II",
 "desc": "Magdalena, the Lady of the Woods: the loadout to bring, why parrying fails, how to survive the Fly Storm at low health, and why four guides give four routes.",
 "h1": "How to beat Magdalena, the Lady of the Woods",
 "eyebrow": "Boss guide",
 "lede": "Mechanically she is one of the simpler fights in the game. She kills people anyway, because almost everything she does punishes the instinct this genre trained into you: parry, then punish. Here, you dodge.",
 "body": """
## The short version

Do not treat this as a parry test. Most of her offence cannot be blocked normally, so dodging is the more consistent way to survive.{{t2}} Bring burn mitigation, bring a fast weapon, and save some Resolve for the end of the fight — at low health she surrounds herself with flies and you will need to finish her at range.{{t2}}

## What to bring

- **Effigy** — Burnt Effigy in the **passive** slot, not the active one. Passive gives you burn mitigation for the whole fight, which matters because her signature move surrounds her in flame.{{t3}}
- **Weapon** — something fast. She moves constantly, and a two-handed sword or axe will not land before she has repositioned.{{t3}}
- **Sidearm** — mandatory. The final phase is not winnable in melee.{{t2}}
- **Seal** — the Slayer Seal builds Break damage quickly, which sets up the riposte loop.{{t2}}

!!Disputed|The Slayer Seal is recommended for this fight without caveat by one wiki, while a separate beginner guide states the Slayer Seal locks some achievements. If you are chasing a full completion, verify before equipping it.

## Getting to her

She is at the end of the Glutted Mire, past the Wandering Shepherd mini-boss and the chest holding the Etching Needles.{{t3}} The run from the nearest Beacon to her arena has no major enemies in it, so a death is cheap in time terms.{{t3}}

!!Disputed|Four published guides give four different routes. One says to enter through the Corrupted Gate behind the Mushroom Village Gate beacon, then push through the Sunken Village in the Glutted Mire and drop from a ledge into the swamp. Another routes you from the Sunken Village Beacon across a wooden bridge, breaking crates and squeezing between fences. That second route comes from a page that describes this as a beta encounter. If you are following a route and the geometry does not match, you are probably reading beta directions.

## Phase one: bait, hit twice, leave

Her attacks telegraph clearly. The mistake that kills people is not misreading them — it is trying to fit in one more hit afterwards.{{t3}}

**The charge.** Unparryable.{{t2}} Give her the space to commit to it, dodge, close while she recovers, land one or two hits, and get out.{{t3}}

**The spinning flame attack.** She surrounds herself in fire and sweeps. Dash outward, wait for the animation to finish, then punish the recovery.{{t2}}

**Staying close.** Her most dangerous moves exist to punish lingering.{{t2}} Distance is not cowardice here, it is the strategy.

## The Break and riposte loop

With Break damage accumulating, fill her Break meter, land the riposte, and repeat two or three more times.{{t2}} The cost is Resolve, which your sidearm also spends — so bait her toward the edges of the arena where you have room to manage both.{{t2}}

## Phase two: the Fly Storm

At roughly five to ten percent health she casts a swarm that circles her and stops you closing in.{{t2}} She also summons additional enemies.{{t3}}

This is where the fight is actually lost. If you arrive at her health bar's last sliver with no Resolve banked, you have no way to damage her and no way to get close. Start conserving Resolve while she is still around a quarter health, and finish the fight with your sidearm.{{t2}}

## Reward

Magdalena's Memento, a Tarstone that spends 100 Resolve to unleash a flurry of strikes.{{t3}}

## Still dying?

| Symptom | Actual cause | Change |
| Parries keep failing | Most of her moveset is unparryable | Dodge instead |
| Fire takes half your health | Burnt Effigy is not in the passive slot | Move it to passive |
| Punished after two hits | Greed | Hit twice, then disengage |
| Cannot finish her off | No Resolve banked for the Fly Storm | Conserve from 25% health |
| Swings never connect | Weapon too slow | Switch to a fast weapon |
""",
 "sources": [
   ("t2", "Game8 — Magdalena location and how to beat", "Route through the Mushroom Village Gate Corrupted Gate; charges are unparryable; ranged and fast weapons favoured; the flame AoE and fly swarm as the two most dangerous moves"),
   ("t2", "Fextralife — Magdalena the Lady of the Woods", "Break meter and riposte loop; Slayer Seal recommendation; the Fly Storm trigger at 5–10% health; managing Resolve against sidearm use. Note: this page describes the fight as a beta encounter."),
   ("t3", "GameTyrant", "Burnt Effigy in the passive slot for burn mitigation; fast weapon reasoning; Magdalena's Memento reward"),
   ("t3", "gamer.org", "Bait-and-punish rhythm; the clean Beacon run; the Wandering Shepherd and Etching Needles as prerequisites"),
   ("t3", "Sportskeeda — beta walkthrough", "The Wandering Shepherd mini-boss and how to approach it"),
   ("ugc", "YouTube fight recordings (June 2026)", "Frame-level timing on the charge wind-up and flame duration — not yet extracted"),
 ],
},
{
 "slug": "shells/best-first-shell",
 "kind": "page",
 "title": "Best Shell for your first Mortal Shell II run",
 "desc": "How to choose your first Shell in Mortal Shell II, why the choice is reversible, and why spending Glimpses to find more Shells early is a mistake.",
 "h1": "Which Shell to take on your first run",
 "eyebrow": "Shell guide",
 "lede": "This is the first real decision the game asks you to make, and it asks before you understand any of the words in it. The good news is that it is the least permanent decision in the game.",
 "body": """
## The decision is reversible

There are eight Shells. None of them are missable — every one can be found after the final boss during free roam, before you commit to New Game Plus.{{t2}} The first two are marked on your map automatically.{{t2}}

So the question is not which Shell is best. It is which Shell makes the opening hours survivable while you learn the systems.

## What a Shell actually is

Your Shell is your class and your armour at once. You invest Glimpse into it to deepen your Bond, which unlocks that Shell's abilities.{{t3}} Bond also gates Shell Memories, which one achievement requires you to see all of.{{t2}}

That coupling is the part people miss. Every Glimpse you spend elsewhere is a Glimpse not spent on Bond, and there are not enough in one playthrough to finish the Memory collection anyway — the earliest anyone can complete it is a second New Game Plus cycle.{{t2}}

## Practical advice for the first hours

- **Take what the game gives you.** Harros is the first Shell the main story hands you.{{t3}} There is no penalty for staying in it through the prologue.
- **Do not pay to mark the others.** You can spend Glimpses in the Shellkeeper's room to reveal remaining Shell locations. Skip it — you will find them anyway, and Bond is the better use.{{t2}}
- **Match the Shell to the fight, not to your identity.** A beta walkthrough reports that using Tiel's Shell ability twice in a row, with ability upgrades and a fast weapon, takes the Wandering Shepherd to half health.{{t3}} That is a fight-specific answer, and it is how the system is meant to be used.
- **Farm before you force it.** If every available path feels too hard, upgrade and come back. Returning to a difficult area better equipped is usually faster than brute-forcing it.{{t2}}

!!Unconfirmed|The official site says eight playable Shells. The open beta build contained nine Shell records including Harros, and the mapping between those and the retail eight has not been verified publicly.

## What to read next

- [[What to spend Glimpses on|/shells/glimpses.html]] — the budget question this page keeps pointing at
- [[Hardening: when it works|/systems/hardening.html]] — no Shell saves you from the core defensive mechanic
- [[Magdalena, the Lady of the Woods|/bosses/magdalena.html]] — the first fight that tests the choice
""",
 "sources": [
   ("t2", "PowerPyx — All Shell Locations", "Nothing is missable; first two Shells auto-marked; Glimpse spent on marking is Glimpse not spent on Bond"),
   ("t2", "Game8 — Shells Tier List", "Relative Shell ranking"),
   ("t2", "GameRant — New Game Plus", "Seeking the Past requires more Glimpses than one run provides"),
   ("t2", "TheGamer — Beginner tips", "Farm and return rather than brute-forcing a wall"),
   ("t3", "games.gg — Beginner's guide", "Shell as class and armour; Glimpse investment into Bond"),
   ("t3", "Sportskeeda — beta walkthrough", "Harros as the first story Shell; Tiel ability against the Wandering Shepherd"),
 ],
},
{
 "slug": "systems/hardening",
 "kind": "page",
 "title": "Mortal Shell II Hardening: why it is not working",
 "desc": "How Hardening fits into Mortal Shell II combat, which attacks it cannot answer, and the timing data that no published guide has yet.",
 "h1": "Hardening, and why it keeps failing you",
 "eyebrow": "Systems",
 "lede": "Hardening is the mechanic the whole combat system is built around, and it is the one most likely to feel broken. Usually it is not broken. Usually you are using it against something it was never meant to stop.",
 "body": """
## What it is for

Hardening turns you to stone mid-animation, absorbing a blow you would otherwise eat. It exists so you can commit to slow attacks in a game full of fast enemies — you swing, you harden through the counterattack, you finish the swing.

The failure mode is treating it as a general-purpose defence. It is not. It is a commitment tool.

## When it will not save you

Several bosses have attacks that simply do not answer to defensive timing. Magdalena's charges are unparryable, and guides consistently recommend dodging over any blocking or parry attempt for the bulk of her moveset.{{t2}} If your Hardening feels like it "did not fire", check whether the move you used it against was ever blockable in the first place.

The general principle from beginner guidance holds: do not rush into fights swinging. Watch what the enemy is doing and look for safe openings before committing.{{t2}} Hardening extends your commitment window — it does not create openings that were not there.

## Break damage is the other half

Most fights are built around filling a Break meter with skills or parries, then landing a riposte, rather than trading raw damage.{{t2}} Hardening and Break work together: hardening through a counterattack keeps your combo alive, and the combo is what fills the meter.

## What we do not know yet

!!Unconfirmed|No published guide gives a frame window for Hardening. Every source describes it qualitatively — "time it well", "watch for openings" — which is not usable advice when you are dying to the same attack repeatedly. We are extracting frame data from launch-window recordings and will replace this section when we have numbers rather than adjectives.

Until then, the honest version is: if a specific attack keeps beating your Hardening, assume that attack is not meant to be hardened through, and dodge it instead.

## Related

- [[Magdalena, the Lady of the Woods|/bosses/magdalena.html]] — the fight where this distinction costs the most
- [[Recovering Gloom after you die|/systems/gloom-recovery.html]] — what those deaths are actually costing you
""",
 "sources": [
   ("t2", "TheGamer — Beginner tips", "Combat pacing: watch openings, do not swing wildly, farm and return"),
   ("t2", "Game8 — Bosses", "Break damage through skills and parries, then riposte, as the general boss framework"),
   ("t2", "Game8 and Fextralife — Magdalena pages", "Which attacks are unparryable, used here as the negative case"),
   ("t3", "games.gg — Beginner's guide", "How Seal, Resolve and sidearm use interact with the defensive loop"),
   ("ugc", "Steam discussions and r/MortalShell", "Player phrasing for Hardening failures — collection starts at launch"),
 ],
},
{
 "slug": "systems/stuttering-fix",
 "kind": "page",
 "title": "Mortal Shell II PC stutter and frame drops: what to try",
 "desc": "A symptom-first checklist for Mortal Shell II stutter on PC, the official system requirements, and why the DirectX 11 launch-option advice is contradictory.",
 "h1": "Stutter and frame drops on PC",
 "eyebrow": "Systems",
 "lede": "Three different problems get called stutter, and they have three different fixes. Sorting out which one you have is worth more than any settings preset someone else wrote.",
 "body": """
## Sort the symptom first

- **Traversal hitch** — a short freeze when you enter a new area or swing the camera. Usually shader compilation or asset streaming.
- **Low average frame rate** — consistently slow everywhere. Usually GPU-bound.
- **Erratic spikes in combat** — fine until effects fire. Usually VRAM or CPU-bound.
- **Delayed-feeling input** — not a frame rate problem at all.

Change one thing at a time and re-run the same route, with the same camera movement and the same weather, before deciding whether it helped.{{t3}} Comparing a quiet indoor scene to a crowded outdoor fight tells you nothing.{{t3}}

## Check the floor first

The official Steam listing sets hard requirements that are easy to skim past: 70 GB of space, and an SSD is required, not recommended.{{t1}} The PC release is Windows-only.{{t1}} The stated minimum is an Intel Core i7-10700K or Ryzen 5 3600, 16 GB of RAM, and an RTX 2060 Super or RX 6600.{{t3}}

If the game is on a mechanical drive, stop reading and move it. Nothing else on this page will help.

## Fixes with agreement behind them

- **Let it sit at the main menu** before loading a save, so background shader compilation finishes.{{t3}}
- **Raise the shader cache size** in the NVIDIA Control Panel under 3D Settings — the AMD Software equivalent is in the same area. More than one independent guide lands on this as the single most effective change.{{t3}}
- **Update GPU drivers**, and if the issue appeared right after a driver change, compare against the previously stable version rather than changing several things at once.{{t3}}
- **Close overlays and hardware-accelerated browsers**, which can hold GPU memory the game wants for combat effects.{{t3}}

## Fixes we are not recommending yet

!!Disputed|Forcing DirectX 11 with the `-dx11` launch option is described by one guide as the highest-impact stability fix available, and by another guide on the same site as something that causes immediate crashes on save load because the game is built natively for DirectX 12. We are not passing on either version until there is an official statement. If you try it, know that you are testing, not fixing.

!!Unconfirmed|Playstack has shipped a Hotfix 1. We have seen it referenced but have not read the official patch notes directly, so nothing from it is stated as fact on this page. Check the game's official channels before applying workarounds that may already be obsolete.

## Before you file a support ticket

Record your resolution, display mode, preset, frame cap, upscaler, driver version and the exact route you tested.{{t3}} A report with those fields gets a useful answer; "the game stutters" does not.

Avoid deleting shader caches or configuration folders unless you have backed them up and official support has asked you to.{{t3}}
""",
 "sources": [
   ("t1", "Steam store listing", "70 GB install, SSD required, Windows-only"),
   ("t3", "mortalshelliiguide.wiki", "Symptom-first diagnostic structure, one-variable-at-a-time methodology, support report fields, warning against deleting caches"),
   ("t3", "mortalshell2.online", "Shader cache size as the most effective single fix; references Playstack Hotfix 1 and a keyboard-bindings save workaround"),
   ("t3", "LagoFast blog", "Root-cause framing: UE5 Lumen and Nanite overhead, VRAM overflow, CPU bottlenecks. Vendor content — promotional claims discarded."),
   ("t3", "Stated minimum specification", "CPU, RAM and GPU floor, reported secondhand and not yet read from the official listing"),
 ],
},
{
 "slug": "systems/beta-carry-over",
 "kind": "page",
 "title": "Does Mortal Shell II beta progress carry over?",
 "desc": "No. Your open beta save resets at launch. Here is exactly what you keep — one cosmetic and a prologue skip — and why some headlines said otherwise.",
 "h1": "Does beta progress carry over?",
 "eyebrow": "Systems",
 "lede": "No. Your save does not transfer. You keep one cosmetic and, if you got far enough, the option to skip the prologue. Everything else resets.",
 "body": """
## What the store listings actually say

To preserve the balance of the full release, beta save progress does not carry over in full. Currency, weapons, Shells, collectibles and other items found during the open beta reset at launch.{{t1}}

Two things survive:

- **The Flayed Harbinger**, an exclusive cosmetic unlocked by playing the open beta, claimable in the full game.{{t1}}
- **A prologue skip**, unlocked if you progressed beyond the Marrow Keep in the beta.{{t1}}

The retail game and the open beta are separate store applications. On Steam the retail app is 2584270 and the beta is 4711740.{{t3}}

## Where the prologue skip drops you

Taking the skip starts you at your first visit to the Keep, which is just after the Tar Golem fight.{{t2}} You lose nothing by skipping, because there is nothing to pick up in the prologue.{{t2}}

## What you definitely lose

Everything collected in the Mushroom Village — items, Tarstones and the Mushroom Village key included.{{t2}} Do not farm beta resources on the assumption that inventory transfers. The reset is deliberate.{{t1}}

## Why you have seen the opposite claim

!!Disputed|At least one outlet published this news under a headline stating that beta progress carries over to the full game, which is the reverse of what the store listings say. Separately, a site we do not link claims the beta rewards include additional shades and a custom parry animation effect — no official listing mentions these. If a source describes beta rewards beyond the Flayed Harbinger and the prologue skip, it is not reading the store page.

## Editions, briefly

The Standard Edition released worldwide on 20 August 2026.{{t1}} The Devout Edition included up to 72 hours of advanced access{{t1}} plus an Obsidian Skin Set covering the eight playable Shells.{{t3}} A physical Revered Edition is PlayStation 5 exclusive.{{t3}}

Cold Symmetry never announced an official closing date for the open beta.{{t3}}
""",
 "sources": [
   ("t1", "PlayStation Store — Mortal Shell II Open Beta listing", "The authoritative carry-over text: save does not transfer, currency/weapons/Shells/collectibles reset, Flayed Harbinger cosmetic, prologue skip past Marrow Keep"),
   ("t1", "Steam store listing", "Same carry-over rules; separate retail and beta applications"),
   ("t2", "GamesRadar — beta rewards and progress", "Where the prologue skip drops you; the Tar Golem timing; Mushroom Village losses including the key"),
   ("t3", "mortalshell2.org", "Store rules tabulated with per-claim check dates; Steam app IDs"),
   ("t3", "backyarddrunkard", "No announced beta end date; Tiel available in the beta"),
   ("t3", "playday.one", "Edition contents. Its headline states the opposite of the official carry-over rule — used here as the misinformation example, not as a source of fact."),
 ],
},

# ---------------------------------------------------------------- P1 pages
{
 "slug": "bosses/zmey-or-malborn",
 "kind": "page",
 "title": "Zmey or Malborn Offspring first? | Mortal Shell II",
 "desc": "Which late-game Mortal Shell II boss to fight first. The only guide that answered admitted its answer depended on a fully upgraded Shell.",
 "h1": "Zmey or Malborn Offspring first?",
 "eyebrow": "Boss guide",
 "lede": "One published guide answers this directly, and it does something unusual: it tells you why its own answer might not apply to you. That caveat is the whole story.",
 "body": """
## The published answer

Zmey is reported as the easier of the two compared with the Malborn Offspring.{{t2}} The guide that says so immediately adds that this may be because they were running a fully powered-up Tiel Shell with several perks unlocked.{{t2}}

That is not hedging. That is the actual answer: the ordering depends on your build, not on the bosses.

## What that means in practice

If your Shell Bond is deep and your perks are unlocked, the reported ordering probably holds for you too. If you arrived here under-levelled — which is common, because this is late-game content and people push through — the comparison was never measured on your situation.

Zmey, the Unbidden is the final boss, at the centre of the Unfound Path.{{t3}} Surviving its Cosmic Flames is the stated prerequisite for having a chance in that fight.{{t2}}

## Before you commit either way

Beating the final boss does not end the game or force you into New Game Plus.{{t3}} You get a free-roam window afterwards, and there is a meaningful cleanup list to run through before you close the cycle. If you are weighing boss order, you are close enough that the cleanup list matters more than the ordering does.

!!Unconfirmed|We have found only one source that compares these two fights directly, and it qualified its own finding. Everything else covers them as separate encounters. Treat the ordering as a reasonable default, not a tested result.

## Related

- [[All bosses in order|/bosses/index.html]]
- [[Which Shell to take on your first run|/shells/best-first-shell.html]] — the variable the comparison actually turned on
""",
 "sources": [
   ("t2", "GameSpot — All bosses and how to beat them", "Direct comparison of Zmey and the Malborn Offspring, with the fully-upgraded-Tiel caveat; Cosmic Flames as the survival gate"),
   ("t3", "KeenGamer", "Zmey, the Unbidden as final boss at the centre of the Unfound Path; the post-boss free roam window"),
   ("t3", "GameTyrant", "Standalone Malborn Offspring page"),
 ],
},
{
 "slug": "shells/glimpses",
 "kind": "page",
 "title": "What to spend Glimpses on in Mortal Shell II",
 "desc": "Glimpses gate Shell Bond, and Bond gates Shell Memories. Here is why paying to mark Shell locations is a trap and how the budget works across cycles.",
 "h1": "What to spend Glimpses on",
 "eyebrow": "Shell guide",
 "lede": "Glimpses look like a minor currency for the first few hours. They are the bottleneck on one of the longest achievement chains in the game, and most guides mention them in a single clause.",
 "body": """
## The one thing not to buy

You can spend Glimpses in the Shellkeeper's room to mark the location of Shells you have not found. Do not.{{t2}} You will find them all anyway — none are missable, and all eight can be collected after the final boss during free roam.{{t2}}

## Where they should go instead

Shell Bond. Bond level is what unlocks Shell Memories,{{t2}} and watching every Memory is required for the Seeking the Past achievement.{{t2}}

Here is the part that reframes the whole budget: there are not enough Glimpses in a single playthrough to see every Memory. The earliest anyone can complete Seeking the Past is a second New Game Plus cycle, and it is likely to be among the last achievements you earn.{{t2}}

## How to budget a first run

Because the achievement is multi-cycle by design, the first run is not where you optimise for completion. It is where you avoid waste.

- **Do not spread thin.** Deepening one or two Shells you actually use beats topping up five you do not.
- **Cleanse Beacons.** Beacon dungeons pay out Ova plus resources and Glimpse, so they are the main faucet.{{t3}}
- **Leave Bond tiers unfinished on purpose.** Bond progress carries into New Game Plus, and the next cycle's Glimpse flow is where you finish them.{{t3}}

!!Disputed|One New Game Plus guide flags an exception: a specific NPC's Bond interaction breaks in the next cycle, so that one has to be pushed to its top tier during the first run. We have seen this in a single source and have not cross-checked it. If you are Bond-farming that character, verify before assuming you can defer.

## Related

- [[Which Shell to take on your first run|/shells/best-first-shell.html]]
- [[Shells, Bonds and Glimpses|/shells/index.html]]
""",
 "sources": [
   ("t2", "PowerPyx — All Shell Locations", "Paying to mark Shells is not recommended; Glimpses are needed for Bond, which gates Memories; nothing is missable"),
   ("t2", "GameRant — New Game Plus", "Seeking the Past needs more Glimpses than one playthrough gives; earliest completion is a second NG+ cycle"),
   ("t3", "games.gg — Beginner's guide", "Cleansing Beacons as the Glimpse source alongside Ova and resources"),
   ("t3", "gamingpromax", "Unfinished Bond tiers can be completed with the next cycle's Glimpse flow"),
   ("t3", "KeenGamer", "The single-source claim about an NPC Bond interaction breaking in New Game Plus"),
 ],
},
{
 "slug": "systems/gloom-recovery",
 "kind": "page",
 "title": "Recovering lost Gloom in Mortal Shell II",
 "desc": "Gloom stays on your corpse when you die. How to get it back, when to spend it before a fight, and the sidearm trick for recovering it at range.",
 "h1": "Recovering Gloom after you die",
 "eyebrow": "Systems",
 "lede": "Gloom is your levelling currency and it drops where you died. The run back to collect it is a second risk stacked on top of the one that killed you — which is why the best recovery strategy happens before you die.",
 "body": """
## How it works

Gloom is the white upgrade currency. You spend it at Beacons to level the Harbinger.{{t3}} When you die it stays on your corpse, and it can be recovered from your death location.{{t3}}

Gold is a separate currency and flows more freely as you clear areas.{{t3}} Losing Gloom hurts; losing gold mostly does not.

## Spend before you gamble

The single most useful habit: if you are carrying enough for an upgrade, spend it at a Beacon before testing an unfamiliar boss or a dangerous route.{{t3}}

This sounds obvious and almost nobody does it, because the upgrade always feels like it can wait one more area. It cannot. The recovery run is a second risk on top of the first, and dying on the way back is how a bad ten minutes becomes a bad hour.{{t3}}

## Getting it back safely

- **Use your sidearm.** Ranged damage costs Resolve, but it lets you clear the area around your drop without walking into it — useful specifically for recovering Gloom at range.{{t3}}
- **Do not re-enter the same fight.** If a boss killed you, your Gloom is inside a boss arena. Clear the arena or accept the loss; do not try to grab and run mid-fight.
- **Do not chase it while under-levelled.** If the area killed you once with a full kit, it will kill you again with no Gloom to spend.

!!Unconfirmed|We have not found a source stating whether Gloom persists indefinitely at the death location or is destroyed by a second death, as it is in comparable games. Assume it can be lost and act accordingly until this is confirmed.

## Related

- [[Hardening: when it works|/systems/hardening.html]]
- [[Systems and PC problems|/systems/index.html]]
""",
 "sources": [
   ("t3", "games.gg — Beginner's guide", "Gloom as levelling currency, stays on corpse, spend before dangerous routes, recovery run as a second risk, sidearm for ranged recovery, gold as a separate currency"),
   ("t2", "Fextralife", "Gloom as the white upgrade currency spent at Beacons"),
   ("t2", "TheGamer — Beginner tips", "Gloom recovery listed among core beginner techniques"),
   ("ugc", "Steam discussions", "Common loss scenarios — collection starts at launch"),
 ],
},
]
