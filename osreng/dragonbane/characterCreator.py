from random import choice

from inputTools import pick_from_list, verified_int_input, show_as_option, to_valid_integer, return_instance
from dice import Random, RandomFunction, RandomList, RandomSpecific
from dragonbane.race import roll_race, available_races
from dragonbane.clazz import roll_class, Craftsman, roll_items, Mage, available_classes
from dragonbane.dragonbane_sheet import DragonBaneSheet
from dragonbane.age import roll_age, available_ages
from dragonbane.attribute import roll_attribute, attribute_names, STRENGTH, CONSTITUTION, AGILITY, INTELLIGENCE, WILL, CHARISMA
from dragonbane.skill import base_skills
from dragonbane.trait import suggested_weaknesses, suggested_keepsakes, suggested_looks
from dragonbane.item import get_desired_skills
from dragonbane.magic import MageSchool, get_starting_cantrips, get_starting_spells


def create_custom_character(all_random):
    if not all_random:
        print("Välj det alternativ du vill i varje steg, lämna tomt för att hoppa över.")
    character_sheet = DragonBaneSheet()
    if not all_random:
        print("Välj folkslag.")
    picked_race = pick_from_list([RandomFunction(roll_race)] + available_races, all_random)
    character_sheet.race = picked_race

    if not all_random:
        print("\nVälj Yrke.")
    picked_class = pick_from_list([RandomFunction(roll_class)] + available_classes, all_random)
    character_sheet.clazz = picked_class
    if isinstance(picked_class, Mage):
        if not all_random:
            print("Välj magiskola.")
        mage_school = pick_from_list([RandomList([*MageSchool])] + [*MageSchool], all_random)
        character_sheet.clazz.main_school = mage_school
        if not all_random:
            print("Välj trolleritrick.")
        cantrips = get_starting_cantrips(mage_school)
        character_sheet.spells = pick_multiple_from_list(
            RandomList(cantrips), cantrips, 3, [], all_random)
        if not all_random:
            print("Välj besvärjelser.")
        spells = get_starting_spells(mage_school)
        character_sheet.spells += pick_multiple_from_list(
            RandomList(spells), spells, 3, [], all_random)
    else:
        character_sheet.hero_abilities = resolve_choice(character_sheet.hero_abilities, all_random)

    if picked_class:
        if not all_random:
            print("\nVälj startutrustning")

        if isinstance(picked_class, Craftsman):
            starting_items = pick_from_list(
                [RandomSpecific(picked_class.get_preferred_items(character_sheet.hero_abilities[0]))] +
                character_sheet.clazz.item_sets, all_random)
            character_sheet.assign_start_items(starting_items)
        else:
            starting_items = resolve_choice(
                pick_from_list([RandomFunction(roll_items, character_sheet.clazz)] +
                               character_sheet.clazz.item_sets, all_random), all_random)
            character_sheet.assign_start_items(starting_items)
        if picked_race:
            if not all_random:
                print("\nVälj förnamn i listan, eller skriv ditt eget")
            first_name = pick_string(
                [RandomList(picked_race.suggested_names)] + picked_race.suggested_names, all_random)
            if not all_random:
                print("\nVälj tillnamn i listan, eller skriv dit eget")
            last_name = pick_string(
                [RandomList(picked_class.suggested_names)] + picked_class.suggested_names, all_random)
            character_sheet.name = first_name + " " + last_name

    if not all_random:
        print("\nVälj ålder")
    character_sheet.age = pick_from_list([RandomFunction(roll_age)] + available_ages, all_random)

    if not all_random:
        print("\nGrundegenskaper\n0) Välj slumpmässigt\n1) Slå fram grundegenskaper\n2) Sätt manuellt")
        attribute_choice = verified_int_input('# ', 0, 2)
    else:
        attribute_choice = 0
    if attribute_choice == 0:
        roll_attributes_random(character_sheet)
    elif attribute_choice == 1:
        roll_attributes_and_select(character_sheet)
    else:
        set_attributes_manually(character_sheet)
    if not all_random:
        print("\nJustera grundegenskaper\n0) Justera högsta grundegenskap till viktigaste för yrket\n" +
              "1) Justera manuellt\n2) Låt grundegenskaperna vara")
        adjust_choice = verified_int_input('# ', 0, 2)
    else:
        adjust_choice = 0
    if adjust_choice == 0:
        character_sheet.shift_max_to_preferred_attribute()
    elif adjust_choice == 1:
        adjust_attributes(character_sheet)
    else:
        pass

    if picked_class:
        desired_skills = get_desired_skills(starting_items)
        class_skill_points, general_skill_points = character_sheet.age.number_of_skillpoints
        available_class_skills = character_sheet.clazz.skills
        if isinstance(character_sheet.clazz, Mage):
            character_sheet.set_trained_skills([available_class_skills.pop(0)])
            class_skill_points -= 1

        if not all_random:
            print("\nFöljande färdigheter rekommenderas utifrån ditt yrke och startutrustning:")
            desired_skills_string = ""
            for item in desired_skills:
                desired_skills_string += "{}, ".format(show_as_option(item))
            print(desired_skills_string)
            print("Välj yrkesfärdigheter")

        class_skills = pick_multiple_from_list(RandomList(available_class_skills), available_class_skills,
                                               class_skill_points, desired_skills, all_random)

        skills_left = [x for x in base_skills if x not in class_skills]
        if not all_random:
            print("Välj övriga färdigheter")
        general_skills = pick_multiple_from_list(RandomList(skills_left), skills_left, general_skill_points,
                                                 desired_skills, all_random)

        character_sheet.set_trained_skills(class_skills + general_skills)

    if not all_random:
        print("\nVälj svaghet")
    character_sheet.weakness = pick_string([RandomList(suggested_weaknesses)] + suggested_weaknesses, all_random)
    if not all_random:
        print("\nVälj minnessak")
    character_sheet.keepsake = pick_string([RandomList(suggested_keepsakes)] + suggested_keepsakes, all_random)
    if not all_random:
        print("\nVälj utseende")
    character_sheet.looks.append(pick_string([RandomList(suggested_looks)] + suggested_looks, all_random))

    return character_sheet








def verified_list_input(prompt, low, high, min_choices, max_choices):
    while True:
        choices_list = input(prompt).split(',')
        if choices_list[0] == '':
            return None
        if min_choices <= len(choices_list) <= max_choices:
            choices = []
            for input_choice in choices_list:
                converted_choice = to_valid_integer(input_choice, low, high)
                if converted_choice is not None:
                    choices.append(converted_choice)
                else:
                    break
            return choices
        else:
            print("Välj ett antal alternativ mellan {} och {} separerat med att komma".format(
                min_choices, max_choices))




def resolve_choice(list_with_choice, all_random):
    resolved_list = []
    for item in list_with_choice:
        if isinstance(item, tuple) and not callable(item[0]):
            if not all_random:
                print("Välj ett av följande")
                print("0) Slumpmässigt")
                for i in range(len(item)):
                    print("{}) {}.".format(i+1, show_as_option(item[i])))
                converted_choice = verified_int_input('# ', 0, len(item))
            else:
                converted_choice = 0
            if converted_choice == 0:
                rnd = choice(item)
                if not all_random:
                    print("Val: {}".format(show_as_option(rnd)))
                resolved_list.append(rnd)
            else:
                resolved_list.append(item[converted_choice-1])
        else:
            resolved_list.append(item)
    return resolved_list


def pick_string(choices, all_random):
    num_choices = len(choices)
    if not all_random:
        for i in range(num_choices):
            print("{}) {}.".format(i, show_as_option(choices[i])))
        raw_choice = input('# ')
    else:
        raw_choice = 0

    try:
        converted_choice = int(raw_choice)
        if 0 <= converted_choice < num_choices:
            selected = choices[converted_choice]

            return return_instance(selected if not isinstance(selected, Random) else selected.roll())
        else:
            print("Ogiltigt val välj ett heltal mellan 0 och {}!".format(num_choices))
    except ValueError:
        if raw_choice:
            return raw_choice
    return ""


def roll_attributes_random(sheet):
    sheet.strength = roll_attribute()
    sheet.constitution = roll_attribute()
    sheet.agility = roll_attribute()
    sheet.intelligence = roll_attribute()
    sheet.will = roll_attribute()
    sheet.charisma = roll_attribute()


def roll_attributes_and_select(sheet):
    available_attributes = [STRENGTH, CONSTITUTION, AGILITY, INTELLIGENCE, WILL, CHARISMA]
    while available_attributes:
        roll = roll_attribute()
        print("Slag: {}".format(roll))
        num_left = len(available_attributes)
        for i in range(num_left):
            print("{}) {}.".format(i, show_as_option(attribute_names[available_attributes[i]])))

        attribute = available_attributes.pop(verified_int_input('# ', 0, num_left))
        sheet.set_attribute(attribute, roll)


def set_attributes_manually(sheet):
    for i in range(len(attribute_names)):
        converted_value = verified_int_input('{}: '.format(attribute_names[i]), 3, 18)
        sheet.set_attribute(i, converted_value)


def adjust_attributes(sheet):
    print("Du har rätt att byta plats på grundegenskaperna 2 gånger")
    print("Ange siffrorna för de grundegenskaper du vill byta plats på separerat med ett kommatecken, " +
          " eller tom rad om du är nöjd\n" +
          "(skriv till exempel 0,1 för att byta plats på Styrka och Fysik)")
    num_attrib = len(attribute_names)
    for _ in range(2):

        for i in range(num_attrib):
            print("{}) {} - {}.".format(
                i, show_as_option(attribute_names[i]), sheet.get_raw_attribute(i)))
        choices_list = verified_list_input('# ', 0, num_attrib, 2, 2)
        if not choices_list:
            return
        else:
            sheet.switch_attributes(choices_list[0], choices_list[1])


def pick_multiple_from_list(randomizer, list_of_choices, number_of_picks, suggestions, all_random):
    if not all_random:
        print("Du kan antingen välja en åt gången eller flera samtidigt separerade med kommatecken")
        print("Tryck retur för att slumpa fram resterande val")
    randomize = all_random
    picked_skills = []
    picks_left = number_of_picks
    while picks_left > 0:
        num_choices = len(list_of_choices)
        if not randomize:
            print("Picks left: {}".format(picks_left))
            for i in range(num_choices):
                print("{}) {}.".format(i, show_as_option(list_of_choices[i])))

            list_choices = verified_list_input('# ', 0, num_choices-1, 1, number_of_picks)
            if not list_choices:
                randomize = True
            else:
                for picked in sorted(list_choices, reverse=True):
                    selected = list_of_choices.pop(picked)
                    picked_skills.append(return_instance(selected))
                    picks_left -= 1

        else:
            for suggestion in suggestions:
                if suggestion in list_of_choices:
                    list_of_choices.remove(suggestion)
                    picked_skills.append(suggestion)
                    picks_left -= 1
            for _ in range(picks_left):
                randomizer.roll_list = list_of_choices
                rnd = randomizer.roll()
                picked_skills.append(rnd)
                list_of_choices.remove(rnd)
            return picked_skills
    return picked_skills
