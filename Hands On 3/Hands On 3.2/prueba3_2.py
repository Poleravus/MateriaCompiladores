from lexico3_2 import lexer
from sintactico3_2 import parser

codigo_valido = "int main() { return (1 AND 0) OR (NOT 1); }"
codigo_invalido = "int main() { return (1 AND (0 OR 1); }"

print("Codigo de prueba (programa válido):")
print(codigo_valido)
try:
    parser.parse(codigo_valido)
except:
    pass

print("\nCodigo de prueba (programa inválido):")
print(codigo_invalido)
try:
    parser.parse(codigo_invalido)
except:
    pass
