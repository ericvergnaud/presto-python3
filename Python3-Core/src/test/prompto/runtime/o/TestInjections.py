# generated: 2015-07-05T23:01:01.829
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestInjections(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testExpressionInjection(self):
        self.checkOutput("injections/expressionInjection.poc")


