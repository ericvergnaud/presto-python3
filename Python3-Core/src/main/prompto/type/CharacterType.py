from prompto.store.InvalidValueError import InvalidValueError
from prompto.store.TypeFamily import TypeFamily
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.NativeType import NativeType
from prompto.type.RangeType import RangeType
from prompto.type.TextType import TextType
from prompto.value.Character import Character
from prompto.value.CharacterRange import CharacterRange



class CharacterType(NativeType):
    instance = None

    def __init__(self):
        super().__init__(TypeFamily.CHARACTER)

    def isAssignableTo(self, context, other):
        return isinstance(other, CharacterType) or isinstance(other, TextType) or isinstance(other, AnyType)

    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "codePoint" == name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)

    def checkAdd(self, context, other, tryReverse):
        return TextType.instance

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return TextType.instance
        else:
            return super().checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        if isinstance(other, CharacterType) or isinstance(other, TextType):
            return BooleanType.instance
        return super().checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, CharacterType):
            return RangeType(self)
        return super().checkRange(context, other)

    def newRange(self, left, right):
        if isinstance(left, Character) and isinstance(right, Character):
            return CharacterRange(left, right)
        return super().newRange(left, right)

    def sort(self, context, list_, desc):
        return sorted(list_, reverse=desc)

    def toString(self, value):
        return "'" + str(value) + "'"

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, str):
            return Character(value)
        else:
            return value  # TODO for now

    def nativeCast(self, context, value):
        if isinstance(value.type, TextType) and len(value.value)>=1:
            return Character(value.value[0:1])
        else:
            raise InvalidValueError("Cannot convert " + str(value) + " to Character")

CharacterType.instance = CharacterType()

