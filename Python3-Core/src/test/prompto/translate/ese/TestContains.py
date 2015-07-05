# generated: 2015-07-05T23:01:01.759
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceESE("contains/containsAllList.pec")

    def testContainsAllSet(self):
        self.compareResourceESE("contains/containsAllSet.pec")

    def testContainsAllText(self):
        self.compareResourceESE("contains/containsAllText.pec")

    def testContainsAllTuple(self):
        self.compareResourceESE("contains/containsAllTuple.pec")

    def testContainsAnyList(self):
        self.compareResourceESE("contains/containsAnyList.pec")

    def testContainsAnySet(self):
        self.compareResourceESE("contains/containsAnySet.pec")

    def testContainsAnyText(self):
        self.compareResourceESE("contains/containsAnyText.pec")

    def testContainsAnyTuple(self):
        self.compareResourceESE("contains/containsAnyTuple.pec")

    def testInCharacterRange(self):
        self.compareResourceESE("contains/inCharacterRange.pec")

    def testInDateRange(self):
        self.compareResourceESE("contains/inDateRange.pec")

    def testInDict(self):
        self.compareResourceESE("contains/inDict.pec")

    def testInIntegerRange(self):
        self.compareResourceESE("contains/inIntegerRange.pec")

    def testInList(self):
        self.compareResourceESE("contains/inList.pec")

    def testInSet(self):
        self.compareResourceESE("contains/inSet.pec")

    def testInText(self):
        self.compareResourceESE("contains/inText.pec")

    def testInTimeRange(self):
        self.compareResourceESE("contains/inTimeRange.pec")

    def testInTuple(self):
        self.compareResourceESE("contains/inTuple.pec")

    def testNinCharacterRange(self):
        self.compareResourceESE("contains/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.compareResourceESE("contains/ninDateRange.pec")

    def testNinDict(self):
        self.compareResourceESE("contains/ninDict.pec")

    def testNinIntegerRange(self):
        self.compareResourceESE("contains/ninIntegerRange.pec")

    def testNinList(self):
        self.compareResourceESE("contains/ninList.pec")

    def testNinSet(self):
        self.compareResourceESE("contains/ninSet.pec")

    def testNinText(self):
        self.compareResourceESE("contains/ninText.pec")

    def testNinTimeRange(self):
        self.compareResourceESE("contains/ninTimeRange.pec")


