from pathfinder.baseValues import AbilityScore, HitPoints, Field, Movement, Perception
from pathfinder.item import Item


class PathfinderSheet:
    def __init__(self):
        self.ancestry = None
        self.heritage = None
        self.size = None
        self.traits = []
        self.ability_scores = AbilityScoreField()
        self.hit_points = HitPointField()
        self.movement = MovementField()
        self.perception = PerceptionField()

        self.languages = []

    def add(self, sheet_modifier):
        if sheet_modifier.attribute in [*AbilityScore]:
            self.ability_scores.add(sheet_modifier)
        elif sheet_modifier.attribute in [*HitPoints]:
            self.hit_points.add(sheet_modifier)
        elif sheet_modifier.attribute == Field.Size:
            self.size = sheet_modifier
        elif sheet_modifier.attribute == Field.Traits:
            self.traits.append(sheet_modifier)
        elif sheet_modifier.attribute == Movement.Speed:
            self.movement.add(sheet_modifier)
        elif sheet_modifier.attribute == Perception.Senses:
            self.perception.add(sheet_modifier)
        elif sheet_modifier.attribute == Field.Languages:
            self.languages.append(sheet_modifier)
        elif isinstance(sheet_modifier, Item):
            pass  # TODO Add item
        else:
            raise CharacterError("Unknown modifier {}".format(sheet_modifier.attribute))

    def get(self, sheet_attribute):
        if sheet_attribute in [*AbilityScore]:
            return self.ability_scores.get(sheet_attribute)
        elif sheet_attribute in [*HitPoints]:
            return self.hit_points.get(sheet_attribute)
        elif sheet_attribute == Field.Size:
            return self.size.value
        elif sheet_attribute == Movement.Speed:
            return self.movement.get(sheet_attribute)
        elif sheet_attribute == Perception.Senses:
            return self.perception.get(sheet_attribute)
        elif sheet_attribute == Field.Languages:
            return self.languages
        else:
            raise CharacterError("Unknown attribute {}".format(sheet_attribute))

    def __str__(self):
        character_string = "CHARACTER"
        if self.ancestry:
            character_string += "\nAncestry: " + self.ancestry
        if self.heritage:
            character_string += "\nHeritage: " + self.heritage
        if self.size:
            character_string += "\nSize: " + str(self.size.value)
        if self.traits:
            character_string += "\nTraits: " + ", ".join([str(trait.value) for trait in self.traits])
        character_string += "\nAttributes"
        character_string += "\nSTR: {}, DEX: {}, CON: {}, INT: {}, WIS: {}, CHA: {}, ".format(
            self.get(AbilityScore.Strength), self.get(AbilityScore.Dexterity),
            self.get(AbilityScore.Constitution), self.get(AbilityScore.Intelligence), self.get(AbilityScore.Wisdom),
            self.get(AbilityScore.Charisma))
        if self.hit_points.get(HitPoints.MaxHitPoints):
            character_string += "\nMAx hit Points: " + str(self.hit_points.get(HitPoints.MaxHitPoints))
            character_string += "\nCurrent hit Points: " + str(self.hit_points.current_hit_points)
        if self.movement.get(Movement.Speed):
            character_string += "\nSpeed: " + str(self.movement.get(Movement.Speed))
        if self.perception.get(Perception.Senses):
            character_string += "\nPerception: " + str(self.perception.get(Perception.Senses))

        if self.languages:
            character_string += "\nLanguages: " + ", ".join([str(language.value) for language in self.languages])

        return character_string


class CharacterError(Exception):
    pass


class AbilityScoreField:
    def __init__(self):
        self._modifications = dict()

    def add(self, sheet_modifier):
        if sheet_modifier.attribute in self._modifications:
            self._modifications[sheet_modifier.attribute].append(sheet_modifier)
        else:
            self._modifications[sheet_modifier.attribute] = [sheet_modifier]

    def get(self, sheet_attribute):
        if sheet_attribute in self._modifications:
            return sum(modifier.value for modifier in self._modifications[sheet_attribute])
        return 0


class HitPointField:
    def __init__(self):
        self._max_hit_points = []
        self.current_hit_points = 0

    def add(self, sheet_modifier):
        if sheet_modifier.attribute == HitPoints.MaxHitPoints:
            self._max_hit_points.append(sheet_modifier)
            self.current_hit_points = self.get(HitPoints.MaxHitPoints)
        else:
            raise CharacterError("Unknown hit point modifier {}".format(sheet_modifier.attribute))

    def get(self, sheet_attribute):
        return sum(modifier.value for modifier in self._max_hit_points)


class MovementField:
    def __init__(self):
        self._speed = []
        self.movement_type = None

    def add(self, sheet_modifier):
        if sheet_modifier.attribute == Movement.Speed:
            self._speed.append(sheet_modifier)
        else:
            raise CharacterError("Unknown movement modifier {}".format(sheet_modifier.attribute))

    def get(self, sheet_attribute):
        if sheet_attribute == Movement.Speed:
            return sum(modifier.value for modifier in self._speed)
        else:
            return self.movement_type


class PerceptionField:
    def __init__(self):
        self.vision = None

    def add(self, sheet_modifier):
        if sheet_modifier.attribute == Perception.Senses:
            self.vision = sheet_modifier
        else:
            raise CharacterError("Unknown perception modifier {}".format(sheet_modifier.attribute))

    def get(self, sheet_attribute):
        if sheet_attribute == Perception.Senses:
            return self.vision.value
        else:
            raise CharacterError("Unknown perception attribute {}".format(sheet_attribute))
