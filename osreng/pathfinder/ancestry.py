import enum

from pathfinder.baseValues import Field, Reaction, Senses, StaticModification, CharacterChoice, \
    SheetModifications, AbilityScore, HitPoints, Movement, Perception
from pathfinder.spell import DetectMagic, Arcane, Divine, Occult, Primal, PreparedCantrips, SpellType
from pathfinder.item import Item


class Size(enum.Enum):
    Medium = enum.auto()
    Small = enum.auto()


class Language(enum.Enum):
    Common = enum.auto()
    Dwarven = enum.auto()
    Elven = enum.auto()
    Gnomish = enum.auto()
    Sylvan = enum.auto()
    Goblin = enum.auto()
    Halfling = enum.auto()


class Trait(enum.Enum):
    Humanoid = enum.auto()
    Dwarf = enum.auto()
    Elf = enum.auto()
    Gnome = enum.auto()
    Goblin = enum.auto()
    Halfling = enum.auto()
    Human = enum.auto()
    Fey = enum.auto()
    HalfElf = enum.auto()
    Orc = enum.auto()
    HalfOrc = enum.auto()


class Ability:
    def __init__(self, name):
        self.name = name


StrengthBoost = StaticModification(AbilityScore.Strength, 2)

DexterityBoost = StaticModification(AbilityScore.Dexterity, 2)

ConstitutionBoost = StaticModification(AbilityScore.Constitution, 2)

IntelligenceBoost = StaticModification(AbilityScore.Intelligence, 2)

WisdomBoost = StaticModification(AbilityScore.Wisdom, 2)

CharismaBoost = StaticModification(AbilityScore.Charisma, 2)



# Dwarf
AncientDwarf = SheetModifications('Ancient-blooded dwarf',
                                  StaticModification(Field.Reactions, Reaction("Call of the ancient blood")))

WardenDwarf = SheetModifications("Death warden dwarf",
                                 StaticModification(Field.Abilities, Ability("Ward of necromancy")))

ForgeDwarf = SheetModifications("Forge dwarf",
                                StaticModification(Field.Abilities, Ability("Fire resistance")))

RockDwarf = SheetModifications("Rock dwarf", StaticModification(Field.SavingThrows, Ability("Rock solid")))

StrongDwarf = SheetModifications("Strong-blooded dwarf",
                                 StaticModification(Field.Abilities, Ability("Poison resistance")))

ClanDagger = Item('Clan dagger')

Dwarf = SheetModifications('Dwarf', [
    StaticModification(HitPoints.MaxHitPoints, 10),
    StaticModification(Field.Size, Size.Medium),
    StaticModification(Movement.Speed, 20),
    StaticModification(AbilityScore.Constitution, 2),
    StaticModification(AbilityScore.Wisdom, 2),
    CharacterChoice("Pick an ability boost", [StrengthBoost, DexterityBoost, IntelligenceBoost, CharismaBoost]),
    StaticModification(AbilityScore.Charisma, -2),
    StaticModification(Field.Languages, Language.Common), StaticModification(Field.Languages, Language.Dwarven),
    StaticModification(Field.Traits, Trait.Dwarf), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.DarkVision),
    ClanDagger])

# Elf
ArcticElf = SheetModifications("Arctic elf",
                               [SheetModifications(Field.Abilities, Ability("Frost resistance"))])

CavernElf = SheetModifications("Cavern elf", [SheetModifications(Perception.Senses, Senses.DarkVision)])

SeerElf = SheetModifications("Seer elf",
                             [SheetModifications(SpellType.Cantrip, DetectMagic),
                              SheetModifications(Field.Abilities, Ability("Frost resistance"))])

WhisperElf = SheetModifications("Whisper elf",
                                [SheetModifications(Field.Abilities, Ability("Detect sound"))])

WoodlandElf = SheetModifications("Woodland elf",
                                 [SheetModifications(Field.Abilities, Ability("Woodland stride"))])

Elf = SheetModifications('Elf', [
    StaticModification(HitPoints.MaxHitPoints, 6),
    StaticModification(Field.Size, Size.Medium),
    StaticModification(Movement.Speed, 30),
    StaticModification(AbilityScore.Dexterity, 2),
    StaticModification(AbilityScore.Intelligence, 2),
    CharacterChoice("Ability boost", [StrengthBoost, ConstitutionBoost, WisdomBoost, CharismaBoost]),
    StaticModification(AbilityScore.Constitution, -2),
    StaticModification(Field.Languages, Language.Common), StaticModification(Field.Languages, Language.Elven),
    StaticModification(Field.Traits, Trait.Elf), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.LowLightVision)])

# Gnome
ChameleonGnome = SheetModifications("Chameleon gnome",
                                    [SheetModifications(Field.Abilities, Ability("Change color"))])

FeyGnome = SheetModifications("Fey-touched gnome", [SheetModifications(Field.Traits, Trait.Fey),
                                                    SheetModifications(SpellType.Cantrip,
                                                                       PreparedCantrips(Primal, 1, False))])

SensateGnome = SheetModifications("Sensate gnome",
                                  [SheetModifications(Perception.Senses, Senses.ImpreciseScent)])

UmbralGnome = SheetModifications("Umbral gnome",
                                 [SheetModifications(Perception.Senses, Senses.DarkVision)])

# TODO: Add cantrip to wellspring choice
WellspringGnome = SheetModifications("Wellspring gnome", CharacterChoice("Magic school",
                                                                         [Arcane, Divine, Occult, Primal]))

Gnome = SheetModifications('Gnome', [
    StaticModification(HitPoints.MaxHitPoints, 8),
    StaticModification(Field.Size, Size.Small),
    StaticModification(Movement.Speed, 25),
    StaticModification(AbilityScore.Constitution, 2),
    StaticModification(AbilityScore.Charisma, 2),
    CharacterChoice("Pick an ability boost",
                    [StrengthBoost, DexterityBoost, IntelligenceBoost, WisdomBoost]),
    StaticModification(AbilityScore.Strength, -2),
    StaticModification(Field.Languages, Language.Common), StaticModification(Field.Languages, Language.Gnomish),
    StaticModification(Field.Languages, Language.Sylvan),
    StaticModification(Field.Traits, Trait.Gnome), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.LowLightVision)])

# Goblin
CharhideGoblin = SheetModifications("Charhide goblin",
                                    [StaticModification(Field.Abilities, Ability("Fire resistance"))])

IrongutGoblin = SheetModifications("Irongut goblin",
                                   [StaticModification(Field.Abilities, Ability("Poison resistance"))])

RazortoothGoblin = SheetModifications("Razortooth goblin",
                                      [StaticModification(Field.Abilities, Ability("Razor teeth"))])

SnowGoblin = SheetModifications("Snow goblin",
                                [StaticModification(Field.Abilities, Ability("Cold resistance"))])

UnbreakableGoblin = SheetModifications("Unbreakable goblin",
                                       [StaticModification(HitPoints.MaxHitPoints, 4),
                                        StaticModification(Field.Abilities, Ability("Unbreakable"))])

Goblin = SheetModifications('Goblin', [
    StaticModification(HitPoints.MaxHitPoints, 6),
    StaticModification(Field.Size, Size.Small),
    StaticModification(Movement.Speed, 25),
    StaticModification(AbilityScore.Dexterity, 2),
    StaticModification(AbilityScore.Charisma, 2),
    CharacterChoice("Pick an ability boost",
                    [StrengthBoost, ConstitutionBoost, IntelligenceBoost, WisdomBoost]),
    StaticModification(AbilityScore.Wisdom, -2),
    StaticModification(Field.Languages, Language.Common), StaticModification(Field.Languages, Language.Goblin),
    StaticModification(Field.Traits, Trait.Goblin), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.DarkVision)])

# Halfling
GutsyHalfling = SheetModifications("Gutsy halfling",
                                   [StaticModification(Field.Abilities, Ability("Brave"))])

HillockHalfling = SheetModifications("Hillock Halfling",
                                     [StaticModification(Field.Abilities, Ability("Comfortable rest"))])

NomadicHalfling = SheetModifications("Nomadic halfling",
                                     [CharacterChoice("First known language", [*Language]),
                                      CharacterChoice("Second known language", [*Language]),
                                      StaticModification(Field.Abilities, Ability("Multilingual"))])

TwilightHalfling = SheetModifications("Twilight halfling",
                                      [SheetModifications(Perception.Senses, Senses.LowLightVision)])

WildwoodHalfling = SheetModifications("Wildwood halfling",
                                      [SheetModifications(Field.Abilities, Ability("Ignore forrest terrain"))])

Halfling = SheetModifications('Halfling', [
    StaticModification(HitPoints.MaxHitPoints, 6),
    StaticModification(Field.Size, Size.Small),
    StaticModification(Movement.Speed, 25),
    StaticModification(AbilityScore.Dexterity, 2),
    StaticModification(AbilityScore.Wisdom, 2),
    CharacterChoice("Pick an ability boost",
                    [StrengthBoost, ConstitutionBoost,IntelligenceBoost, CharismaBoost]),
    StaticModification(AbilityScore.Strength, -2),
    StaticModification(Field.Languages, Language.Common), StaticModification(Field.Languages, Language.Halfling),
    StaticModification(Field.Traits, Trait.Halfling), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.KeenEyes)])

# TODO Humans are a bit special
# Human
HalfElf = SheetModifications("Half-elf",
                             [StaticModification(Field.Traits, Trait.Elf),
                              StaticModification(Field.Traits, Trait.HalfElf),
                              StaticModification(Perception.Senses, Senses.LowLightVision)])

HalfOrc = SheetModifications("Half-orc",
                             [StaticModification(Field.Traits, Trait.Orc),
                              StaticModification(Field.Traits, Trait.HalfOrc),
                              StaticModification(Perception.Senses, Senses.LowLightVision)]
                             )

SkilledHeritage = SheetModifications("Skilled heritage", [StaticModification(Field.Abilities, Ability("Skilled"))])

VersatileHeritage = SheetModifications("Versatile heritage", [])

Human = SheetModifications('Human', [
    StaticModification(HitPoints.MaxHitPoints, 8),
    StaticModification(Field.Size, Size.Medium),
    StaticModification(Movement.Speed, 25),
    CharacterChoice("Pick first ability boost", [StrengthBoost, DexterityBoost, ConstitutionBoost,
                                                 IntelligenceBoost, WisdomBoost, CharismaBoost], 2),
    StaticModification(Field.Languages, Language.Common),
    StaticModification(Field.Traits, Trait.Human), StaticModification(Field.Traits, Trait.Humanoid),
    StaticModification(Perception.Senses, Senses.Normal)])

core_ancestries = [Dwarf, Elf, Gnome, Goblin, Halfling, Human]

advanced_ancestries = []  # Catfolk, Cobold, Orc, Ratfolk, Tengu, Changeling, Dhampir, Planar scion

omen_ancestries = []  # Android, Aphorite, Beastkin, Fetchling, Fleshwarp, Ganzi, Geniekin, Kitsune, Sprite, Strix

omen2_ancestries = []  # Hobgoblins, Leshies, Lizardfolk,

available_ancestries = core_ancestries + advanced_ancestries + omen_ancestries + omen2_ancestries


def get_heritages(ancestry):
    if ancestry == Dwarf:
        return [AncientDwarf, WardenDwarf, ForgeDwarf, RockDwarf, StrongDwarf]
    elif ancestry == Elf:
        return [ArcticElf, CavernElf, SeerElf, WhisperElf, WoodlandElf]
    elif ancestry == Gnome:
        return [ChameleonGnome, FeyGnome, SensateGnome, UmbralGnome, WellspringGnome]
    elif ancestry == Goblin:
        return [CharhideGoblin, IrongutGoblin, RazortoothGoblin, SnowGoblin, UnbreakableGoblin]
    elif ancestry == Halfling:
        return [GutsyHalfling, HillockHalfling, NomadicHalfling, TwilightHalfling, WildwoodHalfling]
    elif ancestry == Human:
        return [HalfElf, HalfOrc, SkilledHeritage, VersatileHeritage]
    else:
        raise ValueError("Unknown ancestry {}".format(ancestry))
