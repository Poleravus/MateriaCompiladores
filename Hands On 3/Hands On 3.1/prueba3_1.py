from lexico3_1 import lexer
from sintactico3_1 import parser

codigo_programa_valido = "int main() { return (4 + 5) * 2; }"
codigo_programa_invalido = "int main() { return (4 + 5) * ; }"

print("Codigo de prueba (programa válido):")
print(codigo_programa_valido)
try:
    parser.parse(codigo_programa_valido)
except:
    pass

print("\nCodigo de prueba (programa inválido):")
print(codigo_programa_invalido)
try:
    parser.parse(codigo_programa_invalido)
except:
    pass

