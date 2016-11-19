from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.parser.Section import Section
from prompto.runtime.TransientVariable import TransientVariable
from prompto.type.BooleanType import BooleanType
from prompto.type.ListType import ListType
from prompto.type.TupleType import TupleType
from prompto.type.SetType import SetType
from prompto.value.ListValue import ListValue
from prompto.value.TupleValue import TupleValue
from prompto.value.SetValue import SetValue
from prompto.error.SyntaxError import SyntaxError


class FilteredExpression(Section, IExpression):

    def __init__(self, itemName, source, predicate):
        super(FilteredExpression, self).__init__()
        self.itemName = itemName
        self.source = source
        self.predicate = predicate



    def __str__(self):
        return "fetch any " + self.itemName + " from " + str(self.source) + " where " + str(self.predicate)



    def toMDialect(self, writer):
        self.source.toDialect(writer)
        writer.append(" filtered with ")
        writer.append(self.itemName)
        writer.append(" where ")
        self.predicate.toDialect(writer)

    def toEDialect(self, writer):
        self.toMDialect(writer)



    def toODialect(self, writer):
        writer.append("filtered (")
        self.source.toDialect(writer)
        writer.append(") with (")
        writer.append(self.itemName)
        writer.append(") where (")
        self.predicate.toDialect(writer)
        writer.append(")")



    def check(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, (ListType, TupleType, SetType)):
            raise SyntaxError("Expecting a collection type as data source !")
        local = context.newLocalContext()
        local.registerValue(TransientVariable(self.itemName, listType.getItemType()))
        filterType = self.predicate.check(local)
        if filterType is not BooleanType.instance:
            raise SyntaxError("Filtering expression must return a boolean !")
        return listType

    def interpret(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, (ListType, TupleType, SetType)):
            raise InternalError("Illegal source type: " + listType.getName())
        itemType = listType.getItemType()
        items = self.source.interpret(context)
        if items is None:
            raise NullReferenceError()
        if not isinstance(items, (ListValue, TupleValue, SetValue)):
            raise InternalError("Illegal fetch source: " + str(items))
        local = context.newLocalContext()
        item = TransientVariable(self.itemName, itemType)
        local.registerValue(item)
        return items.filter(local, self.itemName, self.predicate)
