from pathfinder.attribute import Attribute


class PathfinderSheet:
    def __init__(self):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        self.ancestry = None
        self.languages = []
        self.hit_points = 0

    @property
    def size(self):
        return self.ancestry.size

    @property
    def speed(self):
        return self.ancestry.speed

    def set_ancestry(self, ancestry):
        self.ancestry = ancestry
        self.languages += ancestry.main_languages
        self.hit_points = ancestry.hit_points

    def get_attribute(self, attribute):
        if attribute == Attribute.Strength:
            return self.strength
        elif attribute == Attribute.Constitution:
            return self.constitution
        elif attribute == Attribute.Dexterity:
            return self.dexterity
        elif attribute == Attribute.Intelligence:
            return self.intelligence
        elif attribute == Attribute.Wisdom:
            return self.wisdom
        elif attribute == Attribute.Charisma:
            return self.charisma
        else:
            raise CharacterError("Unknown attribute {}".format(attribute))

    def set_attribute(self, attribute, value):
        if not int(value) == value:
            raise CharacterError("Value {} must be an integer".format(value))
        if attribute == Attribute.Strength:
            self.strength = value
        elif attribute == Attribute.Constitution:
            self.constitution = value
        elif attribute == Attribute.Dexterity:
            self.dexterity = value
        elif attribute == Attribute.Intelligence:
            self.intelligence = value
        elif attribute == Attribute.Wisdom:
            self.wisdom = value
        elif attribute == Attribute.Charisma:
            self.charisma = value
        else:
            raise CharacterError("Unknown attribute {}".format(attribute))

    def boost_attribute(self, attribute):
        self.set_attribute(attribute, self.get_attribute(attribute) + 2)

    def reduce_attribute(self, attribute):
        self.set_attribute(attribute, self.get_attribute(attribute) - 2)

    def __str__(self):
        character_string = "CHARACTER"
        # if self.name:
        #     character_string += "\nNamn: " + str(self.name)

        if self.ancestry:
            character_string += "\nAncestry: " + self.ancestry.name

        # if self.clazz:
        #    character_string += "\nYrke: " + self.clazz.name

        # if self.age:
        #     character_string += "\nÅlder: " + self.age.name

        character_string += "\nAttributes"
        character_string += "\nSTR: {}, CON: {}, DEX: {}, INT: {}, WIS: {}, CHA: {}, ".format(
                self.strength, self.constitution, self.dexterity, self.intelligence, self.wisdom, self.charisma)
        character_string += "\nSpeed: {}".format(self.speed)

        return character_string


class CharacterError(Exception):
    pass
