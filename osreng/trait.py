from random import choice

from dice import pick_n_unique

suggested_weaknesses = ['Godtrogen', 'Girig', 'Lättkränkt', 'Dumdristig', 'Räddhågsen', 'Monsterhatare', 'Intolerant',
                        'Lättjefull', 'Matglad', 'Kleptoman', 'Fåfäng', 'Våghals', 'Arkanofob', 'Bokmal', 'Vilde',
                        'Skrävlare', 'Våldsam', 'Besserwisser', 'Pessimist', 'Högfärdig']

suggested_keepsakes = ['Dina trogna gamla skor', 'En enkel silvermedaljong',
                       'Ett brev från en gammal vän eller släkting', 'En gammal sliten dagbok',
                       'Ett armband som gått i arv i familjen', 'En snidad träfigur du fått som liten',
                       'En märkligt formad sten', 'Ett kopparmynt från en skatt som din far eller mor sökt efter',
                       'En gammal tennplunta', 'Ett horn du tagit som trofé från ett monster',
                       'En huggtand du tagit som trofé av ett odjur', 'Ett par enkla tärningar av ben',
                       'En berlock med en hårlock', 'En ornamenterad nyckel', 'En handritad karta du ärvt',
                       'En ring med en inskription', 'En visselpipa av ben', 'Din förälders slitna hatt',
                       'En fjäder från en grip', 'En välsnidad pipa']

suggested_looks = ['Fult ärr över kinden', 'Märklig huvudbonad', 'Onormalt blek och glåmig',
                  'Ständigt ett leende på läpparna', 'Iskall och genomträngande blick', 'Några extra kilon runt midjan',
                  'Mager och senig', 'Onormalt kraftig kroppsbehåring', 'Mycket tunnhårig', 'Framträdande tatuering',
                  'Luktar illa', 'Storslagen frisyr', 'Haltande gång', 'Lortig', 'Ärliga blå ögon', 'Tand av silver',
                  'Välparfymerad', 'Olika ögonfärg', 'Väsande röst', 'Väderbitet ansikte']


def roll_weakness():
    return choice(suggested_weaknesses)


def roll_keepsake():
    return choice(suggested_keepsakes)


def roll_looks(n=1):
    return pick_n_unique(suggested_looks, n)
