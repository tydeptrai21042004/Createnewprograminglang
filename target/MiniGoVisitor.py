# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramList.
    def visitParamList(self, ctx:MiniGoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockStmt.
    def visitBlockStmt(self, ctx:MiniGoParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniGoParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniGoParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStmt.
    def visitIfStmt(self, ctx:MiniGoParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStmt.
    def visitForStmt(self, ctx:MiniGoParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#loopStmt.
    def visitLoopStmt(self, ctx:MiniGoParser.LoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniGoParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStmt.
    def visitContinueStmt(self, ctx:MiniGoParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStmt.
    def visitCallStmt(self, ctx:MiniGoParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argList.
    def visitArgList(self, ctx:MiniGoParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structInitExpr.
    def visitStructInitExpr(self, ctx:MiniGoParser.StructInitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structInitList.
    def visitStructInitList(self, ctx:MiniGoParser.StructInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structInitField.
    def visitStructInitField(self, ctx:MiniGoParser.StructInitFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeID.
    def visitTypeID(self, ctx:MiniGoParser.TypeIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDecl.
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)



del MiniGoParser