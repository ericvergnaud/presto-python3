from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceOEO("setters/getter.poc")

    def testSetter(self):
        self.compareResourceOEO("setters/setter.poc")


