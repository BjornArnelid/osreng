import unittest

from race import roll_race, roll_first_name, available_races, Human
from clazz import roll_class, roll_surname, available_classes, Warrior
from age import roll_age, Age
from character_sheet import CharacterSheet, CharacterError


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
        self.assertEquals(Age.MiddleAged, sheet.age)

    def test_roll_name(self):
        for Race in available_races:
            self.assertIsNotNone(roll_first_name(Race()))
        for Clazz in available_classes:
            self.assertIsNotNone(roll_surname(Clazz()))


if __name__ == '__main__':
    unittest.main()
