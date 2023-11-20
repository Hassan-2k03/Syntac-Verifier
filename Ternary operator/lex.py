# lexer.py
import ply.lex as lex

tokens = [
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'QUESTION',
    'COLON',
    'LT',  # Less Than
    'GT',  # Greater Than
    'SEMI'
]

literals = ['+', '-', '*', '/', '(', ')', '?', ':', ';']

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.value = t.value
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUESTION = r'\?'
t_COLON = r':'
t_LT = r'<'
t_GT = r'>'
t_SEMI = r';'

# Ignored spaces and tabs
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()