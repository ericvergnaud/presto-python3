
class DictIdentifierKey(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def asText(self):
        from prompto.value.Text import Text
        return Text(self.name)
