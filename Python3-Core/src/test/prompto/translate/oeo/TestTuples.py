# generated: 2015-07-05T23:01:01.978
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceOEO("tuples/multiAssignment.poc")

    def testSingleAssignment(self):
        self.compareResourceOEO("tuples/singleAssignment.poc")

    def testTupleElement(self):
        self.compareResourceOEO("tuples/tupleElement.poc")


