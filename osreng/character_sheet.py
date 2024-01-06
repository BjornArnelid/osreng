from race import available_races
from clazz import available_classes
from age import Age, print_age


class CharacterSheet:
    def __init__(self):
        self._race = None
        self._clazz = None
        self._age = None
        self.name = None

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if any(isinstance(race, cls) for cls in available_races):
            self._race = race
        else:
            raise CharacterError("{} is not an acceptable race".format(race))

    @property
    def clazz(self):
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        if any(isinstance(clazz, cls) for cls in available_classes):
            self._clazz = clazz
        else:
            raise CharacterError("{} is not an acceptable class".format(clazz))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age in [*Age]:
            self._age = age
        else:
            raise CharacterError("{} is not an acceptable age".format(age))

    def __str__(self):
        character_string = "KARAKTÄR"
        if self.name:
            character_string += "\nNamn: " + str(self.name)
        if self.race:
            character_string += "\nSläkte: " + self.race.name
        if self.clazz:
            character_string += "\nYrke: " + self.clazz.name
        if self.age:
            character_string += "\nÅlder: " + print_age(self.age)
        return character_string


class CharacterError(Exception):
    pass
