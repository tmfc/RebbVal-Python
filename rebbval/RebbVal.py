import datetime

from antlr4 import InputStream, CommonTokenStream

from rebbval.RebbValErrorListener import RebbValErrorListener
from rebbval.EvalVisitor import EvalVisitor
from rebbval.RebbValLexer import RebbValLexer
from rebbval.RebbValParser import RebbValParser


class RebbVal:
    global_config = dict()

    def __init__(self):
        self.errors = []
        self.engine = EvalVisitor("", RebbVal.global_config)

    def date(self, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')

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
            return False

        self.engine.set_object(obj)
        self.engine.visit(tree)
        return self.engine.is_valid()

