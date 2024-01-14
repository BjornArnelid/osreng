from race import available_races
from clazz import available_classes
from age import Age, print_age
from attribute import STRENGTH, CONSTITUTION, AGILITY, INTELLIGENCE, WILL, CHARISMA, attribute_names, calculate_movement_modifier, calculate_bonus_damage, calculate_skill_base_chance
from dice import to_die_string
from skill import TrainedSkill


class CharacterSheet:
    def __init__(self):
        self._race = None
        self._clazz = None
        self._age = None
        self.name = None
        self._attributes = []
        self._hitpoints = None
        self._mana = None
        self.trained_skills = []
        self.hero_abilities = []

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
            hero_ability = clazz.hero_ability
            if hero_ability:
                self.hero_abilities.append(hero_ability)
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
            self._adjust_secondary_stats(attribute)
        else:
            raise CharacterError("{} is not an acceptable attribute for {}".format(value, attribute))

    def _adjust_secondary_stats(self, attribute):
        if attribute is CONSTITUTION:
            self._hitpoints = [self.constitution, self.constitution]
        elif attribute is WILL:
            self._mana = [self.will, self.will]

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


    @property
    def dexterity(self):
        return self._get_attribute(AGILITY)

    @dexterity.setter
    def dexterity(self, value):
        self._set_attribute(AGILITY, value)

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

    def set_trained_skills(self, skills_to_train):
        for skill in skills_to_train:
            base_chance = calculate_skill_base_chance(self._get_attribute(skill.skill_attribute))
            self.trained_skills.append(TrainedSkill(base_chance * 2,  skill))

    def get_skill_value(self, skill):
        for trained in self.trained_skills:
            if trained.skill == skill:
                return trained.skill_value

        if skill.base_skill:
            return calculate_skill_base_chance(self._get_attribute(skill.skill_attribute))
        else:
            return 0

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
            character_string += "\nSkadebonus styrka: {}, Skadebonus smidighet: {}".format(to_die_string(self.calculate_bonus_damage(STRENGTH)), to_die_string(self.calculate_bonus_damage(AGILITY)))
            character_string += "\nKroppspoäng: {}, Viljepoäng: {}".format(self.hitpoints, self.mana)

        if self.trained_skills:
            character_string += "\n\nFärdigheter\n"
            delimiter = ""
            for skill in self.trained_skills:
                character_string += delimiter + "{}: {}".format(skill.skill.name, skill.skill_value)
                if delimiter == "\t":
                    delimiter = "\n"
                else:
                    delimiter = "\t"

        if self.hero_abilities:
            character_string += "\nHjälteförmågor:"
            for ability in  self.hero_abilities:
                character_string += "\n{}".format(ability.name)
        return character_string


class CharacterError(Exception):
    pass
