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
