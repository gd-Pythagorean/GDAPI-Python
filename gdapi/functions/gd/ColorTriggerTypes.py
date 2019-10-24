from gdapi.enums.gd import TriggerType, SpecialColorID

class ColorTriggerTypes():

    '''Provides functions for conversion between color triggers and target Color IDs.'''

    def ConvertToSpecialColorID(self, trigger: TriggerType):
    
        '''Returns the special Color ID the color trigger represents.
        trigger: The color trigger whose target special Color ID to retrieve.'''
    
        if trigger == TriggerType.BG:
            return SpecialColorID.BG
        if trigger == TriggerType.GRND:
            return SpecialColorID.GRND
        if trigger == TriggerType.GRND2:
            return SpecialColorID.GRND2
        if trigger == TriggerType.Obj:
            return SpecialColorID.Obj
        if trigger == TriggerType.Line:
            return SpecialColorID.Line
        if trigger == TriggerType.ThreeDL:
            return SpecialColorID.ThreeDL
        else:
            raise SyntaxError("Invalid color trigger type")

    
    def ConvertToColorID(self, trigger: TriggerType):

        '''Returns the Color ID the color trigger represents.
        trigger: The color trigger whose target Color ID to retrieve.'''

        
        if trigger == TriggerType.Color1:
            return 1
        if trigger == TriggerType.Color2:
            return 2
        if trigger == TriggerType.Color3:
            return 3
        if trigger == TriggerType.Color4:
            return 4
        if trigger == TriggerType.BG:
            return int(SpecialColorID.BG.value)
        if trigger == TriggerType.GRND:
            return int(SpecialColorID.GRND.value)
        if trigger == TriggerType.GRND2:
            return int(SpecialColorID.GRND2.value)
        if trigger == TriggerType.Obj:
            return int(SpecialColorID.Obj.value)
        if trigger == TriggerType.Line:
            return int(SpecialColorID.Line.value)
        if trigger == TriggerType.ThreeDL:
            return int(SpecialColorID.ThreeDL.value)
        else:
            raise SyntaxError("Invalid color trigger type")
