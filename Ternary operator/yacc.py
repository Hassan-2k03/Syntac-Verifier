# parser.py
import ply.yacc as yacc
from lex import tokens

def p_expression_ternary(p):
    '''expression : expression QUESTION expression COLON expression SEMI'''
    p[0] = ('ternary', p[1], p[3], p[5])
    print("Valid")

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = ('variable', p[1])

def p_expression_parentheses(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.type}")
    else:
        print("Syntax error: Unexpected end of input")

parser = yacc.yacc()

# Get input from the user
data = input("Enter an expression: ")
parser.parse(data)
