from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEnums(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategoryEnum(self):
        self.compareResourceEOE("enums/categoryEnum.e")

    def testIntegerEnum(self):
        self.compareResourceEOE("enums/integerEnum.e")

    def testTextEnum(self):
        self.compareResourceEOE("enums/textEnum.e")

