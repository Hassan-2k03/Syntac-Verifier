import ply.lex as lex

# condition ? statement 1 : statemet 2;

#list of tokens
tokens=[
    'CONDITION',
    'QUESTION',
    'STATEMENT1',
    'STATEMENT2',
    'COLON',
    'SEMICOLON',
]

#regular expressions for tokens
t_CONDITION = r'[a-zA-Z0-9]+'
t_QUESTION = r'\?'
t_STATEMENT1 = r'(.*)'
t_STATEMENT2 = r'(.*)'
t_COLON = r':'
t_SEMICOLON = r';'

#ignored spaces and tabs
t_ignore = ' \t'

#error handling rule
def t_error(t):
    print(f"Error: Invalid character '{t.value[0]}'")
    t.lexer.skip(1)

#build the lexer
lexer = lex.lex()
