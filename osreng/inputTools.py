import dice


def pick_from_list(options_list, all_random):
    num_choices = len(options_list)
    if not all_random:
        for i in range(num_choices):
            print("{}) {}.".format(i, show_as_option(options_list[i])))
        list_choice = verified_int_input('# ', 0, num_choices-1)
    else:
        list_choice = 0
    selected = options_list[list_choice]

    if isinstance(selected, dice.Random):
        rolled = selected.roll()
        if not all_random:
            print("Valde: " + show_as_option(rolled))
        return return_instance(rolled)
    else:
        return return_instance(selected)


def show_as_option(option):
    try:
        return option.name
    except AttributeError:
        if isinstance(option, (list, tuple)):
            option_string = "["
            for op in option:
                option_string += show_as_option(op) + ", "
            return option_string + "]"
        elif callable(option):
            return dice.to_die_string(option)
        else:
            return str(option)


def verified_int_input(prompt, low, high):
    while True:
        raw_choice = input(prompt)
        converted_choice = to_valid_integer(raw_choice, low, high)
        if converted_choice is not None:
            return converted_choice


def return_instance(class_or_instance):
    return class_or_instance() if callable(class_or_instance) else class_or_instance


def to_valid_integer(raw_input, low, high):
    try:
        converted_choice = int(raw_input)
        if low <= converted_choice <= high:
            return converted_choice
        else:
            print("Måste vara mellan {} och {}, men var {}".format(low, high, converted_choice))
    except ValueError:
        print("{} är inte ett godkänt heltal".format(raw_input))
    return None


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
