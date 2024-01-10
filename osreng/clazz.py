from random import choice
from enum import Enum, auto
from attribute import STRENGTH, AGILITY, INTELLIGENCE, WILL, CHARISMA
from skill import (BLUFFING, LANGUAGES, ACROBATICS, KNIVES, MYTHS_AND_LEGENDS, EVADE, PERFORMANCE, PERSUASION,
                   SLEIGHT_OF_HAND, SPOT_HIDDEN, HAMMERS, CRAFTING, BRAWLING, SWORDS, AXES, HUNTING_AND_FISHING, BOWS,
                   SLINGS, SNEAKING, AWARENESS, BUSHCRAFT, CROSSBOWS, SPEARS, BEAST_LORE, HEALING, ANIMALISM, STAVES,
                   ELEMENTALISM, MENTALISM, BARTERING, RIDING, SWIMMING, SEAMANSHIP)
from dice import pick_n_unique


class Bard:
    name = 'Bard'
    suggested_names = ['Kvädare', 'Skaldekraft', 'Silverstämma', 'Gyllenklav', 'Honungstunga', 'Rimsmidare']
    preferred_attribute = CHARISMA
    skills = [BLUFFING, LANGUAGES, ACROBATICS, KNIVES, MYTHS_AND_LEGENDS, EVADE, PERFORMANCE, PERSUASION]


class Craftsman:
    name = 'Hantverkare'
    suggested_names = ['Stenhammare', 'Timmerklyve', 'Kraftnäve', 'Tunnmakare', 'Brovälvare', 'Järnmästare']
    preferred_attribute = STRENGTH
    skills = [SLEIGHT_OF_HAND, SPOT_HIDDEN, HAMMERS, CRAFTING, KNIVES, BRAWLING, SWORDS, AXES]


class Hunter:
    name = 'Jägare'
    suggested_names = ['Skogsräv', 'Ulvbane', 'Stigfinnare', 'Vindfarne', 'Blodshunger', 'Skuggpil']
    preferred_attribute = AGILITY
    skills = [ACROBATICS, HUNTING_AND_FISHING, KNIVES, BOWS, SLINGS, SNEAKING, AWARENESS, BUSHCRAFT]


class Warrior:
    name = 'Krigare'
    suggested_names = ['Gravmakare', 'Grymkäft', 'Vindhugg', 'Svärdsblank', 'Orädd', 'Slaktaren']
    preferred_attribute = STRENGTH
    skills = [CROSSBOWS, HAMMERS, BOWS, BRAWLING, SPEARS, SWORDS, EVADE, AXES]


class Scholar:
    name = 'Lärd'
    suggested_names = ['Boksynte', 'Allomklok', 'Vidblicke', 'Tankeklar', 'Dammlunga', 'Den lärde och välgödde']
    preferred_attribute = INTELLIGENCE
    skills = [BEAST_LORE, SPOT_HIDDEN, LANGUAGES, HEALING, MYTHS_AND_LEGENDS, EVADE, AWARENESS, BUSHCRAFT]


class MageSchool(Enum):
    Animist = auto()
    Elementalist = auto()
    Mentalist = auto()


class Mage:
    name = 'Magiker'
    suggested_names = ['Rothjärta', 'Krokrygg', 'Gråkåpa', 'Vindhand', 'Stavhalte', 'Skuggmanare']
    preferred_attribute = WILL
    school = None

    @property
    def skills(self):
        if self.school is MageSchool.Animist:
            return [ANIMALISM, BEAST_LORE, HUNTING_AND_FISHING, HEALING, SNEAKING, STAVES, EVADE, BUSHCRAFT]
        elif self.school is MageSchool.Elementalist:
            return [ELEMENTALISM, SPOT_HIDDEN, LANGUAGES, HEALING, MYTHS_AND_LEGENDS, STAVES, EVADE, AWARENESS]
        elif self.school is MageSchool.Mentalist:
            return [MENTALISM, LANGUAGES, ACROBATICS, HEALING, MYTHS_AND_LEGENDS, BRAWLING, EVADE, AWARENESS]
        else:
            self.school = choice([*MageSchool])
            return self.skills


class Peddler:
    name = 'Nasare'
    suggested_names = ['Silversnike', 'Guldtand', 'Silkestunga', 'Den läspe och ärlige', 'Isterbuk', 'Lockenpock']
    preferred_attribute = CHARISMA
    skills = [BLUFFING, SLEIGHT_OF_HAND, SPOT_HIDDEN, KNIVES, BARTERING, EVADE, AWARENESS, PERSUASION]


class Knight:
    name = 'Riddare'
    suggested_names = ['Drakhjärta', 'Gyllenlans', 'Gripenklo', 'Ädelsinne', 'Blankenhjelm', 'Sorgmantel']
    preferred_attribute = STRENGTH
    skills = [BEAST_LORE, HAMMERS, MYTHS_AND_LEGENDS, RIDING, SPEARS, SWORDS, PERFORMANCE, PERSUASION]


class Sailor:
    name = 'Sjöfarare'
    suggested_names = ['Sjöskum', 'Vågryttare', 'Skumfarne', 'Saltstänke', 'Sjöbjörn', 'Havsstorm']
    preferred_attribute = AGILITY
    skills = [LANGUAGES, ACROBATICS, HUNTING_AND_FISHING, KNIVES, SWIMMING, SEAMANSHIP, SWORDS, SPOT_HIDDEN]


class Thief:
    name = 'Tjuv'
    suggested_names = ['Halvfinger', 'Svartråtta', 'Rödöga', 'Kvickfot', 'Dubbeltunga', 'Dolkenstöt']
    preferred_attribute = AGILITY
    skills = [BLUFFING, KNIVES, SLEIGHT_OF_HAND, SPOT_HIDDEN, ACROBATICS, SNEAKING, EVADE, AWARENESS]


available_classes = [Bard, Craftsman, Hunter, Warrior, Scholar, Mage, Peddler, Knight, Sailor, Thief]


def roll_class():
    return choice(available_classes)()


def roll_surname(clazz):
    return choice(clazz.suggested_names)


def roll_clazz_skills(clazz, number_of_skills):
    return pick_n_unique(clazz.skills, number_of_skills)
