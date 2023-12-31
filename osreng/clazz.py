from enum import Enum, auto
from dice import d10

class Class(Enum):
    Bard = auto()
    Craftsman = auto()
    Hunter = auto()
    Warrior = auto()
    Scholar = auto()
    Mage = auto()
    Peddler = auto()
    Knight = auto()
    Sailor = auto()
    Thief = auto()


def roll_class():
    return Class(d10())
