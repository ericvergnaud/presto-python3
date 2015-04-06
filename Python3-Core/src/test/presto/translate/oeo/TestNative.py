from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceOEO("native/category.poc")

    def testMethod(self):
        self.compareResourceOEO("native/method.poc")

    def testReturn(self):
        self.compareResourceOEO("native/return.poc")

    def testReturnBooleanLiteral(self):
        self.compareResourceOEO("native/returnBooleanLiteral.poc")

    def testReturnBooleanObject(self):
        self.compareResourceOEO("native/returnBooleanObject.poc")

    def testReturnBooleanValue(self):
        self.compareResourceOEO("native/returnBooleanValue.poc")

    def testReturnCharacterLiteral(self):
        self.compareResourceOEO("native/returnCharacterLiteral.poc")

    def testReturnCharacterObject(self):
        self.compareResourceOEO("native/returnCharacterObject.poc")

    def testReturnCharacterValue(self):
        self.compareResourceOEO("native/returnCharacterValue.poc")

    def testReturnDecimalLiteral(self):
        self.compareResourceOEO("native/returnDecimalLiteral.poc")

    def testReturnIntegerLiteral(self):
        self.compareResourceOEO("native/returnIntegerLiteral.poc")

    def testReturnIntegerObject(self):
        self.compareResourceOEO("native/returnIntegerObject.poc")

    def testReturnIntegerValue(self):
        self.compareResourceOEO("native/returnIntegerValue.poc")

    def testReturnLongObject(self):
        self.compareResourceOEO("native/returnLongObject.poc")

    def testReturnLongValue(self):
        self.compareResourceOEO("native/returnLongValue.poc")

    def testReturnStringLiteral(self):
        self.compareResourceOEO("native/returnStringLiteral.poc")


