import ply.yacc as yacc
from lexico3_2 import tokens

precedence = (
    ('left', 'AND', 'OR'),
    ('right', 'NOT')
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

def p_decl_return(p):
    'decl : RETURN expr SEMICOLON'
    pass

def p_expr_binop(p):
    '''expr : expr AND term
            | expr OR term'''
    pass

def p_expr_term(p):
    'expr : term'
    pass

def p_term_not(p):
    'term : NOT factor'
    pass

def p_term_factor(p):
    'term : factor'
    pass

def p_factor_group(p):
    'factor : LPAREN expr RPAREN'
    pass

def p_factor_boolean(p):
    '''factor : BOOLEAN
              | NUMBER'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (linea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()
