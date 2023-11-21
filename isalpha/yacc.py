# yacc.py
from ply import yacc
from lex import tokens

def p_statement_isalpha(p):
    'statement : ISALPHA LPAREN CHARACTER RPAREN SEMICOLON'
    print('Valid')

def p_error(p):
    print("Syntax error in input!") 

parser = yacc.yacc()

data = input("Enter the syntax: ")
parser.parse(data)