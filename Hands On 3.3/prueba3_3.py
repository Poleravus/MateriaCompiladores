from lexico3_3 import lexer
from sintactico3_3 import parser

# Casos válidos: expresiones combinadas aritméticas y lógicas correctamente balanceadas
pruebas_validas = [
    # Aritmética simple
    "int main() { return 1 + 2 * 3; }",

    # Lógica con NOT unario
    "int main() { return NOT 0; }",

    # Lógica binaria sin paréntesis
    "int main() { return 1 AND 0 OR 1; }",

    # Aritmética * lógica
    "int main() { return (4 + 5) * (2 AND 1); }",

    # Mezcla lógica y aritmética con paréntesis
    "int main() { return (1 + 2) AND (3 - 1); }",

    # NOT aplicado sobre aritmética
    "int main() { return NOT (1 + 1) AND (0 OR 1); }",

    # Lógica como parte de una aritmética
    "int main() { return ((1 AND 0) + 4) * 3; }"
]

# Casos inválidos: errores sintácticos esperados
pruebas_invalidas = [
    # Operador sin operando
    "int main() { return 1 + ; }",

    # Falta paréntesis de cierre
    "int main() { return (1 AND 0; }",

    # Operadores mal puestos
    "int main() { return 3 + * 2; }",

    # NOT sin operando
    "int main() { return NOT ; }",

    # Mezcla lógica + aritmética mal terminada
    "int main() { return (1 OR 0) + ; }",

    # Falta operando en operación aritmética
    "int main() { return 2 AND (3 - ; }"
]

print("==== PRUEBAS VALIDAS ====\n")
for codigo in pruebas_validas:
    print(f"# {codigo}")
    try:
        parser.parse(codigo)
    except:
        pass
    print()

print("==== PRUEBAS INVALIDAS ====\n")
for codigo in pruebas_invalidas:
    print(f"# {codigo}")
    try:
        parser.parse(codigo)
    except:
        pass
    print()
