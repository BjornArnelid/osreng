from random import choice


class Bard:
    name = 'Bard'
    suggested_names = ['Kvädare', 'Skaldekraft', 'Silverstämma', 'Gyllenklav', 'Honungstunga', 'Rimsmidare']


class Craftsman:
    name = 'Hantverkare'
    suggested_names = ['Stenhammare', 'Timmerklyve', 'Kraftnäve', 'Tunnmakare', 'Brovälvare', 'Järnmästare']


class Hunter:
    name = 'Jägare'
    suggested_names = ['Skogsräv', 'Ulvbane', 'Stigfinnare', 'Vindfarne', 'Blodshunger', 'Skuggpil']


class Warrior:
    name = 'Krigare'
    suggested_names = ['Gravmakare', 'Grymkäft', 'Vindhugg', 'Svärdsblank', 'Orädd', 'Slaktaren']


class Scholar:
    name = 'Lärd'
    suggested_names = ['Boksynte', 'Allomklok', 'Vidblicke', 'Tankeklar', 'Dammlunga', 'Den lärde och välgödde']


class Mage:
    name = 'Magiker'
    suggested_names = ['Rothjärta', 'Krokrygg', 'Gråkåpa', 'Vindhand', 'Stavhalte', 'Skuggmanare']


class Peddler:
    name = 'Nasare'
    suggested_names = ['Silversnike', 'Guldtand', 'Silkestunga', 'Den läspe och ärlige', 'Isterbuk', 'Lockenpock']


class Knight:
    name = 'Riddare'
    suggested_names = ['Drakhjärta', 'Gyllenlans', 'Gripenklo', 'Ädelsinne', 'Blankenhjelm', 'Sorgmantel']


class Sailor:
    name = 'Sjöfarare'
    suggested_names = ['Sjöskum', 'Vågryttare', 'Skumfarne', 'Saltstänke', 'Sjöbjörn', 'Havsstorm']


class Thief:
    name = 'Tjuv'
    suggested_names = ['Halvfinger', 'Svartråtta', 'Rödöga', 'Kvickfot', 'Dubbeltunga', 'Dolkenstöt']


available_classes = [Bard, Craftsman, Hunter, Warrior, Scholar, Mage, Peddler, Knight, Sailor, Thief]


def roll_class():
    return choice(available_classes)()


def roll_surname(clazz):
    return choice(clazz.suggested_names)
