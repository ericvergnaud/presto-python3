from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.CodeParameter import CodeParameter
from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.runtime.ContextFlags import ContextFlags
from prompto.statement.StatementList import StatementList
from prompto.type.DictType import DictType
from prompto.type.IType import IType
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType


class ConcreteMethodDeclaration ( BaseMethodDeclaration ):

    def __init__(self, name, arguments, returnType, statements):
        super(ConcreteMethodDeclaration, self).__init__(name, arguments, returnType)
        if statements is None:
            statements = StatementList()
        self.statements = statements
        self.declarationOf = None
        from prompto.statement.DeclarationStatement import DeclarationStatement
        for statement in statements:
            if isinstance(statement, DeclarationStatement):
                statement.declaration.closureOf = self


    def getStatements(self):
        return self.statements


    def check(self, context, flags:ContextFlags):
        if self.canBeChecked(context):
            return self.fullCheck(context, flags)
        else:
            return VoidType.instance


    def canBeChecked(self, context):
        if context.isGlobalContext():
            return not self.mustBeBeCheckedInCallContext(context)
        else:
            return True


    def mustBeBeCheckedInCallContext(self, context):
        # if at least one argument is 'Code'
        if self.parameters is None:
            return False
        for arg in self.parameters:
            if isinstance(arg, CodeParameter):
                return True
        return False


    def fullCheck(self, context, flags:ContextFlags):
        if flags.isStart:
            context = context.newLocalContext()
            self.registerArguments(context)
        if self.parameters is not None:
            self.parameters.check(context)
        return self.checkStatements(context, self.returnType)


    def checkChild(self, context):
        if self.parameters is not None:
            self.parameters.check(context)
        context = context.newChildContext()
        self.registerArguments(context)
        return self.checkStatements(context, self.returnType)


    def checkStatements(self, context, returnType: IType):
        return self.statements.check(context, returnType)


    def interpret(self, context):
        context.enterMethod(self)
        try:
            return self.statements.interpret(context)
        finally:
            context.leaveMethod(self)


    def isEligibleAsMain(self):
        if self.parameters is None or self.parameters.isEmpty():
            return True
        if self.parameters.size()==1:
            arg = self.parameters[0]
            if isinstance(arg, CategoryParameter):
                itype = arg.getType()
                if isinstance(itype, DictType):
                    return itype.itemType==TextType.instance
        return super(ConcreteMethodDeclaration, self).isEligibleAsMain()


    def toDialect(self, writer):
        if writer.isGlobalContext():
            writer = writer.newLocalWriter()
        self.registerArguments(writer.context)
        super(ConcreteMethodDeclaration, self).toDialect(writer)


    def toMDialect(self, writer):
        writer.append("def ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as method ")
        self.parameters.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning ")
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def toODialect(self, writer):
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("method ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")
