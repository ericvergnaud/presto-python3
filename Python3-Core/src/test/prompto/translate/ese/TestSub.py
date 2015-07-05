# generated: 2015-07-05T23:01:01.964
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceESE("sub/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceESE("sub/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceESE("sub/subDecimal.pec")

    def testSubInteger(self):
        self.compareResourceESE("sub/subInteger.pec")

    def testSubPeriod(self):
        self.compareResourceESE("sub/subPeriod.pec")

    def testSubTime(self):
        self.compareResourceESE("sub/subTime.pec")


