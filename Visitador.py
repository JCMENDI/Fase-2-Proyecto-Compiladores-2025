from MiCompiladorVisitor import MiCompiladorVisitor
from MiCompiladorParser import MiCompiladorParser

class EvalVisitor(MiCompiladorVisitor):
    def _init_(self):
        self.memory = {}
        self.functions = {}

    def visitPrograma(self, ctx):
        print("Visit: programa")
        return self.visit(ctx.bloque())

    def visitBloque(self, ctx):
        print("Visit: bloque")
        if ctx.declaraciones():
            self.visit(ctx.declaraciones())
        return self.visit(ctx.compound_statement())

    def visitDeclaraciones(self, ctx):
        print("Visit: declaraciones")
        for decl in ctx.declaracion():
            self.visit(decl)

    def visitDeclaracion(self, ctx):
        print("Visit: declaracion")
        return self.visitChildren(ctx)

    def visitVar_declaracion(self, ctx):
        print("Visit: var_declaracion")
        var_name = ctx.ID().getText()
        tipo = ctx.tipo().getText()
        self.memory[var_name] = None
        print(f"Declared variable: {var_name} of type {tipo}")
        if ctx.var_declaracion():
            self.visit(ctx.var_declaracion())

    def visitFuncion_declaracion(self, ctx):
        print("Visit: funcion_declaracion")
        func_name = ctx.ID().getText()
        self.functions[func_name] = ctx
        print(f"Declared function: {func_name}")

    def visitCompound_statement(self, ctx):
        print("Visit: compound_statement")
        if ctx.lista_sentencias():
            self.visit(ctx.lista_sentencias())

    def visitLista_sentencias(self, ctx):
        print("Visit: lista_sentencias")
        for stmt in ctx.sentencia():
            result = self.visit(stmt)
            if isinstance(result, dict) and result.get("return") is not None:
                return result


    def visitSentencia(self, ctx):
        print("Visit: sentencia")
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx):
        print("Visit: asignacion")
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            print(f"ERROR: Variable {var_name} no declarada")
            return
        value = self.visit(ctx.expresion())
        if isinstance(value, dict) and "return" in value:
            value = value["return"]
        self.memory[var_name] = value
        print(f"Assigned: {var_name} := {value}")
        return value

    def visitSentencia_io(self, ctx):
        print("Visit: sentencia_io")
        if ctx.getChild(0).getText() == 'PRINTLN':
            expr = ctx.getChild(2)
            if expr.getText() in self.memory:
                value = self.memory[expr.getText()]
            elif expr.getText().startswith('"'):
                value = expr.getText().strip('"')
            else:
                value = self.visit(expr)
            print(f"PRINTLN: {value}")
        elif ctx.getChild(0).getText() == 'READLN':
            var_name = ctx.getChild(2).getText()
            val = input(f"READLN {var_name}: ")
            self.memory[var_name] = int(val) if val.isdigit() else val
            print(f"READ value for {var_name}: {self.memory[var_name]}")



    def visitSentencia_if(self, ctx):
        print("Visit: sentencia_if")
        condition = self.visit(ctx.expresion())

        if condition:
            print("Condition is True")
            self.visit(ctx.sentencia(0))
        elif ctx.sentencia(1):
            print("Condition is False, executing ELSE")
            self.visit(ctx.sentencia(1))


    def visitSentencia_while(self, ctx):
        print("Visit: sentencia_while")
        while self.visit(ctx.expresion()):
            print("WHILE condition True, executing loop body")
            result = self.visit(ctx.sentencia())
            if isinstance(result, dict) and result.get("return") is not None:
                return result

    def visitSentencia_return(self, ctx):
        print("Visit: sentencia_return")
        value = self.visit(ctx.expresion())
        if isinstance(value, dict) and "return" in value:
            value = value["return"]
        print(f"RETURN value: {value}")
        return {"return": value}

    def visitLlamada_procedimiento(self, ctx):
        print("Visit: llamada_procedimiento")
        func_name = ctx.ID().getText()
        if func_name not in self.functions:
            print(f"ERROR: Function {func_name} not defined")
            return

        func_ctx = self.functions[func_name]
        old_memory = self.memory.copy()

        param_list = func_ctx.lista_parametros()
        arg_list = ctx.lista_argumentos()

        if param_list and arg_list:
            params = param_list.parametro()
            args = arg_list.expresion()
            for p, a in zip(params, args):
                param_name = p.ID().getText()
                arg_value = self.visit(a)
                self.memory[param_name] = arg_value
                print(f"Function param {param_name} := {arg_value}")

        result = self.visit(func_ctx.bloque())
        self.memory = old_memory

        if isinstance(result, dict) and "return" in result:
            return result["return"]