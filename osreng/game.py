from jsonpickle import encode, decode

import dragonbane.characterCreator
import pathfinder.characterCreator
import inputTools


def save_character(sheet):
    print(sheet)
    answer = input("Spara karaktären till fil (j/n)?")
    if answer.lower() == 'j':
        file_name = input("Välj användarnamn: ")
        with open(file_name + '.json', 'a', encoding='utf-8') as file:
            file.write(encode(sheet, unpicklable=True))
            file.write("\n")
        print()


def load_character():
    file_name = input("Ange användarnamn: ")
    with open(file_name + '.json', 'r', encoding='utf-8') as file:
        characters = []
        character_lines = file.readlines()
        for line in character_lines:
            characters.append(decode(line))
        print("Välj karaktär.")
        if characters:
            return inputTools.pick_from_list(characters, False)
        else:
            return None


welcome_message = """Välkommen!
1) Skapa DoD karaktär helt slumpmässigt.
2) Skapa DoD karaktär manuellt.
3) Skapa pathfinder karaktär.
4) Spela.
5) Ladda karaktär.
0) Avsluta"""

if __name__ == '__main__':
    running = True
    while running:
        print(welcome_message)
        generating_choice = inputTools.verified_int_input("# ", 0, 3)
        if generating_choice == 1 or generating_choice == 2:
            sheet = dragonbane.characterCreator.create_custom_character(generating_choice == 1)
            save_character(sheet)
        elif generating_choice == 3:
            sheet = pathfinder.characterCreator.create_custom_character()
            # save_character(sheet)
        elif generating_choice == 4:
            print("Den som väntar på något gott...")
        elif generating_choice == 5:
            sheet = load_character()
            print(sheet)
        elif generating_choice == 0:
            running = False
        else:
            print("Var god försök igen")
        print("\n")
