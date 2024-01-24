from attribute import INTELLIGENCE, CHARISMA, AGILITY, STRENGTH


class Skill(object):
    def __init__(self, name, attribute, base):
        self.name = name
        self.skill_attribute = attribute
        self.base_skill = base


class TrainedSkill(object):
    def __init__(self, skill_value, skill):
        self.skill_value = skill_value
        self.skill = skill


BEAST_LORE = Skill('Bestiologi', INTELLIGENCE, True)

BLUFFING = Skill('Bluffa', CHARISMA, True)

SLEIGHT_OF_HAND = Skill('Fingerfärdighet', AGILITY, True)

SPOT_HIDDEN = Skill("Finna dolda ting", INTELLIGENCE, True)

LANGUAGES = Skill("Främmande språk", INTELLIGENCE, True)

CRAFTING = Skill("Hantverk", STRENGTH, True)

ACROBATICS = Skill("Hoppa & klättra", AGILITY, True)

HUNTING_AND_FISHING = Skill("Jakt & fiske", AGILITY, True)

BARTERING = Skill("Köpslå", CHARISMA, True)

HEALING = Skill("Läkekonst", INTELLIGENCE, True)

MYTHS_AND_LEGENDS = Skill("Myter & legender", INTELLIGENCE, True)

RIDING = Skill("Rida", AGILITY, True)

SWIMMING = Skill("Simma", AGILITY, True)

SEAMANSHIP = Skill("Sjökunnighet", INTELLIGENCE, True)

SNEAKING = Skill("Smyga", AGILITY, True)

EVADE = Skill("Undvika", AGILITY, True)

PERFORMANCE = Skill("Uppträda", CHARISMA, True)

AWARENESS = Skill("Upptäcka fara", INTELLIGENCE, True)

BUSHCRAFT = Skill("Vildmarksvana", INTELLIGENCE, True)

PERSUASION = Skill("Övertala", CHARISMA, True)

CROSSBOWS = Skill("Armborst", AGILITY, True)

HAMMERS = Skill("Hammare", STRENGTH, True)

KNIVES = Skill("Kniv", AGILITY, True)

BOWS = Skill("Pilbåge", AGILITY, True)

BRAWLING = Skill("Slagsmål", STRENGTH, True)

SLINGS = Skill("Slunga", AGILITY, True)

SPEARS = Skill("Spjut", STRENGTH, True)

STAVES = Skill("Stav", STRENGTH, True)

SWORDS = Skill("Svärd", STRENGTH, True)

AXES = Skill("Yxa", STRENGTH, True)

ANIMALISM = Skill("Animalism", INTELLIGENCE, False)

ELEMENTALISM = Skill("Elementalism", INTELLIGENCE, False)

MENTALISM = Skill("Mentalism", INTELLIGENCE, False)


base_skills = [BEAST_LORE, BLUFFING, SLEIGHT_OF_HAND, SPOT_HIDDEN, LANGUAGES, CRAFTING, ACROBATICS,
               HUNTING_AND_FISHING, BARTERING, HEALING, MYTHS_AND_LEGENDS, RIDING, SWIMMING, SEAMANSHIP, SNEAKING,
               EVADE, PERFORMANCE, AWARENESS, BUSHCRAFT, PERSUASION, CROSSBOWS, HAMMERS, KNIVES, BOWS, BRAWLING,
               SLINGS, SPEARS, STAVES, SWORDS, AXES]
