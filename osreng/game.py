from race import roll_race, roll_first_name
from clazz import roll_class, roll_surname
from character_sheet import CharacterSheet
from age import roll_age
from dice import roll_attribute


if __name__ == '__main__':
    print('Creating random character')
    sheet = CharacterSheet()
    sheet.race = roll_race()
    sheet.clazz = roll_class()
    sheet.age = roll_age()
    sheet.name = roll_first_name(sheet.race) + ' ' + roll_surname(sheet.clazz)

    sheet.strength = roll_attribute()
    sheet.constitution = roll_attribute()
    sheet.dexterity = roll_attribute()
    sheet.intelligence = roll_attribute()
    sheet.will = roll_attribute()
    sheet.charisma = roll_attribute()

    sheet.shift_max_to_preferred_attribute()

    print(sheet)
