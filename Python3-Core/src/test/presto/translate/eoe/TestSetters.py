from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceEOE("setters/getter.pec")

    def testSetter(self):
        self.compareResourceEOE("setters/setter.pec")


