import ply.lex as lex

# List of token names for syntax (condition) ? expression1 : expression2;
tokens = [
    'CONDITION',
    'EXPRESSION1',
    'EXPRESSION2',
    'SEMICOLON',
    'QUESTIONMARK',
    'COLON'
]

# Regular expressions for tokens
# condition should contain only one of the following: <, >, <=, >=, ==, !=, (, ), &&, ||, !, true, false, 0, 1
t_CONDITION = r'[a-zA-Z0-9][<|>|<=|>=|==|!=|(|)|&&|!|true|false|0|1|][a-zA-Z0-9]'
t_EXPRESSION1 = r'\*[a-zA-Z0-9_]*'
t_EXPRESSION2 = r'\*[a-zA-Z0-9_]*'
t_SEMICOLON = r';'
t_QUESTIONMARK = r'\?'
t_COLON = r':'

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