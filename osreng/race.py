from random import choice
from dice import d12


class Trait:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name


class Human:
    name = "Människa"
    traits = [Trait(3, "Anpasslig")]
    suggested_names = ['Joruna', 'Tym', 'Halvelda', 'Garmander', 'Verolun',  'Lothar']
    base_speed = 10


class Halfling:
    name = "Halvling"
    traits = [Trait(3, "Svårfångad")]
    suggested_names = ['Kvicke', 'Brine', 'Kott', 'Humle', 'Perrywick', 'Theolina']
    base_speed = 8


class Dwarf:
    name = "Dvärg"
    traits = [Trait(3, " Långsint")]
    suggested_names = ['Fnöskberga', 'Halwyld', 'Tymolana', 'Traut', 'Urd', 'Fermer']
    base_speed = 8


class Elf:
    name = 'Alv'
    traits = [Trait(3, "Inre frid")]
    suggested_names = ['Arasin', 'Illyriana', 'Galvander', 'Tyrindelia', 'Erwilnor', 'Andremone']
    base_speed = 10


class Duck:
    name = 'Anka'
    traits = [Trait(3, " Vresig"), Trait(0, " Simfötter")]
    suggested_names = ['Kvucksum', 'Splatts', 'Mogge', 'Groddy', 'Blisandina', 'Svulmhugg']
    base_speed = 8


class Wolf:
    name = 'Varg'
    traits = [Trait(3, "Jaktsinne")]
    suggested_names = ['Wyld', 'Vargskugga', 'Lunariem', 'Obdurian', 'Frostbite', 'Wuldenhall']
    base_speed = 12


available_races = [Human, Halfling, Dwarf, Elf, Duck, Wolf]


def roll_race():
    dice_roll = d12()
    if dice_roll <= 4:
        return Human()

    if dice_roll <= 7:
        return Halfling()

    if dice_roll <= 9:
        return Dwarf()

    if dice_roll == 10:
        return Elf()

    if dice_roll == 11:
        return Duck()

    if dice_roll == 12:
        return Wolf()


def roll_first_name(race):
    return choice(race.suggested_names)
