# generated: 2015-07-05T23:01:01.827
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestInjections(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testExpressionInjection(self):
        self.checkOutput("injections/expressionInjection.pec")


