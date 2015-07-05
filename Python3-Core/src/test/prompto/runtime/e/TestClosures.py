# generated: 2015-07-05T23:01:01.746
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGlobalClosureNoArg(self):
        self.checkOutput("closures/globalClosureNoArg.pec")

    def testGlobalClosureWithArg(self):
        self.checkOutput("closures/globalClosureWithArg.pec")

    def testInstanceClosureNoArg(self):
        self.checkOutput("closures/instanceClosureNoArg.pec")


