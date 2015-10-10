from prompto.type.AnyType import AnyType
from prompto.type.VoidType import VoidType
from prompto.python.PythonClassType import PythonClassType

class PythonStatement(object):

    def __init__(self, expression, isReturn):
        self.expression = expression
        self.isReturn = isReturn

    def __str__(self):
        return ("return " if self.isReturn else "") + str(self.expression)

    def check(self, context):
        return AnyType.instance if self.isReturn else VoidType.instance

    def interpret(self, context, module, returnType):
        o = self.expression.interpret(context, module)
        if self.isReturn:
            if o is not None:
                ct = PythonClassType(type(o))
                o = ct.convertPythonValueToPromptoValue(context, o, returnType)
            return o
        else:
            return None

    def toDialect(self, writer):
        if self.isReturn:
            writer.append("return ")
        self.expression.toDialect(writer)

