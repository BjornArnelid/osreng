from dice import d6
from attribute import STRENGTH, CONSTITUTION, AGILITY, INTELLIGENCE, WILL


class Young:
    name = "Ung"
    number_of_skillpoints = [6, 2]
    _increased_attributes = [AGILITY, CONSTITUTION]

    def adjust_for_age(self, attribute):
        if attribute in self._increased_attributes:
            return 1
        return 0


class MiddleAged:
    name = "Medelålders"
    number_of_skillpoints = [6, 4]

    def adjust_for_age(self, attribute):
        return 0


class Old:
    name = "Gammal"
    number_of_skillpoints = [6, 6]
    _increased_attributes = [INTELLIGENCE, WILL]
    _decreased_attributes = [STRENGTH, AGILITY, CONSTITUTION]

    def adjust_for_age(self, attribute):
        if attribute in self._increased_attributes:
            return 1
        elif attribute in self._decreased_attributes:
            return -2
        return 0


available_ages = [Young, MiddleAged, Old]


def roll_age():
    dice_roll = d6()
    if dice_roll <= 3:
        return Young()
    elif dice_roll <= 5:
        return MiddleAged()
    elif dice_roll == 6:
        return Old()
