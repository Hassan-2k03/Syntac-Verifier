import ply.lex as lex

# List of token names
tokens = [
    'INT',
    'FLOAT',
    'CHAR',
    'DOUBLE',
    'LONG',
    'SHORT',
    'VOID',
    'UNSIGNED',
    'SIGNED',
    'POINTERNAME',
    'NEW',
    'ASSIGN',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'NUMBER',  # Added for array size
]

# Regular expressions for tokens
t_INT = r'int'
t_FLOAT = r'float'
t_CHAR = r'char'
t_DOUBLE = r'double'
t_LONG = r'long'
t_SHORT = r'short'
t_VOID = r'void'
t_UNSIGNED = r'unsigned'
t_SIGNED = r'signed'
t_POINTERNAME = r'\*[a-zA-Z_][a-zA-Z0-9_]*'
t_NEW = r'new'
t_ASSIGN = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'

# Regular expression for an integer
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Error: Invalid character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()