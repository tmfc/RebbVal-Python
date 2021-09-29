from datetime import timezone, datetime, time
from dateutil.relativedelta import relativedelta

from rebbval.BuildInFunctions import BuildInFunctions
from rebbval.RebbValConfig import RebbValConfig
from rebbval.RebbValHelper import RebbValHelper
from rebbval.RebbValParser import RebbValParser
from rebbval.RebbValVisitor import RebbValVisitor


class EvalVisitor(RebbValVisitor):
    __timezone = "Asia/Shanghai"
    __valid = False
    __error = ""
    __values = dict()
    __custom_functions = dict()
    __config = dict()

    def __init__(self, obj, global_setting):
        self.__obj = obj
        self.__init_config(global_setting)

    def __init_config(self, global_setting):
        if global_setting is not None:
            self.__config = global_setting.copy()
        else:
            self.__config = dict()

        if RebbValConfig.TRUE_STRING not in self.__config:
            self.__config[RebbValConfig.TRUE_STRING] = ['true', 'on', '1', 'yes', 'ok']

    def set_timezone(self, tz):
        self.__timezone = tz

    def get_timezone(self):
        return self.__timezone

    def set_object(self, obj):
        self.__valid = False
        self.__error = ""

        self.__obj = obj

    def is_valid(self):
        return self.__valid

    def get_error(self):
        return self.__error

    def register_custom_validator(self, name, func):
        self.__custom_functions[name] = func

    def add_config(self, key, value):
        self.__config[key] = value

    def __get_value(self, key):
        if key in self.__values:
            return self.__values[key]
        else:
            return None

    def __set_value(self, key, value):
        self.__values[key] = value

    @staticmethod
    def __is_bool(value):
        return RebbValHelper.is_bool(value)

    @staticmethod
    def __is_date(value):
        return RebbValHelper.is_date(value)

    @staticmethod
    def __is_list(value):
        return RebbValHelper.is_list(value)
    
    @staticmethod
    def __is_number(value):
        return RebbValHelper.is_number(value)

    @staticmethod
    def __parse_number(value):
        return RebbValHelper.parse_number(value)

    @staticmethod
    def __is_string(value):
        return RebbValHelper.is_string(value)

    # region Unary Test and Combination
    def visitConjunction(self, ctx: RebbValParser.ConjunctionContext):
        unary_ctx_0 = ctx.unaryTests()
        unary_ctx_1 = ctx.unaryTest()

        self.visit(unary_ctx_0)
        self.visit(unary_ctx_1)
        if self.__is_bool(self.__get_value(unary_ctx_0)) \
                and self.__is_bool(self.__get_value(unary_ctx_1)):
            value_0 = self.__get_value(unary_ctx_0)
            value_1 = self.__get_value(unary_ctx_1)
            self.__set_value(ctx, value_0 and value_1)
            self.__valid = value_0 and value_1
        else:
            self.__set_value(ctx, False)
            self.__valid = False

    def visitDisjunction(self, ctx: RebbValParser.DisjunctionContext):
        unary_ctx_0 = ctx.unaryTests()
        unary_ctx_1 = ctx.unaryTest()
        self.visit(unary_ctx_0)
        self.visit(unary_ctx_0)
        if self.__is_bool(self.__get_value(unary_ctx_0)) \
                and self.__is_bool(self.__get_value(unary_ctx_1)):
            value_0 = self.__get_value(unary_ctx_0)
            value_1 = self.__get_value(unary_ctx_1)
            self.__set_value(ctx, value_0 or value_1)
            self.__valid = value_0 or value_1
        else:
            self.__set_value(ctx, False)
            self.__valid = False
            self.__error = "ExpressionValueTypeNotMatch"

    def visitSingleTest(self, ctx: RebbValParser.SingleTestContext):
        unary_ctx = ctx.unaryTest()
        self.visit(unary_ctx)

        if self.__is_bool(self.__get_value(unary_ctx)):
            value = self.__get_value(unary_ctx)
            self.__set_value(ctx, value)
            self.__valid = value
        else:
            self.__set_value(ctx, False)
            self.__valid = False
            self.__error = "ExpressionValueTypeNotMatch"

    def visitNormalUnaryTest(self, ctx: RebbValParser.NormalUnaryTestContext):
        self.visit(ctx.positiveUnaryTest())
        self.__set_value(ctx, self.__get_value(ctx.positiveUnaryTest()))

    def visitNegationUnaryTest(self, ctx: RebbValParser.NegationUnaryTestContext):
        unary_test_ctx = ctx.positiveUnaryTest()
        self.visit(unary_test_ctx)
        if self.__is_bool(self.__get_value(unary_test_ctx)):
            value = self.__get_value(unary_test_ctx)
            self.__set_value(ctx, not value)
        else:
            self.__set_value(ctx, False)
            self.__error = "ExpressionValueTypeNotMatch"

    def visitIgnoreUnaryTest(self, ctx: RebbValParser.IgnoreUnaryTestContext):
        self.__set_value(ctx, True)

    def visitPositiveUnaryTest(self, ctx: RebbValParser.PositiveUnaryTestContext):
        self.visit(ctx.expression())
        self.__set_value(ctx, self.__get_value(ctx.expression()))
    # endregion

    # region Basic element
    # String
    def visitString(self, ctx: RebbValParser.StringContext):
        str_value = ctx.StringLiteral().getText()
        if str_value is not None:
            self.__set_value(ctx, str_value.substring(1, str_value.length() -1))

    # Number 
    def visitNumber(self, ctx: RebbValParser.NumberContext):
        try:
            self.__set_value(ctx, self.__parse_number(ctx.NumbericLiteral().getText()))
        except ValueError as e:
            self.__set_value(ctx, None)
            self.__error = e

    # Date 
    def visitDate(self, ctx: RebbValParser.DateContext):
        try:
            date = datetime.strptime(ctx.DateLiteral().getText(), '%Y-%m-%d')
            self.__set_value(ctx, date)
        except ValueError as e:
            self.__set_value(ctx, None)
            self.__error = e

    # Array
    def visitArray(self, ctx: RebbValParser.ArrayContext):
        try:
            array = []
            for tree in ctx.arrayLiteral().NumbericLiteral():
                element = tree.getText()
                if self.__is_number(element):
                    element = self.__parse_number(element)
                array.append(element)

            self.__set_value(ctx, array)
        except ValueError as e:
            self.__set_value(ctx, None)
            self.__error = e

    # endregion

    def visitAgeCompare(self, ctx: RebbValParser.AgeCompareContext):
        result = False
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_date(self.__obj) and self.__is_number(expr_value):
            birth = self.__obj

            now = datetime.now()

            diff = relativedelta(now, birth)
            diff_y = diff.years
            if diff.months > 0:
                diff_y = diff_y + diff.months / 12.0
            if diff.days > 0:
                diff_y = diff_y + diff.days / 365.2425

            expr_value = expr_value

            if ctx.op.type == RebbValParser.OLDER:
                result = diff_y > expr_value
            elif ctx.op.type == RebbValParser.YOUNGER:
                result = diff_y < expr_value

            if result:
                self.__set_value(ctx, True)
            else:
                self.__set_value(ctx, False)
        else:
            self.__valid = False
            self.__error = "ObjectTypeNotSupported"

    def visitBetween(self, ctx: RebbValParser.BetweenContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        l_value = self.__get_value(ctx.expression(0))
        r_value = self.__get_value(ctx.expression(1))
        if self.__is_number(self.__obj) and self.__is_number(l_value) and self.__is_number(r_value):
            if l_value <= self.__obj <= r_value:
                self.__set_value(ctx, True)
            else:
                self.__set_value(ctx, False)
        elif self.__is_date(self.__obj) and self.__is_date(l_value) and self.__is_date(r_value):
            if l_value <= self.__obj <= r_value:
                self.__set_value(ctx, True)

            else:
                self.__set_value(ctx, False)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"

    def visitIn(self, ctx: RebbValParser.InContext):
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_string(self.__obj) and self.__is_string(expr_value):
            self.__set_value(ctx, self.__obj in expr_value)
        elif self.__is_number(self.__obj) and self.__is_list(expr_value):
            self.__set_value(ctx, self.__obj in expr_value)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"

    def visitContains(self, ctx: RebbValParser.ContainsContext):
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_string(self.__obj) and self.__is_string(expr_value):
            if expr_value in self.__obj:
                self.__set_value(ctx, True)
            else:
                self.__set_value(ctx, False)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"

    def visitIs(self, ctx: RebbValParser.IsContext):
        b = BuildInFunctions(self.__config)
        # result = False
        self.__set_value(ctx, b.check(ctx.is_type.type, self.__obj))
