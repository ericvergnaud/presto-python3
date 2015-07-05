# generated: 2015-07-05T23:01:01.918
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testIntegerEnumeration(self):
        self.checkOutput("patterns/integerEnumeration.poc")

    def testIntegerPattern(self):
        self.checkOutput("patterns/integerPattern.poc")

    def testNegativeIntegerRange(self):
        self.checkOutput("patterns/negativeIntegerRange.poc")

    def testPositiveIntegerRange(self):
        self.checkOutput("patterns/positiveIntegerRange.poc")

    def testTextEnumeration(self):
        self.checkOutput("patterns/textEnumeration.poc")

    def testTextPattern(self):
        self.checkOutput("patterns/textPattern.poc")


