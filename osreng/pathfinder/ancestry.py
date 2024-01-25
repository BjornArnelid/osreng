import enum


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


class Dwarf:
    name = "Dwarf"
    size = Size.Medium
    speed = 20
    languages = [Language.Common, Language.Dwarven]
    hit_points = 10


class Elf:
    name = "Elf"
    size = Size.Medium
    speed = 30
    languages = [Language.Common, Language.Elven]
    hit_points = 6


class Gnome:
    name = "Gnome"
    size = Size.Small
    speed = 25
    languages = [Language.Common, Language.Gnomish, Language.Sylvan]
    hit_points = 8


class Goblin:
    name = "Goblin"
    size = Size.Small
    speed = 25
    languages = [Language.Common, Language.Goblin]
    hit_points = 6


class Halfling:
    name = "Halfling"
    size = Size.Small
    speed = 25
    languages = [Language.Common, Language.Halfling]
    hit_points = 6


class Human:
    name = "Human"
    size = Size.Medium
    speed = 25
    languages = [Language.Common]
    hit_points = 8


available_ancestries = [Dwarf, Elf, Gnome, Goblin, Halfling, Human]
