from enum import Enum, auto
from dice import d6
from attribute import STRENGTH, CONSTITUTION, DEXTERITY, INTELLIGENCE, WILL, CHARISMA


class Age(Enum):
    Young = auto()
    MiddleAged = auto()
    Old = auto()

    def adjust_for_age(self, attribute):
        if self is Age.Young and (attribute == DEXTERITY or attribute == CONSTITUTION):
            return + 1
        elif self is Age.Old and (attribute == STRENGTH or attribute == DEXTERITY or attribute == CONSTITUTION):
            return -2
        elif self is Age.Old and (attribute == INTELLIGENCE or attribute == WILL):
            return +1
        else:
            return 0

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
