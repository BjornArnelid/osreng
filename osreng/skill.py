from attribute import INTELLIGENCE, CHARISMA, AGILITY, STRENGTH


class Skill:
    def __init__(self, index, name, attribute, base):
        self.index = index
        self.name = name
        self.skill_attribute = attribute
        self.base_skill = base


class TrainedSkill:
    def __init__(self, skill_value, skill):
        self.skill_value = skill_value
        self.skill = skill


BEAST_LORE = Skill(0, 'Bestiologi', INTELLIGENCE, True)

BLUFFING = Skill(1, 'Bluffa', CHARISMA, True)

SLEIGHT_OF_HAND = Skill(2, 'Fingerfärdighet', AGILITY, True)

SPOT_HIDDEN = Skill(3, "Finna dolda ting", INTELLIGENCE, True)

LANGUAGES = Skill(4, "Främmande språk", INTELLIGENCE, True)

CRAFTING = Skill(5, "Hantverk", STRENGTH, True)

ACROBATICS = Skill(6, "Hoppa & klättra", AGILITY, True)

HUNTING_AND_FISHING = Skill(7, "Jakt & fiske", AGILITY, True)

BARTERING = Skill(8, "Köpslå", CHARISMA, True)

HEALING = Skill(9, "Läkekonst", INTELLIGENCE, True)

MYTHS_AND_LEGENDS = Skill(10, "Myter & legender", INTELLIGENCE, True)

RIDING = Skill(11, "Rida", AGILITY, True)

SWIMMING = Skill(12, "Simma", AGILITY, True)

SEAMANSHIP = Skill(13, "Sjökunnighet", INTELLIGENCE, True)

SNEAKING = Skill(14, "Smyga", AGILITY, True)

EVADE = Skill(15, "Undvika", AGILITY, True)

PERFORMANCE = Skill(16, "Uppträda", CHARISMA, True)

AWARENESS = Skill(17, "Upptäcka fara", INTELLIGENCE, True)

BUSHCRAFT = Skill(18, "Vildmarksvana", INTELLIGENCE, True)

PERSUASION = Skill(19, "Övertala", CHARISMA, True)

CROSSBOWS = Skill(20, "Armborst", AGILITY, True)

HAMMERS = Skill(21, "Hammare", STRENGTH, True)

KNIVES = Skill(22, "Kniv", AGILITY, True)

BOWS = Skill(23, "Pilbåge", AGILITY, True)

BRAWLING = Skill(24, "Slagsmål", STRENGTH, True)

SLINGS = Skill(25, "Slunga", AGILITY, True)

SPEARS = Skill(26, "Spjut", STRENGTH, True)

STAVES = Skill(27, "Stav", STRENGTH, True)

SWORDS = Skill(28, "Svärd", STRENGTH, True)

AXES = Skill(29, "Yxa", STRENGTH, True)

ANIMALISM = Skill(30, "Animalism", INTELLIGENCE, False)

ELEMENTALISM = Skill(31, "Elementalism", INTELLIGENCE, False)

MENTALISM = Skill(32, "Mentalism", INTELLIGENCE, False)


base_skills = [BEAST_LORE, BLUFFING, SLEIGHT_OF_HAND, SPOT_HIDDEN, LANGUAGES, CRAFTING, ACROBATICS,
               HUNTING_AND_FISHING, BARTERING, HEALING, MYTHS_AND_LEGENDS, RIDING, SWIMMING, SEAMANSHIP, SNEAKING,
               EVADE, PERFORMANCE, AWARENESS, BUSHCRAFT, PERSUASION, CROSSBOWS, HAMMERS, KNIVES, BOWS, BRAWLING,
               SLINGS, SPEARS, STAVES, SWORDS, AXES]
