from race import available_races
from clazz import available_classes
from age import Age, print_age
from attribute import STRENGTH, CONSTITUTION, DEXTERITY, INTELLIGENCE, WILL, CHARISMA, attribute_names, calculate_movement_modifier, calculate_bonus_damage
from dice import to_die_string


class CharacterSheet:
    def __init__(self):
        self._race = None
        self._clazz = None
        self._age = None
        self.name = None
        self._attributes = []
        self._hitpoints = None
        self._mana = None

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

    def _get_attribute(self, attribute):
        adjustment = self.age.adjust_for_age(attribute) if self.age else 0
        return self._attributes[attribute] + adjustment

    def _set_attribute(self, attribute, value):
        if int(value) == value:
            if not self._attributes:
                self._attributes = [None] * 6
            self._attributes[attribute] = value
        else:
            raise CharacterError("{} is not an acceptable attribute for {}".format(value, attribute))

    @property
    def strength(self):
        return self._get_attribute(STRENGTH)

    @strength.setter
    def strength(self, value):
        self._set_attribute(STRENGTH, value)

    @property
    def constitution(self):
        return self._get_attribute(CONSTITUTION)

    @constitution.setter
    def constitution(self, value):
        self._set_attribute(CONSTITUTION, value)
        self._hitpoints = [self.constitution, self.constitution]

    @property
    def dexterity(self):
        return self._get_attribute(DEXTERITY)

    @dexterity.setter
    def dexterity(self, value):
        self._set_attribute(DEXTERITY, value)

    @property
    def intelligence(self):
        return self._get_attribute(INTELLIGENCE)

    @intelligence.setter
    def intelligence(self, value):
        self._set_attribute(INTELLIGENCE, value)

    @property
    def will(self):
        return self._get_attribute(WILL)

    @will.setter
    def will(self, value):
        self._set_attribute(WILL, value)
        self._mana = [self.will, self.will]

    @property
    def charisma(self):
        return self._get_attribute(CHARISMA)

    @charisma.setter
    def charisma(self, value):
        self._set_attribute(CHARISMA, value)

    @property
    def movement_speed(self):
        return self.race.base_speed + calculate_movement_modifier(self.dexterity)

    @property
    def hitpoints(self):
        return self._hitpoints

    def modify_hitpoints(self, new_value):
        if self._hitpoints[0] + new_value > self._hitpoints[1]:
            self._hitpoints[0] = self._hitpoints[1]
        else:
            self._hitpoints[0] += new_value

    @property
    def mana(self):
        return self._mana

    def modify_mana(self, new_value):
        if self._mana[0] + new_value > self._mana[1]:
            self._mana[0] = self._mana[1]
        else:
            self._mana[0] += new_value

    def calculate_bonus_damage(self, damage_attribute):
        return calculate_bonus_damage(self._get_attribute(damage_attribute))

    def switch_attributes(self, first, second):
        first_value = self._get_attribute(first)
        self._set_attribute(first, self._get_attribute(second))
        self._set_attribute(second, first_value)

    def shift_max_to_preferred_attribute(self):
        if not self.clazz:
            raise CharacterError("Cannot switch to preferred attribute without selected class")
        preferred_id = self.clazz.preferred_attribute

        max_index = self._attributes.index(max(self._attributes))
        self.switch_attributes(preferred_id, max_index)

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

        if self._attributes:
            character_string += "\n\nGrundegenskaper\n"
            for attribute_index in range(6):
                character_string += "{}: {}, ".format(attribute_names[attribute_index], self._get_attribute(attribute_index))
            character_string += "\nFörflyttning: {}".format(self.movement_speed)
            character_string += "\nSkadebonus styrka: {}, Skadebonus smidighet: {}".format(to_die_string(self.calculate_bonus_damage(STRENGTH)), to_die_string(self.calculate_bonus_damage(DEXTERITY)))
            character_string += "\nKroppspoäng: {}, Viljepoäng: {}".format(self.hitpoints, self.mana)

        return character_string


class CharacterError(Exception):
    pass
