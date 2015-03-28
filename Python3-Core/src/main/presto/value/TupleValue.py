from io import StringIO
from presto.literal.Literal import Literal
from presto.type.TupleType import TupleType
from presto.value.BaseValueList import BaseValueList

class TupleValue ( BaseValueList ):

    def __init__(self, items=None, item = None):
        super().__init__(TupleType(), items)
        if item is not None:
            self.items.append(item)

    def newInstance(self, items):
        return TupleValue(items)

    def Add(self, context, value):
        if isinstance(value, BaseValueList):
            return self.merge(value)
        else:
            raise SyntaxError("Illegal: Tuple + " + type(value).__name__)

    def __str__(self):
        with StringIO() as sb:
            sb.write("(")
            for v in self.items:
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len-2)
            sb.write(")")
            return sb.getvalue()

    def toDialect(self, writer):
        writer.append('(')
        if self.size()>0:
            for o in self.items:
                if isinstance(o, Literal):
                    o.toDialect(writer)
                else:
                    writer.append(str(o))
                writer.append(", ")
            writer.trimLast(2)
        writer.append(')')

    def __hash__(self):
        return hash(frozenset(self.items))