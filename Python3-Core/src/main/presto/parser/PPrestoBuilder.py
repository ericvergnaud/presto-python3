from antlr4 import ParserRuleContext
from antlr4.tree.Tree import ParseTree
from presto.csharp.CSharpBooleanLiteral import CSharpBooleanLiteral
from presto.csharp.CSharpCharacterLiteral import CSharpCharacterLiteral
from presto.csharp.CSharpDecimalLiteral import CSharpDecimalLiteral
from presto.csharp.CSharpExpressionList import CSharpExpressionList
from presto.csharp.CSharpIdentifierExpression import CSharpIdentifierExpression
from presto.csharp.CSharpIntegerLiteral import CSharpIntegerLiteral
from presto.csharp.CSharpMethodExpression import CSharpMethodExpression
from presto.csharp.CSharpNativeCall import CSharpNativeCall
from presto.csharp.CSharpNativeCategoryMapping import CSharpNativeCategoryMapping
from presto.csharp.CSharpStatement import CSharpStatement
from presto.csharp.CSharpTextLiteral import CSharpTextLiteral
from presto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from presto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from presto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from presto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from presto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from presto.declaration.MemberMethodDeclaration import MemberMethodDeclaration
from presto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from presto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from presto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from presto.declaration.TestMethodDeclaration import TestMethodDeclaration
from presto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from presto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from presto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from presto.expression.AddExpression import AddExpression
from presto.expression.AndExpression import AndExpression
from presto.expression.CastExpression import CastExpression
from presto.expression.CodeExpression import CodeExpression
from presto.expression.CompareExpression import CompareExpression
from presto.expression.ConstructorExpression import ConstructorExpression
from presto.expression.ContainsExpression import ContainsExpression
from presto.expression.DivideExpression import DivideExpression
from presto.expression.DocumentExpression import DocumentExpression
from presto.expression.EqualsExpression import EqualsExpression
from presto.expression.ExecuteExpression import ExecuteExpression
from presto.expression.FetchExpression import FetchExpression
from presto.expression.IntDivideExpression import IntDivideExpression
from presto.expression.ItemSelector import ItemSelector
from presto.expression.MemberSelector import MemberSelector
from presto.expression.MethodExpression import MethodExpression
from presto.expression.MethodSelector import MethodSelector
from presto.expression.MinusExpression import MinusExpression
from presto.expression.ModuloExpression import ModuloExpression
from presto.expression.MultiplyExpression import MultiplyExpression
from presto.expression.NotExpression import NotExpression
from presto.expression.OrExpression import OrExpression
from presto.expression.ParenthesisExpression import ParenthesisExpression
from presto.expression.ReadExpression import ReadExpression
from presto.expression.SliceSelector import SliceSelector
from presto.expression.SortedExpression import SortedExpression
from presto.expression.SubtractExpression import SubtractExpression
from presto.expression.SymbolExpression import SymbolExpression
from presto.expression.TernaryExpression import TernaryExpression
from presto.expression.ThisExpression import ThisExpression
from presto.expression.TypeExpression import TypeExpression
from presto.grammar.CmpOp import CmpOp
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.ArgumentList import ArgumentList
from presto.grammar.CategoryArgument import CategoryArgument
from presto.grammar.CategoryMethodDeclarationList import CategoryMethodDeclarationList
from presto.grammar.CategorySymbol import CategorySymbol
from presto.grammar.CategorySymbolList import CategorySymbolList
from presto.grammar.CodeArgument import CodeArgument
from presto.grammar.ContOp import ContOp
from presto.grammar.DeclarationList import DeclarationList
from presto.grammar.EqOp import EqOp
from presto.grammar.IdentifierList import IdentifierList
from presto.grammar.ItemInstance import ItemInstance
from presto.grammar.MatchingCollectionConstraint import MatchingCollectionConstraint
from presto.grammar.MatchingExpressionConstraint import MatchingExpressionConstraint
from presto.grammar.MatchingPatternConstraint import MatchingPatternConstraint
from presto.grammar.MemberInstance import MemberInstance
from presto.grammar.NativeCategoryMappingList import NativeCategoryMappingList
from presto.grammar.NativeSymbol import NativeSymbol
from presto.grammar.NativeSymbolList import NativeSymbolList
from presto.grammar.Operator import Operator
from presto.grammar.UnresolvedArgument import UnresolvedArgument
from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
from presto.grammar.VariableInstance import VariableInstance
from presto.java.JavaBooleanLiteral import JavaBooleanLiteral
from presto.java.JavaCharacterLiteral import JavaCharacterLiteral
from presto.java.JavaDecimalLiteral import JavaDecimalLiteral
from presto.java.JavaExpressionList import JavaExpressionList
from presto.java.JavaIdentifierExpression import JavaIdentifierExpression
from presto.java.JavaIntegerLiteral import JavaIntegerLiteral
from presto.java.JavaItemExpression import JavaItemExpression
from presto.java.JavaMethodExpression import JavaMethodExpression
from presto.java.JavaNativeCall import JavaNativeCall
from presto.java.JavaNativeCategoryMapping import JavaNativeCategoryMapping
from presto.java.JavaStatement import JavaStatement
from presto.java.JavaTextLiteral import JavaTextLiteral
from presto.javascript.JavaScriptBooleanLiteral import JavaScriptBooleanLiteral
from presto.javascript.JavaScriptCharacterLiteral import JavaScriptCharacterLiteral
from presto.javascript.JavaScriptDecimalLiteral import JavaScriptDecimalLiteral
from presto.javascript.JavaScriptExpressionList import JavaScriptExpressionList
from presto.javascript.JavaScriptIdentifierExpression import JavaScriptIdentifierExpression
from presto.javascript.JavaScriptIntegerLiteral import JavaScriptIntegerLiteral
from presto.javascript.JavaScriptMethodExpression import JavaScriptMethodExpression
from presto.javascript.JavaScriptModule import JavaScriptModule
from presto.javascript.JavaScriptNativeCall import JavaScriptNativeCall
from presto.javascript.JavaScriptNativeCategoryMapping import JavaScriptNativeCategoryMapping
from presto.javascript.JavaScriptStatement import JavaScriptStatement
from presto.javascript.JavaScriptTextLiteral import JavaScriptTextLiteral
from presto.literal.BooleanLiteral import BooleanLiteral
from presto.literal.CharacterLiteral import CharacterLiteral
from presto.literal.DateLiteral import DateLiteral
from presto.literal.DateTimeLiteral import DateTimeLiteral
from presto.literal.DecimalLiteral import DecimalLiteral
from presto.literal.DictEntry import DictEntry
from presto.literal.DictEntryList import DictEntryList
from presto.literal.DictLiteral import DictLiteral
from presto.literal.HexaLiteral import HexaLiteral
from presto.literal.IntegerLiteral import IntegerLiteral, MaxIntegerLiteral, MinIntegerLiteral
from presto.literal.ListLiteral import ListLiteral
from presto.literal.NullLiteral import NullLiteral
from presto.literal.PeriodLiteral import PeriodLiteral
from presto.literal.RangeLiteral import RangeLiteral
from presto.literal.SetLiteral import SetLiteral
from presto.literal.TextLiteral import TextLiteral
from presto.literal.TimeLiteral import TimeLiteral
from presto.literal.TupleLiteral import TupleLiteral
from presto.parser.PParser import PParser
from presto.parser.PParserListener import PParserListener
from presto.parser.Section import Section
from presto.parser.Dialect import Dialect
from presto.python.PythonArgument import PythonNamedArgument, PythonArgumentList
from presto.python.PythonBooleanLiteral import PythonBooleanLiteral
from presto.python.PythonCharacterLiteral import PythonCharacterLiteral
from presto.python.PythonDecimalLiteral import PythonDecimalLiteral
from presto.python.PythonIdentifierExpression import PythonIdentifierExpression
from presto.python.PythonIntegerLiteral import PythonIntegerLiteral
from presto.python.PythonMethodExpression import PythonMethodExpression
from presto.python.PythonModule import PythonModule
from presto.python.PythonNativeCall import Python2NativeCall, Python3NativeCall, PythonNativeCall
from presto.python.PythonNativeCategoryMapping import PythonNativeCategoryMapping, Python2NativeCategoryMapping, \
    Python3NativeCategoryMapping
from presto.python.PythonStatement import PythonStatement
from presto.python.PythonTextLiteral import PythonTextLiteral
from presto.statement.AssignInstanceStatement import AssignInstanceStatement
from presto.statement.AssignTupleStatement import AssignTupleStatement
from presto.statement.AssignVariableStatement import AssignVariableStatement
from presto.statement.AtomicSwitchCase import AtomicSwitchCase
from presto.statement.CollectionSwitchCase import CollectionSwitchCase
from presto.statement.DeclarationInstruction import DeclarationInstruction
from presto.statement.DoWhileStatement import DoWhileStatement
from presto.statement.ForEachStatement import ForEachStatement
from presto.statement.IfStatement import IfElement, IfElementList, IfStatement
from presto.statement.UnresolvedCall import UnresolvedCall
from presto.statement.RaiseStatement import RaiseStatement
from presto.statement.ReturnStatement import ReturnStatement
from presto.statement.StatementList import StatementList
from presto.statement.SwitchCase import SwitchCaseList
from presto.statement.SwitchErrorStatement import SwitchErrorStatement
from presto.statement.SwitchStatement import SwitchStatement
from presto.statement.WhileStatement import WhileStatement
from presto.statement.WithResourceStatement import WithResourceStatement
from presto.statement.WithSingletonStatement import WithSingletonStatement
from presto.statement.WriteStatement import WriteStatement
from presto.type.AnyType import AnyType
from presto.type.BooleanType import BooleanType
from presto.type.CategoryType import CategoryType
from presto.type.CharacterType import CharacterType
from presto.type.CodeType import CodeType
from presto.type.DateType import DateType
from presto.type.DecimalType import DecimalType
from presto.type.DictType import DictType
from presto.type.DocumentType import DocumentType
from presto.type.IntegerType import IntegerType
from presto.type.ListType import ListType
from presto.type.TextType import TextType
from presto.type.TimeType import TimeType


class PPrestoBuilder(PParserListener):

    def __init__(self, parser:PParser):
        self.input = parser.getTokenStream()
        self.path = parser.path
        self.nodeValues = dict()

    def getNodeValue(self, node:ParseTree) -> object:
        return self.nodeValues.get(node, None)

    def setNodeValue(self, node:ParseTree, value:object):
        self.nodeValues[node] = value
        if isinstance(value, Section):
            self.buildSection(node, value)

    def buildSection(self, node:ParserRuleContext, section:Section):
        first = self.findFirstValidToken(node.start.tokenIndex)
        last = self.findLastValidToken(node.stop.tokenIndex)
        section.setFrom(self.path, first, last, Dialect.P)

    def findFirstValidToken(self, idx:int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx < len(self.input.tokens):
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx += 1
        return None

    def findLastValidToken(self, idx:int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx >= 0:
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx -= 1
        return None

    def readValidToken(self, idx:int):
        token = self.input.tokens[idx]
        text = token.text
        if text is not None and len(text) > 0 and not text[0].isspace():
            return token
        else:
            return None


    def exitAbstract_method_declaration(self, ctx:PParser.Abstract_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, type))


    def exitAbstractMethod(self, ctx:PParser.AbstractMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitAddExpression(self, ctx:PParser.AddExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = AddExpression(left, right) if ctx.op.type == PParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)


    def exitAndExpression(self, ctx:PParser.AndExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))


    def exitAnyArgumentType(self, ctx:PParser.AnyArgumentTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, type)


    def exitAnyDictType(self, ctx:PParser.AnyDictTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, DictType(type))


    def exitAnyListType(self, ctx:PParser.AnyListTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, ListType(type))


    def exitAnyType(self, ctx:PParser.AnyTypeContext):
        self.setNodeValue(ctx, AnyType.instance)


    def exitArgument_assignment(self, ctx:PParser.Argument_assignmentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedArgument(name)
        item = ArgumentAssignment(arg, exp)
        self.setNodeValue(ctx, item)


    def exitArgumentAssignmentList(self, ctx:PParser.ArgumentAssignmentListContext):
        item = self.getNodeValue(ctx.item)
        items = ArgumentAssignmentList(item=item)
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentListItem(self, ctx:PParser.ArgumentAssignmentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitArgumentList(self, ctx:PParser.ArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, ArgumentList(item))


    def exitArgumentListItem(self, ctx:PParser.ArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitAssertion(self, ctx:PParser.AssertionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertionList(self, ctx:PParser.AssertionListContext):
        item = self.getNodeValue(ctx.item)
        items = [ item ]
        self.setNodeValue(ctx, items)


    def exitAssertionListItem(self, ctx:PParser.AssertionListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.push(item)
        self.setNodeValue(ctx, items)


    def exitAssign_instance_statement(self, ctx:PParser.Assign_instance_statementContext):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))


    def exitAssign_tuple_statement(self, ctx:PParser.Assign_tuple_statementContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)


    def exitAssign_variable_statement(self, ctx:PParser.Assign_variable_statementContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))


    def exitAssignInstanceStatement(self, ctx:PParser.AssignInstanceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAssignTupleStatement(self, ctx:PParser.AssignTupleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAtomicLiteral(self, ctx:PParser.AtomicLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAtomicSwitchCase(self, ctx:PParser.AtomicSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))


    def exitAttribute_declaration(self, ctx:PParser.Attribute_declarationContext):
        name = self.getNodeValue(ctx.name)
        type = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(ctx.match)
        self.setNodeValue(ctx, AttributeDeclaration(name, type, match))


    def exitAttribute_list(self, ctx:PParser.Attribute_listContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitAttributeDeclaration(self, ctx:PParser.AttributeDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitBooleanLiteral(self, ctx:PParser.BooleanLiteralContext):
        self.setNodeValue(ctx, BooleanLiteral(ctx.t.text))


    def exitBooleanType(self, ctx:PParser.BooleanTypeContext):
        self.setNodeValue(ctx, BooleanType.instance)


    def exitCallableRoot(self, ctx:PParser.CallableRootContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitCastExpression(self, ctx:PParser.CastExpressionContext):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ))

    def exitCatchAtomicStatement(self, ctx:PParser.CatchAtomicStatementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))


    def exitCatchCollectionStatement(self, ctx:PParser.CatchCollectionStatementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCatchStatementList(self, ctx:PParser.CatchStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitCatchStatementListItem(self, ctx:PParser.CatchStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitCategory_symbol(self, ctx:PParser.Category_symbolContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))


    def exitCategory_type(self, ctx:PParser.Category_typeContext):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))


    def exitCategoryArgumentType(self, ctx:PParser.CategoryArgumentTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, type)


    def exitCategoryDeclaration(self, ctx:PParser.CategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitCategoryMethodList(self, ctx:PParser.CategoryMethodListContext):
        item = self.getNodeValue(ctx.item)
        items = CategoryMethodDeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitCategoryMethodListItem(self, ctx:PParser.CategoryMethodListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategorySymbolList(self, ctx:PParser.CategorySymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CategorySymbolList(item))


    def exitCategorySymbolListItem(self, ctx:PParser.CategorySymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategoryType(self, ctx:PParser.CategoryTypeContext):
        type = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, type)


    def exitCharacterLiteral(self, ctx:PParser.CharacterLiteralContext):
        self.setNodeValue(ctx, CharacterLiteral(ctx.t.text))


    def exitCharacterType(self, ctx:PParser.CharacterTypeContext):
        self.setNodeValue(ctx, CharacterType.instance)


    def exitChildInstance(self, ctx:PParser.ChildInstanceContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitClosure_expression(self, ctx:PParser.Closure_expressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))


    def exitClosureExpression(self, ctx:PParser.ClosureExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitClosureStatement(self, ctx:PParser.ClosureStatementContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationInstruction(decl))


    def exitCode_argument(self, ctx:PParser.Code_argumentContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeArgument(name))


    def exitCode_type(self, ctx:PParser.Code_typeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCodeArgument(self, ctx:PParser.CodeArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitCodeExpression(self, ctx:PParser.CodeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))


    def exitCodeType(self, ctx:PParser.CodeTypeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCollectionLiteral(self, ctx:PParser.CollectionLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCollectionSwitchCase(self, ctx:PParser.CollectionSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitConcrete_category_declaration(self, ctx:PParser.Concrete_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteCategoryDeclaration(name)
        ccd.setAttributes(attrs)
        ccd.setDerivedFrom(derived)
        ccd.setMethods(methods)
        self.setNodeValue(ctx, ccd)


    def exitConcrete_method_declaration(self, ctx:PParser.Concrete_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, type, stmts))


    def exitConcreteCategoryDeclaration(self, ctx:PParser.ConcreteCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConcreteMethod(self, ctx:PParser.ConcreteMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConstructor_expression(self, ctx:PParser.Constructor_expressionContext):
        type = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(type, args))


    def exitConstructorExpression(self, ctx:PParser.ConstructorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitContainsAllExpression(self, ctx:PParser.ContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ALL, right))


    def exitContainsAnyExpression(self, ctx:PParser.ContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ANY, right))


    def exitContainsExpression(self, ctx:PParser.ContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS, right))


    def exitCsharp_identifier(self, ctx:PParser.Csharp_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitCsharp_method_expression(self, ctx:PParser.Csharp_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))


    def exitCSharpArgumentList(self, ctx:PParser.CSharpArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))


    def exitCSharpArgumentListItem(self, ctx:PParser.CSharpArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitCSharpBooleanLiteral(self, ctx:PParser.CSharpBooleanLiteralContext):
        self.setNodeValue(ctx, CSharpBooleanLiteral(ctx.getText()))


    def exitCSharpCategoryMapping(self, ctx:PParser.CSharpCategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, CSharpNativeCategoryMapping(map))


    def exitCSharpCharacterLiteral(self, ctx:PParser.CSharpCharacterLiteralContext):
        self.setNodeValue(ctx, CSharpCharacterLiteral(ctx.getText()))


    def exitCSharpChildIdentifier(self, ctx:PParser.CSharpChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)


    def exitCSharpDecimalLiteral(self, ctx:PParser.CSharpDecimalLiteralContext):
        self.setNodeValue(ctx, CSharpDecimalLiteral(ctx.getText()))


    def exitCSharpIdentifier(self, ctx:PParser.CSharpIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitCSharpIdentifierExpression(self, ctx:PParser.CSharpIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpIntegerLiteral(self, ctx:PParser.CSharpIntegerLiteralContext):
        self.setNodeValue(ctx, CSharpIntegerLiteral(ctx.getText()))


    def exitCSharpLiteralExpression(self, ctx:PParser.CSharpLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpMethodExpression(self, ctx:PParser.CSharpMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpNativeStatement(self, ctx:PParser.CSharpNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitCSharpPrimaryExpression(self, ctx:PParser.CSharpPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpReturnStatement(self, ctx:PParser.CSharpReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitCSharpSelectorExpression(self, ctx:PParser.CSharpSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitCSharpStatement(self, ctx:PParser.CSharpStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, False))


    def exitCSharpTextLiteral(self, ctx:PParser.CSharpTextLiteralContext):
        self.setNodeValue(ctx, CSharpTextLiteral(ctx.getText()))


    def exitDateLiteral(self, ctx:PParser.DateLiteralContext):
        self.setNodeValue(ctx, DateLiteral(ctx.t.text))


    def exitDateTimeLiteral(self, ctx:PParser.DateTimeLiteralContext):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.t.text))


    def exitDateTimeType(self, ctx:PParser.DateTimeTypeContext):
        self.setNodeValue(ctx, TextType.instance)


    def exitDateType(self, ctx:PParser.DateTypeContext):
        self.setNodeValue(ctx, DateType.instance)


    def exitDecimalLiteral(self, ctx:PParser.DecimalLiteralContext):
        self.setNodeValue(ctx, DecimalLiteral(ctx.t.text))


    def exitDecimalType(self, ctx:PParser.DecimalTypeContext):
        self.setNodeValue(ctx, DecimalType.instance)


    def exitDeclarationList(self, ctx:PParser.DeclarationListContext):
        item = self.getNodeValue(ctx.item)
        items = DeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitDeclarationListItem(self, ctx:PParser.DeclarationListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitDerived_list(self, ctx:PParser.Derived_listContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitDict_entry(self, ctx:PParser.Dict_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDict_literal(self, ctx:PParser.Dict_literalContext):
        items = self.getNodeValue(ctx.items)
        value = DictLiteral(items)
        self.setNodeValue(ctx, value)


    def exitDictEntryList(self, ctx:PParser.DictEntryListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, DictEntryList(item))


    def exitDictEntryListItem(self, ctx:PParser.DictEntryListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitDictLiteral(self, ctx:PParser.DictLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDictType(self, ctx:PParser.DictTypeContext):
        type = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(type))


    def exitDivideExpression(self, ctx:PParser.DivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, DivideExpression(left, right))


    def exitDo_while_statement(self, ctx:PParser.Do_while_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, DoWhileStatement(exp, stmts))


    def exitDocument_expression(self, ctx:PParser.Document_expressionContext):
        self.setNodeValue(ctx, DocumentExpression())


    def exitDocument_type(self, ctx:PParser.Document_typeContext):
        self.setNodeValue(ctx, DocumentType.instance)


    def exitDocumentExpression(self, ctx:PParser.DocumentExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDoWhileStatement(self, ctx:PParser.DoWhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitElseIfStatementList(self, ctx:PParser.ElseIfStatementListContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        self.setNodeValue(ctx, IfElementList(elem))


    def exitElseIfStatementListItem(self, ctx:PParser.ElseIfStatementListItemContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        items.add(elem)
        self.setNodeValue(ctx, items)


    def exitEnum_category_declaration(self, ctx:PParser.Enum_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        parent = self.getNodeValue(ctx.derived)
        derived = None if parent is None else IdentifierList(parent)
        symbols = self.getNodeValue(ctx.symbols)
        ecd = EnumeratedCategoryDeclaration(name)
        ecd.setAttributes(attrs)
        ecd.setDerivedFrom(derived)
        ecd.setSymbols(symbols)
        self.setNodeValue(ctx, ecd)


    def exitEnum_native_declaration(self, ctx:PParser.Enum_native_declarationContext):
        name = self.getNodeValue(ctx.name)
        type = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, type, symbols))


    def exitEnumCategoryDeclaration(self, ctx:PParser.EnumCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEnumDeclaration(self, ctx:PParser.EnumDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEnumNativeDeclaration(self, ctx:PParser.EnumNativeDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEqualsExpression(self, ctx:PParser.EqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.EQUALS, right))


    def exitExecuteExpression(self, ctx:PParser.ExecuteExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))


    def exitExpressionAssignmentList(self, ctx:PParser.ExpressionAssignmentListContext):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentAssignmentList()
        items.append(ArgumentAssignment(None, exp))
        self.setNodeValue(ctx, items)


    def exitFetch_expression(self, ctx:PParser.Fetch_expressionContext):
        itemName = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        filter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchExpression(itemName, source, filter))


    def exitFetchExpression(self, ctx:PParser.FetchExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitFor_each_statement(self, ctx:PParser.For_each_statementContext):
        name1 = self.getNodeValue(ctx.name1)
        name2 = self.getNodeValue(ctx.name2)
        source = self.getNodeValue(ctx.source)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ForEachStatement(name1, name2, source, stmts))


    def exitForEachStatement(self, ctx:PParser.ForEachStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitFullDeclarationList(self, ctx:PParser.FullDeclarationListContext):
        items = self.getNodeValue(ctx.items)
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)


    def exitGetter_method_declaration(self, ctx:PParser.Getter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))


    def exitGetterMethod(self, ctx:PParser.GetterMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitGreaterThanExpression(self, ctx:PParser.GreaterThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GT, right))


    def exitGreaterThanOrEqualExpression(self, ctx:PParser.GreaterThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GTE, right))


    def exitHexadecimalLiteral(self, ctx:PParser.HexadecimalLiteralContext):
        self.setNodeValue(ctx, HexaLiteral(ctx.t.text))


    def exitIdentifierExpression(self, ctx:PParser.IdentifierExpressionContext):
        name = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitIf_statement(self, ctx:PParser.If_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elseIfs = self.getNodeValue(ctx.elseIfs)
        elseStmts = self.getNodeValue(ctx.elseStmts)
        stmt = IfStatement(exp, stmts)
        if elseIfs is not None:
            stmt.addAdditionals(elseIfs)
        if elseStmts is not None:
            stmt.setFinal(elseStmts)
        self.setNodeValue(ctx, stmt)


    def exitIfStatement(self, ctx:PParser.IfStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitInExpression(self, ctx:PParser.InExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.IN, right))


    def exitInstanceExpression(self, ctx:PParser.InstanceExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitIntDivideExpression(self, ctx:PParser.IntDivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, IntDivideExpression(left, right))


    def exitIntegerLiteral(self, ctx:PParser.IntegerLiteralContext):
        self.setNodeValue(ctx, IntegerLiteral(ctx.t.text))


    def exitIntegerType(self, ctx:PParser.IntegerTypeContext):
        self.setNodeValue(ctx, IntegerType.instance)

    def exitIsATypeExpression(self, ctx:PParser.IsATypeExpressionContext):
        typ = self.getNodeValue(ctx.typ)
        exp = TypeExpression(typ)
        self.setNodeValue(ctx, exp)

    def exitIsOtherExpression(self, ctx:PParser.IsOtherExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitIsExpression(self, ctx:PParser.IsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_A if isinstance(right, TypeExpression) else EqOp.IS
        self.setNodeValue(ctx, EqualsExpression(left, op, right))

    def exitIsNotExpression(self, ctx:PParser.IsNotExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_NOT_A if isinstance(right, TypeExpression) else EqOp.IS_NOT
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitItemInstance(self, ctx:PParser.ItemInstanceContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))


    def exitItemSelector(self, ctx:PParser.ItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))


    def exitJava_identifier(self, ctx:PParser.Java_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitJava_item_expression(self, ctx:PParser.Java_item_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaItemExpression(exp))


    def exitJava_method_expression(self, ctx:PParser.Java_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))


    def exitJava_parenthesis_expression(self, ctx:PParser.Java_parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaArgumentList(self, ctx:PParser.JavaArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))


    def exitJavaArgumentListItem(self, ctx:PParser.JavaArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitJavaBooleanLiteral(self, ctx:PParser.JavaBooleanLiteralContext):
        self.setNodeValue(ctx, JavaBooleanLiteral(ctx.getText()))


    def exitJavaCategoryMapping(self, ctx:PParser.JavaCategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, JavaNativeCategoryMapping(map))


    def exitJavaCharacterLiteral(self, ctx:PParser.JavaCharacterLiteralContext):
        self.setNodeValue(ctx, JavaCharacterLiteral(ctx.getText()))


    def exitJavaChildClassIdentifier(self, ctx:PParser.JavaChildClassIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        child = JavaIdentifierExpression(parent, ctx.name.getText())
        self.setNodeValue(ctx, child)


    def exitJavaChildIdentifier(self, ctx:PParser.JavaChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitJavaClassIdentifier(self, ctx:PParser.JavaClassIdentifierContext):
        klass = self.getNodeValue(ctx.klass)
        self.setNodeValue(ctx, klass)


    def exitJavaDecimalLiteral(self, ctx:PParser.JavaDecimalLiteralContext):
        self.setNodeValue(ctx, JavaDecimalLiteral(ctx.getText()))


    def exitJavaIdentifier(self, ctx:PParser.JavaIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))


    def exitJavaIdentifierExpression(self, ctx:PParser.JavaIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaIntegerLiteral(self, ctx:PParser.JavaIntegerLiteralContext):
        self.setNodeValue(ctx, JavaIntegerLiteral(ctx.getText()))


    def exitJavaItemExpression(self, ctx:PParser.JavaItemExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaLiteralExpression(self, ctx:PParser.JavaLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaMethodExpression(self, ctx:PParser.JavaMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaNativeStatement(self, ctx:PParser.JavaNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitJavaParenthesisExpression(self, ctx:PParser.JavaParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaPrimaryExpression(self, ctx:PParser.JavaPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaReturnStatement(self, ctx:PParser.JavaReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, True))


    def exitJavascriptBooleanLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_mapping(self, ctx:PParser.Javascript_category_mappingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.javascript_module())
        map = JavaScriptNativeCategoryMapping(identifier, module)
        self.setNodeValue(ctx, map)


    def exitJavascriptCharacterLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))


    def exitJavascript_identifier(self, ctx:PParser.Javascript_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)

    def exitJavascriptLiteralExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavascript_method_expression(self, ctx:PParser.Javascript_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        method = JavaScriptMethodExpression(name)
        args = self.getNodeValue(ctx.args)
        method.arguments = args
        self.setNodeValue(ctx, method)


    def exitJavascript_module(self, ctx:PParser.Javascript_moduleContext):
        ids = []
        for ic in ctx.javascript_identifier():
            ids.append(ic.getText())
        module = JavaScriptModule(ids)
        self.setNodeValue(ctx, module)


    def exitJavascript_native_statement(self, ctx:PParser.Javascript_native_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        stmt.module = module
        self.setNodeValue(ctx, stmt)


    def exitJavascriptArgumentList(self, ctx:PParser.JavascriptArgumentListContext):
        exp = self.getNodeValue(ctx.item)
        list = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, list)


    def exitJavascriptArgumentListItem(self, ctx:PParser.JavascriptArgumentListItemContext):
        exp = self.getNodeValue(ctx.item)
        list = self.getNodeValue(ctx.items)
        list.add(exp)
        self.setNodeValue(ctx, list)


    def exitJavaScriptCategoryMapping(self, ctx:PParser.JavaScriptCategoryMappingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.mapping))


    def exitJavascriptChildIdentifier(self, ctx:PParser.JavascriptChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(parent, name)
        self.setNodeValue(ctx, exp)

    def exitJavascriptDecimalLiteral(self, ctx:PParser.JavascriptDecimalLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))

    def exitJavascriptIdentifier(self, ctx:PParser.JavascriptIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaScriptIdentifierExpression(None, name))


    def exitJavascriptIdentifierExpression(self, ctx:PParser.JavascriptIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavascriptIntegerLiteral(self, ctx:PParser.JavascriptIntegerLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))


    def exitJavascriptMethodExpression(self, ctx:PParser.JavascriptMethodExpressionContext):
        method = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, method)


    def exitJavaScriptNativeStatement(self, ctx:PParser.JavaScriptNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))


    def exitJavascriptPrimaryExpression(self, ctx:PParser.JavascriptPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavascriptReturnStatement(self, ctx:PParser.JavascriptReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, True))


    def exitJavascriptSelectorExpression(self, ctx:PParser.JavascriptSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)


    def exitJavascriptStatement(self, ctx:PParser.JavascriptStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))

    def exitJavascriptTextLiteral(self, ctx:PParser.JavascriptTextLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))


    def exitJavaSelectorExpression(self, ctx:PParser.JavaSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitJavaStatement(self, ctx:PParser.JavaStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, False))


    def exitJavaTextLiteral(self, ctx:PParser.JavaTextLiteralContext):
        self.setNodeValue(ctx, JavaTextLiteral(ctx.getText()))


    def exitKey_token(self, ctx:PParser.Key_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitLessThanExpression(self, ctx:PParser.LessThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LT, right))


    def exitLessThanOrEqualExpression(self, ctx:PParser.LessThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LTE, right))


    def exitList_literal(self, ctx:PParser.List_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)


    def exitListLiteral(self, ctx:PParser.ListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitListType(self, ctx:PParser.ListTypeContext):
        type = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(type))


    def exitLiteralExpression(self, ctx:PParser.LiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitLiteralList(self, ctx:PParser.LiteralListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitLiteralListItem(self, ctx:PParser.LiteralListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitLiteralListLiteral(self, ctx:PParser.LiteralListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ListLiteral(exp))


    def exitLiteralRangeLiteral(self, ctx:PParser.LiteralRangeLiteralContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))

    def exitLiteralSetLiteral(self, ctx:PParser.LiteralSetLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, SetLiteral(exp))

    def exitMatchingExpression(self, ctx:PParser.MatchingExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MatchingExpressionConstraint(exp))


    def exitMatchingList(self, ctx:PParser.MatchingListContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingPattern(self, ctx:PParser.MatchingPatternContext):
        self.setNodeValue(ctx, MatchingPatternConstraint(TextLiteral(ctx.text.text)))


    def exitMatchingRange(self, ctx:PParser.MatchingRangeContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))

    def exitMatchingSet(self, ctx:PParser.MatchingSetContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMaxIntegerLiteral(self, ctx:PParser.MaxIntegerLiteralContext):
        self.setNodeValue(ctx, MaxIntegerLiteral())


    def exitMember_method_declaration(self, ctx:PParser.Member_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, MemberMethodDeclaration(name, args, type, stmts))


    def exitMemberInstance(self, ctx:PParser.MemberInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))


    def exitMemberMethod(self, ctx:PParser.MemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitMemberSelector(self, ctx:PParser.MemberSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))


    def exitMethod_call(self, ctx:PParser.Method_callContext):
        method = self.getNodeValue(ctx.method)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(method, args))


    def exitMethodCallExpression(self, ctx:PParser.MethodCallExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodCallStatement(self, ctx:PParser.MethodCallStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitMethodDeclaration(self, ctx:PParser.MethodDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitMethodExpression(self, ctx:PParser.MethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodName(self, ctx:PParser.MethodNameContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitMethodParent(self, ctx:PParser.MethodParentContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodSelector(name, parent))


    def exitMethodTypeIdentifier(self, ctx:PParser.MethodTypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitMethodVariableIdentifier(self, ctx:PParser.MethodVariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitMinIntegerLiteral(self, ctx:PParser.MinIntegerLiteralContext):
        self.setNodeValue(ctx, MinIntegerLiteral())


    def exitMinusExpression(self, ctx:PParser.MinusExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MinusExpression(exp))


    def exitModuloExpression(self, ctx:PParser.ModuloExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ModuloExpression(left, right))


    def exitMultiplyExpression(self, ctx:PParser.MultiplyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))


    def exitNamed_argument(self, ctx:PParser.Named_argumentContext):
        name = self.getNodeValue(ctx.name)
        arg = UnresolvedArgument(name)
        exp = self.getNodeValue(ctx.value)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitNamedArgument(self, ctx:PParser.NamedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitNative_category_declaration(self, ctx:PParser.Native_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        mappings = self.getNodeValue(ctx.mappings)
        self.setNodeValue(ctx, NativeCategoryDeclaration(name, attrs, mappings, None))


    def exitNative_category_mappings(self, ctx:PParser.Native_category_mappingsContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitNative_method_declaration(self, ctx:PParser.Native_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, type, stmts))


    def exitNative_resource_declaration(self, ctx:PParser.Native_resource_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        mappings = self.getNodeValue(ctx.mappings)
        self.setNodeValue(ctx, NativeResourceDeclaration(name, attrs, mappings, None))


    def exitNative_symbol(self, ctx:PParser.Native_symbolContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))


    def exitNativeCategoryDeclaration(self, ctx:PParser.NativeCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryMappingList(self, ctx:PParser.NativeCategoryMappingListContext):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryMappingList(item)
        self.setNodeValue(ctx, items)


    def exitNativeCategoryMappingListItem(self, ctx:PParser.NativeCategoryMappingListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeMethod(self, ctx:PParser.NativeMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeStatementList(self, ctx:PParser.NativeStatementListContext):
        item = self.getNodeValue(ctx.item)
        items = StatementList(item)
        self.setNodeValue(ctx, items)


    def exitNativeStatementListItem(self, ctx:PParser.NativeStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeSymbolList(self, ctx:PParser.NativeSymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, NativeSymbolList(item))


    def exitNativeSymbolListItem(self, ctx:PParser.NativeSymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeType(self, ctx:PParser.NativeTypeContext):
        type = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, type)


    def exitNotContainsAllExpression(self, ctx:PParser.NotContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ALL, right))


    def exitNotContainsAnyExpression(self, ctx:PParser.NotContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ANY, right))


    def exitNotContainsExpression(self, ctx:PParser.NotContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS, right))


    def exitNotEqualsExpression(self, ctx:PParser.NotEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.NOT_EQUALS, right))


    def exitNotExpression(self, ctx:PParser.NotExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NotExpression(exp))


    def exitNotInExpression(self, ctx:PParser.NotInExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_IN, right))


    def exitNullLiteral(self, ctx:PParser.NullLiteralContext):
        self.setNodeValue(ctx, NullLiteral.instance)


    def exitOperatorArgument(self, ctx:PParser.OperatorArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitOperatorPlus(self, ctx:PParser.OperatorPlusContext):
        self.setNodeValue(ctx, Operator.PLUS)


    def exitOperatorMinus(self, ctx:PParser.OperatorMinusContext):
        self.setNodeValue(ctx, Operator.MINUS)


    def exitOperatorMultiply(self, ctx:PParser.OperatorMultiplyContext):
        self.setNodeValue(ctx, Operator.MULTIPLY)


    def exitOperatorDivide(self, ctx:PParser.OperatorDivideContext):
        self.setNodeValue(ctx, Operator.DIVIDE)


    def exitOperatorIDivide(self, ctx:PParser.OperatorIDivideContext):
        self.setNodeValue(ctx, Operator.IDIVIDE)


    def exitOperatorModulo(self, ctx:PParser.OperatorModuloContext):
        self.setNodeValue(ctx, Operator.MODULO)


    def exitOperator_method_declaration(self, ctx:PParser.Operator_method_declarationContext):
        op = self.getNodeValue(ctx.op)
        arg = self.getNodeValue(ctx.arg)
        typ = self.getNodeValue(ctx.typ)
        stmts = self.getNodeValue(ctx.stmts)
        decl = OperatorMethodDeclaration(op, arg, typ, stmts)
        self.setNodeValue(ctx, decl)


    def exitOperatorMethod(self, ctx:PParser.OperatorMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitOrExpression(self, ctx:PParser.OrExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))


    def exitParenthesis_expression(self, ctx:PParser.Parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ParenthesisExpression(exp))


    def exitParenthesisExpression(self, ctx:PParser.ParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPeriodLiteral(self, ctx:PParser.PeriodLiteralContext):
        self.setNodeValue(ctx, PeriodLiteral(ctx.t.text))


    def exitPrimaryType(self, ctx:PParser.PrimaryTypeContext):
        type = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, type)


    def exitPython_category_mapping(self, ctx:PParser.Python_category_mappingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.python_module())
        map = PythonNativeCategoryMapping(identifier, module)
        self.setNodeValue(ctx, map)


    def exitPython_identifier(self, ctx:PParser.Python_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitPython_method_expression(self, ctx:PParser.Python_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        method = PythonMethodExpression(name, args)
        self.setNodeValue(ctx, method)


    def exitPython_module(self, ctx:PParser.Python_moduleContext):
        ids = []
        for ic in ctx.identifier():
            ids.append(ic.getText())
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)


    def exitPython_native_statement(self, ctx:PParser.Python_native_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))


    def exitPython2CategoryMapping(self, ctx:PParser.Python2CategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, Python2NativeCategoryMapping(map.identifier, map.module))


    def exitPython2NativeStatement(self, ctx:PParser.Python2NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3CategoryMapping(self, ctx:PParser.Python3CategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, Python3NativeCategoryMapping(map.identifier, map.module))


    def exitPython3NativeStatement(self, ctx:PParser.Python3NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))


    def exitPythonArgumentList(self, ctx:PParser.PythonArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        named = self.getNodeValue(ctx.named)
        ordinal.addAll(named)
        self.setNodeValue(ctx, ordinal)


    def exitPythonBooleanLiteral(self, ctx:PParser.PythonBooleanLiteralContext):
        self.setNodeValue(ctx, PythonBooleanLiteral(ctx.getText()))


    def exitPythonCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))


    def exitPythonChildIdentifier(self, ctx:PParser.PythonChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitPythonDecimalLiteral(self, ctx:PParser.PythonDecimalLiteralContext):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))


    def exitPythonGlobalMethodExpression(self, ctx:PParser.PythonGlobalMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIdentifier(self, ctx:PParser.PythonIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))


    def exitPythonIdentifierExpression(self, ctx:PParser.PythonIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIntegerLiteral(self, ctx:PParser.PythonIntegerLiteralContext):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))


    def exitPythonLiteralExpression(self, ctx:PParser.PythonLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonMethodExpression(self, ctx:PParser.PythonMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonNamedArgumentList(self, ctx:PParser.PythonNamedArgumentListContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = PythonNamedArgument(name, exp)
        arglist = PythonArgumentList()
        arglist.append(arg)
        self.setNodeValue(ctx, arglist)


    def exitPythonNamedArgumentListItem(self, ctx:PParser.PythonNamedArgumentListItemContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = PythonNamedArgument(name, exp)
        items = self.getNodeValue(ctx.items)
        items.append(arg)
        self.setNodeValue(ctx, items)


    def exitPythonNamedOnlyArgumentList(self, ctx:PParser.PythonNamedOnlyArgumentListContext):
        named = self.getNodeValue(ctx.named)
        self.setNodeValue(ctx, named)


    def exitPythonPrimaryExpression(self, ctx:PParser.PythonPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonReturnStatement(self, ctx:PParser.PythonReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitPythonSelectorExpression(self, ctx:PParser.PythonSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.child)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitPythonStatement(self, ctx:PParser.PythonStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, False))


    def exitPythonTextLiteral(self, ctx:PParser.PythonTextLiteralContext):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))


    def exitRaise_statement(self, ctx:PParser.Raise_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, RaiseStatement(exp))


    def exitRaiseStatement(self, ctx:PParser.RaiseStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRange_literal(self, ctx:PParser.Range_literalContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitRangeLiteral(self, ctx:PParser.RangeLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitRead_expression(self, ctx:PParser.Read_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadExpression(source))


    def exitReadExpression(self, ctx:PParser.ReadExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitResource_declaration(self, ctx:PParser.Resource_declarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitResourceDeclaration(self, ctx:PParser.ResourceDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitReturn_statement(self, ctx:PParser.Return_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ReturnStatement(exp))


    def exitReturnStatement(self, ctx:PParser.ReturnStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRootInstance(self, ctx:PParser.RootInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, VariableInstance(name))

    def exitRoughlyEqualsExpression(self, ctx:PParser.RoughlyEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.ROUGHLY, right))

    def exitSelectableExpression(self, ctx:PParser.SelectableExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, parent)


    def exitSelectorExpression(self, ctx:PParser.SelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitSetter_method_declaration(self, ctx:PParser.Setter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))


    def exitSetterMethod(self, ctx:PParser.SetterMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSingleton_category_declaration(self, ctx:PParser.Singleton_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, SingletonCategoryDeclaration(name, attrs, methods))


    def exitSingletonCategoryDeclaration(self, ctx:PParser.SingletonCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSliceFirstAndLast(self, ctx:PParser.SliceFirstAndLastContext):
        first = self.getNodeValue(ctx.first)
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(first, last))


    def exitSliceFirstOnly(self, ctx:PParser.SliceFirstOnlyContext):
        first = self.getNodeValue(ctx.first)
        self.setNodeValue(ctx, SliceSelector(first, None))


    def exitSliceLastOnly(self, ctx:PParser.SliceLastOnlyContext):
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(None, last))


    def exitSliceSelector(self, ctx:PParser.SliceSelectorContext):
        slice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, slice)


    def exitSorted_expression(self, ctx:PParser.Sorted_expressionContext):
        source = self.getNodeValue(ctx.source)
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, key))


    def exitSortedExpression(self, ctx:PParser.SortedExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitStatementList(self, ctx:PParser.StatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, StatementList(item))


    def exitStatementListItem(self, ctx:PParser.StatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitch_statement(self, ctx:PParser.Switch_statementContext):
        exp = self.getNodeValue(ctx.exp)
        cases = self.getNodeValue(ctx.cases)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = SwitchStatement(exp)
        stmt.setSwitchCases(cases)
        stmt.setDefaultCase(stmts)
        self.setNodeValue(ctx, stmt)


    def exitSwitchCaseStatementList(self, ctx:PParser.SwitchCaseStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitSwitchCaseStatementListItem(self, ctx:PParser.SwitchCaseStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitchStatement(self, ctx:PParser.SwitchStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitSymbol_identifier(self, ctx:PParser.Symbol_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitSymbolIdentifier(self, ctx:PParser.SymbolIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitSymbols_token(self, ctx:PParser.Symbols_tokenContext):
        self.setNodeValue(ctx, ctx.getText())

    def exitTernaryExpression(self, ctx):
        condition = self.getNodeValue(ctx.test)
        ifTrue = self.getNodeValue(ctx.ifTrue)
        ifFalse = self.getNodeValue(ctx.ifFalse)
        exp = TernaryExpression(condition, ifTrue, ifFalse)
        self.setNodeValue(ctx, exp)

    def exitTextLiteral(self, ctx:PParser.TextLiteralContext):
        self.setNodeValue(ctx, TextLiteral(ctx.t.text))

    def exitTest_method_declaration(self, ctx:PParser.Test_method_declarationContext):
        name = ctx.name.text
        stmts = self.getNodeValue(ctx.stmts)
        exps = self.getNodeValue(ctx.exps)
        errorName = self.getNodeValue(ctx.error)
        error = None if errorName is None else SymbolExpression(errorName)
        self.setNodeValue(ctx, TestMethodDeclaration(name, stmts, exps, error))


    def exitTestMethod(self, ctx:PParser.TestMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)

    def exitTextType(self, ctx:PParser.TextTypeContext):
        self.setNodeValue(ctx, TextType.instance)

    def exitThisExpression(self, ctx:PParser.ThisExpressionContext):
        self.setNodeValue(ctx, ThisExpression())


    def exitTimeLiteral(self, ctx:PParser.TimeLiteralContext):
        self.setNodeValue(ctx, TimeLiteral(ctx.t.text))


    def exitTimeType(self, ctx:PParser.TimeTypeContext):
        self.setNodeValue(ctx, TimeType.instance)


    def exitTry_statement(self, ctx:PParser.Try_statementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        handlers = self.getNodeValue(ctx.handlers)
        anyStmts = self.getNodeValue(ctx.anyStmts)
        finalStmts = self.getNodeValue(ctx.finalStmts)
        stmt = SwitchErrorStatement(name, stmts)
        stmt.setSwitchCases(handlers)
        stmt.setDefaultCase(anyStmts)
        stmt.setAlwaysInstructions(finalStmts)
        self.setNodeValue(ctx, stmt)


    def exitTryStatement(self, ctx:PParser.TryStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitTuple_literal(self, ctx:PParser.Tuple_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = TupleLiteral(items)
        self.setNodeValue(ctx, value)


    def exitTupleLiteral(self, ctx:PParser.TupleLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitSet_literal(self, ctx:PParser.Set_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitSetLiteral(self, ctx:PParser.SetLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitType_identifier(self, ctx:PParser.Type_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitTyped_argument(self, ctx:PParser.Typed_argumentContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        arg = CategoryArgument(type, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitTypedArgument(self, ctx:PParser.TypedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitTypeIdentifier(self, ctx:PParser.TypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitTypeIdentifierList(self, ctx:PParser.TypeIdentifierListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))


    def exitTypeIdentifierListItem(self, ctx:PParser.TypeIdentifierListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitValue_token(self, ctx:PParser.Value_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitValueList(self, ctx:PParser.ValueListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitValueListItem(self, ctx:PParser.ValueListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitValueTuple(self, ctx:PParser.ValueTupleContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitValueTupleItem(self, ctx:PParser.ValueTupleItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitVariable_identifier(self, ctx:PParser.Variable_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariableIdentifier(self, ctx:PParser.VariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitVariableList(self, ctx:PParser.VariableListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))


    def exitVariableListItem(self, ctx:PParser.VariableListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitWhile_statement(self, ctx:PParser.While_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WhileStatement(exp, stmts))


    def exitWhileStatement(self, ctx:PParser.WhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_singleton_statement(self, ctx:PParser.With_singleton_statementContext):
        name = self.getNodeValue(ctx.typ)
        typ = CategoryType(name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithSingletonStatement(typ, stmts))


    def exitWithSingletonStatement(self, ctx:PParser.WithSingletonStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_resource_statement(self, ctx:PParser.With_resource_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithResourceStatement(stmt, stmts))


    def exitWithResourceStatement(self, ctx:PParser.WithResourceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWrite_statement(self, ctx:PParser.Write_statementContext):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        self.setNodeValue(ctx, WriteStatement(what, target))


    def exitWriteStatement(self, ctx:PParser.WriteStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
