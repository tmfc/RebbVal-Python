# Generated from RebbVal.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\3\3\3\5\3\"\n\3\3\3\5\3%\n\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5U\n\5\3\6\3\6\3\6\3\6\7\6[\n\6")
        buf.write("\f\6\16\6^\13\6\3\6\3\6\3\6\2\3\2\7\2\4\6\b\n\2\t\3\2")
        buf.write("\',\4\2/ACH\4\2??BB\3\2-.\3\2\24\25\4\2\6\6\27\30\4\2")
        buf.write("\7\7\27\30\2u\2\f\3\2\2\2\4$\3\2\2\2\6&\3\2\2\2\bT\3\2")
        buf.write("\2\2\nV\3\2\2\2\f\r\b\2\1\2\r\16\5\4\3\2\16\27\3\2\2\2")
        buf.write("\17\20\f\5\2\2\20\21\7\3\2\2\21\26\5\4\3\2\22\23\f\4\2")
        buf.write("\2\23\24\7\4\2\2\24\26\5\4\3\2\25\17\3\2\2\2\25\22\3\2")
        buf.write("\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3")
        buf.write("\2\2\2\31\27\3\2\2\2\32%\5\6\4\2\33\35\7\5\2\2\34\36\7")
        buf.write("\6\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37!\5")
        buf.write("\6\4\2 \"\7\7\2\2! \3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#%\7")
        buf.write("\b\2\2$\32\3\2\2\2$\33\3\2\2\2$#\3\2\2\2%\5\3\2\2\2&\'")
        buf.write("\5\b\5\2\'\7\3\2\2\2()\t\2\2\2)U\5\b\5\2*+\7\t\2\2+,\5")
        buf.write("\b\5\2,-\7\3\2\2-.\5\b\5\2.U\3\2\2\2/\60\7\n\2\2\60U\5")
        buf.write("\b\5\2\61\62\7\13\2\2\62U\5\b\5\2\63\64\7\5\2\2\64U\7")
        buf.write("\f\2\2\65\66\7\r\2\2\66\67\7\16\2\2\67U\7\35\2\289\7\17")
        buf.write("\2\29U\t\3\2\2:;\7\17\2\2;U\7\20\2\2<=\7\17\2\2=>\7\21")
        buf.write("\2\2>U\t\4\2\2?@\7\17\2\2@U\7I\2\2AB\7\22\2\2BU\7\33\2")
        buf.write("\2CD\t\5\2\2DE\7\23\2\2EU\5\b\5\2FG\t\6\2\2GH\7\26\2\2")
        buf.write("HU\5\b\5\2IJ\t\7\2\2JK\5\b\5\2KL\7\31\2\2LM\5\b\5\2MN")
        buf.write("\t\b\2\2NU\3\2\2\2OU\5\n\6\2PU\7\34\2\2QU\7\35\2\2RU\7")
        buf.write("\36\2\2SU\7\37\2\2T(\3\2\2\2T*\3\2\2\2T/\3\2\2\2T\61\3")
        buf.write("\2\2\2T\63\3\2\2\2T\65\3\2\2\2T8\3\2\2\2T:\3\2\2\2T<\3")
        buf.write("\2\2\2T?\3\2\2\2TA\3\2\2\2TC\3\2\2\2TF\3\2\2\2TI\3\2\2")
        buf.write("\2TO\3\2\2\2TP\3\2\2\2TQ\3\2\2\2TR\3\2\2\2TS\3\2\2\2U")
        buf.write("\t\3\2\2\2VW\7\30\2\2W\\\7\35\2\2XY\7\32\2\2Y[\7\35\2")
        buf.write("\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2")
        buf.write("^\\\3\2\2\2_`\7\27\2\2`\13\3\2\2\2\t\25\27\35!$T\\")
        return buf.getvalue()


class RebbValParser ( Parser ):

    grammarFileName = "RebbVal.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'('", "')'", 
                     "'-'", "'between'", "'in'", "'contains'", "'empty'", 
                     "'max'", "'length'", "'is'", "'unique'", "'hex'", "'match'", 
                     "'than'", "'starts'", "'ends'", "'with'", "']'", "'['", 
                     "'..'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'older'", "'younger'", "'true'", "'false'", "'leapyear'", 
                     "'leapday'", "'domain'", "'email'", "'ipv4'", "'ipv6'", 
                     "'private_ip'", "'url'", "'MAC'", "'IMEI'", "'IMEISV'", 
                     "'ISBN'", "'percentage'", "'base64'", "'number'", "'int'", 
                     "'float'", "'color'", "'phone'", "'mobile'", "'UUID'", 
                     "'gbcode'", "'ID'", "'passport'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "RegularExpressionLiteral", "StringLiteral", 
                      "NumbericLiteral", "DateLiteral", "TimeLiteral", "DIGITS", 
                      "YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", 
                      "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "OLDER", 
                      "YOUNGER", "TRUE", "FALSE", "LEAPYEAR", "LEAPDAY", 
                      "DOMAIN", "EMAIL", "IPV4", "IPV6", "PRIVATEIP", "URL", 
                      "MAC", "IMEI", "IMEISV", "ISBN", "PERCENTAGE", "BASE64", 
                      "NUMBER", "INT", "FLOAT", "COLOR", "PHONE", "MOBILE", 
                      "UUID", "GBCODE", "ID", "PASSPORT", "CustomFunction", 
                      "NEWLINE", "WS" ]

    RULE_unaryTests = 0
    RULE_unaryTest = 1
    RULE_positiveUnaryTest = 2
    RULE_expression = 3
    RULE_arrayLiteral = 4

    ruleNames =  [ "unaryTests", "unaryTest", "positiveUnaryTest", "expression", 
                   "arrayLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    RegularExpressionLiteral=25
    StringLiteral=26
    NumbericLiteral=27
    DateLiteral=28
    TimeLiteral=29
    DIGITS=30
    YEAR=31
    MONTH=32
    DAY=33
    HOUR=34
    MINUTE=35
    SECOND=36
    EQUAL=37
    NEQUAL=38
    LT=39
    LTE=40
    GT=41
    GTE=42
    OLDER=43
    YOUNGER=44
    TRUE=45
    FALSE=46
    LEAPYEAR=47
    LEAPDAY=48
    DOMAIN=49
    EMAIL=50
    IPV4=51
    IPV6=52
    PRIVATEIP=53
    URL=54
    MAC=55
    IMEI=56
    IMEISV=57
    ISBN=58
    PERCENTAGE=59
    BASE64=60
    NUMBER=61
    INT=62
    FLOAT=63
    COLOR=64
    PHONE=65
    MOBILE=66
    UUID=67
    GBCODE=68
    ID=69
    PASSPORT=70
    CustomFunction=71
    NEWLINE=72
    WS=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UnaryTestsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RebbValParser.RULE_unaryTests

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DisjunctionContext(UnaryTestsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryTests(self):
            return self.getTypedRuleContext(RebbValParser.UnaryTestsContext,0)

        def unaryTest(self):
            return self.getTypedRuleContext(RebbValParser.UnaryTestContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(UnaryTestsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryTests(self):
            return self.getTypedRuleContext(RebbValParser.UnaryTestsContext,0)

        def unaryTest(self):
            return self.getTypedRuleContext(RebbValParser.UnaryTestContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class SingleTestContext(UnaryTestsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryTest(self):
            return self.getTypedRuleContext(RebbValParser.UnaryTestContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTest" ):
                listener.enterSingleTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTest" ):
                listener.exitSingleTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTest" ):
                return visitor.visitSingleTest(self)
            else:
                return visitor.visitChildren(self)



    def unaryTests(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RebbValParser.UnaryTestsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_unaryTests, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RebbValParser.SingleTestContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 11
            self.unaryTest()
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = RebbValParser.ConjunctionContext(self, RebbValParser.UnaryTestsContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryTests)
                        self.state = 13
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 14
                        self.match(RebbValParser.T__0)
                        self.state = 15
                        self.unaryTest()
                        pass

                    elif la_ == 2:
                        localctx = RebbValParser.DisjunctionContext(self, RebbValParser.UnaryTestsContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryTests)
                        self.state = 16
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 17
                        self.match(RebbValParser.T__1)
                        self.state = 18
                        self.unaryTest()
                        pass

             
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryTestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RebbValParser.RULE_unaryTest

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IgnoreUnaryTestContext(UnaryTestContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoreUnaryTest" ):
                listener.enterIgnoreUnaryTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoreUnaryTest" ):
                listener.exitIgnoreUnaryTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnoreUnaryTest" ):
                return visitor.visitIgnoreUnaryTest(self)
            else:
                return visitor.visitChildren(self)


    class NormalUnaryTestContext(UnaryTestContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def positiveUnaryTest(self):
            return self.getTypedRuleContext(RebbValParser.PositiveUnaryTestContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalUnaryTest" ):
                listener.enterNormalUnaryTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalUnaryTest" ):
                listener.exitNormalUnaryTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalUnaryTest" ):
                return visitor.visitNormalUnaryTest(self)
            else:
                return visitor.visitChildren(self)


    class NegationUnaryTestContext(UnaryTestContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.UnaryTestContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def positiveUnaryTest(self):
            return self.getTypedRuleContext(RebbValParser.PositiveUnaryTestContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegationUnaryTest" ):
                listener.enterNegationUnaryTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegationUnaryTest" ):
                listener.exitNegationUnaryTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegationUnaryTest" ):
                return visitor.visitNegationUnaryTest(self)
            else:
                return visitor.visitChildren(self)



    def unaryTest(self):

        localctx = RebbValParser.UnaryTestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unaryTest)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = RebbValParser.NormalUnaryTestContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.positiveUnaryTest()
                pass

            elif la_ == 2:
                localctx = RebbValParser.NegationUnaryTestContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(RebbValParser.T__2)
                self.state = 27
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.match(RebbValParser.T__3)


                self.state = 29
                self.positiveUnaryTest()
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.match(RebbValParser.T__4)


                pass

            elif la_ == 3:
                localctx = RebbValParser.IgnoreUnaryTestContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(RebbValParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositiveUnaryTestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)


        def getRuleIndex(self):
            return RebbValParser.RULE_positiveUnaryTest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositiveUnaryTest" ):
                listener.enterPositiveUnaryTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositiveUnaryTest" ):
                listener.exitPositiveUnaryTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositiveUnaryTest" ):
                return visitor.visitPositiveUnaryTest(self)
            else:
                return visitor.visitChildren(self)




    def positiveUnaryTest(self):

        localctx = RebbValParser.PositiveUnaryTestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_positiveUnaryTest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RebbValParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DateLiteral(self):
            return self.getToken(RebbValParser.DateLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)


    class AgeCompareContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)

        def OLDER(self):
            return self.getToken(RebbValParser.OLDER, 0)
        def YOUNGER(self):
            return self.getToken(RebbValParser.YOUNGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgeCompare" ):
                listener.enterAgeCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgeCompare" ):
                listener.exitAgeCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgeCompare" ):
                return visitor.visitAgeCompare(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StringLiteral(self):
            return self.getToken(RebbValParser.StringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class InContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIn" ):
                listener.enterIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIn" ):
                listener.exitIn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIn" ):
                return visitor.visitIn(self)
            else:
                return visitor.visitChildren(self)


    class ArrayIsUniqueContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayIsUnique" ):
                listener.enterArrayIsUnique(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayIsUnique" ):
                listener.exitArrayIsUnique(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayIsUnique" ):
                return visitor.visitArrayIsUnique(self)
            else:
                return visitor.visitChildren(self)


    class IsCustomContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.is_type = None # Token
            self.copyFrom(ctx)

        def CustomFunction(self):
            return self.getToken(RebbValParser.CustomFunction, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsCustom" ):
                listener.enterIsCustom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsCustom" ):
                listener.exitIsCustom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsCustom" ):
                return visitor.visitIsCustom(self)
            else:
                return visitor.visitChildren(self)


    class BetweenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RebbValParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RebbValParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetween" ):
                listener.enterBetween(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetween" ):
                listener.exitBetween(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetween" ):
                return visitor.visitBetween(self)
            else:
                return visitor.visitChildren(self)


    class IsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.is_type = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(RebbValParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(RebbValParser.FALSE, 0)
        def LEAPYEAR(self):
            return self.getToken(RebbValParser.LEAPYEAR, 0)
        def LEAPDAY(self):
            return self.getToken(RebbValParser.LEAPDAY, 0)
        def DOMAIN(self):
            return self.getToken(RebbValParser.DOMAIN, 0)
        def EMAIL(self):
            return self.getToken(RebbValParser.EMAIL, 0)
        def IPV4(self):
            return self.getToken(RebbValParser.IPV4, 0)
        def IPV6(self):
            return self.getToken(RebbValParser.IPV6, 0)
        def PRIVATEIP(self):
            return self.getToken(RebbValParser.PRIVATEIP, 0)
        def URL(self):
            return self.getToken(RebbValParser.URL, 0)
        def MAC(self):
            return self.getToken(RebbValParser.MAC, 0)
        def IMEI(self):
            return self.getToken(RebbValParser.IMEI, 0)
        def IMEISV(self):
            return self.getToken(RebbValParser.IMEISV, 0)
        def ISBN(self):
            return self.getToken(RebbValParser.ISBN, 0)
        def PERCENTAGE(self):
            return self.getToken(RebbValParser.PERCENTAGE, 0)
        def BASE64(self):
            return self.getToken(RebbValParser.BASE64, 0)
        def NUMBER(self):
            return self.getToken(RebbValParser.NUMBER, 0)
        def INT(self):
            return self.getToken(RebbValParser.INT, 0)
        def FLOAT(self):
            return self.getToken(RebbValParser.FLOAT, 0)
        def PHONE(self):
            return self.getToken(RebbValParser.PHONE, 0)
        def MOBILE(self):
            return self.getToken(RebbValParser.MOBILE, 0)
        def UUID(self):
            return self.getToken(RebbValParser.UUID, 0)
        def GBCODE(self):
            return self.getToken(RebbValParser.GBCODE, 0)
        def ID(self):
            return self.getToken(RebbValParser.ID, 0)
        def PASSPORT(self):
            return self.getToken(RebbValParser.PASSPORT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIs" ):
                listener.enterIs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIs" ):
                listener.exitIs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIs" ):
                return visitor.visitIs(self)
            else:
                return visitor.visitChildren(self)


    class IsHexContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.is_type = None # Token
            self.copyFrom(ctx)

        def COLOR(self):
            return self.getToken(RebbValParser.COLOR, 0)
        def NUMBER(self):
            return self.getToken(RebbValParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsHex" ):
                listener.enterIsHex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsHex" ):
                listener.exitIsHex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsHex" ):
                return visitor.visitIsHex(self)
            else:
                return visitor.visitChildren(self)


    class MaxLengthContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NumbericLiteral(self):
            return self.getToken(RebbValParser.NumbericLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxLength" ):
                listener.enterMaxLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxLength" ):
                listener.exitMaxLength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxLength" ):
                return visitor.visitMaxLength(self)
            else:
                return visitor.visitChildren(self)


    class StringPositionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringPosition" ):
                listener.enterStringPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringPosition" ):
                listener.exitStringPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringPosition" ):
                return visitor.visitStringPosition(self)
            else:
                return visitor.visitChildren(self)


    class MatchContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.regex = None # Token
            self.copyFrom(ctx)

        def RegularExpressionLiteral(self):
            return self.getToken(RebbValParser.RegularExpressionLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch" ):
                listener.enterMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch" ):
                listener.exitMatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch" ):
                return visitor.visitMatch(self)
            else:
                return visitor.visitChildren(self)


    class ArrayContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(RebbValParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NumbericLiteral(self):
            return self.getToken(RebbValParser.NumbericLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class ContainsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContains" ):
                listener.enterContains(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContains" ):
                listener.exitContains(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContains" ):
                return visitor.visitContains(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(RebbValParser.ExpressionContext,0)

        def EQUAL(self):
            return self.getToken(RebbValParser.EQUAL, 0)
        def NEQUAL(self):
            return self.getToken(RebbValParser.NEQUAL, 0)
        def LT(self):
            return self.getToken(RebbValParser.LT, 0)
        def LTE(self):
            return self.getToken(RebbValParser.LTE, 0)
        def GT(self):
            return self.getToken(RebbValParser.GT, 0)
        def GTE(self):
            return self.getToken(RebbValParser.GTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class NotEmptyContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEmpty" ):
                listener.enterNotEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEmpty" ):
                listener.exitNotEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEmpty" ):
                return visitor.visitNotEmpty(self)
            else:
                return visitor.visitChildren(self)


    class TimeContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TimeLiteral(self):
            return self.getToken(RebbValParser.TimeLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime" ):
                return visitor.visitTime(self)
            else:
                return visitor.visitChildren(self)


    class IntervalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RebbValParser.ExpressionContext
            super().__init__(parser)
            self.start = None # Token
            self.end = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RebbValParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RebbValParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval" ):
                listener.enterInterval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval" ):
                listener.exitInterval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = RebbValParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = RebbValParser.CompareContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RebbValParser.EQUAL) | (1 << RebbValParser.NEQUAL) | (1 << RebbValParser.LT) | (1 << RebbValParser.LTE) | (1 << RebbValParser.GT) | (1 << RebbValParser.GTE))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 39
                self.expression()
                pass

            elif la_ == 2:
                localctx = RebbValParser.BetweenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(RebbValParser.T__6)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(RebbValParser.T__0)
                self.state = 43
                self.expression()
                pass

            elif la_ == 3:
                localctx = RebbValParser.InContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(RebbValParser.T__7)
                self.state = 46
                self.expression()
                pass

            elif la_ == 4:
                localctx = RebbValParser.ContainsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.match(RebbValParser.T__8)
                self.state = 48
                self.expression()
                pass

            elif la_ == 5:
                localctx = RebbValParser.NotEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.match(RebbValParser.T__2)
                self.state = 50
                self.match(RebbValParser.T__9)
                pass

            elif la_ == 6:
                localctx = RebbValParser.MaxLengthContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.match(RebbValParser.T__10)
                self.state = 52
                self.match(RebbValParser.T__11)
                self.state = 53
                self.match(RebbValParser.NumbericLiteral)
                pass

            elif la_ == 7:
                localctx = RebbValParser.IsContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(RebbValParser.T__12)
                self.state = 55
                localctx.is_type = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (RebbValParser.TRUE - 45)) | (1 << (RebbValParser.FALSE - 45)) | (1 << (RebbValParser.LEAPYEAR - 45)) | (1 << (RebbValParser.LEAPDAY - 45)) | (1 << (RebbValParser.DOMAIN - 45)) | (1 << (RebbValParser.EMAIL - 45)) | (1 << (RebbValParser.IPV4 - 45)) | (1 << (RebbValParser.IPV6 - 45)) | (1 << (RebbValParser.PRIVATEIP - 45)) | (1 << (RebbValParser.URL - 45)) | (1 << (RebbValParser.MAC - 45)) | (1 << (RebbValParser.IMEI - 45)) | (1 << (RebbValParser.IMEISV - 45)) | (1 << (RebbValParser.ISBN - 45)) | (1 << (RebbValParser.PERCENTAGE - 45)) | (1 << (RebbValParser.BASE64 - 45)) | (1 << (RebbValParser.NUMBER - 45)) | (1 << (RebbValParser.INT - 45)) | (1 << (RebbValParser.FLOAT - 45)) | (1 << (RebbValParser.PHONE - 45)) | (1 << (RebbValParser.MOBILE - 45)) | (1 << (RebbValParser.UUID - 45)) | (1 << (RebbValParser.GBCODE - 45)) | (1 << (RebbValParser.ID - 45)) | (1 << (RebbValParser.PASSPORT - 45)))) != 0)):
                    localctx.is_type = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 8:
                localctx = RebbValParser.ArrayIsUniqueContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.match(RebbValParser.T__12)
                self.state = 57
                self.match(RebbValParser.T__13)
                pass

            elif la_ == 9:
                localctx = RebbValParser.IsHexContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 58
                self.match(RebbValParser.T__12)
                self.state = 59
                self.match(RebbValParser.T__14)
                self.state = 60
                localctx.is_type = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RebbValParser.NUMBER or _la==RebbValParser.COLOR):
                    localctx.is_type = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 10:
                localctx = RebbValParser.IsCustomContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 61
                self.match(RebbValParser.T__12)
                self.state = 62
                localctx.is_type = self.match(RebbValParser.CustomFunction)
                pass

            elif la_ == 11:
                localctx = RebbValParser.MatchContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 63
                self.match(RebbValParser.T__15)
                self.state = 64
                localctx.regex = self.match(RebbValParser.RegularExpressionLiteral)
                pass

            elif la_ == 12:
                localctx = RebbValParser.AgeCompareContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 65
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RebbValParser.OLDER or _la==RebbValParser.YOUNGER):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.match(RebbValParser.T__16)
                self.state = 67
                self.expression()
                pass

            elif la_ == 13:
                localctx = RebbValParser.StringPositionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 68
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RebbValParser.T__17 or _la==RebbValParser.T__18):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self.match(RebbValParser.T__19)
                self.state = 70
                self.expression()
                pass

            elif la_ == 14:
                localctx = RebbValParser.IntervalContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 71
                localctx.start = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RebbValParser.T__3) | (1 << RebbValParser.T__20) | (1 << RebbValParser.T__21))) != 0)):
                    localctx.start = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72
                self.expression()
                self.state = 73
                self.match(RebbValParser.T__22)
                self.state = 74
                self.expression()
                self.state = 75
                localctx.end = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RebbValParser.T__4) | (1 << RebbValParser.T__20) | (1 << RebbValParser.T__21))) != 0)):
                    localctx.end = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 15:
                localctx = RebbValParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 77
                self.arrayLiteral()
                pass

            elif la_ == 16:
                localctx = RebbValParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 78
                self.match(RebbValParser.StringLiteral)
                pass

            elif la_ == 17:
                localctx = RebbValParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 79
                self.match(RebbValParser.NumbericLiteral)
                pass

            elif la_ == 18:
                localctx = RebbValParser.DateContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 80
                self.match(RebbValParser.DateLiteral)
                pass

            elif la_ == 19:
                localctx = RebbValParser.TimeContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 81
                self.match(RebbValParser.TimeLiteral)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumbericLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(RebbValParser.NumbericLiteral)
            else:
                return self.getToken(RebbValParser.NumbericLiteral, i)

        def getRuleIndex(self):
            return RebbValParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = RebbValParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RebbValParser.T__21)
            self.state = 85
            self.match(RebbValParser.NumbericLiteral)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RebbValParser.T__23:
                self.state = 86
                self.match(RebbValParser.T__23)
                self.state = 87
                self.match(RebbValParser.NumbericLiteral)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(RebbValParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.unaryTests_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unaryTests_sempred(self, localctx:UnaryTestsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




