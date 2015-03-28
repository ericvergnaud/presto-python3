from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSliceList(self):
        self.checkOutput("slice/sliceList.o")

    def testSliceRange(self):
        self.checkOutput("slice/sliceRange.o")

    def testSliceText(self):
        self.checkOutput("slice/sliceText.o")

