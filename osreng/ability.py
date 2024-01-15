from skill import (CRAFTING, PERFORMANCE, HUNTING_AND_FISHING, CROSSBOWS, HAMMERS, KNIVES, BOWS, BRAWLING, SLINGS,
                   SPEARS, STAVES, SWORDS, AXES, MYTHS_AND_LEGENDS, BARTERING, SWIMMING)


class HeroAbility:
    def __init__(self, requirement, cost, name):
        self.requirement = requirement
        self.cost = cost
        self.name = name


MUSICIAN = HeroAbility((PERFORMANCE, 12), 3, 'Tonkonst')

TANNER = HeroAbility((CRAFTING, 12), None, 'Garverimästare,')

SMITH = HeroAbility((CRAFTING, 12), None, 'Mästersmed')

CARPENTER = HeroAbility((CRAFTING, 12), None, 'Mästersnickare')

COMPANION = HeroAbility((HUNTING_AND_FISHING, 12), 3, 'Följeslagare')

COMBAT_EXPERIENCE = HeroAbility(((CROSSBOWS, HAMMERS, KNIVES, BOWS, BRAWLING, SLINGS, SPEARS, STAVES, SWORDS, AXES), 12), 3, 'Stridsvana')

INTUITION = HeroAbility((MYTHS_AND_LEGENDS, 12), 3, 'Intuition')

TREASURE_HUNTER = HeroAbility((BARTERING, 12), 3, 'Skattletare')

CHAMPION = HeroAbility(((HAMMERS, SWORDS, AXES), 12), 2, 'Förkämpe')

SEA_LEGS = HeroAbility((SWIMMING, 12), 1, 'Sjöben')

BACKSTAB = HeroAbility((KNIVES, 12), 3, 'Tjuvhugg')
