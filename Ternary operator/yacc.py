import ply.yacc as yacc
from lex import tokens

# Define the grammar rules
def p_conditional(p):
    '''conditional : condition COLON question SEMICOLON statement1 SEMICOLON statement2'''
    p[0] = (p[1], p[4], p[6])

def p_condition(p):
    '''condition : CONDITION'''
    p[0] = p[1]

def p_question(p):
    '''question : QUESTION'''
    p[0] = p[1]

def p_statement(p):
    '''statement : STATEMENT1'''
    p[0] = p[1]

def p_statement2(p):
    '''statement2 : STATEMENT2'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()