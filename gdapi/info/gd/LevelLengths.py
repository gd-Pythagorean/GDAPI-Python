import sys

MinXLLength = 120
MinLongLength = 60
MinMediumLength = 30
MinSmallLength = 10
MinTinyLength = 0

MaxXLLength = sys.float_info.max
MaxLongLength = 120
MaxMediumLength = 60
MaxSmallLength = 30
MaxTinyLength = 10

XLLengthRange = range(MinXLLength, MaxXLLength)
LongLengthRange = range(MinLongLength, MaxLongLength)
MediumLengthRange = range(MinMediumLength, MaxMediumLength)
SmallLengthRange = range(MinSmallLength, MaxSmallLength)
TinyLengthRange = range(MinTinyLength, MaxTinyLength)