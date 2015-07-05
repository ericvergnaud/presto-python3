from prompto.csharp.CSharpExpression import CSharpExpression

class CSharpIdentifierExpression (CSharpExpression):

    @staticmethod
    def parse(ids):
        parts = ids.split("\\.")
        result = None
        for part in parts:
            result = CSharpIdentifierExpression(parent=result, identifier=part)
        return result

    def __init__(self, parent, identifier):
        super().__init__(identifier)
        self.parent = parent
        self.identifier = identifier

    def getParent(self):
        return self.parent

    def getIdentifier(self):
        return self.identifier

    def __str__(self):
        if self.parent is None:
            return self.identifier
        else:
            return str(self.parent) + '.' + self.identifier

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append(".")
        writer.append(self.identifier)
