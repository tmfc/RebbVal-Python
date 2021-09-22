import datetime

from antlr4 import InputStream, CommonTokenStream

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

    def val(self, obj, condition):
        self.errors = []

        input_stream = InputStream(condition)
        lexer = RebbValLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = RebbValParser(stream)
        tree = parser.unaryTests()

        self.engine.set_object(obj)
        self.engine.visit(tree)
        return self.engine.is_valid()

