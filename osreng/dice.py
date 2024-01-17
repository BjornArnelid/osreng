import random


def d12():
    return random.randint(1, 12)


def d10():
    return random.randint(1, 10)


def d8():
    return random.randint(1, 8)


def d6():
    return random.randint(1, 6)


def d4():
    return random.randint(1, 4)


def no_die():
    return 0


def pick_n_unique(original_list, number_of_picks):
    options_left = original_list.copy()
    picked = []
    for _ in range(number_of_picks):
        picked.append(options_left.pop(random.randint(0, len(options_left) - 1)))
    return picked


def to_die_string(die_function):
    if die_function == no_die:
        return "----"
    elif die_function == d4:
        return "T4"
    elif die_function == d6:
        return "T6"
    elif die_function == d8:
        return "T8"
    elif die_function == d10:
        return "T10"
    elif die_function == d12:
        return "T12"

