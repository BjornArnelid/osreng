import enum

from pathfinder.attribute import Attribute, Any


class Size(enum.Enum):
    Medium = enum.auto()
    Small = enum.auto()


class Language(enum.Enum):
    Common = enum.auto()
    Dwarven = enum.auto()
    Elven = enum.auto()
    Gnomish = enum.auto()
    Sylvan = enum.auto()
    Goblin = enum.auto()
    Halfling = enum.auto()


class Ancestry:
    def __init__(self, name, size, speed, main_languages, hit_points, ability_boosts, ability_flaws):
        self.name = name
        self.size = size
        self.speed = speed
        self.main_languages = main_languages
        self.hit_points = hit_points
        self.ability_boosts = ability_boosts
        self.ability_flaws = ability_flaws


Dwarf = Ancestry("Dwarf", Size.Medium, 20, [Language.Common, Language.Dwarven], 10,
                 [Attribute.Constitution, Attribute.Wisdom, Any()], [Attribute.Charisma])

Elf = Ancestry("Elf", Size.Medium, 30, [Language.Common, Language.Elven], 6,
               [Attribute.Dexterity, Attribute.Intelligence, Any()],  [Attribute.Constitution])

Gnome = Ancestry("Gnome", Size.Small, 25,
                 [Language.Common, Language.Gnomish, Language.Sylvan],
                 8, [Attribute.Constitution, Attribute.Charisma, Any()],
                 [Attribute.Strength])

Goblin = Ancestry("Goblin", Size.Small, 25, [Language.Common, Language.Goblin], 6,
                  [Attribute.Dexterity, Attribute.Charisma, Any()], [Attribute.Wisdom])

Halfling = Ancestry("Halfling", Size.Small, 25, [Language.Common, Language.Halfling],
                   6, [Attribute.Dexterity, Attribute.Wisdom, Any()], [Attribute.Strength])

Human = Ancestry("Human", Size.Medium, 25, [Language.Common], 8,
                 [Any(), Any()], [])


core_ancestries = [Dwarf, Elf, Gnome, Goblin, Halfling, Human]

advanced_ancestries = []  # Catfolk, Cobold, Orc, Ratfolk, Tengu, Changeling, Dhampir, Planar scion

omen_ancestries = []  # Android, Aphorite, Beastkin, Fetchling, Fleshwarp, Ganzi, Geniekin, Kitsune, Sprite, Strix

omen2_ancestries = []  # Hobgoblins, Leshies, Lizardfolk,

available_ancestries = core_ancestries + advanced_ancestries + omen_ancestries + omen2_ancestries
