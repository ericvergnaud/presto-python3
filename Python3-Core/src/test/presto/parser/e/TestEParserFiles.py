from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestParserFiles ( BaseEParserTest ):

    def testEmpty(self):
        stmts = self.parseString("")
        self.assertIsNotNone(stmts)
        self.assertEquals(0,len(stmts))

    def testNative(self):
        stmts = self.parseResource("native/method.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(2,len(stmts))

    def testSpecified(self):
        stmts = self.parseResource("methods/specified.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testAttribute(self):
        stmts = self.parseResource("methods/attribute.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testImplicit(self):
        stmts = self.parseResource("methods/implicit.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testPolymorphicImplicit(self):
        stmts = self.parseResource("methods/polymorphic_implicit.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(12,len(stmts))

    def testEnumeratedCategory(self):
        stmts = self.parseResource("enums/categoryEnum.e")
        self.assertIsNotNone(stmts)
        self.assertEquals(5,len(stmts))