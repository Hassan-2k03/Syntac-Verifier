# yacc.py
import ply.yacc as yacc
from lex import tokens

def p_array_declaration(p):
    'array_declaration : DATATYPE IDENTIFIER array_dimensions SEMICOLON'
    print("Valid")
    p[0] = (p[1], p[2], p[3], p[4])

def p_array_dimensions(p):
    '''
    array_dimensions : LBRACKET NUMBER RBRACKET
                     | array_dimensions LBRACKET NUMBER RBRACKET
    '''
    p[0] = (p[1], p[2], p[3]) if len(p) == 4 else (p[1], p[2], p[3], p[4])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

data = input("Enter array declaration: ")
result = parser.parse(data)
print(result)