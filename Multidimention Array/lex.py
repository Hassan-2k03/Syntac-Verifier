# lex.py
import ply.lex as lex

tokens = [
    'DATATYPE',
    'IDENTIFIER',
    'LBRACKET',
    'RBRACKET',
    'NUMBER',
    'SEMICOLON',
]

t_DATATYPE = r'int|float|char|double|long|short|void'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_NUMBER = r'\d+'
t_SEMICOLON = r';'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()