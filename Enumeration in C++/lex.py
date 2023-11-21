# lex.py
import ply.lex as lex

tokens = [
    'ENUM',
    'IDENTIFIER',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
]

t_ENUM = r'enum'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()