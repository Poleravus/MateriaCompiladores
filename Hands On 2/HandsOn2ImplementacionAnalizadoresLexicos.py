import ply.lex as lex

# Definir tokens
tokens = (
    'INT', 'RETURN', 'ID', 'NUMBER', 'STRING', 'COMMENT'
)

# Palabras reservadas
reserved = {
    'int': 'INT',
    'return': 'RETURN'
}

# Operadores y delimitadores
literals = ['+', '-', '*', '/', '=', ';']

# Definir reglas para los tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'  
    t.value = t.value[1:-1]  
    return t

def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'  
    pass  
# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]} en posición {t.lexpos}")
    t.lexer.skip(1)

# Crear analizador léxico
lexer = lex.lex()

# Función para contar tokens y mostrar sus posiciones
def contar_tokens(codigo):
    lexer.input(codigo)
    conteo = {'INT': 0, 'RETURN': 0, 'ID': 0, 'NUMBER': 0, 'STRING': 0, 'OPERADORES': 0, 'DELIMITADORES': 0}

    print("\nTokens generados en entrada:")
    for tok in lexer:
        print(f"Tipo: {tok.type}, Valor: {tok.value}, Posición: {tok.lexpos}")
        if tok.type in conteo:
            conteo[tok.type] += 1
        elif tok.value in literals:
            conteo['OPERADORES'] += 1  

    return conteo

# Función para contar tokens desde un archivo y mostrar posiciones
def contar_tokens_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return
    
    print(f"\nTokens generados en {nombre_archivo}:")
    conteo = contar_tokens(codigo)
    print(f"\nConteo de tokens en {nombre_archivo}: {conteo}")

# Código de prueba desde una cadena
codigo = """
int x = 10;
return x;
"Hola mundo"
"""
print("Conteo de tokens desde cadena:", contar_tokens(codigo))

# Código de prueba desde un archivo
nombre_archivo = "hola.c"  
contar_tokens_desde_archivo(nombre_archivo)
