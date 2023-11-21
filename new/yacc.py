import ply.yacc as yacc
from lex import tokens

# Grammar rules
def p_statement(p):
    '''
    statement : datatype POINTERNAME ASSIGN NEW datatype LBRACKET NUMBER RBRACKET SEMICOLON
    '''
    print("Valid")

def p_datatype(p):
    '''
    datatype : INT
             | FLOAT
             | CHAR
             | DOUBLE
             | LONG
             | SHORT
             | VOID
             | UNSIGNED
             | SIGNED
    '''

def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# User input for syntax
user_input = input("Enter the syntax: ")

# Parse the input and check for valid syntax
result = parser.parse(user_input)
