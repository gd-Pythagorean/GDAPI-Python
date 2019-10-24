#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum


class ColorChannelPlayerColor(Enum):

    '''Represents the player color property of a color channel.'''

    _None = -1
    P1 = 1
    P2 = 2


class CustomParticleGrouping(Enum):

    '''Provides values for custom particle grouping types'''

    Free = 0
    Relative = 1
    Grouped = 2


class CustomParticleProperty1(Enum):

    '''Provides values for custom particle property 1.'''

    Gravity = 0
    Radius = 1


class Easing(Enum):

    '''This enumeration provides values for the Easing of a movement command of a trigger.'''

    _None = 0
    EaseInOut = 1
    EaseIn = 2
    EaseOut = 3
    ElasticInOut = 4
    ElasticIn = 5
    ElasticOut = 6
    BounceInOut = 7
    BounceIn = 8
    BounceOut = 9
    ExponentialInOut = 10
    ExponentialIn = 11
    ExponentialOut = 12
    SineInOut = 13
    SineIn = 14
    SineOut = 15
    BackInOut = 16
    BackIn = 17
    BackOut = 18


class EasingMethod(Enum):

    '''This enumeration provides values for the Easing method of a movement command of a trigger.'''

    _None = 0
    Ease = 1
    Elastic = 2
    Bounce = 3
    Exponential = 4
    Sine = 5
    Back = 6


class EasingType(Enum):

    '''Provides values for the easing types.'''

    _None = 0
    Ease = 1 << 2
    Elastic = 1 << 3
    Bounce = 1 << 4
    Exponential = 1 << 5
    Sine = 1 << 6
    Back = 1 << 7

    # Easing Modifiers

    In = 1
    Out = 2
    InOut = In | Out

    # Easing Combinations

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


class PulseMode(Enum):

    '''This enumeration provides values for the Pulse Type of a Pulse trigger.'''

    Color = 0
    HSV = 1


class Gamemode(Enum):

    '''Represents player's gamemode'''

    Cube = 0
    Ship = 1
    Ball = 2
    UFO = 3
    Wave = 4
    Robot = 5
    Spider = 6


class InstantCountComparison(Enum):

    '''This enumeration provides values for the comparison of an Instant Count trigger.'''

    Equals = 0
    Larger = 1
    Smaller = 2


class LevelDifficulty(Enum):

    '''Represents the difficulty of a level.'''

    _None = 0
    NA = 1
    Easy = 2
    Normal = 3
    Hard = 4
    Harder = 5
    Insane = 6
    EasyDemon = 7
    MediumDemon = 8
    HardDemon = 9
    InsaneDemon = 10
    ExtremeDemon = 11
    Auto = 12

    Demon = EasyDemon


class LevelLength(Enum):

    '''This enumeration provides values representing the length of a level.'''

    Tiny = 0
    Small = 1
    Medium = 2
    Long = 3
    XL = 4


class ObjectProperty(Enum):

    ID = 1
    X = 2
    Y = 3
    FlippedHorizontaly = 4
    FlippedVerticaly = 5
    Rotation = 6
    Red = 7
    Green = 8
    Blue = 9
    Duration = 10
    TouchTriggered = 11
    SecretCoinID = 12
    SpecialObjectChecked = 13
    TintGround = 14
    SetColorToPlayerColor1 = 15
    SetColorToPlayerColor2 = 16
    Blending = 17
    UnknownFeature18 = 18
    UnknownFeature19 = 19
    EL1 = 20
    Color1 = 21
    Color2 = 22
    TargetColorID = 23
    ZLayer = 24
    ZOrder = 25
    UnknownFeature26 = 26
    UnknownFeature27 = 27
    OffsetX = 28
    OffsetY = 29
    Easing = 30
    TextObjectText = 31
    Scaling = 32
    UnknownFeature33 = 33
    GroupParent = 34
    Opacity = 35
    UnknownFeature36 = 36
    UnknownFeature37 = 37
    UnknownFeature38 = 38
    UnknownFeature39 = 39
    UnknownFeature40 = 40
    Color1HSVEnabled = 41
    Color2HSVEnabled = 42
    Color1HSVValues = 43
    Color2HSVValues = 44
    FadeIn = 45
    Hold = 46
    FadeOut = 47
    PulseMode = 48
    CopiedColorHSVValues = 49
    CopiedColorID = 50
    TargetGroupID = 51
    TargetType = 52
    UnknownFeature53 = 53
    YellowTeleportationPortalDistance = 54
    UnknownFeature55 = 55
    ActivateGroup = 56
    GroupIDs = 57
    LockToPlayerX = 58
    LockToPlayerY = 59
    CopyOpacity = 60
    EL2 = 61
    SpawnTriggered = 62
    SpawnDelay = 63
    DontFade = 64
    MainOnly = 65
    DetailOnly = 66
    DontEnter = 67
    Degrees = 68
    Times360 = 69
    LockObjectRotation = 70
    FollowGroupID = 71
    TargetPosGroupID = 71
    CenterGroupID = 71
    SecondaryGroupID = 71
    XMod = 72
    YMod = 73
    UnknownFollowTriggerFeature = 74
    Strength = 75
    AnimationID = 76
    Count = 77
    SubtractCount = 78
    PickupMode = 79
    ItemID = 80
    BlockID = 80
    BlockAID = 80
    HoldMode = 81
    ToggleMode = 82
    UnknownFeature83 = 83
    Interval = 84
    EasingRate = 85
    Exclusive = 86
    MultiTrigger = 87
    Comparison = 88
    DualMode = 89
    Speed = 90
    FollowDelay = 91
    YOffset = 92
    TriggerOnExit = 93
    DynamicBlock = 94
    BlockBID = 95
    DisableGlow = 96
    CustomRotationSpeed = 97
    DisableRotation = 98
    MultiActivate = 99
    EnableUseTarget = 100
    TargetPosCoordinates = 101
    EditorDisable = 102
    HighDetail = 103
    UnknownFeature104 = 104
    MaxSpeed = 105
    RandomizeStart = 106
    AnimationSpeed = 107
    LinkedGroupID = 108

    # region General
    UnrevealedTextBoxFeature115 = 115
    SwitchPlayerDirection = 117
    NoEffects = 116
    IceBlock = -201
    NonStick = -202
    Unstuckable = -203
    UnreadableProperty1 = -204
    UnreadableProperty2 = -205
    TransformationScalingX = -206
    TransformationScalingY = -207
    TransformationScalingCenterX = -208
    TransformationScalingCenterY = -209
    # endregion

    # region Camera Offset Trigger
    # endregion

    # region Static Camera Trigger
    ExitStatic = 110
    # endregion

    # region End Trigger
    Reversed = 118
    LockY = 59
    # endregion

    # region Random Trigger
    Chance = 10
    ChanceLots = -300
    ChanceLotGroups = -301
    # endregion

    # region Zoom Trigger
    Zoom = 109
    # endregion

    # region Custom Particle Object
    Grouping = -108
    Property1 = -109
    MaxParticles = -110
    CustomParticleDuration = -111
    Lifetime = -112
    LifetimeAdjustment = -113
    Emission = -114
    Angle = -115
    AngleAdjustment = -116
    CustomParticleSpeed = -117
    SpeedAdjustment = -118
    PosVarX = -119
    PosVarY = -120
    GravityX = -121
    GravityY = -122
    AccelRad = -123
    AccelRadAdjustment = -124
    AccelTan = -125
    AccelTanAdjustment = -126
    StartSize = -127
    StartSizeAdjustment = -128
    EndSize = -129
    EndSizeAdjustment = -130
    StartSpin = -131
    StartSpinAdjustment = -132
    EndSpin = -133
    EndSpinAdjustment = -134
    StartA = -135
    StartAAdjustment = -136
    StartR = -137
    StartRAdjustment = -138
    StartG = -139
    StartGAdjustment = -140
    StartB = -141
    StartBAdjustment = -142
    EndA = -143
    EndAAdjustment = -144
    EndR = -145
    EndRAdjustment = -146
    EndG = -147
    EndGAdjustment = -148
    EndB = -149
    EndBAdjustment = -150
    CustomParticleFadeIn = -151
    FadeInAdjustment = -152
    CustomParticleFadeOut = -153
    FadeOutAdjustment = -15
    Additive = -155
    StartSizeEqualsEnd = -156
    StartSpinEqualsEnd = -157
    StartRadiusEqualsEnd = -158
    StartRotationIsDir = -159
    DynamicRotation = -160
    UseObjectColor = -161
    UniformObjectColor = -162
    Texture = -163
    # endregion

    # region Scale Trigger
    ScaleX = -164
    ScaleY = -165
    LockObjectScale = -166
    OnlyMoveScale = -167
    # endregion

    # region Move Trigger
    LockToCameraX = -302
    LockToCameraY = -303

    # endregion

# TODO:
# Add:
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
