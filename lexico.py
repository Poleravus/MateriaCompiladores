import ply.lex as lex

# Tokens
tokens = (
    'INT', 'RETURN', 'ID', 'NUMBER', 
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'EQUALS', 'SEMICOLON'
)

# Palabras reservadas
reserved = {
    'int': 'INT',
    'return': 'RETURN',
}

# Reglas de los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]} en posicion {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()
