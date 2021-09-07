# Generated from RebbVal.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RebbValParser import RebbValParser
else:
    from RebbValParser import RebbValParser

# This class defines a complete generic visitor for a parse tree produced by RebbValParser.

class RebbValVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RebbValParser#Disjunction.
    def visitDisjunction(self, ctx:RebbValParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Conjunction.
    def visitConjunction(self, ctx:RebbValParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#SingleTest.
    def visitSingleTest(self, ctx:RebbValParser.SingleTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#NormalUnaryTest.
    def visitNormalUnaryTest(self, ctx:RebbValParser.NormalUnaryTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#NegationUnaryTest.
    def visitNegationUnaryTest(self, ctx:RebbValParser.NegationUnaryTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#IgnoreUnaryTest.
    def visitIgnoreUnaryTest(self, ctx:RebbValParser.IgnoreUnaryTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#positiveUnaryTest.
    def visitPositiveUnaryTest(self, ctx:RebbValParser.PositiveUnaryTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Compare.
    def visitCompare(self, ctx:RebbValParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Between.
    def visitBetween(self, ctx:RebbValParser.BetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#In.
    def visitIn(self, ctx:RebbValParser.InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Contains.
    def visitContains(self, ctx:RebbValParser.ContainsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#NotEmpty.
    def visitNotEmpty(self, ctx:RebbValParser.NotEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#MaxLength.
    def visitMaxLength(self, ctx:RebbValParser.MaxLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Is.
    def visitIs(self, ctx:RebbValParser.IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#IsHex.
    def visitIsHex(self, ctx:RebbValParser.IsHexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#IsCustom.
    def visitIsCustom(self, ctx:RebbValParser.IsCustomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Match.
    def visitMatch(self, ctx:RebbValParser.MatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#AgeCompare.
    def visitAgeCompare(self, ctx:RebbValParser.AgeCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#StringPosition.
    def visitStringPosition(self, ctx:RebbValParser.StringPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Interval.
    def visitInterval(self, ctx:RebbValParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#Array.
    def visitArray(self, ctx:RebbValParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#string.
    def visitString(self, ctx:RebbValParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#number.
    def visitNumber(self, ctx:RebbValParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#date.
    def visitDate(self, ctx:RebbValParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#time.
    def visitTime(self, ctx:RebbValParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RebbValParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:RebbValParser.ArrayLiteralContext):
        return self.visitChildren(ctx)



del RebbValParser