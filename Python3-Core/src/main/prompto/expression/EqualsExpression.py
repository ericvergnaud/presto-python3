from prompto.expression.IExpression import IExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.EqOp import EqOp
from prompto.grammar.INamedValue import INamedValue
from prompto.runtime.LinkedValue import LinkedValue
from prompto.runtime.LinkedVariable import LinkedVariable
from prompto.store.MatchOp import MatchOp
from prompto.type.BooleanType import BooleanType
from prompto.type.CharacterType import CharacterType
from prompto.type.ContainerType import ContainerType
from prompto.type.NullType import NullType
from prompto.type.TextType import TextType
from prompto.utils.CodeWriter import CodeWriter
from prompto.value.Boolean import Boolean
from prompto.value.IInstance import IInstance
from prompto.value.IValue import IValue
from prompto.value.NullValue import NullValue
from prompto.value.TypeValue import TypeValue
from prompto.error.SyntaxError import SyntaxError

VOWELS = "AEIO" # sufficient here

class EqualsExpression ( IExpression ):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return str(self.left) + " " + str(self.operator) + " " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" ")
        self.operator.toDialect(writer)
        # make this a AN
        if self.operator is EqOp.IS_A or self.operator is EqOp.IS_NOT_A:
            name = str(self.right)
            if name[0] in VOWELS:
                writer.append("n")
        writer.append(" ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        if self.operator in [EqOp.CONTAINS, EqOp.NOT_CONTAINS]:
            if isinstance(lt, ContainerType):
                lt = lt.itemType
            if isinstance(rt, ContainerType):
                rt = rt.itemType
            if lt is not TextType.instance or rt not in [TextType.instance, CharacterType.instance]:
                raise SyntaxError("'contains' only operates on textual values!")
        return BooleanType.instance # can compare all objects

    def interpret(self, context):
        lval = self.left.interpret(context)
        if lval is None:
            lval = NullValue.instance
        rval = self.right.interpret(context)
        if rval is None:
            rval = NullValue.instance
        return self.interpretValues(context, lval, rval)

    def interpretValues(self, context, lval, rval):
        if self.operator is EqOp.IS:
            equal = id(lval)==id(rval)
        elif self.operator is EqOp.IS_NOT:
            equal = id(lval)!=id(rval)
        elif self.operator is EqOp.IS_A:
            equal = self.isA(context,lval,rval)
        elif self.operator is EqOp.IS_NOT_A:
            equal = not self.isA(context,lval,rval)
        elif self.operator is EqOp.EQUALS:
            equal = self.areEqual(context,lval,rval)
        elif self.operator is EqOp.NOT_EQUALS:
            equal = not self.areEqual(context,lval,rval)
        elif self.operator is EqOp.CONTAINS:
            equal = self.contains(context, lval, rval)
        elif self.operator is EqOp.NOT_CONTAINS:
            equal = not self.contains(context, lval, rval)
        else:
            equal = self.roughly(context,lval,rval)
        return Boolean.ValueOf(equal)


    def contains(self, context, lval, rval):
        if isinstance(lval, IValue):
            return lval.Contains(context, rval)
        else:
            return self.areEqual(context,lval,rval)


    def roughly(self, context, lval, rval):
        if self.operator is EqOp.ROUGHLY and isinstance(lval, IValue):
            return lval.Roughly(context, rval)
        else:
            return self.areEqual(context,lval,rval)

    def areEqual(self, context, lval, rval):
        if lval is rval:
            return True
        elif lval is None or rval is None:
            return False
        else:
            return lval==rval

    def isA(self, context, lval, rval):
        if isinstance(lval, IValue) and isinstance(rval, TypeValue):
            actual = lval.GetType(context)
            if actual is NullType.instance:
                return False
            toCheck = rval.value
            return toCheck.isAssignableFrom(context, actual)
        else:
            return False

    def downCast(self, context, setValue):
        if self.operator is EqOp.IS_A:
            name = self.readLeftName()
            if name is not None:
                value = context.getRegisteredValue(INamedValue, name)
                type = self.right.type
                local = context.newChildContext()
                value = LinkedVariable(type, value)
                local.registerValue(value, False)
                if setValue:
                    local.setValue(name, LinkedValue(context))
                context = local
        return context

    def readLeftName(self):
        if isinstance(self.left, InstanceExpression):
            return self.left.name
        elif isinstance(self.left, UnresolvedIdentifier):
            return self.left.name
        else:
            return None

    def interpretAssert(self, context, test):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        result = self.interpretValues(context, lval, rval)
        if result is Boolean.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = str(lval) + " " + self.operator.toString(test.dialect) + " " + str(rval)
        test.printFailedAssertion(context, expected, actual)
        return False

    def interpretQuery(self, context, query):
        value = None
        name = self.readFieldName(self.left)
        if name is not None:
            value = self.right.interpret(context)
        else:
            name = self.readFieldName(self.right)
            if name is not None:
                value = self.left.interpret(context)
            else:
                raise SyntaxError("Unable to interpret predicate")
        if isinstance(value, IInstance):
            value = value.getMemberValue(context, "dbId", False)
        decl = context.findAttribute(name)
        info = None if decl is None else decl.getAttributeInfo()
        data = None if value is None else value.getStorableData()
        match = self.getMatchOp()
        query.verify(info, match, data)
        if self.operator is EqOp.NOT_EQUALS:
            query.Not()


    def getMatchOp(self):
        if self.operator is EqOp.EQUALS:
            return MatchOp.EQUALS
        elif self.operator is EqOp.NOT_EQUALS:
            return MatchOp.EQUALS
        elif self.operator is EqOp.ROUGHLY:
            return MatchOp.ROUGHLY
        elif self.operator is EqOp.CONTAINS:
            return MatchOp.CONTAINS
        elif self.operator is EqOp.NOT_CONTAINS:
            return MatchOp.CONTAINS
        else:
            raise Exception("Not supported:" + str(self.operator))


    def readFieldName(self, exp):
        if isinstance(exp, (UnresolvedIdentifier, InstanceExpression, MemberSelector)):
            return str(exp)
        else:
            return None

