from antlr4 import *


def main():
    print("Ingresa tu código (finaliza con una línea vacía):")
    user_input = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_input.append(line)
    
    input_stream = InputStream("\n".join(user_input))


if __name__ == '__main__':
    main()