from dice import no_die, d4, d6


STRENGTH = 0
CONSTITUTION = 1
DEXTERITY = 2
INTELLIGENCE = 3
WILL = 4
CHARISMA = 5

attribute_names = ['Styrka', 'Fysik', 'Smidighet', 'Intelligens', 'Psyke', 'Karisma']


def roll_attribute():
    dies = [d6() for _ in range(4)]
    dies.remove(min(dies))
    return sum(dies)


def calculate_movement_modifier(dexterity):
    if dexterity <= 6:
        return -4
    elif dexterity <= 9:
        return -2
    elif dexterity <= 12:
        return 0
    elif dexterity <= 15:
        return 2
    else:
        # Highest possible according to dragonbane rules.
        return 4


def calculate_bonus_damage(value):
    if value <= 12:
        return no_die
    elif value <= 16:
        return d4
    else:
        return d6
