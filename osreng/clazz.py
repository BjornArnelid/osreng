from random import choice
from attribute import STRENGTH, DEXTERITY, INTELLIGENCE, WILL, CHARISMA

class Bard:
    name = 'Bard'
    suggested_names = ['Kvädare', 'Skaldekraft', 'Silverstämma', 'Gyllenklav', 'Honungstunga', 'Rimsmidare']
    preferred_attribute = CHARISMA


class Craftsman:
    name = 'Hantverkare'
    suggested_names = ['Stenhammare', 'Timmerklyve', 'Kraftnäve', 'Tunnmakare', 'Brovälvare', 'Järnmästare']
    preferred_attribute = STRENGTH


class Hunter:
    name = 'Jägare'
    suggested_names = ['Skogsräv', 'Ulvbane', 'Stigfinnare', 'Vindfarne', 'Blodshunger', 'Skuggpil']
    preferred_attribute = DEXTERITY


class Warrior:
    name = 'Krigare'
    suggested_names = ['Gravmakare', 'Grymkäft', 'Vindhugg', 'Svärdsblank', 'Orädd', 'Slaktaren']
    preferred_attribute = STRENGTH


class Scholar:
    name = 'Lärd'
    suggested_names = ['Boksynte', 'Allomklok', 'Vidblicke', 'Tankeklar', 'Dammlunga', 'Den lärde och välgödde']
    preferred_attribute = INTELLIGENCE


class Mage:
    name = 'Magiker'
    suggested_names = ['Rothjärta', 'Krokrygg', 'Gråkåpa', 'Vindhand', 'Stavhalte', 'Skuggmanare']
    preferred_attribute = WILL


class Peddler:
    name = 'Nasare'
    suggested_names = ['Silversnike', 'Guldtand', 'Silkestunga', 'Den läspe och ärlige', 'Isterbuk', 'Lockenpock']
    preferred_attribute = CHARISMA


class Knight:
    name = 'Riddare'
    suggested_names = ['Drakhjärta', 'Gyllenlans', 'Gripenklo', 'Ädelsinne', 'Blankenhjelm', 'Sorgmantel']
    preferred_attribute = STRENGTH


class Sailor:
    name = 'Sjöfarare'
    suggested_names = ['Sjöskum', 'Vågryttare', 'Skumfarne', 'Saltstänke', 'Sjöbjörn', 'Havsstorm']
    preferred_attribute = DEXTERITY


class Thief:
    name = 'Tjuv'
    suggested_names = ['Halvfinger', 'Svartråtta', 'Rödöga', 'Kvickfot', 'Dubbeltunga', 'Dolkenstöt']
    preferred_attribute = DEXTERITY


available_classes = [Bard, Craftsman, Hunter, Warrior, Scholar, Mage, Peddler, Knight, Sailor, Thief]


def roll_class():
    return choice(available_classes)()


def roll_surname(clazz):
    return choice(clazz.suggested_names)
