import ply.yacc as yacc
from lexico3_3 import tokens

precedence = (
    ('right', 'NOT'),
    ('left', 'AND', 'OR'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS')
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

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    pass

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    pass

def p_factor_group(p):
    'factor : LPAREN expr RPAREN'
    pass

def p_factor_logical(p):
    'factor : logical'
    pass

def p_logical_binop(p):
    '''logical : logical AND logic_term
               | logical OR logic_term'''
    pass

def p_logical_term(p):
    'logical : logic_term'
    pass

def p_logic_term_not(p):
    'logic_term : NOT logic_factor'
    pass

def p_logic_term_factor(p):
    'logic_term : logic_factor'
    pass

def p_logic_factor_group(p):
    'logic_factor : LPAREN logical RPAREN'
    pass

def p_logic_factor_boolean(p):
    '''logic_factor : BOOLEAN
                    | NUMBER'''
    pass

def p_logic_factor_expr(p):
    'logic_factor : expr'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (linea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()
