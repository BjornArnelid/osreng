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
    character_sheet.ancestry = ancestry_pick
    resolve_choice(ancestry_pick.modifications, character_sheet)
    print("Pick heritage")
    heritage_pick = inputTools.pick_from_list(ancestry.get_heritages(ancestry_pick), False)
    character_sheet.heritage = heritage_pick
    resolve_choice(heritage_pick.modifications, character_sheet)

    print(character_sheet)


def resolve_choice(choices, character_sheet):
    for choice in choices:
        if isinstance(choice, StaticModification):
            character_sheet.add(choice)
        elif isinstance(choice, CharacterChoice):
            print(choice.description)
            choices = inputTools.pick_multiple_from_list(choice.choices, choice.number_of_picks)
            resolve_choice(choices, character_sheet)
        else:
            print("Unknown modification {}".format(choice))



CoreValues = SheetModifications("Core modifications", [
    baseValues.StaticModification(AbilityScore.Strength, 10),
    baseValues.StaticModification(AbilityScore.Dexterity, 10),
    baseValues.StaticModification(AbilityScore.Constitution, 10),
    baseValues.StaticModification(AbilityScore.Intelligence, 10),
    baseValues.StaticModification(AbilityScore.Wisdom, 10),
    baseValues.StaticModification(AbilityScore.Charisma, 10)])
