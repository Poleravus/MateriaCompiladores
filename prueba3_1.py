from lexico3_1 import lexer
from sintactico3_1 import parser

codigo_programa = "int main() { return (4 + 5) * 2; }"


print("Codigo de prueba (programa):")
try:
    parser.parse(codigo_programa)
except:
    pass

