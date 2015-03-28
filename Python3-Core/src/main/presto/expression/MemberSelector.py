from presto.error.NullReferenceError import NullReferenceError
from presto.expression.IExpression import IExpression
from presto.expression.SelectorExpression import SelectorExpression
from presto.expression.SymbolExpression import SymbolExpression
from presto.expression.TypeExpression import TypeExpression
from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
from presto.value.IValue import IValue
from presto.value.NullValue import NullValue
from presto.value.Text import Text
from presto.error.SyntaxError import SyntaxError

class MemberSelector (SelectorExpression):

    def __init__(self, name, parent = None):
        super(MemberSelector, self).__init__(parent)
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return str(self.parent) + "." + self.name

    def toDialect(self, writer):
        try:
            self.resolveParent(writer.context)
        except:
            pass # ignore
        self.parent.toDialect(writer)
        writer.append(".")
        writer.append(self.name)

    def check(self, context):
        parentType = self.checkParent(context)
        return parentType.checkMember(context, self.name)

    def interpret(self, context):
        # resolve parent to keep clarity
        parent = self.resolveParent(context)
        # special case for Symbol which evaluates as value
        value = self.interpretSymbol(context, parent)
        if value is not None:
            return value
        # special case for singletons
        value = self.interpretSingleton(context, parent)
        if value is not None:
            return value
        # special case for 'static' type members (like Enum.symbols, Type.name etc...)
        value = self.interpretTypeMember(context, parent)
        if value is not None:
            return value
        # finally resolve instance member
        return self.interpretInstanceMember(context, parent)


    def interpretInstanceMember(self, context, parent):
        instance = parent.interpret(context)
        if instance is None or instance is NullValue.instance:
            raise NullReferenceError()
        else:
            return instance.getMember(context, self.name)

    def interpretTypeMember(self, context, parent):
       if isinstance(parent, TypeExpression):
           return parent.getMember(context, self.name)
       else:
           return None

    def interpretSingleton(self, context, parent):
        from presto.type.CategoryType import CategoryType
        if isinstance(parent, TypeExpression) and isinstance(parent.type, CategoryType):
            instance = context.loadSingleton(parent.type)
            if instance is not None:
                return instance.getMember(context, self.name)
        return None

    def interpretSymbol(self, context, parent):
        if isinstance(parent, SymbolExpression):
            if "name"==self.name:
                return Text(parent.name)
            if "value"==self.name:
                return parent.interpret(context)
        return None

    def resolveParent(self, context):
        if isinstance(self.parent, UnresolvedIdentifier):
            self.parent.checkMember(context)
            return self.parent.resolved
        else:
            return self.parent