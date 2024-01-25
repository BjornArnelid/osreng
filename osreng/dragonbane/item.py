from enum import Enum, auto

from dragonbane.attribute import STRENGTH
from dice import d6, d8, d10, d12, to_die_string
from dragonbane.skill import (KNIVES, SWORDS, AXES, HAMMERS, STAVES, SPEARS, SLINGS, BOWS, CROSSBOWS, PERFORMANCE,
                              SLEIGHT_OF_HAND, BUSHCRAFT, ACROBATICS, CRAFTING, HEALING, HUNTING_AND_FISHING, RIDING)


class ItemAttribute(Enum):
    AGILE = auto()
    PIERCING = auto()
    CUTTING = auto()
    THROWABLE = auto()
    CRUSHING = auto()
    TRIPPING = auto()
    DEMANDS_QUIVER = auto()
    TINY = auto()
    NO_BONUS_DAMAGE = auto()
    LONG = auto()
    DEMANDS_MOUNT = auto()


class Armor(object):
    def __init__(self, name, protection):
        self.name = name
        self.protection = protection
        self.required_skill = None


class Weapon(object):
    def __init__(self, name, number_of_hands, requirement, item_range, damage, durability, attributes,
                 required_skill=None):
        self.number_of_hands = number_of_hands
        self.name = name
        self.requirement = requirement
        self.item_range = item_range
        self.damage = damage
        self.durability = durability
        self.attributes = attributes
        self.required_skill = required_skill

    def __str__(self):
        weapon_string = self.name + " "
        if callable(self.damage):
            weapon_string += "1" + to_die_string(self.damage)
        else:
            weapon_string += str(self.damage[1]) + to_die_string(self.damage[0])

        return weapon_string


class Item(object):
    def __init__(self, name, weight, required_skill=None):
        self.name = name
        self.weight = weight
        self.required_skill = required_skill
        self.amount = 1

    def __str__(self):
        return self.name


class MultiItem(object):
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return str(self.item) + " : " + str(self.amount)

    @property
    def required_skill(self):
        return self.item.required_skill


# Armors
LEATHER_ARMOR = Armor('Läder', 1)

STUDDED_LEATHER_ARMOR = Armor('Nitläder', 2)

CHAINMAIL_ARMOR = Armor('Ringbrynja', 4)

PLATE_ARMOR = Armor('Plåtrustning', 6)

OPEN_HELMET = Armor('Öppen hjälm', 1)

GREAT_HELMET = Armor('Tunnhjälm', 2)

# Melee weapons
KNIFE = Weapon('Kniv', 1, 0, STRENGTH, d8, 6,
               [ItemAttribute.AGILE, ItemAttribute.PIERCING, ItemAttribute.THROWABLE], KNIVES)

DAGGER = Weapon('Dolk', 1, 0, STRENGTH, d8, 9,
                [ItemAttribute.AGILE, ItemAttribute.PIERCING, ItemAttribute.CUTTING, ItemAttribute.THROWABLE],
                KNIVES)

SHORT_SWORD = Weapon('Kortsvärd', 1, 7, 2, d10, 12,
                     [ItemAttribute.PIERCING, ItemAttribute.CUTTING], SWORDS)

BROAD_SWORD = Weapon('Bredsvärd', 1, 10, 2, (d6, 2), 15,
                     [ItemAttribute.PIERCING, ItemAttribute.CUTTING], SWORDS)

SCIMITAR = Weapon('Kroksabel', 1, 10, 2, (d6, 2), 12,
                  [ItemAttribute.TRIPPING, ItemAttribute.CUTTING], SWORDS)

HAND_AXE = Weapon('Handyxa', 1, 7, STRENGTH, (d6, 2), 9,
                  [ItemAttribute.TRIPPING, ItemAttribute.CUTTING, ItemAttribute.THROWABLE], AXES)

BATTLE_AXE = Weapon('Stridsyxa', 1, 13, 2, (d8, 2), 9,
                    [ItemAttribute.TRIPPING, ItemAttribute.CUTTING], AXES)

MORNING_STAR = Weapon('Morgonstjärna', 1, 13, 2, (d8, 2), 9,
                      [ItemAttribute.CRUSHING], HAMMERS)

FLAIL = Weapon('Stridsgissel', 1, 13, 2, (d8, 2), None,
               [ItemAttribute.CRUSHING, ItemAttribute.TRIPPING], HAMMERS)

WAR_HAMMER_LIGHT = Weapon('Stridshammare (lätt)', 1, 10, 2, (d6, 2),
                          12, [ItemAttribute.CRUSHING, ItemAttribute.TRIPPING], HAMMERS)

WOODEN_STAFF = Weapon('Trästav', 2, 7, 2, d8, 9,
                      [ItemAttribute.CRUSHING, ItemAttribute.TRIPPING], STAVES)

SHORT_SPEAR = Weapon('Kortspjut', 1, 7, (STRENGTH, 2), d10, 9,
                     [ItemAttribute.PIERCING, ItemAttribute.THROWABLE], SPEARS)

LONG_SPEAR = Weapon('Långspjut', 2, 10, 4, (d8, 2), 9,
                    [ItemAttribute.LONG, ItemAttribute.PIERCING], SPEARS)

LANCE = Weapon('Lans', 1, 13, 4, (d10, 2), 12,
               [ItemAttribute.LONG, ItemAttribute.PIERCING, ItemAttribute.DEMANDS_MOUNT], SPEARS)

TRIDENT = Weapon('Treudd', 1, 10, STRENGTH, (d6, 2), 9,
                 [ItemAttribute.TRIPPING, ItemAttribute.PIERCING, ItemAttribute.THROWABLE], SPEARS)

SMALL_SHIELD = Weapon('Liten sköld', 1, 7, 2, d8, 15,
                      [ItemAttribute.CRUSHING])

# Range weapons

SLING = Weapon('Slunga', 1, 0, 20, d8, None,
               [ItemAttribute.CRUSHING, ItemAttribute.TINY], SLINGS)

SHORT_BOW = Weapon('Kortbåge', 2, 7, 30, d10, 3,
                   [ItemAttribute.PIERCING, ItemAttribute.DEMANDS_QUIVER], BOWS)

LONG_BOW = Weapon('Långbåge', 2, 13, 100, d12, 6,
                  [ItemAttribute.PIERCING, ItemAttribute.DEMANDS_QUIVER], BOWS)

LIGHT_CROSSBOW = Weapon('Lätt armborst', 2, 7, 40, (d6, 2), 6,
                        [ItemAttribute.PIERCING, ItemAttribute.DEMANDS_QUIVER, ItemAttribute.NO_BONUS_DAMAGE],
                        CROSSBOWS)

# Coins
SILVER_COIN = Item('Silvermynt', 0.01)

# Instruments
BRASS_HORN = Item('Blåshorn', 1, PERFORMANCE)

FLUTE = Item('Flöjt', 1, PERFORMANCE)

LYRE = Item('Lyra', 1, PERFORMANCE)

# General items
SIMPLE_LOCKPICKS = Item('Dyrkar, enkla', 1, SLEIGHT_OF_HAND)

FIELD_KITCHEN = Item('Fältkök', 2, BUSHCRAFT)

FOOD = Item('Ransoner mat', 0.25)

QUIVER = Item('Koger', 1)

BINOCULARS = Item('Kikare', 1, BUSHCRAFT)

ROPE = Item('Rep', 1, ACROBATICS)

SLEEPING_TRAP = Item('Sovfäll', 1, BUSHCRAFT)

PEBBLES = Item('Stenkulor', 1)

LARGE_TENT = Item('Stort tält', 4, BUSHCRAFT)

GRAPPLING_HOOK = Item('Änterhake', 1, ACROBATICS)

# Magic accessories
AMULET = Item('Amulett', 0)

NOTEBOOK = Item('Anteckningsbok', 1)

BOOK = Item('Bok', 1)

QUILL_PEN = Item('Fjäderpenna', 1)

SPELL_BOOK = Item('Formelbok', 1)

CRYSTAL_BALL = Item('Spåkula', 1)

WAND = Item('Trollspö', 1)

# Light sources
TINDER_BOX = Item('Elddon', 0)

TORCH = Item('Fackla', 1)

LAMP_OIL = Item('Lampolja', 1)

OIL_LAMP = Item('Oljelampa', 1)

STORM_LANTERN = Item('Stormlykta', 1)

# Tools
FORGING_TOOLS = Item('Smidesverktyg', 1, CRAFTING)

CARPENTRY_TOOLS = Item('Snickarverktyg', 1, CRAFTING)

LEATHER_TOOLS = Item('Läderverktyg', 1, CRAFTING)

# Storage
BACKPACK = Item('Ryggsäck', -2)

# Medical supplies
SLEEPING_POTION = Item('Sövande gift', 1)

DRESSING = Item('Förband', 0.1, HEALING)

# Hunting and fishing
FISHING_ROD = Item('Fiskespö', 1, HUNTING_AND_FISHING)

SNARE = Item('Snara', 1, HUNTING_AND_FISHING)

# Transportation
CART = Item('Kärra', -50)

# Animals
WAR_HORSE = Item('Stridstränad häst', -10, RIDING)

DONKEY = Item('Åsna', -10)


def get_desired_skills(items):
    skills = []
    for item in items:
        if not isinstance(item, tuple) and item.required_skill:
            skills.append(item.required_skill)
    return skills


def calculate_item_amounts(items):
    converted_items = []
    for item in items:
        if isinstance(item, tuple):
            if isinstance(item[0], int):
                converted_items.append(MultiItem(item[1], item[0]))
            elif callable(item[0]):
                converted_items.append(MultiItem(item[1], item[0]()))
        else:
            converted_items.append(item)
    return converted_items
