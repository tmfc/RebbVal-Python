from datetime import timezone

from rebbval.RebbValConfig import RebbValConfig
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
        return self.__values[key]

    def __set_value(self, key, value):
        self.__values[key] = value

    def __is_bool(self, value):
        return isinstance(value, bool)

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


    # endregion
