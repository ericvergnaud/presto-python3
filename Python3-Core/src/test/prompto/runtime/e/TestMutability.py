# generated: 2015-07-05T23:01:01.891
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testImmutable(self):
        self.checkOutput("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.checkOutput("mutability/immutableArgument.pec")

    def testImmutableMember(self):
        self.checkOutput("mutability/immutableMember.pec")

    def testMutable(self):
        self.checkOutput("mutability/mutable.pec")

    def testMutableArgument(self):
        self.checkOutput("mutability/mutableArgument.pec")

    def testMutableMember(self):
        self.checkOutput("mutability/mutableMember.pec")


