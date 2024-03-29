import unittest

from parameterized import parameterized

from pathfinder import ancestry
from pathfinder.ancestry import Dwarf, get_heritages, available_ancestries
from pathfinder.baseValues import AbilityScore, StaticModification, HitPoints, Movement
from pathfinder.characterCreator import CoreValues
from pathfinder.pathfinderSheet import PathfinderSheet


class MyTestCase(unittest.TestCase):
    def test_add_core_values_attributes(self):
        character = PathfinderSheet()

        self.assertEqual(0, character.get(AbilityScore.Strength))
        self.assertEqual(0, character.get(AbilityScore.Dexterity))
        self.assertEqual(0, character.get(AbilityScore.Constitution))
        self.assertEqual(0, character.get(AbilityScore.Intelligence))
        self.assertEqual(0, character.get(AbilityScore.Wisdom))
        self.assertEqual(0, character.get(AbilityScore.Charisma))

        character = _create_clean_sheet()

        self.assertEqual(10, character.get(AbilityScore.Strength))
        self.assertEqual(10, character.get(AbilityScore.Dexterity))
        self.assertEqual(10, character.get(AbilityScore.Constitution))
        self.assertEqual(10, character.get(AbilityScore.Intelligence))
        self.assertEqual(10, character.get(AbilityScore.Wisdom))
        self.assertEqual(10, character.get(AbilityScore.Charisma))

    def test_dwarf_ability_scores(self):
        character = _create_clean_sheet()

        for modification in Dwarf.modifications:
            if isinstance(modification, StaticModification):
                character.add(modification)

        # Dwarf chooses strength as free boost
        character.add(StaticModification(AbilityScore.Strength, 2))

        self.assertEqual(12, character.get(AbilityScore.Strength))
        self.assertEqual(10, character.get(AbilityScore.Dexterity))
        self.assertEqual(12, character.get(AbilityScore.Constitution))
        self.assertEqual(10, character.get(AbilityScore.Intelligence))
        self.assertEqual(12, character.get(AbilityScore.Wisdom))
        self.assertEqual(8, character.get(AbilityScore.Charisma))

        self.assertEqual(10, character.get(HitPoints.MaxHitPoints))
        self.assertEqual(20, character.get(Movement.Speed))

    @parameterized.expand(ancestry.available_ancestries)
    def test_pick_ancestry(self, the_ancestry):
        self.assertTrue(the_ancestry.modifications, "Ancestry {} should have modifications".format(the_ancestry.name))

    @parameterized.expand(ancestry.available_ancestries)
    def test_heritage_abilities(self, the_ancestry):
        for heritage in get_heritages(the_ancestry):
            self.assertIsNotNone(heritage.modifications, "Heritage {} should have modifications".format(heritage.name))


def _create_clean_sheet():
    character = PathfinderSheet()
    for modification in CoreValues.modifications:
        if isinstance(modification, StaticModification):
            character.add(modification)
    return character


if __name__ == '__main__':
    unittest.main()
