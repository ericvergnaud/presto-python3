from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestFetch(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceEPE("fetch/fetchFromList.e")

    def testFetchFromSet(self):
        self.compareResourceEPE("fetch/fetchFromSet.e")

