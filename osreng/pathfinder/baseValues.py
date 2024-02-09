import enum


class AbilityScore(enum.Enum):
    Strength = enum.auto()
    Dexterity = enum.auto()
    Constitution = enum.auto()
    Intelligence = enum.auto()
    Wisdom = enum.auto()
    Charisma = enum.auto()

    def __str__(self):
        return self.name


class Field(enum.Enum):
    HitPoints = enum.auto()
    Languages = enum.auto()
    Reactions = enum.auto()
    SavingThrows = enum.auto()
    Size = enum.auto()
    Speed = enum.auto()
    Traits = enum.auto()
    Abilities = enum.auto()


class HitPoints(enum.Enum):
    MaxHitPoints = enum.auto()


class Movement(enum.Enum):
    Speed = enum.auto()


class Perception(enum.Enum):
    Senses = enum.auto()


class Reaction:
    def __init__(self, name):
        self.name = name


class Senses(enum.Enum):
    DarkVision = enum.auto()
    LowLightVision = enum.auto()
    KeenEyes = enum.auto()
    ImpreciseScent = enum.auto()
    Normal = enum.auto()


class SheetModifications:
    def __init__(self, name, modifications):
        self.name = name
        self.modifications = modifications


class StaticModification:
    def __init__(self, attribute, value=True):
        self.attribute = attribute
        self.value = value

    def __str__(self):
        return "{}".format(self.attribute)


class CharacterChoice:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices
