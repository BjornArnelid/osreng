from pathfinder import pathfinderSheet, ancestry
import inputTools
def create_custom_character():
    print("Pick the alternative you want in each step, leave empty to skip.")
    character_sheet = pathfinderSheet.PathfinderSheet()
    print("Pick Ancestry")
    character_sheet.set_ancestry(inputTools.pick_from_list(ancestry.available_ancestries, False))
