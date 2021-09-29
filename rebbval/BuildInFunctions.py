from rebbval.RebbValConfig import RebbValConfig
from rebbval.RebbValHelper import RebbValHelper
from rebbval.RebbValParser import RebbValParser


class BuildInFunctions:
    def __init__(self, config):
        self.__config = config
        self.__function_map = dict()
        self.error = ""
        self.__init_function_map()

    def __init_function_map(self):
        self.__function_map[str(RebbValParser.TRUE)] = self.check_true
        self.__function_map[str(RebbValParser.FALSE)] = self.check_false

    def check(self, check_type, obj):
        return self.__function_map[str(check_type)](obj)

    def check_true(self, obj):
        if isinstance(obj, bool):
            return obj is True
        elif isinstance(obj, str):
            return obj in self.__config[RebbValConfig.TRUE_STRING]
        elif RebbValHelper.is_number(obj):
            return RebbValHelper.parse_number(obj) == 1
        else:
            self.error = "ObjectTypeNotSupport"
            return False

    def check_false(self, obj):
        return not self.check_true(obj)