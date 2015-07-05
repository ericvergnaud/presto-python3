# generated: 2015-07-05T23:01:01.737
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceEOE("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.compareResourceEOE("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromDescendantWithOverride.pec")


