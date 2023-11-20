#write a yacc program file for lex.py file

import ply.yacc as yacc
from new.lex import tokens

def p_statement(p):