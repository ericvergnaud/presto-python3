# generated: 2015-07-05T23:01:01.939
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceESE("singleton/attribute.pec")

    def testMember(self):
        self.compareResourceESE("singleton/member.pec")


