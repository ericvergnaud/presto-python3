from presto.literal.Literal import *
from presto.type.TextType import *


class TextLiteral(Literal):

    def __init__(self, text):
        from presto.value.Text import Text
        c = compile(text, "__no_file__", mode='eval')
        s = eval(c)
        value = Text(s)
        super().__init__(text, value)

    def check(self, context):
        return TextType.instance