
import ply.lex as lex

tokens = [
    'DATATYPE',
    'POINTERNAME',
    'SIZE',
    'SEMICOLON',
    'EQUALS',
    'NEW',
    'OPENBRACKET',
    'CLOSEBRACKET',
    'NUMBER',
]

t_DATATYPE = r'int|char|float|double'
t_POINTERNAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SEMICOLON = r';'
t_EQUALS = r'='
t_NEW = r'new'
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_SIZE(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()