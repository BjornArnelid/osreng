class CharacterSheet:
    def __init__(self):
        self.race = None
        self.clazz = None

    def __str__(self):
        character_string = "CHARACTER"
        if self.race:
            character_string += "\nRace: " + str(self.race.name)
        if self.clazz:
            character_string += "\nClass: " + str(self.clazz.name)
        return character_string
