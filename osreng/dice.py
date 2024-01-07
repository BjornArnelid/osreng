import random


def d12():
    return random.randint(1, 12)


def d10():
    return random.randint(1, 10)


def d6():
    return random.randint(1, 6)


def roll_attribute():
    dies = [d6() for _ in range(4)]
    dies.remove(min(dies))
    return sum(dies)
