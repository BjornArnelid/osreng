import unittest

from osreng.race import roll_race, Race
from osreng.clazz import roll_class, Class


class MyTestCase(unittest.TestCase):
    def test_roll_race(self):
        race = roll_race()
        self.assertTrue(race in [*Race])

    def test_race_trait(self):
        for race in [*Race]:
            self.assertIsNotNone(race.trait)

    def test_roll_class(self):
        cls = roll_class()
        self.assertTrue(cls in [*Class])


if __name__ == '__main__':
    unittest.main()
