# lex.py
from ply import lex

tokens = (
    'CHARACTER',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ISALPHA',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_ISALPHA = r'isalpha'
t_CHARACTER = r'\'[a-zA-Z]\''



# Error handling rule
def t_error(t):
    print(f"Error: Invalid character '{t.value[0]}'")
    t.lexer.skip(1)



lexer = lex.lex()
