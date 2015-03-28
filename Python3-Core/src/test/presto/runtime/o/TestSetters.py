from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGetter(self):
        self.checkOutput("setters/getter.o")

    def testSetter(self):
        self.checkOutput("setters/setter.o")

