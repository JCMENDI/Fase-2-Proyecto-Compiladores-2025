# Generated from MiCompilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiCompiladorParser import MiCompiladorParser
else:
    from MiCompiladorParser import MiCompiladorParser

# This class defines a complete generic visitor for a parse tree produced by MiCompiladorParser.

class MiCompiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiCompiladorParser#programa.
    def visitPrograma(self, ctx:MiCompiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#bloque.
    def visitBloque(self, ctx:MiCompiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#declaraciones.
    def visitDeclaraciones(self, ctx:MiCompiladorParser.DeclaracionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#declaracion.
    def visitDeclaracion(self, ctx:MiCompiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#var_declaracion.
    def visitVar_declaracion(self, ctx:MiCompiladorParser.Var_declaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#funcion_declaracion.
    def visitFuncion_declaracion(self, ctx:MiCompiladorParser.Funcion_declaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#lista_parametros.
    def visitLista_parametros(self, ctx:MiCompiladorParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#parametro.
    def visitParametro(self, ctx:MiCompiladorParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#tipo.
    def visitTipo(self, ctx:MiCompiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#compound_statement.
    def visitCompound_statement(self, ctx:MiCompiladorParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#lista_sentencias.
    def visitLista_sentencias(self, ctx:MiCompiladorParser.Lista_sentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#sentencia.
    def visitSentencia(self, ctx:MiCompiladorParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#asignacion.
    def visitAsignacion(self, ctx:MiCompiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#sentencia_if.
    def visitSentencia_if(self, ctx:MiCompiladorParser.Sentencia_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#sentencia_while.
    def visitSentencia_while(self, ctx:MiCompiladorParser.Sentencia_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#llamada_procedimiento.
    def visitLlamada_procedimiento(self, ctx:MiCompiladorParser.Llamada_procedimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#lista_argumentos.
    def visitLista_argumentos(self, ctx:MiCompiladorParser.Lista_argumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#sentencia_return.
    def visitSentencia_return(self, ctx:MiCompiladorParser.Sentencia_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#sentencia_io.
    def visitSentencia_io(self, ctx:MiCompiladorParser.Sentencia_ioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#expresion.
    def visitExpresion(self, ctx:MiCompiladorParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#expresion_simple.
    def visitExpresion_simple(self, ctx:MiCompiladorParser.Expresion_simpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#termino.
    def visitTermino(self, ctx:MiCompiladorParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#factor.
    def visitFactor(self, ctx:MiCompiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#booleano.
    def visitBooleano(self, ctx:MiCompiladorParser.BooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#operador_relacional.
    def visitOperador_relacional(self, ctx:MiCompiladorParser.Operador_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#operador_aditivo.
    def visitOperador_aditivo(self, ctx:MiCompiladorParser.Operador_aditivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiCompiladorParser#operador_multiplicativo.
    def visitOperador_multiplicativo(self, ctx:MiCompiladorParser.Operador_multiplicativoContext):
        return self.visitChildren(ctx)



del MiCompiladorParser