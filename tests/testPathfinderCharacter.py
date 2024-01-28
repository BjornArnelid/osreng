import unittest

from parameterized import parameterized

from pathfinder import pathfinderSheet, ancestry


class MyTestCase(unittest.TestCase):
    def test_default_attributes(self):
        character = pathfinderSheet.PathfinderSheet()
        self.assertEqual(10, character.strength)
        self.assertEqual(10, character.dexterity)
        self.assertEqual(10, character.constitution)
        self.assertEqual(10, character.intelligence)
        self.assertEqual(10, character.wisdom)
        self.assertEqual(10, character.charisma)

    @parameterized.expand(ancestry.available_ancestries)
    def test_pick_ancestry(self, ancestry):
        character = pathfinderSheet.PathfinderSheet()

        self.assertIsNotNone(ancestry.ability_boosts)
        self.assertIsNotNone(ancestry.ability_flaws)

        character.set_ancestry(ancestry)
        self.assertIsNotNone(character.size)
        self.assertIsNotNone(character.speed)
        self.assertTrue(character.languages, "Languages should not be empty for ancestry {}".format(ancestry.name))
        self.assertTrue(character.hit_points, "Hit points should not be 0 for ancestry {}".format(ancestry.name))

    @parameterized.expand([*ancestry.Attribute])
    def test_adjust_attribute(self, Attribute):
        character = pathfinderSheet.PathfinderSheet()
        character.boost_attribute(Attribute)
        self.assertEqual(12, character.get_attribute(Attribute))
        character.reduce_attribute(Attribute)
        self.assertEqual(10, character.get_attribute(Attribute))


if __name__ == '__main__':
    unittest.main()
