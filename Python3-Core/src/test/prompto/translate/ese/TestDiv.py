# generated: 2015-07-05T23:01:01.769
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceESE("div/divDecimal.pec")

    def testDivInteger(self):
        self.compareResourceESE("div/divInteger.pec")

    def testIdivInteger(self):
        self.compareResourceESE("div/idivInteger.pec")

    def testModInteger(self):
        self.compareResourceESE("div/modInteger.pec")


