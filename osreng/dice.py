import random


class Random(object):
    name = "Slumpmässigt"

    def roll(self):
        raise "Not implemented!"


class RandomFunction(Random):
    def __init__(self, roll_function, function_input=None):
        self.roll_function = roll_function
        self.function_input = function_input

    def roll(self):
        if self.function_input:
            return self.roll_function(self.function_input)
        else:
            return self.roll_function()


class RandomList(Random):
    def __init__(self, roll_list):
        self.roll_list = roll_list

    def roll(self):
        return random.choice(self.roll_list)


class RandomSpecific(Random):
    def __init__(self, specific_input):
        self.specific_input = specific_input

    def roll(self):
        return self.specific_input


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
