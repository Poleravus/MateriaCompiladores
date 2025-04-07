import ply.yacc as yacc
from lexico3_1 import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    'program : function'
    print("Programa valido")

def p_function(p):
    'function : INT ID LPAREN RPAREN block'
    pass

def p_block(p):
    'block : LBRACE decls RBRACE'
    pass

def p_decls(p):
    '''decls : decl decls
             | decl'''
    pass

def p_decl_variable(p):
    'decl : INT ID EQUALS expr SEMICOLON'
    pass

def p_decl_return(p):
    'decl : RETURN expr SEMICOLON'
    pass

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    # Validación simple para operador mal formado
    if not isinstance(p[1], int) or not isinstance(p[3], int):
        print(f"Error de sintaxis en operador: {p[2]}")
        raise SyntaxError()
    p[0] = 0

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_expr_id(p):
    'expr : ID'
    p[0] = 0

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (linea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()