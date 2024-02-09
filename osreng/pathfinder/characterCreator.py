import inputTools
from pathfinder import pathfinderSheet, baseValues, spell, ancestry
from pathfinder.baseValues import SheetModifications, AbilityScore, CharacterChoice, StaticModification
from dice import RandomList


def create_custom_character():
    print("Pick the alternative you want in each step, leave empty to skip.")

    # Step 1
    character_sheet = pathfinderSheet.PathfinderSheet()
    for value in CoreValues.modifications:
        character_sheet.add(value)

    # Step 2
    print("Pick Ancestry")
    ancestry_pick = inputTools.pick_from_list(ancestry.available_ancestries, False)
    character_sheet.ancestry = ancestry_pick.name
    for modification in ancestry_pick.modifications:
        if isinstance(modification, StaticModification):
            character_sheet.add(modification)
        elif isinstance(modification, CharacterChoice):
            print(modification.description)
            choices = inputTools.pick_multiple_from_list(modification.choices, modification.number_of_picks)
            for choice in choices:
                if isinstance(choice, StaticModification):
                    character_sheet.add(choice)
                elif isinstance(modification, SheetModifications):
                    character_sheet.heritage = modification.name
                    for value in modification.modifications:
                        # TODO Same parsing thing here
                        character_sheet.add(value)
        else:
            print("Unknown modification {}".format(modification))
    print(character_sheet)


CoreValues = SheetModifications("Core modifications", [
    baseValues.StaticModification(AbilityScore.Strength, 10),
    baseValues.StaticModification(AbilityScore.Dexterity, 10),
    baseValues.StaticModification(AbilityScore.Constitution, 10),
    baseValues.StaticModification(AbilityScore.Intelligence, 10),
    baseValues.StaticModification(AbilityScore.Wisdom, 10),
    baseValues.StaticModification(AbilityScore.Charisma, 10)])
