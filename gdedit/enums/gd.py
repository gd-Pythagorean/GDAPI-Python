# from enum import Enum

class ColorChannelPlayerColor():
    '''Represents the player color property of a color channel.'''
    _None = -1
    P1    = 1
    P2    = 2

class CustomParticleGrouping():
    '''Provides values for custom particle grouping types'''
    Free     = 0
    Relative = 1
    Grouped  = 2

class CustomParticleProperty1():
    Gravity = 0
    Radius  = 1

class Easing():
    _None            = 0
    EaseInOut        = 1
    EaseIn           = 2
    EaseOut          = 3
    ElasticInOut     = 4
    ElasticIn        = 5
    ElasticOut       = 6
    BounceInOut      = 7
    BounceIn         = 8
    BounceOut        = 9
    ExponentialInOut = 10
    ExponentialIn    = 11
    ExponentialOut   = 12
    SineInOut        = 13
    SineIn           = 14
    SineOut          = 15
    BackInOut        = 16
    BackIn           = 17
    BackOut          = 18


class EasingMethod():
    _None       = 0
    Ease        = 1
    Elastic     = 2
    Bounce      = 3
    Exponential = 4
    Sine        = 5
    Back        = 6
    
class EasingType():
    _None = 0
    Ease = 1 << 2
    Elastic = 1 << 3
    Bounce = 1 << 4
    Exponential = 1 << 5
    Sine = 1 << 6
    Back = 1 << 7

#     Easing Modifiers
    In = 1
    Out = 2
    InOut = In | Out

#     Easing Combinations
    EaseInOut = Ease | InOut
    EaseIn = Ease | In
    EaseOut = Ease | Out
    ElasticInOut = Elastic | InOut
    ElasticIn = Elastic | In
    ElasticOut = Elastic | Out
    BounceInOut = Bounce | InOut
    BounceIn = Bounce | In
    BounceOut = Bounce | Out
    ExponentialInOut = Exponential | InOut
    ExponentialIn = Exponential | In
    ExponentialOut = Exponential | Out
    SineInOut = Sine | InOut
    SineIn = Sine | In
    SineOut = Sine | Out
    BackInOut = Back | InOut
    BackIn = Back | In
    BackOut = Back | Out

class PulseMode():
    '''This enumeration provides values for the Pulse Type of a Pulse trigger.'''
    Color = 1
    HSV   = 2

# TODO: 
# Add:
#     Gamemode
#     InstantCountComparison
#     LevelDifficulty
#     LevelLength
#     ObjectProperty
#     OrbType
#     PadType
#     PickupItemPickupMode
#     PlayerSize
#     PortalType
#     PulseMode
#     PulseTargetType
#     SpecialBlockType
#     SpecialColorID
#     SpecialObjectType
#     Speed
#     TargetPosCoordinates
#     TouchToggleMode
#     TriggerType
#     ZLayer
#     ZLayerPosition.cs 
