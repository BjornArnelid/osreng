import unittest

from parameterized import parameterized

from race import roll_race, roll_first_name, available_races, Human
from clazz import roll_class, roll_surname, available_classes, Warrior
from age import roll_age, Age
from character_sheet import CharacterSheet, CharacterError
from dice import no_die, d4, d6
from attribute import STRENGTH, CHARISMA, roll_attribute


class MyTestCase(unittest.TestCase):
    def test_roll_race(self):
        race = roll_race()
        self.assertTrue(any(isinstance(race, cls) for cls in available_races))

    def test_set_race_manually(self):
        sheet = CharacterSheet()
        with self.assertRaises(CharacterError):
            sheet.race = "orc"
        sheet.race = Human()
        self.assertTrue(isinstance(sheet.race, Human))

    def test_race_attributes(self):
        for Race in available_races:
            race = Race()
            self.assertIsNotNone(race.traits)
            self.assertIsNotNone(race.suggested_names)

    def test_roll_class(self):
        clazz = roll_class()
        self.assertTrue(any(isinstance(clazz, cls) for cls in available_classes))

    def test_set_class_manually(self):
        sheet = CharacterSheet()
        with self.assertRaises(CharacterError):
            sheet.clazz = "warrior"
        sheet.clazz = Warrior()
        self.assertTrue(isinstance(sheet.clazz, Warrior))

    def test_class_attributes(self):
        for Clazz in available_classes:
            clazz = Clazz()
            self.assertIsNotNone(clazz.suggested_names)

    def test_roll_age(self):
        age = roll_age()
        self.assertTrue(age in [*Age])

    def test_set_age_manually(self):
        sheet = CharacterSheet()
        with self.assertRaises(CharacterError):
            sheet.age = 2
        sheet.age = Age.MiddleAged
        self.assertEqual(Age.MiddleAged, sheet.age)

    def test_roll_name(self):
        for Race in available_races:
            self.assertIsNotNone(roll_first_name(Race()))
        for Clazz in available_classes:
            self.assertIsNotNone(roll_surname(Clazz()))

    def test_roll_attribute(self):
        attribute = roll_attribute()
        self.assertTrue(3 <= attribute <= 18)

    @parameterized.expand(available_classes)
    def test_switch_for_preferred_attribute(self, Clazz):
        sheet = CharacterSheet()
        sheet.clazz = Clazz()
        sheet.strength = roll_attribute()
        sheet.constitution = roll_attribute()
        sheet.dexterity = roll_attribute()
        sheet.intelligence = roll_attribute()
        sheet.will = roll_attribute()
        sheet.charisma = roll_attribute()
        sheet.shift_max_to_preferred_attribute()
        self.assertEqual(sheet._get_attribute(sheet.clazz.preferred_attribute), max(sheet._attributes))

    def test_adjust_for_age(self):
        sheet = CharacterSheet()
        sheet._attributes = [11, 11, 11, 11, 11, 11]
        self.assertEqual(11, sheet.charisma)

        sheet.age = Age.Young
        self.assertEqual(12, sheet.dexterity)
        self.assertEqual(12, sheet.constitution)

        sheet.age = Age.MiddleAged
        self.assertEqual(11, sheet.dexterity)
        self.assertEqual(11, sheet.constitution)

        sheet.age = Age.Old
        self.assertEqual(9, sheet.strength)
        self.assertEqual(9, sheet.dexterity)
        self.assertEqual(9, sheet.constitution)
        self.assertEqual(12, sheet.intelligence)
        self.assertEqual(12, sheet.will)

    def test_switch_attributes(self):
        sheet = CharacterSheet()
        sheet._attributes = [13, 11, 11, 11, 11, 15]
        sheet.switch_attributes(STRENGTH, CHARISMA)
        self.assertEqual(15, sheet.strength)
        self.assertEqual(13, sheet.charisma)

    @parameterized.expand(available_races)
    def test_get_movement_speed_for_races(self, Race):
        sheet = CharacterSheet()
        sheet.race = Race()
        sheet.dexterity = 11
        self.assertTrue(0 < sheet.movement_speed < 20)

    def test_adjust_speed_with_dexterity(self):
        sheet = CharacterSheet()
        sheet.race = Human()

        sheet.dexterity = 6
        self.assertEqual(6, sheet.movement_speed)

        sheet.dexterity = 7
        self.assertEqual(8, sheet.movement_speed)

        sheet.dexterity = 11
        self.assertEqual(10, sheet.movement_speed)

        sheet.dexterity = 13
        self.assertEqual(12, sheet.movement_speed)

        sheet.dexterity = 16
        self.assertEqual(14, sheet.movement_speed)

    def test_calculate_bonus_damage(self):
        sheet = CharacterSheet()
        sheet.strength = 3
        self.assertEqual(no_die, sheet.calculate_bonus_damage(STRENGTH))

        sheet.strength = 13
        self.assertEqual(d4, sheet.calculate_bonus_damage(STRENGTH))

        sheet.strength = 17
        self.assertEqual(d6, sheet.calculate_bonus_damage(STRENGTH))

    def test_hitpoints(self):
        sheet = CharacterSheet()
        sheet.constitution = 11
        self.assertEqual([11, 11], sheet.hitpoints)

        sheet.modify_hitpoints(-3)
        self.assertEqual([8, 11], sheet.hitpoints)

        sheet.modify_hitpoints(+5)
        self.assertEqual([11, 11], sheet.hitpoints)


if __name__ == '__main__':
    unittest.main()
