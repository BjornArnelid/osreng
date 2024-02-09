from pathfinder.baseValues import Attribute, Any


class Background:
    def __init__(self, name, ability_boosts):
        self.name = name
        self.ability_boosts = ability_boosts


Acolyte = Background("Acolyte", [(Attribute.Intelligence, Attribute.Wisdom), Any])

Acrobat = Background("Acrobat", [(Attribute.Strength, Attribute.Dexterity), Any])

AnimalWhisperer = Background("Animal whisperer", ([Attribute.Wisdom, Attribute.Charisma], Any))

Artisian = Background("Artisian", [(Attribute.Strength, Attribute.Intelligence), Any])

Artist = Background("Artist", [(Attribute.Dexterity, Attribute.Charisma), Any])

Barkeep = Background("Barkeep", [(Attribute.Constitution, Attribute.Charisma), Any])

Barrister = Background("Barrister", [(Attribute.Intelligence, Attribute.Charisma), Any])

BountyHunter = Background("Bounty hunter", [(Attribute.Strength, Attribute.Wisdom), Any])


