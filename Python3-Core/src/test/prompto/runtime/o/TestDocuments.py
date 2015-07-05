# generated: 2015-07-05T23:01:01.780
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.poc")

    def testDeepVariable(self):
        self.checkOutput("documents/deepVariable.poc")

    def testItem(self):
        self.checkOutput("documents/item.poc")

    def testVariable(self):
        self.checkOutput("documents/variable.poc")


