from enum import Enum, auto


class MageSchool(Enum):
    Animist = auto()
    Elementalist = auto()
    Mentalist = auto()


class Props(Enum):
    Gesture = auto()
    IngredientDrawing = auto()


class Cantrip(object):
    def __init__(self, name, school):
        self.name = name
        self.school = school


class Spell(object):
    def __init__(self, name, level, school):
        self.name = name
        self.level = level
        self.school = school


# General
FETCH = Cantrip('Hämta', None)

FLICK = Cantrip('Knäpp', None)

DETECT_MAGIC = Cantrip('Känna magi', None)

MEND_CLOTHES = Cantrip('Laga kläder', None)

LIGHT = Cantrip('Ljus', None)

OPEN_AND_CLOSE = Cantrip('Öppna/Stänga', None)

PROTECTOR = Spell('Beskyddare', 1, None)

DISPEL = Spell('Skingra', 1, None)


# Animist
FLOWER_TRAIL = Cantrip('Blomsterspår', MageSchool.Animist)

HAIR_STYLE = Cantrip('Frisyr', MageSchool.Animist)

BIRD_SONG = Cantrip('Fågelsång', MageSchool.Animist)

COOK = Cantrip('Laga mat', MageSchool.Animist)

CLEAN = Cantrip('Städa', MageSchool.Animist)

EVICT = Spell('Fördriva', 1, MageSchool.Animist)

LIGHTNING = Spell('Ljungeld', 1, MageSchool.Animist)

HEAL = Spell('Läka', 1, MageSchool.Animist)

ENSNARE = Spell('Snärja', 1, MageSchool.Animist)

SPEAK_WITH_ANIMALS = Spell('Tala med djur', 1, MageSchool.Animist)


# Elementalist
PUFF_OF_SMOKE = Cantrip('Rökpuff', MageSchool.Elementalist)

IGNITE = Cantrip('Tända', MageSchool.Elementalist)

HEAT_AND_COOL = Cantrip('Värma/Kyla', MageSchool.Elementalist)

FLAME = Spell('Flamma', 1, MageSchool.Elementalist)

FROST = Spell('Frost', 1, MageSchool.Elementalist)

PILLAR = Spell('Pelare', 1, MageSchool.Elementalist)

SPLINTER = Spell('Splittra', 1, MageSchool.Elementalist)

GUST = Spell('Vinpuff', 1, MageSchool.Elementalist)


#Mentalism
BREAK_FALL = Cantrip('Bromsa fall', MageSchool.Mentalist)

LOCK_AND_UNLOCK = Cantrip('Låsa/Låsa upp', MageSchool.Mentalist)

MAGIC_STOOL = Cantrip('Magisk pall', MageSchool.Mentalist)

FAR_SIGHT = Spell('Fjärrsyn', 1, MageSchool.Mentalist)

POWER_FIST = Spell('Kraftnäve', 1, MageSchool.Mentalist)

LIFT = Spell('Lyft', 1, MageSchool.Mentalist)

LONG_STRIDER = Spell('Långstige', 1, MageSchool.Mentalist)

STONE_SKIN = Spell('Stenhud', 1, MageSchool.Mentalist)


general_cantrips = [FETCH, FLICK, DETECT_MAGIC, MEND_CLOTHES, LIGHT, OPEN_AND_CLOSE]

general_spells = [PROTECTOR, DISPEL]

animist_cantrips = [FLOWER_TRAIL, HAIR_STYLE, BIRD_SONG, COOK, CLEAN]

animist_spells = [EVICT, LIGHTNING, HEAL, ENSNARE, SPEAK_WITH_ANIMALS]

elementalist_cantrips = [PUFF_OF_SMOKE, IGNITE, HEAT_AND_COOL]

elementalist_spells = [FLAME, FROST, PILLAR, SPLINTER, GUST]

mentalist_cantrips = [BREAK_FALL, LOCK_AND_UNLOCK, MAGIC_STOOL]

mentalist_spells = [FAR_SIGHT, POWER_FIST, LIFT, LONG_STRIDER, STONE_SKIN]


def get_starting_cantrips(school):
    if school is MageSchool.Animist:
        return general_cantrips + animist_cantrips
    elif school is MageSchool.Elementalist:
        return general_cantrips + elementalist_cantrips
    else:
        return general_cantrips + mentalist_cantrips


def get_starting_spells(school):
    if school is MageSchool.Animist:
        return general_spells + animist_spells
    elif school is MageSchool.Elementalist:
        return general_spells + elementalist_spells
    else:
        return general_spells + mentalist_spells
