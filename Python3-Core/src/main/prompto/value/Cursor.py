from prompto.error.InvalidDataError import InvalidDataError
from prompto.value.BaseValue import BaseValue
from prompto.type.CursorType import CursorType
from prompto.value.IIterable import IIterable
from prompto.value.Integer import Integer

class Cursor(BaseValue, IIterable):

    def __init__(self, context, itemType, documents):
        super().__init__(CursorType(itemType))
        self.context = context
        self.documents = documents

    def isEmpty(self):
        return len(self.documents)==0

    def __len__(self):
        return len(self.documents)

    def getIterator(self, context):
        for doc in self.documents:
            val = self.type.itemType.newInstanceFromDocument(context, doc)
            yield val

    def getMember(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self))
        else:
            raise InvalidDataError("No such member:" + name)


