from prompto.argument.CategoryArgument import CategoryArgument
from prompto.argument.ExtendedArgument import ExtendedArgument
from prompto.grammar.IdentifierList import IdentifierList
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.CategoryType import CategoryType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType


class TestAnonymousTypes(BaseOParserTest):

    def setUp(self):
        super(TestAnonymousTypes, self).setUp()
        stmts = self.parseString("attribute id: Integer;\r\n" +
                                 "attribute name: String;\r\n" +
                                 "attribute other: String;\r\n" +
                                 "category Simple ( name );\r\n" +
                                 "category Root(id);\r\n" +
                                 "category DerivedWithOther(other) extends Root;\r\n" +
                                 "category DerivedWithName(name) extends Root;\r\n")
        stmts.register(self.context)


    def testAnonymousAnyType(self):
        # any x
        argument = CategoryArgument(AnyType.instance, "x")
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, AnyType)
        self.assertTrue(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertTrue(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertTrue(TextType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DateType.instance.isAssignableTo(self.context, st))
        self.assertTrue(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertTrue(AnyType.instance.isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("Simple").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("Root").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("DerivedWithOther").isAssignableTo(self.context, st))
        self.assertTrue(CategoryType("DerivedWithName").isAssignableTo(self.context, st))


    def testAnonymousAnyTypeWithAttribute(self):
        # any x with attribute: name
        list = IdentifierList("name")
        argument = ExtendedArgument(AnyType.instance, "x", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertTrue(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple has a name
        self.assertFalse(CategoryType("Root").isAssignableTo(self.context, st))  # since Root has no name
        self.assertFalse(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther has no name
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName has a name


    def testAnonymousCategoryType(self):
        # Root x
        argument = CategoryArgument(CategoryType("Root"), "x")
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertFalse(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple does not extend Root
        self.assertTrue(CategoryType("Root").isAssignableTo(self.context, st))  # since Root is Root
        self.assertTrue(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther extends Root
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName extends Root


    def testAnonymousCategoryTypeWithAttribute(self):
        # Root x with attribute: name
        list = IdentifierList("name")
        argument = ExtendedArgument(CategoryType("Root"), "test", list)
        argument.register(self.context)
        st = argument.getType(self.context)
        self.assertIsInstance(st, CategoryType)
        self.assertFalse(BooleanType.instance.isAssignableTo(self.context, st))
        self.assertFalse(IntegerType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DecimalType.instance.isAssignableTo(self.context, st))
        self.assertFalse(TextType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateType.instance.isAssignableTo(self.context, st))
        self.assertFalse(DateTimeType.instance.isAssignableTo(self.context, st))
        self.assertTrue(MissingType.instance.isAssignableTo(self.context, st))  # missing type always compatible
        self.assertFalse(AnyType.instance.isAssignableTo(self.context, st))  # any type never compatible
        self.assertFalse(CategoryType("Simple").isAssignableTo(self.context, st))  # since Simple does not extend Root
        self.assertFalse(CategoryType("Root").isAssignableTo(self.context, st))  # since Root has no name
        self.assertFalse(
            CategoryType("DerivedWithOther").isAssignableTo(self.context, st))  # since DerivedWithOther has no name
        self.assertTrue(
            CategoryType("DerivedWithName").isAssignableTo(self.context, st))  # since DerivedWithName has a name
