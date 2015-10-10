from prompto.grammar.NativeCategoryBinding import NativeCategoryBinding


class PythonNativeCategoryBinding(NativeCategoryBinding):

    def __init__(self, identifier, module):
        super(PythonNativeCategoryBinding, self).__init__()
        self.identifier = identifier
        self.module = module

    def getIdentifier(self):
        return self.identifier

    def getModule(self):
        return self.module

    def interpret(self):
        m = None if self.module is None else self.module.resolve()
        if m is None:
            return eval(self.identifier)
        else:
            return m.__dict__.get(self.identifier, None)

    def toDialect(self, writer):
        writer.append(self.identifier)
        if self.module is not None:
            self.module.toDialect(writer)

class Python2NativeCategoryBinding(PythonNativeCategoryBinding):

    def __init__(self, identifier, module):
        super(Python2NativeCategoryBinding, self).__init__(identifier, module)

    def toDialect(self, writer):
        writer.append("Python2: ")
        super(Python2NativeCategoryBinding, self).toDialect(writer)

class Python3NativeCategoryBinding(PythonNativeCategoryBinding):

    def __init__(self, identifier, module):
        super(Python3NativeCategoryBinding, self).__init__(identifier, module)

    def toDialect(self, writer):
        writer.append("Python3: ")
        super(Python3NativeCategoryBinding, self).toDialect(writer)
