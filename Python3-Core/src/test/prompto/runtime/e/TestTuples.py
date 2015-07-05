# generated: 2015-07-05T23:01:01.977
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultiAssignment(self):
        self.checkOutput("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.checkOutput("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.checkOutput("tuples/tupleElement.pec")


