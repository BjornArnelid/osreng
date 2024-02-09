import enum


class MagicTradition:
    def __init__(self, name):
        self.name = name


class SpellType(enum.Enum):
    Cantrip = enum.auto()


class Spell:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class ChoiceOfSpell:
    def __init__(self, tradition, level, number_of_picks, prepared):
        self.tradition = tradition
        self.level = level
        self.number_of_picks = number_of_picks
        self.prepared = prepared


class Cantrip:
    def __init__(self, name):
        self.name = name


class PreparedCantrips:
    def __init__(self, tradition, number_of_picks, prepared):
        self.tradition = tradition
        self.number_of_picks = number_of_picks
        self.prepared = prepared


Arcane = MagicTradition('Arcane')
Divine = MagicTradition('Divine')
Occult = MagicTradition('Occult')
Primal = MagicTradition('Primal')

# Cantrips
AcidSplash = Cantrip("Acid Splash")
ChillTouch = Cantrip("Chill Touch")
DancingLights = Cantrip("Dancing Lights")
Daze = Cantrip("Daze")
DetectMagic = Cantrip("Detect Magic")
ForbiddingWard = Cantrip("Forbidding Ward")
DisruptUndead = Cantrip("Disrupt Undead")
DivineLance = Cantrip("Divine Lance")
ElectricArc = Cantrip("Electric Arc")
GhostSound = Cantrip("Ghost Sound")
Guidance = Cantrip("Guidance")
KnowDirection = Cantrip("Know Direction")
Light = Cantrip("Light")
MageHand = Cantrip("Mage Hand")
Message = Cantrip("Message")
Prestidigitation = Cantrip("Prestidigitation")
ProduceFlame = Cantrip("Produce Flame")
RayOfFrost = Cantrip("Ray of Frost")
ReadAura = Cantrip("Read Aura")
Shield = Cantrip("Shield")
Sigil = Cantrip("Sigil")
Stabilize = Cantrip("Stabilize")
Tanglefoot = Cantrip("Tanglefoot")
TelekineticProjectile = Cantrip("Telekinetic Projectile")

ArcanteCantrips = [AcidSplash, ChillTouch, DancingLights, Daze, DetectMagic, ElectricArc, GhostSound, Light, MageHand,
                   Message, Prestidigitation, ProduceFlame, RayOfFrost, ReadAura, Shield, Sigil, Tanglefoot,
                   TelekineticProjectile]

DivineCantrips = [ChillTouch, Daze, DetectMagic, DisruptUndead, DivineLance, ForbiddingWard, Guidance, KnowDirection,
                  Light, Message, Prestidigitation, ReadAura, Shield, Sigil, Stabilize]

OccultCantrips = [ChillTouch, DancingLights, Daze, DetectMagic, ForbiddingWard, GhostSound, Guidance, KnowDirection,
                  Light, MageHand, Message, Prestidigitation, ReadAura, Shield, Sigil, TelekineticProjectile]

PrimalCantrips = [AcidSplash, DancingLights, DetectMagic, DisruptUndead, ElectricArc, Guidance, KnowDirection, Light,
                  Prestidigitation, ProduceFlame, RayOfFrost, ReadAura, Sigil, Stabilize, Tanglefoot]
