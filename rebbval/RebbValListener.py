# Generated from RebbVal.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RebbValParser import RebbValParser
else:
    from RebbValParser import RebbValParser

# This class defines a complete listener for a parse tree produced by RebbValParser.
class RebbValListener(ParseTreeListener):

    # Enter a parse tree produced by RebbValParser#Disjunction.
    def enterDisjunction(self, ctx:RebbValParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by RebbValParser#Disjunction.
    def exitDisjunction(self, ctx:RebbValParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by RebbValParser#Conjunction.
    def enterConjunction(self, ctx:RebbValParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by RebbValParser#Conjunction.
    def exitConjunction(self, ctx:RebbValParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by RebbValParser#SingleTest.
    def enterSingleTest(self, ctx:RebbValParser.SingleTestContext):
        pass

    # Exit a parse tree produced by RebbValParser#SingleTest.
    def exitSingleTest(self, ctx:RebbValParser.SingleTestContext):
        pass


    # Enter a parse tree produced by RebbValParser#NormalUnaryTest.
    def enterNormalUnaryTest(self, ctx:RebbValParser.NormalUnaryTestContext):
        pass

    # Exit a parse tree produced by RebbValParser#NormalUnaryTest.
    def exitNormalUnaryTest(self, ctx:RebbValParser.NormalUnaryTestContext):
        pass


    # Enter a parse tree produced by RebbValParser#NegationUnaryTest.
    def enterNegationUnaryTest(self, ctx:RebbValParser.NegationUnaryTestContext):
        pass

    # Exit a parse tree produced by RebbValParser#NegationUnaryTest.
    def exitNegationUnaryTest(self, ctx:RebbValParser.NegationUnaryTestContext):
        pass


    # Enter a parse tree produced by RebbValParser#IgnoreUnaryTest.
    def enterIgnoreUnaryTest(self, ctx:RebbValParser.IgnoreUnaryTestContext):
        pass

    # Exit a parse tree produced by RebbValParser#IgnoreUnaryTest.
    def exitIgnoreUnaryTest(self, ctx:RebbValParser.IgnoreUnaryTestContext):
        pass


    # Enter a parse tree produced by RebbValParser#positiveUnaryTest.
    def enterPositiveUnaryTest(self, ctx:RebbValParser.PositiveUnaryTestContext):
        pass

    # Exit a parse tree produced by RebbValParser#positiveUnaryTest.
    def exitPositiveUnaryTest(self, ctx:RebbValParser.PositiveUnaryTestContext):
        pass


    # Enter a parse tree produced by RebbValParser#Compare.
    def enterCompare(self, ctx:RebbValParser.CompareContext):
        pass

    # Exit a parse tree produced by RebbValParser#Compare.
    def exitCompare(self, ctx:RebbValParser.CompareContext):
        pass


    # Enter a parse tree produced by RebbValParser#Between.
    def enterBetween(self, ctx:RebbValParser.BetweenContext):
        pass

    # Exit a parse tree produced by RebbValParser#Between.
    def exitBetween(self, ctx:RebbValParser.BetweenContext):
        pass


    # Enter a parse tree produced by RebbValParser#In.
    def enterIn(self, ctx:RebbValParser.InContext):
        pass

    # Exit a parse tree produced by RebbValParser#In.
    def exitIn(self, ctx:RebbValParser.InContext):
        pass


    # Enter a parse tree produced by RebbValParser#Contains.
    def enterContains(self, ctx:RebbValParser.ContainsContext):
        pass

    # Exit a parse tree produced by RebbValParser#Contains.
    def exitContains(self, ctx:RebbValParser.ContainsContext):
        pass


    # Enter a parse tree produced by RebbValParser#NotEmpty.
    def enterNotEmpty(self, ctx:RebbValParser.NotEmptyContext):
        pass

    # Exit a parse tree produced by RebbValParser#NotEmpty.
    def exitNotEmpty(self, ctx:RebbValParser.NotEmptyContext):
        pass


    # Enter a parse tree produced by RebbValParser#MaxLength.
    def enterMaxLength(self, ctx:RebbValParser.MaxLengthContext):
        pass

    # Exit a parse tree produced by RebbValParser#MaxLength.
    def exitMaxLength(self, ctx:RebbValParser.MaxLengthContext):
        pass


    # Enter a parse tree produced by RebbValParser#Is.
    def enterIs(self, ctx:RebbValParser.IsContext):
        pass

    # Exit a parse tree produced by RebbValParser#Is.
    def exitIs(self, ctx:RebbValParser.IsContext):
        pass


    # Enter a parse tree produced by RebbValParser#IsHex.
    def enterIsHex(self, ctx:RebbValParser.IsHexContext):
        pass

    # Exit a parse tree produced by RebbValParser#IsHex.
    def exitIsHex(self, ctx:RebbValParser.IsHexContext):
        pass


    # Enter a parse tree produced by RebbValParser#IsCustom.
    def enterIsCustom(self, ctx:RebbValParser.IsCustomContext):
        pass

    # Exit a parse tree produced by RebbValParser#IsCustom.
    def exitIsCustom(self, ctx:RebbValParser.IsCustomContext):
        pass


    # Enter a parse tree produced by RebbValParser#Match.
    def enterMatch(self, ctx:RebbValParser.MatchContext):
        pass

    # Exit a parse tree produced by RebbValParser#Match.
    def exitMatch(self, ctx:RebbValParser.MatchContext):
        pass


    # Enter a parse tree produced by RebbValParser#AgeCompare.
    def enterAgeCompare(self, ctx:RebbValParser.AgeCompareContext):
        pass

    # Exit a parse tree produced by RebbValParser#AgeCompare.
    def exitAgeCompare(self, ctx:RebbValParser.AgeCompareContext):
        pass


    # Enter a parse tree produced by RebbValParser#StringPosition.
    def enterStringPosition(self, ctx:RebbValParser.StringPositionContext):
        pass

    # Exit a parse tree produced by RebbValParser#StringPosition.
    def exitStringPosition(self, ctx:RebbValParser.StringPositionContext):
        pass


    # Enter a parse tree produced by RebbValParser#Interval.
    def enterInterval(self, ctx:RebbValParser.IntervalContext):
        pass

    # Exit a parse tree produced by RebbValParser#Interval.
    def exitInterval(self, ctx:RebbValParser.IntervalContext):
        pass


    # Enter a parse tree produced by RebbValParser#Array.
    def enterArray(self, ctx:RebbValParser.ArrayContext):
        pass

    # Exit a parse tree produced by RebbValParser#Array.
    def exitArray(self, ctx:RebbValParser.ArrayContext):
        pass


    # Enter a parse tree produced by RebbValParser#string.
    def enterString(self, ctx:RebbValParser.StringContext):
        pass

    # Exit a parse tree produced by RebbValParser#string.
    def exitString(self, ctx:RebbValParser.StringContext):
        pass


    # Enter a parse tree produced by RebbValParser#number.
    def enterNumber(self, ctx:RebbValParser.NumberContext):
        pass

    # Exit a parse tree produced by RebbValParser#number.
    def exitNumber(self, ctx:RebbValParser.NumberContext):
        pass


    # Enter a parse tree produced by RebbValParser#date.
    def enterDate(self, ctx:RebbValParser.DateContext):
        pass

    # Exit a parse tree produced by RebbValParser#date.
    def exitDate(self, ctx:RebbValParser.DateContext):
        pass


    # Enter a parse tree produced by RebbValParser#time.
    def enterTime(self, ctx:RebbValParser.TimeContext):
        pass

    # Exit a parse tree produced by RebbValParser#time.
    def exitTime(self, ctx:RebbValParser.TimeContext):
        pass


    # Enter a parse tree produced by RebbValParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:RebbValParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by RebbValParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:RebbValParser.ArrayLiteralContext):
        pass



del RebbValParser