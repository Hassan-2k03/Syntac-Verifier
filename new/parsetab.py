
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHAR DOUBLE FLOAT INT LBRACKET LONG NEW NUMBER POINTERNAME RBRACKET SEMICOLON SHORT SIGNED UNSIGNED VOID\n    statement : datatype POINTERNAME ASSIGN NEW datatype LBRACKET NUMBER RBRACKET SEMICOLON\n              | datatype POINTERNAME ASSIGN NEW datatype LBRACKET NUMBER RBRACKET SEMICOLON error SEMICOLON\n    \n    datatype : INT\n             | FLOAT\n             | CHAR\n             | DOUBLE\n             | LONG\n             | SHORT\n             | VOID\n             | UNSIGNED\n             | SIGNED\n    '
    
_lr_action_items = {'INT':([0,14,],[3,3,]),'FLOAT':([0,14,],[4,4,]),'CHAR':([0,14,],[5,5,]),'DOUBLE':([0,14,],[6,6,]),'LONG':([0,14,],[7,7,]),'SHORT':([0,14,],[8,8,]),'VOID':([0,14,],[9,9,]),'UNSIGNED':([0,14,],[10,10,]),'SIGNED':([0,14,],[11,11,]),'$end':([1,19,21,],[0,-1,-2,]),'POINTERNAME':([2,3,4,5,6,7,8,9,10,11,],[12,-3,-4,-5,-6,-7,-8,-9,-10,-11,]),'LBRACKET':([3,4,5,6,7,8,9,10,11,15,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,16,]),'ASSIGN':([12,],[13,]),'NEW':([13,],[14,]),'NUMBER':([16,],[17,]),'RBRACKET':([17,],[18,]),'SEMICOLON':([18,20,],[19,21,]),'error':([19,],[20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'datatype':([0,14,],[2,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> datatype POINTERNAME ASSIGN NEW datatype LBRACKET NUMBER RBRACKET SEMICOLON','statement',9,'p_statement','yacc.py',7),
  ('statement -> datatype POINTERNAME ASSIGN NEW datatype LBRACKET NUMBER RBRACKET SEMICOLON error SEMICOLON','statement',11,'p_statement','yacc.py',8),
  ('datatype -> INT','datatype',1,'p_datatype','yacc.py',14),
  ('datatype -> FLOAT','datatype',1,'p_datatype','yacc.py',15),
  ('datatype -> CHAR','datatype',1,'p_datatype','yacc.py',16),
  ('datatype -> DOUBLE','datatype',1,'p_datatype','yacc.py',17),
  ('datatype -> LONG','datatype',1,'p_datatype','yacc.py',18),
  ('datatype -> SHORT','datatype',1,'p_datatype','yacc.py',19),
  ('datatype -> VOID','datatype',1,'p_datatype','yacc.py',20),
  ('datatype -> UNSIGNED','datatype',1,'p_datatype','yacc.py',21),
  ('datatype -> SIGNED','datatype',1,'p_datatype','yacc.py',22),
]