# generated: 2015-07-05T23:01:01.749
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGlobalClosureNoArg(self):
        self.checkOutput("closures/globalClosureNoArg.poc")

    def testGlobalClosureWithArg(self):
        self.checkOutput("closures/globalClosureWithArg.poc")

    def testInstanceClosureNoArg(self):
        self.checkOutput("closures/instanceClosureNoArg.poc")


