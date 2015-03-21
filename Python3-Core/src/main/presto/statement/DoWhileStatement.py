from presto.error.InvalidDataError import InvalidDataError
from presto.statement.BaseStatement import BaseStatement
from presto.type.BooleanType import BooleanType
from presto.value.Boolean import Boolean


class DoWhileStatement ( BaseStatement ):

    def __init__(self, condition, instructions):
        super().__init__()
        self.condition = condition
        self.instructions = instructions

    def getCondition(self):
        return self.condition

    def getInstructions(self):
        return self.instructions

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean condition!")
        child = context.newChildContext()
        return self.instructions.check(child)

    def interpret(self, context):
        while True:
            child = context.newChildContext()
            value = self.instructions.interpret(child)
            if value is not None:
                return value
            if not self.interpretCondition(context):
                return None
        return None

    def interpretCondition(self, context):
        value = self.condition.interpret(context)
        if not isinstance(value, Boolean):
            raise InvalidDataError("Expected a Boolean, got:" + type(value).__name__)
        return value.value

    def toEDialect(self, writer):
        writer.append("do:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("while ")
        self.condition.toDialect(writer)
        writer.newLine()

    def toODialect(self, writer):
        writer.append("do {\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("} while (")
        self.condition.toDialect(writer)
        writer.append(");\n")

    def toPDialect(self, writer):
        self.toEDialect(writer)
