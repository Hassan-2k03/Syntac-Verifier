import ply.yacc as yacc
from lex import tokens

# Grammar rules for syntax (condition) ? expression1 : expression2;
def p_statement(p):
    '''
    statement : CONDITION QUESTIONMARK EXPRESSION1 COLON EXPRESSION2 SEMICOLON
    '''
    print("Valid")


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
parser.parse(user_input)