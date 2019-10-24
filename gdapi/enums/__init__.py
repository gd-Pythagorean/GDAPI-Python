from enum import Enum

class IDMigrationMode(Enum):

    '''Represents the mode of an ID migration operation.'''

    Groups = 0
    Colors = 1
    Items  = 2
    Blocks = 3


class MusicalNoteValue(Enum):

    '''Represents a note value.'''

    Whole               = 1
    Half                = 2
    Quarter             = 4
    Eighth              = 8
    Sixteenth           = 16
    ThirtySecond        = 32
    SixtyFourth         = 64
    HundredTwentyEighth = 128


class PathItemType(Enum):

    '''Represents the type of an item in a path.'''

    File      = 0
    Directory = 1
    Volume    = 2
