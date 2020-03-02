from prompto.param.BaseParameter import BaseParameter
from prompto.param.ITypedParameter import ITypedParameter
from prompto.error.SyntaxError import SyntaxError

class CategoryParameter(BaseParameter, ITypedParameter):

    def __init__(self, itype, name, default=None):
        super(CategoryParameter, self).__init__(name)
        self.itype = itype
        self.resolved = None
        self.defaultExpression = default

    def getSignature(self, dialect):
        return self.getProto()

    def getProto(self):
        return self.itype.typeName

    def __str__(self):
        return self.name + ':' + self.getProto()

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, CategoryParameter):
            return False
        return self.getType() == obj.getType() \
            and self.getName() == obj.getName()


    def register(self, context):
        actual = context.contextForValue(self.name)
        if actual is self:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)
        if self.defaultExpression is not None:
            value = self.defaultExpression.interpret(context)
            context.setValue(self.name, value)


    def check(self, context):
        self.resolve(context)
        self.resolved.checkExists(context)


    def resolve(self, context):
        if self.resolved is None:
            self.resolved = self.itype.resolve(context)


    def getType(self, context=None):
        return self.itype


    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        super(CategoryParameter, self).toDialect(writer)
        if self.defaultExpression is not None:
            writer.append(" = ")
            self.defaultExpression.toDialect(writer)


    def toEDialect(self, writer):
        self.itype.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)


    def toODialect(self, writer):
        self.itype.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)

    def toMDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.itype.toDialect(writer)
