from pathfinder import pathfinderSheet, ancestry, attribute

import inputTools


def create_custom_character():
    print("Pick the alternative you want in each step, leave empty to skip.")
    character_sheet = pathfinderSheet.PathfinderSheet()
    print("Pick Ancestry")
    character_sheet.set_ancestry(inputTools.pick_from_list(ancestry.available_ancestries, False))
    boosts = character_sheet.ancestry.ability_boosts
    print("Boosts: " + ', '.join(map(str, boosts)))
    flaws = character_sheet.ancestry.ability_flaws
    print("Flaws: " + ', '.join(map(str, flaws)))
    for boost in boosts:
        if isinstance(boost, attribute.Attribute):
            character_sheet.boost_attribute(boost)
        elif isinstance(boost, attribute.Any):
            selection = [a for a in [*attribute.Attribute] if a not in boosts]
            character_sheet.boost_attribute(inputTools.pick_from_list(selection, False))

    for flaw in flaws:
        if isinstance(flaw, attribute.Attribute):
            character_sheet.reduce_attribute(flaw)
        elif isinstance(flaw, attribute.Any):
            selection = [a for a in [*attribute.Attribute] if a not in flaws]
            character_sheet.boost_attribute(inputTools.pick_from_list(selection, False))
    print(character_sheet)
