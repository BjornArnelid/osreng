from enum import Enum, auto
from dice import d6


class Age(Enum):
    Young = auto()
    MiddleAged = auto()
    Old = auto()


def roll_age():
    dice_roll = d6()
    if dice_roll <= 3:
        return Age.Young
    elif dice_roll <= 5:
        return Age.MiddleAged
    elif dice_roll == 6:
        return Age.Old


def print_age(age):
    if age == Age.Young:
        return "Ung"
    elif age == Age.MiddleAged:
        return "Medelålders"
    else:
        return "Gammal"
