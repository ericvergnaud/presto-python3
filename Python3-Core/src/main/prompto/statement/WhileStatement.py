from prompto.error.InvalidDataError import InvalidDataError
from prompto.runtime.BreakResult import BreakResult
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class WhileStatement ( BaseStatement ):

    def __init__(self, condition, statements):
        super(WhileStatement, self).__init__()
        self.condition = condition
        self.statements = statements

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean condition!")
        child = context.newChildContext()
        return self.statements.check(child, None)

    def interpret(self, context):
        while self.interpretCondition(context):
            child = context.newChildContext()
            value = self.statements.interpret(child)
            if value is BreakResult.instance:
                break
            if value is not None:
                return value
        return None

    def interpretCondition(self, context):
        value = self.condition.interpret(context)
        if not isinstance(value, Boolean):
            raise InvalidDataError("Expected a Boolean, got:" + type(value).__name__)
        return value.value

    def toEDialect(self, writer):
        writer.append("while ")
        self.condition.toDialect(writer)
        writer.append(" :\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("while (")
        self.condition.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")

    def toSDialect(self, writer):
        self.toEDialect(writer)


