# generated: 2015-10-05T21:35:40.771
from prompto.parser.s.BaseSParserTest import BaseSParserTest
from prompto.runtime.utils.Out import Out

class TestAdd(BaseSParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddInteger(self):
        self.checkOutput("add/addInteger.psc")


