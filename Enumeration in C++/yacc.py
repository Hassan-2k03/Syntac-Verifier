import ply.yacc as yacc
from lex import tokens

def p_enum_declaration(p):
    'enum_declaration : ENUM IDENTIFIER LBRACE enum_list RBRACE SEMICOLON'
    print("Enum Declaration:", p[2])
    for value in p[4]:
        print("  ", value)

def p_enum_list(p):
    'enum_list : enum_list COMMA IDENTIFIER'
    p[0] = p[1] + [p[3]]

def p_enum_list_single(p):
    'enum_list : IDENTIFIER'
    p[0] = [p[1]]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

# Test the parser
data = input("Enter enum declaration: ")
result = parser.parse(data)
