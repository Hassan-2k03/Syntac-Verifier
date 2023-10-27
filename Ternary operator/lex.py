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
t_CONDITION=r''