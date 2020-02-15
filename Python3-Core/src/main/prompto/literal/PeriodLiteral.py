from datetime import timedelta

from prompto.literal.Literal import Literal
from prompto.type.PeriodType import PeriodType
from prompto.value.PeriodValue import PeriodValue


class PeriodLiteral ( Literal ):

	def __init__(self, text):
		super(PeriodLiteral, self).__init__(text, PeriodValue.Parse(text[1:-1]))

	def check(self, context):
		return PeriodType.instance
	
