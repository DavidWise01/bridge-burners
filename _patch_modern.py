#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patch roster.json with the six-W weave for every member."""
import json
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roster.json")

WEAVE = {
    "Mallet": {
        "who": "A Bridge Burner squad healer, the cutter the soldiers trust with their lives.",
        "what": "He mends the broken and stitches the dying, keeping the company on its feet through every grinding campaign.",
        "where": "Wherever the squad bleeds — battlefields, retreats, and the quiet aftermath when the killing stops.",
        "why": "Because someone must answer the wounds that magic and steel leave behind, and he chose that burden.",
        "when": "Through the company's hardest marches, when the warrens go quiet and only craft remains.",
        "how": "By the patient labour of Denul healing, hands and will closing what blades and sorcery have opened."
    },
    "Bluepearl": {
        "who": "A Bridge Burner mage, blunt and dependable where others are subtle.",
        "what": "He is the squad's hammer of sorcery, meeting force with force when finesse will not do.",
        "where": "In the thick of the line, standing where the magic has to land hardest.",
        "why": "To shield his squad and break what stands against it, the simplest of loyalties.",
        "when": "Across the company's campaigns, called up whenever raw power is the only answer.",
        "how": "Through Mockra and unrefined force — the blunt instrument of the squad's magic."
    },
    "Spindle": {
        "who": "A sapper-mage known for the famous, much-mocked hair shirt he wears.",
        "what": "He doubles as munitions man and mage, turning destruction into a careful craft.",
        "where": "Beneath walls and along the breaking points, where sappers do their grim, exacting work.",
        "why": "To bring down what must come down, trusting craft over chance.",
        "when": "Through the company's sieges and hard fights, where a sapper earns his keep.",
        "how": "By marrying munitions to Mockra — destruction measured out by skill rather than fury."
    },
    "Fiddler": {
        "who": "A Bridge Burner sapper with no warren to his name, later the Master of the Deck of Dragons.",
        "what": "He is the moral spine of the company, the soldier the others steady themselves against.",
        "where": "On the front lines among his marines, and later in the wider weave of the Deck's portents.",
        "why": "Out of stubborn loyalty to the soldiers beside him and a refusal to let the wrong thing pass.",
        "when": "From the early campaigns through to the saga's gravest turns, when his nerve matters most.",
        "how": "With cussers, sharpers, and sheer nerve — no sorcery, only craft, courage, and an unflinching conscience."
    },
    "Hedge": {
        "who": "Fiddler's partner in munitions, a sapper who would not stay dead.",
        "what": "He came back from death to lead the fallen Bridge Burners, a commander of the company's ghosts.",
        "where": "On the old battlefields and in the strange country between the living and the dead.",
        "why": "Because the work was not finished and the dead Bridge Burners still needed someone to lead them.",
        "when": "After his own fall, in the saga's later movements when the dead return to the reckoning.",
        "how": "Through munitions, gallows wit, and a refusal to let death have the last word."
    },
    "Beak": {
        "who": "A quiet savant whose hidden genius eclipses far prouder mages.",
        "what": "He can shield those he loves and annihilate their enemies with the very same hand.",
        "where": "In the heart of the fight, where his one improbable candle of power burns brightest.",
        "why": "Out of devotion to the squad that finally saw him as more than a simpleton.",
        "when": "In the singular moment his gift is needed, spent without hesitation.",
        "how": "By a savant's impossible command of magic — one candle of genius, given all at once."
    },
    "Tayschrenn": {
        "who": "The Imperial High Mage, the mortal who comes nearest to holding all powers at once.",
        "what": "He is the empire's foremost sorcerer, a force the powers themselves must reckon with.",
        "where": "At the apex of imperial sorcery and at the crossroads of gods and ascendants.",
        "why": "His purposes run deep and guarded — to serve, to survive, and to see further than those around him.",
        "when": "Through the empire's defining sorcerous conflicts, when the highest magic is in play.",
        "how": "By a command of power so broad that he is touched, it is said, by every authority there is."
    },
    "Quick Ben": {
        "who": "Ben Adaephon Delat, the wizard of twelve souls and a dozen schemes.",
        "what": "He is the company's master planner, the architect of the plan inside the plan inside the plan.",
        "where": "At the secret center of events, where strategy and sorcery braid together.",
        "why": "To outthink every adversary and keep his people alive by sheer cunning.",
        "when": "Throughout the saga's deepest gambits, whenever the long game must be won.",
        "how": "By wielding every warren and twelve bound souls — purple by right, aristocrat by design."
    },
    "Kalam Mekhar": {
        "who": "A master assassin of the company, the long knives at Quick Ben's side.",
        "what": "He is the one you send when a thing simply must be done, the company's edge made flesh.",
        "where": "In the shadows and the close dark, wherever a blade must reach what armies cannot.",
        "why": "Out of fierce loyalty to his friends and a soldier's hard sense of what is owed.",
        "when": "At the saga's decisive blows, when the work falls to one knife and one nerve.",
        "how": "With the long knives and a killer's patience — Quick Ben's other half, the deed done quietly."
    },
    "Gesler": {
        "who": "A heavy-infantry soldier left half-immortal after an encounter with the Stormriders.",
        "what": "He is one half of the company's eternal bickering double act, and a deadly hand in a fight.",
        "where": "On the line with the heavies and in whatever scrape his temper drags him into.",
        "why": "To do his soldier's duty and trade insults with Stormy while doing it.",
        "when": "Across the campaigns following his brush with the Stormriders, his odd gift carried ever after.",
        "how": "By brute soldiering, a hide touched by the sea's old power, and an inexhaustible appetite for argument."
    },
    "Stormy": {
        "who": "Adjunct Stormy, a red-bearded soldier of grief and fury.",
        "what": "He is the other half of the bickering act and, beneath the comedy, lethally capable.",
        "where": "Shoulder to shoulder with Gesler wherever the fighting is thickest.",
        "why": "Out of loyalty, grief carried close, and the same stubborn duty that drives his partner.",
        "when": "Through the same campaigns that bound him to Gesler, the bit running the length of the saga.",
        "how": "With red-bearded fury, a soldier's craft, and a wail of grief that turns to violence."
    },
    "The Marines": {
        "who": "The squad marines — Hellian, Throatslitter, Deadsmell, and the rest — the company's ragged backbone.",
        "what": "They hold the line under fire, trading gallows humour for the courage to keep standing.",
        "where": "In the worst of the fighting, where soldiers either laugh or break.",
        "why": "For each other above all, the squad that is the only family some of them have left.",
        "when": "Through every campaign, in the long hours between terror and the next terror.",
        "how": "By dark jokes, hard discipline, and a refusal to quit even when there is every reason to."
    },
    "Cotillion": {
        "who": "The Rope, patron god of assassins, who was once the man called Dancer.",
        "what": "He is the divine blade of the House of Shadow, a god still playing a mortal's long game.",
        "where": "Throughout the realm of Shadow and the mortal world he refuses to abandon.",
        "why": "His true aims stay veiled — but he moves, ceaselessly, toward an end he will not yet name.",
        "when": "From the days of his mortal partnership onward, into the saga's godly maneuverings.",
        "how": "Through the patient knife of an assassin-god — possession, misdirection, and the quiet cut."
    },
    "Shadowthrone": {
        "who": "Ammanas, who holds the throne of Shadow and was once the Emperor Kellanved.",
        "what": "He is the master of the House of Shadow, scheming across the board the gods themselves play on.",
        "where": "Upon the throne of Shadow and through every realm his manipulations can reach.",
        "why": "Toward a vast design begun in his mortal days, its full shape his to keep and not mine to guess.",
        "when": "From the empire's founding through the saga's grandest godly gambits.",
        "how": "By cunning, misdirection, and the dominion of Shadow — the long game played with a partner across time."
    },
    "Dancer": {
        "who": "Kellanved's partner and blade, the mortal who ascended into Cotillion.",
        "what": "He is one half of the partnership that built an empire and then walked into godhood.",
        "where": "At Kellanved's side in the mortal world, and afterward woven into the realm of Shadow.",
        "why": "Out of a partnership and purpose that outlasted his mortality itself.",
        "when": "From the empire's beginnings into his ascension, so that two names became one knife across time.",
        "how": "With a peerless blade and a partner's trust — the man who became the god Cotillion."
    },
    "Tehol Beddict": {
        "who": "A Letherii genius who plays the idiot, ruling a rooftop kingdom in a blanket.",
        "what": "He set out to crash an empire's economy on purpose, and very nearly did it for fun.",
        "where": "Mostly from a rooftop in the city of Letheras, mostly under that famous blanket.",
        "why": "To topple a rotten system at its root — economic ruin as a kind of mercy.",
        "when": "During the Letherii arc, while the empire counts its coins and never sees him coming.",
        "how": "By financial sabotage dressed as foolishness — genius wearing idiot's clothes."
    },
    "Bugg": {
        "who": "Tehol's devoted manservant, secretly Mael, the Elder God of the Sea.",
        "what": "He is the engine beneath Tehol's scheme, doing the real work behind the rooftop comedy.",
        "where": "At Tehol's side in Letheras, and in the deep tides of the world only a sea-god knows.",
        "why": "Out of undying loyalty to Tehol and an Elder God's long patience with mortal folly.",
        "when": "Through the Letherii arc, the ancient power content, for now, to play the servant.",
        "how": "By boundless competence and hidden divinity — the Elder God of the Sea answering to a man in a blanket."
    },
    "Brys Beddict": {
        "who": "Tehol's brother, King's Champion and the finest blade in all of Lether.",
        "what": "He is the realm's protector by the sword, honor made into a man.",
        "where": "At the king's side and on the duelling ground where the realm's fate is wagered.",
        "why": "Out of a loyalty that does not break and an honor that will not bend.",
        "when": "Through the Letherii arc, when the kingdom most needs a blade it can trust.",
        "how": "By a swordsmanship beyond rival, wielded always in service to duty rather than self."
    },
    "Tehol's Household": {
        "who": "The rooftop court of Tehol Beddict — Bugg and the rest of the absurd, faithful crew.",
        "what": "They are the loyal engine of the scheme, each playing a part in the world-saving farce.",
        "where": "On Tehol's rooftop in Letheras, headquarters of the unlikeliest revolution.",
        "why": "Out of loyalty to Tehol and his last, ridiculous, world-saving scheme.",
        "when": "Through the Letherii arc, holding together while the empire crumbles below.",
        "how": "By devotion, competence, and comedy — a household bound to one man's impossible plan."
    },
    "Apsalar": {
        "who": "Once the fishergirl 'Sorry' and a Bridge Burner, then the vessel of Cotillion, now her own woman.",
        "what": "She is a peerless assassin who reclaimed herself from the god who once wore her.",
        "where": "In the shadows where assassins work, and at last on a path she chooses for herself.",
        "why": "To live as her own avatar after being made a weapon — the rest is hers to tell, not mine to invent.",
        "when": "From her possession onward into her hard-won freedom across the saga.",
        "how": "By the lethal skills Cotillion left in her hands, now turned to ends that are her own."
    },
    "Karsa Orlong": {
        "who": "A Toblakai warrior who names himself, and demands to be named, the Witness.",
        "what": "He is the one who stands and sees, refusing to look away from any truth, however terrible.",
        "where": "Wherever the world would rather not be watched — among its cruelties, its lies, its reckonings.",
        "why": "To bear witness without flinching, and to compel everyone around him to do the same.",
        "when": "Across his long path through the saga, from his first terrible march to his standing as Witness.",
        "how": "By unbending will and the refusal of any comfortable blindness — he will not look away, nor let you."
    }
}

def main():
    with open(PATH, "r", encoding="utf-8") as f:
        R = json.load(f)

    members = R["members"]
    unmatched = []
    patched = 0
    for m in members:
        name = m.get("name")
        if name not in WEAVE:
            unmatched.append(name)
            continue
        w = WEAVE[name]
        for k in ("who", "what", "where", "why", "when", "how"):
            m[k] = w[k]
        patched += 1

    extra = [k for k in WEAVE if k not in {m.get("name") for m in members}]
    if unmatched:
        raise SystemExit("Unmatched members (no weave provided): %r" % unmatched)
    if extra:
        raise SystemExit("Weave entries with no matching member: %r" % extra)

    appendix = " Every ACI now carries the full DLW tag with an authored six-W .spun."
    if not R["note"].endswith(appendix):
        R["note"] = R["note"] + appendix

    with open(PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(R, ensure_ascii=False, indent=2) + "\n")

    print("Patched %d / %d members." % (patched, len(members)))
    if patched != len(members):
        raise SystemExit("Coverage gap: patched %d but roster has %d members." % (patched, len(members)))

if __name__ == "__main__":
    main()
