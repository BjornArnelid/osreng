import random


def d12():
    return random.randint(1, 12)


def d10():
    return random.randint(1, 10)


def d6():
    return random.randint(1, 6)


def d4():
    return random.randint(1, 4)


def no_die():
    return 0

def to_die_string(die_function):
    if die_function == no_die:
        return "----"
    elif die_function == d4:
        return "+T4"
    elif die_function == d6:
        return "+T6"
