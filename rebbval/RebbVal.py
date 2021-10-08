import datetime

from antlr4 import InputStream, CommonTokenStream

from rebbval.RebbValErrorListener import RebbValErrorListener
from rebbval.EvalVisitor import EvalVisitor
from rebbval.RebbValHelper import RebbValHelper
from rebbval.RebbValLexer import RebbValLexer
from rebbval.RebbValParser import RebbValParser


class RebbVal:
    global_config = dict()

    def __init__(self):
        self.has_error = False
        self.errors = []
        self.engine = EvalVisitor("", RebbVal.global_config)

    def date(self, date_str):
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as error:
            self.errors.append(str(error))
            return None

    def year(self, year_str):
        try:
            return datetime.datetime.strptime(year_str + "-01-01", '%Y-%m-%d')
        except ValueError as error:
            self.errors.append(str(error))
            return None


    @staticmethod
    def add_global_config(key, value):
        RebbVal.global_config[key] = value

    def add_config(self, key, value):
        self.engine.add_config(key, value)

    def val(self, obj, condition):
        self.errors = []

        input_stream = InputStream(condition)
        lexer = RebbValLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = RebbValParser(stream)
        parser.addErrorListener(RebbValErrorListener.INSTANCE)
        tree = parser.unaryTests()
        if RebbValErrorListener.INSTANCE.error:
            self.errors.append(RebbValErrorListener.INSTANCE.error)
            RebbValErrorListener.INSTANCE.error = ""
            return False

        self.engine.set_object(obj)
        self.engine.visit(tree)
        if not self.engine.is_valid():
            self.has_error = True
            if obj is None:
                error_message = "object is null"
            else:
                error_message = str(obj) + " " + condition + " failed"

            if self.engine.get_error() is not None and self.engine.get_error() != "":
                error_message = error_message + "(" + self.engine.get_error() + ")"

            self.errors.append(error_message)
            return False

        return True

