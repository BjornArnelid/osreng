import enum

class Attribute(enum.Enum):
    Strength = enum.auto()
    Dexterity = enum.auto()
    Constitution = enum.auto()
    Intelligence = enum.auto()
    Wisdom = enum.auto()
    Charisma = enum.auto()

    def __str__(self):
        return self.name


class Any:
    def __str__(self):
        return "Free"
