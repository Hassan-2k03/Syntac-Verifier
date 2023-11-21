import ply.lex as lex

tokens = [
    'ENUM',
    'IDENTIFIER',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
]


def t_ENUM(t):
    r'enum'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
