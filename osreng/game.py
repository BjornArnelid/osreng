from race import roll_race, roll_first_name
from clazz import roll_class, roll_surname, roll_clazz_skills, Craftsman
from character_sheet import CharacterSheet
from age import roll_age
from attribute import roll_attribute
from skill import roll_general_skills
from random import choice


if __name__ == '__main__':
    print('Creating random character')
    sheet = CharacterSheet()
    sheet.race = roll_race()
    sheet.clazz = roll_class()
    if isinstance(sheet.clazz, Craftsman):
        sheet.hero_abilities.append(choice(Craftsman.heroic_abilities))
    sheet.age = roll_age()
    sheet.name = roll_first_name(sheet.race) + ' ' + roll_surname(sheet.clazz)

    sheet.strength = roll_attribute()
    sheet.constitution = roll_attribute()
    sheet.dexterity = roll_attribute()
    sheet.intelligence = roll_attribute()
    sheet.will = roll_attribute()
    sheet.charisma = roll_attribute()

    sheet.shift_max_to_preferred_attribute()

    skill_points = sheet.age.number_of_skillpoints
    class_skills = roll_clazz_skills(sheet.clazz, skill_points[0])
    general_skills = roll_general_skills(class_skills, skill_points[1])
    sheet.set_trained_skills(class_skills + general_skills)

    print(sheet)
