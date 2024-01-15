from random import choice


suggested_weaknesses = ['Godtrogen', 'Girig', 'Lättkränkt', 'Dumdristig', 'Räddhågsen', 'Monsterhatare', 'Intolerant',
                        'Lättjefull', 'Matglad', 'Kleptoman', 'Fåfäng', 'Våghals', 'Arkanofob', 'Bokmal', 'Vilde',
                        'Skrävlare', 'Våldsam', 'Besserwisser', 'Pessimist', 'Högfärdig']


def roll_weakness():
    return choice(suggested_weaknesses)