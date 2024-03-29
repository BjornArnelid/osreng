from dragonbane.race import available_races
from dragonbane.clazz import available_classes
from dragonbane.age import available_ages
from dragonbane.attribute import (STRENGTH, CONSTITUTION, AGILITY, INTELLIGENCE, WILL, CHARISMA,
                                  calculate_movement_modifier, calculate_bonus_damage, calculate_skill_base_chance)
from dice import to_die_string
from dragonbane.skill import TrainedSkill
from dragonbane.item import Weapon, Armor, MultiItem, SILVER_COIN, calculate_item_amounts


class DragonBaneSheet(object):
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
        self.weakness = None
        self.weapons = []
        self.armor = []
        self.items = []
        self.keepsake = None
        self.looks = []

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if not race:
            return
        elif any(isinstance(race, cls) for cls in available_races):
            self._race = race
        else:
            raise CharacterError("{} is not an acceptable race".format(race))

    @property
    def clazz(self):
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        if not clazz:
            return
        elif any(isinstance(clazz, cls) for cls in available_classes):
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
        if not age:
            return
        elif any(isinstance(age, cls) for cls in available_ages):
            self._age = age
        else:
            raise CharacterError("{} is not an acceptable age".format(age))

    def get_attribute(self, attribute):
        if attribute == STRENGTH:
            return self.strength
        elif attribute == CONSTITUTION:
            return self.constitution
        elif attribute == AGILITY:
            return self.agility
        elif attribute == INTELLIGENCE:
            return self.intelligence
        elif attribute == WILL:
            return self.will
        elif attribute == CHARISMA:
            return self.charisma
        else:
            raise CharacterError("unknown attribute")

    def get_raw_attribute(self, attribute):
        return self._attributes[attribute]

    def set_attribute(self, attribute, value):
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
        adjustment = self.age.adjust_for_age(STRENGTH) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(STRENGTH) + adjustment)

    @strength.setter
    def strength(self, value):
        self.set_attribute(STRENGTH, value)

    @property
    def constitution(self):
        adjustment = self.age.adjust_for_age(CONSTITUTION) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(CONSTITUTION) + adjustment)

    @constitution.setter
    def constitution(self, value):
        self.set_attribute(CONSTITUTION, value)

    @property
    def agility(self):
        adjustment = self.age.adjust_for_age(AGILITY) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(AGILITY) + adjustment)

    @agility.setter
    def agility(self, value):
        self.set_attribute(AGILITY, value)

    @property
    def intelligence(self):
        adjustment = self.age.adjust_for_age(INTELLIGENCE) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(INTELLIGENCE) + adjustment)

    @intelligence.setter
    def intelligence(self, value):
        self.set_attribute(INTELLIGENCE, value)

    @property
    def will(self):
        adjustment = self.age.adjust_for_age(WILL) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(WILL) + adjustment)

    @will.setter
    def will(self, value):
        self.set_attribute(WILL, value)

    @property
    def charisma(self):
        adjustment = self.age.adjust_for_age(CHARISMA) if self.age else 0
        return _adjust_attribute_to_limits(self.get_raw_attribute(CHARISMA) + adjustment)

    @charisma.setter
    def charisma(self, value):
        self.set_attribute(CHARISMA, value)

    @property
    def movement_speed(self):
        return self.race.base_speed + calculate_movement_modifier(self.agility)

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

    @property
    def money(self):
        net_worth = 0
        for item in self.items:
            if isinstance(item, MultiItem):
                if item.item == SILVER_COIN:
                    net_worth += item.amount
        return net_worth

    def modify_mana(self, new_value):
        if self._mana[0] + new_value > self._mana[1]:
            self._mana[0] = self._mana[1]
        else:
            self._mana[0] += new_value

    def calculate_bonus_damage(self, damage_attribute):
        return calculate_bonus_damage(self.get_attribute(damage_attribute))

    def switch_attributes(self, first, second):
        first_value = self.get_raw_attribute(first)
        self.set_attribute(first, self.get_raw_attribute(second))
        self.set_attribute(second, first_value)

    def shift_max_to_preferred_attribute(self):
        if not self.clazz:
            raise CharacterError("Cannot switch to preferred attribute without selected class")
        preferred_id = self.clazz.preferred_attribute

        max_index = self._attributes.index(max(self._attributes))
        self.switch_attributes(preferred_id, max_index)

    def set_trained_skills(self, skills_to_train):
        for skill in skills_to_train:
            base_chance = calculate_skill_base_chance(self.get_attribute(skill.skill_attribute))
            self.trained_skills.append(TrainedSkill(base_chance * 2,  skill))

    def get_skill_value(self, skill):
        for trained in self.trained_skills:
            if trained.skill == skill:
                return trained.skill_value

        if skill.base_skill:
            return calculate_skill_base_chance(self.get_attribute(skill.skill_attribute))
        else:
            return 0

    def assign_start_items(self, starting_items):
        for item in calculate_item_amounts(starting_items):
            if isinstance(item, Weapon):
                self.weapons.append(item)
            elif isinstance(item, Armor):
                self.armor.append(item)
            else:
                self.items.append(item)

    def __str__(self):
        character_string = "KARAKTÄR"
        if self.name:
            character_string += "\nNamn: " + str(self.name)

        if self.race:
            character_string += "\nSläkte: " + self.race.name

        if self.clazz:
            character_string += "\nYrke: " + self.clazz.name

        if self.age:
            character_string += "\nÅlder: " + self.age.name

        if self._attributes:
            character_string += "\n\nGrundegenskaper"
            character_string += "\nStyrka: {}, Fysik: {}, Smidighet: {}, Intelligens: {}, Psyke: {}, Karisma: {}, ".format(
                self.strength, self.constitution, self.agility, self.intelligence, self.will, self.charisma)
            character_string += "\nFörflyttning: {}".format(self.movement_speed)
            character_string += "\nSkadebonus styrka: {}, Skadebonus smidighet: {}".format(to_die_string(self.calculate_bonus_damage(STRENGTH)), to_die_string(self.calculate_bonus_damage(AGILITY)))
            character_string += "\nKroppspoäng: [{} / {}], Viljepoäng: [{} / {}]".format(self.hitpoints[0], self.hitpoints[1],
                                                                                         self.mana[0], self.mana[1])

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
            character_string += "\n\nHjälteförmågor:\n"
            hero_ability_part = ""
            for ability in self.hero_abilities:
                if hero_ability_part:
                    hero_ability_part += ", "
                hero_ability_part += ability.name
            character_string += hero_ability_part

        if self.weakness:
            character_string += "\n\nSvaghet: {}".format(self.weakness)

        if self.looks:
            character_string += "\nUtseende: "
            for look in self.looks:
                character_string += look + ", "

        if self.weapons:
            character_string += "\n\nVapen:"
            for weapon in self.weapons:
                character_string += "\n{}".format(weapon)

        if self.armor:
            character_string += "\n\nRustning:"
            for piece in self.armor:
                character_string += "\n{}".format(piece.name)

        if self.items:
            character_string += "\n\nUtrustning:"
            for item in self.items:
                character_string += "\n{}".format(item)

        if self.keepsake:
            character_string += "\n\nMinnessak: {}".format(self.keepsake)

        return character_string


def _adjust_attribute_to_limits(attribute):
    if attribute < 3:
        return 3
    elif attribute > 18:
        return 18
    else:
        return attribute


class CharacterError(Exception):
    pass
