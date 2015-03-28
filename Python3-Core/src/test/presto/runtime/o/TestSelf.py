from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSelf(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSelfAsParameter(self):
        self.checkOutput("self/selfAsParameter.o")

    def testSelfMember(self):
        self.checkOutput("self/selfMember.o")

