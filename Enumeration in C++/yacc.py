# yacc.py
import ply.yacc as yacc
from lex import tokens

def p_enum_declaration(p):
    'enum_declaration : ENUM IDENTIFIER LBRACE identifiers RBRACE SEMICOLON'
    print('Valid')
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])

def p_identifiers(p):
    '''
    identifiers : IDENTIFIER
                | identifiers COMMA IDENTIFIER
    '''
    p[0] = (p[1],) if len(p) == 2 else p[1] + (p[3],)

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

data = input("Enter a enum declaration: ")
parser.parse(data)
