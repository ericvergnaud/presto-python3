# generated: 2015-07-05T23:01:01.894
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testImmutable(self):
        self.checkOutput("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.checkOutput("mutability/immutableArgument.poc")

    def testImmutableMember(self):
        self.checkOutput("mutability/immutableMember.poc")

    def testMutable(self):
        self.checkOutput("mutability/mutable.poc")

    def testMutableArgument(self):
        self.checkOutput("mutability/mutableArgument.poc")

    def testMutableMember(self):
        self.checkOutput("mutability/mutableMember.poc")


