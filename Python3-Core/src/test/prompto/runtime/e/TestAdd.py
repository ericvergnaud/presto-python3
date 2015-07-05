# generated: 2015-07-05T23:01:01.717
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddCharacter(self):
        self.checkOutput("add/addCharacter.pec")

    def testAddDate(self):
        self.checkOutput("add/addDate.pec")

    def testAddDateTime(self):
        self.checkOutput("add/addDateTime.pec")

    def testAddDecimal(self):
        self.checkOutput("add/addDecimal.pec")

    def testAddDict(self):
        self.checkOutput("add/addDict.pec")

    def testAddInteger(self):
        self.checkOutput("add/addInteger.pec")

    def testAddList(self):
        self.checkOutput("add/addList.pec")

    def testAddPeriod(self):
        self.checkOutput("add/addPeriod.pec")

    def testAddSet(self):
        self.checkOutput("add/addSet.pec")

    def testAddText(self):
        self.checkOutput("add/addText.pec")

    def testAddTime(self):
        self.checkOutput("add/addTime.pec")

    def testAddTuple(self):
        self.checkOutput("add/addTuple.pec")


