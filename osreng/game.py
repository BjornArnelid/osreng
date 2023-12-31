from race import roll_race
from clazz import roll_class
from character_sheet import CharacterSheet

if __name__ == '__main__':
    print('Creating random character')
    sheet = CharacterSheet()
    sheet.race = roll_race()
    sheet.clazz = roll_class()
    print(sheet)
