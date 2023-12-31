from enum import Enum, auto
from dice import d12


class Trait:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name


class Race(Enum):
    Human = auto()
    Halfling = auto()
    Dwarf = auto()
    Elf = auto()
    Duck = auto()
    Wolf = auto()

    @property
    def trait(self):
        if self == Race.Human:
            return [Trait(3, "Adaptable")]
        elif self == Race.Halfling:
            return [Trait(3, "Elusive")]
        elif self == Race.Dwarf:
            return [Trait(3, " Resentful")]
        elif self == Race.Elf:
            return [Trait(3, "Inner peace")]
        elif self == Race.Duck:
            return [Trait(3, " Crusty"), Trait(0, " Flippers")]
        elif self == Race.Wolf:
            return [Trait(3, "Hunt sense")]
        else:
            raise Exception("race {} not found".format(self))


def roll_race():
    dice_roll = d12()
    if dice_roll <= 4:
        return Race.Human

    if dice_roll <= 7:
        return Race.Halfling

    if dice_roll <= 9:
        return Race.Dwarf

    if dice_roll == 10:
        return Race.Elf

    if dice_roll == 11:
        return Race.Duck

    if dice_roll == 12:
        return Race.Wolf
