from datetime import datetime
from prompto.type.NativeType import NativeType


class DateTimeType(NativeType):
    instance = None

    def __init__(self):
        super(DateTimeType, self).__init__("DateTime")

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, datetime):
            from prompto.value.DateTime import DateTime
            return DateTime(value)
        else:
            return value  # TODO for now

    def isAssignableTo(self, context, other):
        from prompto.type.AnyType import AnyType
        from prompto.type.DateType import DateType
        from prompto.type.TimeType import TimeType
        return isinstance(other, (DateTimeType, DateType, TimeType, AnyType))

    def checkAdd(self, context, other, tryReverse):
        from prompto.type.PeriodType import PeriodType
        if isinstance(other, PeriodType):
            return self
        else:
            return super(DateTimeType, self).checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.PeriodType import PeriodType
        if isinstance(other, DateTimeType):
            return PeriodType.instance
        elif isinstance(other, PeriodType):
            return self
        else:
            return super(DateTimeType, self).checkSubstract(context, other)


    def checkCompare(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.DateType import DateType
        if isinstance(other, DateType):
            return BooleanType.instance
        elif isinstance(other, DateTimeType):
            return BooleanType.instance
        else:
            return super(DateTimeType, self).checkCompare(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.TextType import TextType
        if "year" == name:
            return IntegerType.instance
        elif "month" == name:
            return IntegerType.instance
        elif "dayOfMonth" == name:
            return IntegerType.instance
        elif "dayOfYear" == name:
            return IntegerType.instance
        elif "hour" == name:
            return IntegerType.instance
        elif "minute" == name:
            return IntegerType.instance
        elif "second" == name:
            return IntegerType.instance
        elif "millisecond" == name:
            return IntegerType.instance
        elif "tzOffset" == name:
            return IntegerType.instance
        elif "tzName" == name:
            return TextType.instance
        else:
            return super(DateTimeType, self).checkMember(context, name)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)


    def toString(self, value):
        return "'" + str(value) + "'"


DateTimeType.instance = DateTimeType()
