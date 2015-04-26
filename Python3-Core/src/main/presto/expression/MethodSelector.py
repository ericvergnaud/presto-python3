from presto.expression.MemberSelector import MemberSelector
from presto.runtime.Context import Context, InstanceContext
from presto.error.SyntaxError import SyntaxError
from presto.value.NullValue import NullValue
from presto.value.TypeValue import TypeValue


class MethodSelector(MemberSelector):

    def __init__(self, name, parent=None):
        super(MethodSelector, self).__init__(name, parent)

    def __str__(self):
        if self.parent == None:
            return self.name
        else:
            return str(self.parent) + '.' + self.name

    def toDialect(self, writer):
        if self.parent is None:
            writer.append(self.name)
        else:
            super(MethodSelector, self).toDialect(writer)

    def getCandidates(self, context:Context):
        if self.parent == None:
            return self.getGlobalCandidates(context)
        else:
            return self.getCategoryCandidates(context)

    def getGlobalCandidates(self, context:Context):
        from presto.runtime.Context import MethodDeclarationMap
        methods = []
        # if called from a member method, could be a member method called without this/self
        if isinstance(context.getParentContext(), InstanceContext):
            from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
            typ = context.getParentContext().instanceType
            cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, typ.getName())
            if cd is not None:
                members = cd.findMemberMethods(context, self.name)
                if members is not None:
                    methods.extend(members)
        globs = context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if globs is not None:
            methods.extend(globs.values())
        return methods

    def getCategoryCandidates(self, context:Context):
        from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from presto.type.CategoryType import CategoryType
        type_ = self.checkParent(context)
        if not isinstance(type_, CategoryType):
            raise SyntaxError(self.parent.toString() + " is not a category")
        cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, type_.getName())
        if cd is None:
            raise SyntaxError("Unknown category:" + type_.getName())
        return cd.findMemberMethods(context, self.name)

    def newLocalContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context)
        else:
            return context.newLocalContext()

    def newLocalCheckContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceCheckContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context)
        else:
            return context.newLocalContext()

    def newLocalInstanceContext(self, context:Context):
        parent = context.getParentContext()
        if not isinstance(parent, InstanceContext):
            raise SyntaxError("Not in instance context !")
        context = context.newLocalContext()
        context.setParentContext(parent) # make local context child of the existing instance context
        return context

    def newInstanceCheckContext(self, context:Context):
        from presto.type.CategoryType import CategoryType
        typ = self.parent.check (context)
        if not isinstance(typ, CategoryType):
            raise SyntaxError ("Not an instance !")
        context = context.newInstanceContext (None, typ)
        return context.newChildContext ()

    def newInstanceContext(self, context:Context):
        value = self.parent.interpret(context)
        if value == None or value is NullValue.instance:
            from presto.error.NullReferenceError import NullReferenceError
            raise NullReferenceError()
        from presto.type.CategoryType import CategoryType
        if isinstance(value, TypeValue) and isinstance(value.value, CategoryType):
            value = context.loadSingleton(value.value)
        from presto.value.ConcreteInstance import ConcreteInstance
        if not isinstance(value, ConcreteInstance):
            from presto.error.InvalidDataError import InvalidDataError
            raise InvalidDataError("Not a concrete instance !")
        context = context.newInstanceContext(value, None)
        return context.newChildContext()

    def toInstanceExpression(self):
        if self.parent == None:
            from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
            return UnresolvedIdentifier(self.name)
        else:
            return MemberSelector(self.parent, self.name)
