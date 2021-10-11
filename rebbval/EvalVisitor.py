import re
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
    def __is_numeric(value):
        return RebbValHelper.is_numeric(value)

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
        self.visit(unary_ctx_1)
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
            self.__set_value(ctx, str_value[1:len(str_value) - 1])

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
                if self.__is_numeric(element):
                    element = self.__parse_number(element)
                array.append(element)

            self.__set_value(ctx, array)
        except ValueError as e:
            self.__set_value(ctx, None)
            self.__error = e

    # endregion

    # region Compare
    def visitAgeCompare(self, ctx: RebbValParser.AgeCompareContext):
        result = False
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_date(self.__obj) and self.__is_numeric(expr_value):
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

    def visitCompare(self, ctx: RebbValParser.CompareContext):
        result = False
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_string(self.__obj) and self.__is_string(expr_value):
            if ctx.op.type == RebbValParser.EQUAL:
                result = self.__obj == expr_value
            else:
                result = False
                self.__error = "Unsupported Operation"

            self.__set_value(ctx, result)
        elif (self.__is_numeric(self.__obj) and self.__is_numeric(expr_value)) \
                or (self.__is_date(self.__obj) and self.__is_date(expr_value)):
            result = self.__do_compare(self.__obj, expr_value, ctx.op.type)
            self.__set_value(ctx, result)
        else:
            self.__set_value(ctx, False)
            self.__error = "UnsupportedObjectType"

    def __do_compare(self, obj, v, t):
        result = False
        if self.__is_date(obj):
            obj = obj.timestamp()
            v = v.timestamp()

        if t == RebbValParser.EQUAL:
            result = obj == v
        elif t == RebbValParser.NEQUAL:
            result = obj != v
        elif t == RebbValParser.GT:
            result = obj > v
        elif t == RebbValParser.GTE:
            result = obj >= v
        elif t == RebbValParser.LT:
            result = obj < v
        elif t == RebbValParser.LTE:
            result = obj <= v

        return result

    def visitBetween(self, ctx: RebbValParser.BetweenContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        l_value = self.__get_value(ctx.expression(0))
        r_value = self.__get_value(ctx.expression(1))
        if self.__is_numeric(self.__obj) and self.__is_numeric(l_value) and self.__is_numeric(r_value):
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

    def visitInterval(self, ctx: RebbValParser.IntervalContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        l_value = self.__get_value(ctx.expression(0))
        r_value = self.__get_value(ctx.expression(1))
        if (self.__is_numeric(l_value) and self.__is_numeric(r_value) and self.__is_numeric(self.__obj)) \
                or (self.__is_date(self.__obj) and self.__is_date(l_value) and self.__is_date(r_value)):
            result = self.__do_interval_compare(self.__obj, l_value, r_value, ctx.start.text, ctx.end.text)
            self.__set_value(ctx, result)
        else:
            self.__set_value(ctx, False)
            self.__error = "UnsupportedObjectType"

    def __do_interval_compare(self, obj, l, r, start, end):
        if self.__is_date(obj):
            obj = obj.timestamp()
            l = l.timestamp()
            r = r.timestamp()

        start_result = False
        if start == "(" or start == "]":
            start_result = obj > l
        if start == "[":
            start_result = obj >= l

        end_result = False
        if start_result:
            if end == ")" or end == "[":
                end_result = obj < r
            if end == "]":
                end_result = obj <= r;

        return start_result and end_result
    # endregion

    # region Contain/In
    def visitIn(self, ctx: RebbValParser.InContext):
        self.visit(ctx.expression())
        expr_value = self.__get_value(ctx.expression())
        if self.__is_string(self.__obj) and self.__is_string(expr_value):
            self.__set_value(ctx, self.__obj in expr_value)
        elif self.__is_numeric(self.__obj) and self.__is_list(expr_value):
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

    def visitStringPosition(self, ctx: RebbValParser.StringPositionContext):
        expr_context = ctx.expression()
        self.visit(expr_context)
        expr_value = self.__get_value(expr_context)
        if self.__is_string(self.__obj) and self.__is_string(expr_value):
            result = False
            length = len(expr_value)
            if ctx.op.text == "starts":
                result = self.__obj[0:length] == expr_value
            elif ctx.op.text == "ends":
                result = self.__obj[-length:] == expr_value
            self.__set_value(ctx, result)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"
    # endregion

    # region string
    def visitNotEmpty(self, ctx: RebbValParser.NotEmptyContext):
        if self.__is_string(self.__obj):
            self.__set_value(ctx, not(self.__obj is None or self.__obj == ""))
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"

    def visitMaxLength(self, ctx: RebbValParser.MaxLengthContext):
        expr_value = int(ctx.NumbericLiteral().getText())
        if self.__is_string(self.__obj):
            if len(self.__obj) <= expr_value:
                self.__set_value(ctx, True)
            else:
                self.__set_value(ctx, False)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"

    def visitMatch(self, ctx: RebbValParser.MatchContext):
        if self.__is_string(self.__obj):
            expr_value = ctx.regex.text
            regex = expr_value.replace('/', '')
            p = re.compile(regex)
            m = p.search(self.__obj)
            if m is not None:
                self.__set_value(ctx, True)
            else:
                self.__set_value(ctx, False)
        else:
            self.__set_value(ctx, False)
            self.__error = "ObjectTypeNotSupported"
    # endregion

    def visitIs(self, ctx: RebbValParser.IsContext):
        b = BuildInFunctions(self.__config)
        self.__set_value(ctx, b.check(ctx.is_type.type, self.__obj))

    def visitIsHex(self, ctx: RebbValParser.IsHexContext):
        b = BuildInFunctions(self.__config)
        self.__set_value(ctx, b.check_hex(ctx.is_type.type, self.__obj))
