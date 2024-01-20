from random import choice
from enum import Enum, auto
from attribute import STRENGTH, AGILITY, INTELLIGENCE, WILL, CHARISMA
from skill import (BLUFFING, LANGUAGES, ACROBATICS, KNIVES, MYTHS_AND_LEGENDS, EVADE, PERFORMANCE, PERSUASION,
                   SLEIGHT_OF_HAND, SPOT_HIDDEN, HAMMERS, CRAFTING, BRAWLING, SWORDS, AXES, HUNTING_AND_FISHING, BOWS,
                   SLINGS, SNEAKING, AWARENESS, BUSHCRAFT, CROSSBOWS, SPEARS, BEAST_LORE, HEALING, ANIMALISM, STAVES,
                   ELEMENTALISM, MENTALISM, BARTERING, RIDING, SWIMMING, SEAMANSHIP)
from dice import d6, d8, d10, d12
from ability import (MUSICIAN, TANNER, SMITH, CARPENTER, COMPANION, COMBAT_EXPERIENCE, INTUITION, TREASURE_HUNTER,
                     CHAMPION, SEA_LEGS, BACKSTAB)
from item import (LYRE, KNIFE, OIL_LAMP, LAMP_OIL, TINDER_BOX, FOOD, SILVER_COIN, FLUTE,
                  DAGGER, ROPE, TORCH, BRASS_HORN, WAR_HAMMER_LIGHT, LEATHER_ARMOR, FORGING_TOOLS, HAND_AXE,
                  CARPENTRY_TOOLS, LEATHER_TOOLS, STORM_LANTERN, SHORT_BOW, QUIVER, SLEEPING_TRAP, SNARE, LONG_BOW,
                  FISHING_ROD, SLING, BROAD_SWORD, BATTLE_AXE, MORNING_STAR, SMALL_SHIELD, CHAINMAIL_ARMOR, SHORT_SPEAR,
                  SHORT_SWORD, LIGHT_CROSSBOW, LONG_SPEAR, STUDDED_LEATHER_ARMOR, OPEN_HELMET, WOODEN_STAFF, NOTEBOOK,
                  QUILL_PEN, BOOK, DRESSING, SLEEPING_POTION, CRYSTAL_BALL, SPELL_BOOK, WAND, AMULET, DONKEY,
                  FIELD_KITCHEN, CART, LARGE_TENT, BACKPACK, PLATE_ARMOR, GREAT_HELMET, FLAIL, LANCE, WAR_HORSE,
                  GRAPPLING_HOOK, SCIMITAR, TRIDENT, BINOCULARS, SIMPLE_LOCKPICKS, PEBBLES, Item, Weapon)


class Bard:
    name = 'Bard'
    suggested_names = ['Kvädare', 'Skaldekraft', 'Silverstämma', 'Gyllenklav', 'Honungstunga', 'Rimsmidare']
    preferred_attribute = CHARISMA
    skills = [BLUFFING, LANGUAGES, ACROBATICS, KNIVES, MYTHS_AND_LEGENDS, EVADE, PERFORMANCE, PERSUASION]
    hero_ability = MUSICIAN
    item_sets = [[LYRE, KNIFE, OIL_LAMP, LAMP_OIL, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)],
                 [FLUTE, DAGGER, ROPE, TORCH, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)],
                 [BRASS_HORN, KNIFE, TORCH, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)]]


class Craftsman:
    name = 'Hantverkare'
    suggested_names = ['Stenhammare', 'Timmerklyve', 'Kraftnäve', 'Tunnmakare', 'Brovälvare', 'Järnmästare']
    preferred_attribute = STRENGTH
    skills = [SLEIGHT_OF_HAND, SPOT_HIDDEN, HAMMERS, CRAFTING, KNIVES, BRAWLING, SWORDS, AXES]
    heroic_abilities = [TANNER, SMITH, CARPENTER]
    hero_ability = (TANNER, SMITH, CARPENTER)
    item_sets = [[WAR_HAMMER_LIGHT, LEATHER_ARMOR, FORGING_TOOLS, TORCH, TINDER_BOX, (d8, FOOD), (d8, SILVER_COIN)],
                 [HAND_AXE, LEATHER_ARMOR, CARPENTRY_TOOLS, TORCH, ROPE, TINDER_BOX, (d8, FOOD), (d8, SILVER_COIN)],
                 [KNIFE, LEATHER_ARMOR, LEATHER_TOOLS, STORM_LANTERN, LAMP_OIL, TINDER_BOX, (d8, FOOD),
                  (d8, SILVER_COIN)]]

    def get_preferred_items(self, hero_ability):
        if hero_ability == SMITH:
            return self.item_sets[0]
        elif hero_ability == CARPENTER:
            return self.item_sets[1]
        else:
            return self.item_sets[2]


class Hunter:
    name = 'Jägare'
    suggested_names = ['Skogsräv', 'Ulvbane', 'Stigfinnare', 'Vindfarne', 'Blodshunger', 'Skuggpil']
    preferred_attribute = AGILITY
    skills = [ACROBATICS, HUNTING_AND_FISHING, KNIVES, BOWS, SLINGS, SNEAKING, AWARENESS, BUSHCRAFT]
    hero_ability = COMPANION
    item_sets = [[DAGGER, SHORT_BOW, QUIVER, LEATHER_ARMOR, SLEEPING_TRAP, TORCH, TINDER_BOX, ROPE, SNARE, (d8, FOOD),
                  (d6, SILVER_COIN)],
                 [KNIFE, LONG_BOW, QUIVER, LEATHER_ARMOR, SLEEPING_TRAP, TORCH, TINDER_BOX, ROPE, FISHING_ROD,
                  (d8, FOOD), (d6, SILVER_COIN)],
                 [DAGGER, SLING, LEATHER_ARMOR, SLEEPING_TRAP, TORCH, TINDER_BOX, ROPE, SNARE, (d8, FOOD),
                  (d6, SILVER_COIN)]]


class Warrior:
    name = 'Krigare'
    suggested_names = ['Gravmakare', 'Grymkäft', 'Vindhugg', 'Svärdsblank', 'Orädd', 'Slaktaren']
    preferred_attribute = STRENGTH
    skills = [CROSSBOWS, HAMMERS, BOWS, BRAWLING, SPEARS, SWORDS, EVADE, AXES]
    hero_ability = COMBAT_EXPERIENCE
    item_sets = [[(BROAD_SWORD, BATTLE_AXE, MORNING_STAR), SMALL_SHIELD, CHAINMAIL_ARMOR, TORCH, TINDER_BOX, (d6, FOOD),
                  (d6, SILVER_COIN)],
                 [(SHORT_SWORD, HAND_AXE, SHORT_SPEAR), LIGHT_CROSSBOW, QUIVER, LEATHER_ARMOR, TORCH, TINDER_BOX,
                  (d6, FOOD), (d6, SILVER_COIN)],
                 [LONG_SPEAR, STUDDED_LEATHER_ARMOR, OPEN_HELMET, TORCH, TINDER_BOX, (d6, FOOD), (d6, SILVER_COIN)]]


class Scholar:
    name = 'Lärd'
    suggested_names = ['Boksynte', 'Allomklok', 'Vidblicke', 'Tankeklar', 'Dammlunga', 'Den lärde och välgödde']
    preferred_attribute = INTELLIGENCE
    skills = [BEAST_LORE, SPOT_HIDDEN, LANGUAGES, HEALING, MYTHS_AND_LEGENDS, EVADE, AWARENESS, BUSHCRAFT]
    hero_ability = INTUITION
    item_sets = [[WOODEN_STAFF, NOTEBOOK, QUILL_PEN, SLEEPING_TRAP, TORCH, TINDER_BOX, (d6, FOOD), (d10, SILVER_COIN)],
                 [KNIFE, BOOK, SLEEPING_TRAP, OIL_LAMP, LAMP_OIL, TINDER_BOX, (d6, FOOD), (d10, SILVER_COIN)],
                 [SHORT_SWORD, (10, DRESSING), SLEEPING_POTION, SLEEPING_TRAP, STORM_LANTERN, LAMP_OIL, TINDER_BOX,
                  (d6, FOOD), (d10, SILVER_COIN)]]


class MageSchool(Enum):
    Animist = auto()
    Elementalist = auto()
    Mentalist = auto()


class Mage:
    name = 'Magiker'
    suggested_names = ['Rothjärta', 'Krokrygg', 'Gråkåpa', 'Vindhand', 'Stavhalte', 'Skuggmanare']
    preferred_attribute = WILL
    main_school = None
    hero_ability = None
    item_sets = [[WOODEN_STAFF, CRYSTAL_BALL, SPELL_BOOK, TORCH, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)],
                 [KNIFE, WAND, SPELL_BOOK, TORCH, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)],
                 [AMULET, SPELL_BOOK, SLEEPING_TRAP, TORCH, TINDER_BOX, (d6, FOOD), (d8, SILVER_COIN)]]

    @property
    def skills(self):
        if self.main_school is MageSchool.Animist:
            return [ANIMALISM, BEAST_LORE, HUNTING_AND_FISHING, HEALING, SNEAKING, STAVES, EVADE, BUSHCRAFT]
        elif self.main_school is MageSchool.Elementalist:
            return [ELEMENTALISM, SPOT_HIDDEN, LANGUAGES, HEALING, MYTHS_AND_LEGENDS, STAVES, EVADE, AWARENESS]
        elif self.main_school is MageSchool.Mentalist:
            return [MENTALISM, LANGUAGES, ACROBATICS, HEALING, MYTHS_AND_LEGENDS, BRAWLING, EVADE, AWARENESS]
        else:
            self.main_school = choice([*MageSchool])
            return self.skills


class Peddler:
    name = 'Nasare'
    suggested_names = ['Silversnike', 'Guldtand', 'Silkestunga', 'Den läspe och ärlige', 'Isterbuk', 'Lockenpock']
    preferred_attribute = CHARISMA
    skills = [BLUFFING, SLEIGHT_OF_HAND, SPOT_HIDDEN, KNIVES, BARTERING, EVADE, AWARENESS, PERSUASION]
    hero_ability = TREASURE_HUNTER
    item_sets = [[DAGGER, SLEEPING_TRAP, TORCH, TINDER_BOX, ROPE, DONKEY, (d6, FOOD), (d12, SILVER_COIN)],
                 [KNIFE, SLEEPING_TRAP, STORM_LANTERN, LAMP_OIL, TINDER_BOX, FIELD_KITCHEN, DONKEY, CART,
                  (d6, FOOD), (d12, SILVER_COIN)],
                 [DAGGER, SLEEPING_TRAP, LARGE_TENT, OIL_LAMP, LAMP_OIL, TINDER_BOX, BACKPACK, (d6, FOOD),
                  (d12, SILVER_COIN)]]


class Knight:
    name = 'Riddare'
    suggested_names = ['Drakhjärta', 'Gyllenlans', 'Gripenklo', 'Ädelsinne', 'Blankenhjelm', 'Sorgmantel']
    preferred_attribute = STRENGTH
    skills = [BEAST_LORE, HAMMERS, MYTHS_AND_LEGENDS, RIDING, SPEARS, SWORDS, PERFORMANCE, PERSUASION]
    hero_ability = CHAMPION
    item_sets = [[(BROAD_SWORD, MORNING_STAR), SMALL_SHIELD, PLATE_ARMOR, GREAT_HELMET, TORCH, TINDER_BOX, (d6, FOOD),
                  (d12, SILVER_COIN)],
                 [(FLAIL, WAR_HAMMER_LIGHT), SMALL_SHIELD, CHAINMAIL_ARMOR, OPEN_HELMET, TORCH, TINDER_BOX, (d6, FOOD),
                  (d12, SILVER_COIN)],
                 [SHORT_SWORD, LANCE, SMALL_SHIELD, CHAINMAIL_ARMOR, OPEN_HELMET, WAR_HORSE, (d6, FOOD),
                  (d12, SILVER_COIN)]]


class Sailor:
    name = 'Sjöfarare'
    suggested_names = ['Sjöskum', 'Vågryttare', 'Skumfarne', 'Saltstänke', 'Sjöbjörn', 'Havsstorm']
    preferred_attribute = AGILITY
    skills = [LANGUAGES, ACROBATICS, HUNTING_AND_FISHING, KNIVES, SWIMMING, SEAMANSHIP, SWORDS, SPOT_HIDDEN]
    hero_ability = SEA_LEGS
    item_sets = [[DAGGER, SHORT_BOW, QUIVER, ROPE, GRAPPLING_HOOK, SLEEPING_TRAP, TORCH, TINDER_BOX, (d8, FOOD),
                  (d10, SILVER_COIN)],
                 [SCIMITAR, LEATHER_ARMOR, ROPE, GRAPPLING_HOOK, TORCH, TINDER_BOX, (d8, FOOD), (d10, SILVER_COIN)],
                 [TRIDENT, BINOCULARS, ROPE, GRAPPLING_HOOK, TORCH, TINDER_BOX, (d8, FOOD), (d10, SILVER_COIN)]]


class Thief:
    name = 'Tjuv'
    suggested_names = ['Halvfinger', 'Svartråtta', 'Rödöga', 'Kvickfot', 'Dubbeltunga', 'Dolkenstöt']
    preferred_attribute = AGILITY
    skills = [BLUFFING, KNIVES, SLEIGHT_OF_HAND, SPOT_HIDDEN, ACROBATICS, SNEAKING, EVADE, AWARENESS]
    hero_ability = BACKSTAB
    item_sets = [[DAGGER, SLING, ROPE, GRAPPLING_HOOK, TORCH, TINDER_BOX, (d6, FOOD), (d10, SILVER_COIN)],
                 [KNIFE, SIMPLE_LOCKPICKS, TORCH, TINDER_BOX, (d6, FOOD), (d10, SILVER_COIN)],
                 [DAGGER, DAGGER, PEBBLES, ROPE, TORCH, TINDER_BOX, (d6, FOOD), (d10, SILVER_COIN)]]


available_classes = [Bard, Craftsman, Hunter, Warrior, Scholar, Mage, Peddler, Knight, Sailor, Thief]


def roll_class():
    return choice(available_classes)()


def roll_items(clazz):
    items = []
    starting_items = choice(clazz.item_sets)
    for item in starting_items:
        if isinstance(item, tuple) and isinstance(item[0], (Item, Weapon)):
            items.append(choice(item))
        else:
            items.append(item)
    return items
