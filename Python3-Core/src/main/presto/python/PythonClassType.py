from datetime import date, time, datetime, timedelta
from presto.type.CategoryType import CategoryType
from presto.type.IntegerType import IntegerType
from presto.type.BooleanType import BooleanType
from presto.type.DecimalType import DecimalType
from presto.type.TextType import TextType
from presto.type.DateType import DateType
from presto.type.TimeType import TimeType
from presto.type.DateTimeType import DateTimeType
from presto.type.PeriodType import PeriodType
from presto.type.AnyType import AnyType
from presto.value.IValue import IValue
from presto.value.Period import Period
from presto.error.InternalError import InternalError


class PythonClassType(CategoryType):
    pythonToPrestoMap = { bool.__name__: BooleanType.instance,
                         int.__name__: IntegerType.instance,
                         float.__name__: DecimalType.instance,
                         str.__name__: TextType.instance,
                         date.__name__: DateType.instance,
                         time.__name__: TimeType.instance,
                         datetime.__name__: DateTimeType.instance,
                         timedelta.__name__: PeriodType.instance,
                         Period.__name__: PeriodType.instance,
                         object.__name__: AnyType.instance
                        }


    def __init__(self, klass):
        super(PythonClassType, self).__init__(klass.__name__)
        self.klass = klass

    def convertPythonTypeToPrestoType(self):
        result = PythonClassType.pythonToPrestoMap.get(self.klass.__name__, None)
        if result is None:
            return self
        else:
            return result

    def convertPythonValueToPrestoValue(self, value):
        if isinstance(value, IValue):
            return value
        type_ = PythonClassType.pythonToPrestoMap.get(self.klass.__name__, None)
        if type_ is not None:
            return type_.convertPythonValueToPrestoValue(value)
        else:
            raise InternalError("Unable to convert:" + type(value).__name__);