from antlr4.error.ErrorListener import ErrorListener


class RebbValErrorListener(ErrorListener):
    INSTANCE = None

    def __init__(self):
        self.error = ""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error = "line " + str(line) + ":" + str(column) + " " + msg


RebbValErrorListener.INSTANCE = RebbValErrorListener()
