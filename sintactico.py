import ply.yacc as yacc
from lexico import tokens

# Gramática
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    'program : decls'
    print("Programa valido")

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
    if p[2] in ['+', '-', '*', '/']:
        if not isinstance(p[1], int) or not isinstance(p[3], int):
            print(f"Error de sintaxis en operador: {p[2]}")
            return
    pass

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    pass

def p_expr_number(p):
    'expr : NUMBER'
    pass

def p_expr_id(p):
    'expr : ID'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (linea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()
