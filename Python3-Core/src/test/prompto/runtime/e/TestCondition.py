# generated: 2015-07-05T23:01:01.753
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.pec")

    def testElseIf(self):
        self.checkOutput("condition/elseIf.pec")

    def testReturnIf(self):
        self.checkOutput("condition/returnIf.pec")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.pec")

    def testSwitch(self):
        self.checkOutput("condition/switch.pec")

    def testTernary(self):
        self.checkOutput("condition/ternary.pec")


