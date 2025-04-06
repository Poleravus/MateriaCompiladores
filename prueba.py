from lexico import lexer
from sintactico import parser

codigo_programa = "int main() { int x = 10; return x; }"
codigo_expr = "3 + * 2"

print("Codigo de prueba (lexico):")
lexer.input("int x = 10;")
for tok in lexer:
    print(tok)

print("\nCodigo de prueba (programa):")
parser.parse(codigo_programa)

print("\nCodigo de prueba (expresion matematica):")
parser.parse(codigo_expr)
