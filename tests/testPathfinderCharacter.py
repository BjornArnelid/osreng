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

    @parameterized.expand(ancestries.available_ancestries)
    def test_pick_ancestry(self, Ancestry):
        character = pathfinderSheet.PathfinderSheet()
        character.set_ancestry(Ancestry())
        self.assertIsNotNone(character.size)
        self.assertIsNotNone(character.speed)
        self.assertTrue(character.languages, "Languages should not be empty for ancestry {}".format(Ancestry.name))
        self.assertTrue(character.hit_points, "Hit points should not be 0 for ancestry {}".format(Ancestry.name))


if __name__ == '__main__':
    unittest.main()
