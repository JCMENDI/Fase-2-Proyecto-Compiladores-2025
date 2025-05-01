from antlr4 import *
from MiCompiladorLexer import MiCompiladorLexer
from MiCompiladorParser import MiCompiladorParser
from Visitador import EvalVisitor

def main():
    print("Ingresa tu código (finaliza con una línea vacía):")
    user_input = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_input.append(line)
    
    input_stream = InputStream("\n".join(user_input))

    Lexer = MiCompiladorLexer(input_stream)
    stream = CommonTokenStream(Lexer)
    parser = MiCompiladorParser(stream)

    tree = parser.programa()  # Cambia 'programa' por el nombre de tu regla de inicio
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()