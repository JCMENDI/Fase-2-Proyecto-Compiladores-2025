# Generated from MiCompilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiCompiladorParser import MiCompiladorParser
else:
    from MiCompiladorParser import MiCompiladorParser

# This class defines a complete listener for a parse tree produced by MiCompiladorParser.
class MiCompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by MiCompiladorParser#programa.
    def enterPrograma(self, ctx:MiCompiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#programa.
    def exitPrograma(self, ctx:MiCompiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#bloque.
    def enterBloque(self, ctx:MiCompiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#bloque.
    def exitBloque(self, ctx:MiCompiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#declaraciones.
    def enterDeclaraciones(self, ctx:MiCompiladorParser.DeclaracionesContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#declaraciones.
    def exitDeclaraciones(self, ctx:MiCompiladorParser.DeclaracionesContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#declaracion.
    def enterDeclaracion(self, ctx:MiCompiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#declaracion.
    def exitDeclaracion(self, ctx:MiCompiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#var_declaracion.
    def enterVar_declaracion(self, ctx:MiCompiladorParser.Var_declaracionContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#var_declaracion.
    def exitVar_declaracion(self, ctx:MiCompiladorParser.Var_declaracionContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#funcion_declaracion.
    def enterFuncion_declaracion(self, ctx:MiCompiladorParser.Funcion_declaracionContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#funcion_declaracion.
    def exitFuncion_declaracion(self, ctx:MiCompiladorParser.Funcion_declaracionContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#lista_parametros.
    def enterLista_parametros(self, ctx:MiCompiladorParser.Lista_parametrosContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#lista_parametros.
    def exitLista_parametros(self, ctx:MiCompiladorParser.Lista_parametrosContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#parametro.
    def enterParametro(self, ctx:MiCompiladorParser.ParametroContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#parametro.
    def exitParametro(self, ctx:MiCompiladorParser.ParametroContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#tipo.
    def enterTipo(self, ctx:MiCompiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#tipo.
    def exitTipo(self, ctx:MiCompiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#compound_statement.
    def enterCompound_statement(self, ctx:MiCompiladorParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#compound_statement.
    def exitCompound_statement(self, ctx:MiCompiladorParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#lista_sentencias.
    def enterLista_sentencias(self, ctx:MiCompiladorParser.Lista_sentenciasContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#lista_sentencias.
    def exitLista_sentencias(self, ctx:MiCompiladorParser.Lista_sentenciasContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#sentencia.
    def enterSentencia(self, ctx:MiCompiladorParser.SentenciaContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#sentencia.
    def exitSentencia(self, ctx:MiCompiladorParser.SentenciaContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#asignacion.
    def enterAsignacion(self, ctx:MiCompiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#asignacion.
    def exitAsignacion(self, ctx:MiCompiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#sentencia_if.
    def enterSentencia_if(self, ctx:MiCompiladorParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#sentencia_if.
    def exitSentencia_if(self, ctx:MiCompiladorParser.Sentencia_ifContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#sentencia_while.
    def enterSentencia_while(self, ctx:MiCompiladorParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#sentencia_while.
    def exitSentencia_while(self, ctx:MiCompiladorParser.Sentencia_whileContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#llamada_procedimiento.
    def enterLlamada_procedimiento(self, ctx:MiCompiladorParser.Llamada_procedimientoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#llamada_procedimiento.
    def exitLlamada_procedimiento(self, ctx:MiCompiladorParser.Llamada_procedimientoContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#lista_argumentos.
    def enterLista_argumentos(self, ctx:MiCompiladorParser.Lista_argumentosContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#lista_argumentos.
    def exitLista_argumentos(self, ctx:MiCompiladorParser.Lista_argumentosContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#sentencia_return.
    def enterSentencia_return(self, ctx:MiCompiladorParser.Sentencia_returnContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#sentencia_return.
    def exitSentencia_return(self, ctx:MiCompiladorParser.Sentencia_returnContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#sentencia_io.
    def enterSentencia_io(self, ctx:MiCompiladorParser.Sentencia_ioContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#sentencia_io.
    def exitSentencia_io(self, ctx:MiCompiladorParser.Sentencia_ioContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#expresion.
    def enterExpresion(self, ctx:MiCompiladorParser.ExpresionContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#expresion.
    def exitExpresion(self, ctx:MiCompiladorParser.ExpresionContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#expresion_simple.
    def enterExpresion_simple(self, ctx:MiCompiladorParser.Expresion_simpleContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#expresion_simple.
    def exitExpresion_simple(self, ctx:MiCompiladorParser.Expresion_simpleContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#termino.
    def enterTermino(self, ctx:MiCompiladorParser.TerminoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#termino.
    def exitTermino(self, ctx:MiCompiladorParser.TerminoContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#factor.
    def enterFactor(self, ctx:MiCompiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#factor.
    def exitFactor(self, ctx:MiCompiladorParser.FactorContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#booleano.
    def enterBooleano(self, ctx:MiCompiladorParser.BooleanoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#booleano.
    def exitBooleano(self, ctx:MiCompiladorParser.BooleanoContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#operador_relacional.
    def enterOperador_relacional(self, ctx:MiCompiladorParser.Operador_relacionalContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#operador_relacional.
    def exitOperador_relacional(self, ctx:MiCompiladorParser.Operador_relacionalContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#operador_aditivo.
    def enterOperador_aditivo(self, ctx:MiCompiladorParser.Operador_aditivoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#operador_aditivo.
    def exitOperador_aditivo(self, ctx:MiCompiladorParser.Operador_aditivoContext):
        pass


    # Enter a parse tree produced by MiCompiladorParser#operador_multiplicativo.
    def enterOperador_multiplicativo(self, ctx:MiCompiladorParser.Operador_multiplicativoContext):
        pass

    # Exit a parse tree produced by MiCompiladorParser#operador_multiplicativo.
    def exitOperador_multiplicativo(self, ctx:MiCompiladorParser.Operador_multiplicativoContext):
        pass



del MiCompiladorParser