from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBlob(self):
        self.compareResourceESE("documents/blob.pec")

    def testDeepItem(self):
        self.compareResourceESE("documents/deepItem.pec")

    def testDeepVariable(self):
        self.compareResourceESE("documents/deepVariable.pec")

    def testItem(self):
        self.compareResourceESE("documents/item.pec")

    def testNamedItem(self):
        self.compareResourceESE("documents/namedItem.pec")

    def testVariable(self):
        self.compareResourceESE("documents/variable.pec")


