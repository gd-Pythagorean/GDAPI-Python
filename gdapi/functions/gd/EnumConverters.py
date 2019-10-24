from gdapi.enums.gd import LevelDifficulty, LevelLength
from gdapi.info.gd.LevelLengths import MinLongLength, MinMediumLength, MinSmallLength, MinTinyLength, MinXLLength, XLLengthRange, LongLengthRange, MediumLengthRange, SmallLengthRange, TinyLengthRange

class EnumConverters():

    '''Provides functions to convert values based on level lengths.'''
    
    def GetLevelLength(self, seconds):

        '''Returns the LevelLength of a level from the seconds.'''
    
        if (seconds >= MinXLLength):
            return LevelLength.XL
        if (seconds >= MinLongLength):
            return LevelLength.Long
        if (seconds >= MinMediumLength):
            return LevelLength.Medium
        if (seconds >= MinSmallLength):
            return LevelLength.Small
        return LevelLength.Tiny
    
    
    def GetLevelLengthRange(self, length: LevelLength):

        '''Returns the respective time length range, given a LevelLength.'''

        if length == LevelLength.XL:
            return XLLengthRange
        if length == LevelLength.Long:
            return LongLengthRange
        if length == LevelLength.Medium:
            return MediumLengthRange
        if length == LevelLength.Small:
            return SmallLengthRange
        if length == LevelLength.Tiny:
            pass
        else:
            return TinyLengthRange
    
    def GetLevelDifficulty(self, stars: int):
        
        '''Returns the LevelDifficulty of a level from the specified star rating.'''

        if stars == 0:
            return LevelDifficulty.Auto
        if stars == 1:
            return LevelDifficulty.Auto
        if stars == 2:
            return LevelDifficulty.Easy
        if stars == 3:
            return LevelDifficulty.Normal
        if stars == 4:
            return LevelDifficulty.Hard
        if stars == 5:
            return LevelDifficulty.Hard
        if stars == 6:
            return LevelDifficulty.Harder
        if stars == 7:
            return LevelDifficulty.Harder
        if stars == 8:
            return LevelDifficulty.Insane
        if stars == 9:
            return LevelDifficulty.Insane
        if stars == 10:
            return LevelDifficulty.Demon
        else:
            return LevelDifficulty.NA
