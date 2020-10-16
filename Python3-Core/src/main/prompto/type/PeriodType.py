from prompto.type.BooleanType import *
from prompto.type.NativeType import *


class PeriodType(NativeType):
    instance = None

    def __init__(self):
        super(PeriodType, self).__init__(TypeFamily.PERIOD)


    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, PeriodType):
            return self
        else:
            return super(PeriodType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, PeriodType):
            return self
        else:
            return super(PeriodType, self).checkSubstract(context, other)

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        else:
            return super(PeriodType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        if isinstance(other, PeriodType):
            return BooleanType.instance
        else:
            return super(PeriodType, self).checkCompare(context, other)

    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "years" == name:
            return IntegerType.instance
        elif "months" == name:
            return IntegerType.instance
        elif "weeks" == name:
            return IntegerType.instance
        elif "days" == name:
            return IntegerType.instance
        elif "hours" == name:
            return IntegerType.instance
        elif "minutes" == name:
            return IntegerType.instance
        elif "seconds" == name:
            return IntegerType.instance
        elif "milliseconds" == name:
            return IntegerType.instance
        else:
            return super(PeriodType, self).checkMember(context, name)

PeriodType.instance = PeriodType()

