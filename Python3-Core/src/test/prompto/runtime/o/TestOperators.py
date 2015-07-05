# generated: 2015-07-05T23:01:01.911
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddAmount(self):
        self.checkOutput("operators/addAmount.poc")

    def testDivAmount(self):
        self.checkOutput("operators/divAmount.poc")

    def testIdivAmount(self):
        self.checkOutput("operators/idivAmount.poc")

    def testModAmount(self):
        self.checkOutput("operators/modAmount.poc")

    def testMultAmount(self):
        self.checkOutput("operators/multAmount.poc")

    def testSubAmount(self):
        self.checkOutput("operators/subAmount.poc")


