
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSANT AND ARRAY ASSERT ASSIGN BEGIN CASE COLON COMMA CONST DEQUAL DISTINT DIV DIVIDE DO DOT DOWNTO ELSE END EQUAL FALSE FILE FOR FUNCTION GOTO GREATER GREATEREQUAL HASHTAG ID IF IN INTEGER ISEQUAL LABEL LBLOCK LBRACKET LESS LESSEQUAL LPAREN LSQBRACKET MINUS MINUSMINUS MOD NIL NOT NUMBER OF OR PACKED PERCENTAGE PLUS PLUSPLUS PROCEDURE PROGRAM QUOTE RBLOCK RBRACKET READ RECORD REPEAT RETURN RPAREN RSQBRACKET SEMICOLON SET SIMPLEQUOTE SIZE SLASH THEN TILDE TIMES TO TRUE TYPE UNTIL VAR WHILE WITH WRITELNprogram : PROGRAM ID SEMICOLON block declaration : var_declaration\n            | procedure_declaration\n            | function_declarationvar_declaration : VAR ID var_declaration2 COLON typevar_declaration2 : empty\t\n\t\t\t| COMMA ID var_declaration2 procedure_declaration : procedure_declaration2 SEMICOLON\n\t\t\t| emptyprocedure_declaration2 : PROCEDURE ID SEMICOLON blockfunction_declaration : FUNCTION ID LPAREN parameters RPAREN COLON type SEMICOLON block parameters : VAR ID COLON type parameters2 \n\t\t\t| ID COLON type parameters2 \n\t\t\t| empty  parameters2 : COMMA VAR ID COLON type parameters2 \n\t\t\t| COMMA ID COLON type parameters2 \n\t\t\t| empty type :  simple_type \n\t\t\t| array_typearray_type : ARRAY LBRACKET NUMBER RBRACKET OF simple_type simple_type : INTEGERblock : BEGIN statement block2 SEMICOLON END DOT \n\t\t\t| BEGIN statement block2 END DOTblock2 : empty \n\t\t\t\t| SEMICOLON statement block2empty : statement : simple_statement\n\t\t\t| structured_statement\n\t\t\t| declarationsimple_statement : assignment_statement\n\t\t\t| call\n\t\t\t| return_statement\n\t\t\t| read_statement\n\t\t\t| write_statement\n\t\t\t| assert_statementassignment_statement : variable ASSIGN exprcall : ID LPAREN arguments RPARENarguments : expr arguments2 \n\t\t\t| SIMPLEQUOTE expr SIMPLEQUOTE arguments2\n\t\t\t| emptyarguments2 : empty\n\t\t\t| COMMA expr arguments2\n\t\t\t| COMMA SIMPLEQUOTE expr SIMPLEQUOTE arguments2return_statement : RETURN\n\t\t\t| RETURN exprread_statement : READ LPAREN read_statement2 RPARENread_statement2 : variable\n\t\t\t| COMMA variable read_statement2 write_statement : WRITELN LPAREN arguments RPARENassert_statement : ASSERT LPAREN boolean_expr RPARENboolean_expr : TRUE \n\t\t\t| FALSE\n\t\t\t| literal relational_operator literal\nstructured_statement : block \n\t\t\t| if_statement \n\t\t\t| while_statementif_statement : IF boolean_expr THEN statement \n\t\t\t\t\t| IF boolean_expr THEN statement ELSE statementwhile_statement : WHILE boolean_expr DO statementexpr : simple_expr \n\t\t\t| simple_expr relational_operator simple_exprsimple_expr : sign term simple_expr2 \n\t\t\t| term simple_expr2 simple_expr2 : empty \n\t\t\t| adding_operator term simple_expr2 term : factor\n\t\t\t| factor multiplying_operator factorfactor : call \n\t\t\t| variable \n\t\t\t| literal \n\t\t\t| LPAREN expr RPAREN\n\t\t\t| NOT factor\n\t\t\t| factor DOT SIZEvariable : ID \n\t\t\t| LBRACKET ID NUMBER RBRACKET relational_operator : EQUAL \n\t| LESS GREATER \n\t| LESS\n\t| LESSEQUAL \n\t| GREATER EQUAL \n\t| GREATER sign : PLUS \n\t\t\t| MINUS adding_operator : PLUS\n\t\t\t| MINUS \n\t\t\t| ORmultiplying_operator : TIMES \n\t\t\t| DIVIDE\n\t\t\t| PERCENTAGE \n\t\t\t| ANDliteral : NUMBER \n\t\t\t| stringstring : empty\t\n\t\t\t\t| ID string'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,117,147,],[0,-1,-23,-22,]),'ID':([2,6,25,29,30,31,34,35,36,38,40,41,44,46,47,52,53,54,58,59,60,65,78,80,81,82,83,84,88,89,90,91,92,94,95,96,97,103,104,107,108,109,112,113,122,125,126,133,143,145,149,153,174,180,],[3,24,54,65,65,67,69,70,71,24,54,54,54,-82,-83,54,54,65,104,54,65,65,54,54,-76,-78,-81,-79,54,-84,-85,-86,54,-87,-88,-89,-90,104,-74,24,65,24,140,141,54,-77,-80,104,162,-75,54,24,181,185,]),'SEMICOLON':([3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,32,33,37,38,39,40,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,65,68,71,74,75,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,99,100,107,109,117,118,119,124,125,126,127,128,129,130,131,132,134,135,136,138,145,146,147,151,153,154,155,156,157,166,176,187,188,],[4,-26,38,-27,-28,-29,-30,-31,-32,-33,-34,-35,-54,-55,-56,-2,-3,-4,-26,68,-9,72,-26,-24,-26,-45,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-91,-92,-93,-26,-8,115,38,-36,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-26,-26,-23,-25,-37,-61,-77,-80,-62,-26,-67,-73,-71,-46,-49,-50,-57,-59,-75,-10,-22,-65,-26,-5,-18,-19,-21,-58,182,-11,-20,]),'BEGIN':([4,6,38,107,109,115,153,182,],[6,6,6,6,6,6,6,6,]),'RETURN':([6,38,107,109,153,],[25,25,25,25,25,]),'READ':([6,38,107,109,153,],[26,26,26,26,26,]),'WRITELN':([6,38,107,109,153,],[27,27,27,27,27,]),'ASSERT':([6,38,107,109,153,],[28,28,28,28,28,]),'IF':([6,38,107,109,153,],[29,29,29,29,29,]),'WHILE':([6,38,107,109,153,],[30,30,30,30,30,]),'VAR':([6,38,107,109,113,153,174,],[31,31,31,31,143,31,180,]),'FUNCTION':([6,38,107,109,153,],[34,34,34,34,34,]),'LBRACKET':([6,25,38,40,41,44,46,47,52,53,58,59,78,80,81,82,83,84,88,89,90,91,92,94,95,96,97,103,104,107,109,122,125,126,133,145,149,153,158,],[35,35,35,35,35,35,-82,-83,35,35,35,35,35,35,-76,-78,-81,-79,35,-84,-85,-86,35,-87,-88,-89,-90,35,-74,35,35,35,-77,-80,35,-75,35,35,167,]),'PROCEDURE':([6,38,107,109,153,],[36,36,36,36,36,]),'END':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,33,37,38,39,40,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,65,68,72,74,75,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,99,100,107,109,117,118,119,124,125,126,127,128,129,130,131,132,134,135,136,138,145,147,151,153,154,155,156,157,166,187,188,],[-26,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-54,-55,-56,-2,-3,-4,-26,-9,73,-26,-24,-26,-45,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-91,-92,-93,-26,-8,116,-26,-36,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-26,-26,-23,-25,-37,-61,-77,-80,-62,-26,-67,-73,-71,-46,-49,-50,-57,-59,-75,-22,-65,-26,-5,-18,-19,-21,-58,-11,-20,]),'ELSE':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,33,40,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,65,68,75,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,99,100,107,109,117,119,124,125,126,127,128,129,130,131,132,134,135,136,138,145,147,151,153,154,155,156,157,166,187,188,],[-27,-28,-29,-30,-31,-32,-33,-34,-35,-54,-55,-56,-2,-3,-4,-26,-9,-26,-45,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-91,-92,-93,-26,-8,-36,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-26,-26,-23,-37,-61,-77,-80,-62,-26,-67,-73,-71,-46,-49,-50,153,-59,-75,-22,-65,-26,-5,-18,-19,-21,-58,-11,-20,]),'ASSIGN':([23,24,145,],[40,-74,-75,]),'LPAREN':([24,25,26,27,28,40,41,44,46,47,52,53,54,59,69,78,80,81,82,83,84,88,89,90,91,92,94,95,96,97,122,125,126,149,],[41,52,58,59,60,52,52,52,-82,-83,52,52,41,52,113,52,52,-76,-78,-81,-79,52,-84,-85,-86,52,-87,-88,-89,-90,52,-77,-80,52,]),'PLUS':([25,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,85,88,89,90,91,92,94,95,96,97,99,100,119,122,125,126,128,129,130,131,145,149,],[46,46,46,-26,89,-82,-83,-66,-68,-69,-70,46,-26,-26,-91,-92,-93,46,-26,46,-93,46,-76,-78,-81,-79,89,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,46,-77,-80,89,-67,-73,-71,-75,46,]),'MINUS':([25,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,85,88,89,90,91,92,94,95,96,97,99,100,119,122,125,126,128,129,130,131,145,149,],[47,47,47,-26,90,-82,-83,-66,-68,-69,-70,47,-26,-26,-91,-92,-93,47,-26,47,-93,47,-76,-78,-81,-79,90,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,47,-77,-80,90,-67,-73,-71,-75,47,]),'NOT':([25,40,41,44,46,47,52,53,59,78,80,81,82,83,84,88,89,90,91,92,94,95,96,97,122,125,126,149,],[53,53,53,53,-82,-83,53,53,53,53,53,-76,-78,-81,-79,53,-84,-85,-86,53,-87,-88,-89,-90,53,-77,-80,53,]),'NUMBER':([25,29,30,40,41,44,46,47,52,53,59,60,70,78,80,81,82,83,84,88,89,90,91,92,94,95,96,97,108,122,125,126,149,167,],[55,55,55,55,55,55,-82,-83,55,55,55,55,114,55,55,-76,-78,-81,-79,55,-84,-85,-86,55,-87,-88,-89,-90,55,55,-77,-80,55,172,]),'DOT':([25,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,59,65,73,78,79,80,81,82,83,84,88,89,90,91,92,94,95,96,97,99,100,116,119,122,125,126,129,130,131,145,149,],[-26,-26,-26,-26,-82,-83,93,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,117,-26,-93,-26,-76,-78,-81,-79,-26,-84,-85,-86,-26,-87,-88,-89,-90,93,-94,147,-37,-26,-77,-80,93,-73,-71,-75,-26,]),'TIMES':([25,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,88,89,90,91,99,100,119,122,125,126,130,131,145,149,],[-26,-26,-26,-26,-82,-83,94,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,-26,-93,-26,-76,-78,-81,-79,-26,-84,-85,-86,-72,-94,-37,-26,-77,-80,-73,-71,-75,-26,]),'DIVIDE':([25,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,88,89,90,91,99,100,119,122,125,126,130,131,145,149,],[-26,-26,-26,-26,-82,-83,95,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,-26,-93,-26,-76,-78,-81,-79,-26,-84,-85,-86,-72,-94,-37,-26,-77,-80,-73,-71,-75,-26,]),'PERCENTAGE':([25,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,88,89,90,91,99,100,119,122,125,126,130,131,145,149,],[-26,-26,-26,-26,-82,-83,96,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,-26,-93,-26,-76,-78,-81,-79,-26,-84,-85,-86,-72,-94,-37,-26,-77,-80,-73,-71,-75,-26,]),'AND':([25,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,88,89,90,91,99,100,119,122,125,126,130,131,145,149,],[-26,-26,-26,-26,-82,-83,97,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,-26,-93,-26,-76,-78,-81,-79,-26,-84,-85,-86,-72,-94,-37,-26,-77,-80,-73,-71,-75,-26,]),'OR':([25,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,65,78,79,80,81,82,83,84,85,88,89,90,91,92,94,95,96,97,99,100,119,122,125,126,128,129,130,131,145,149,],[-26,-26,-26,-26,91,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,-26,-93,-26,-76,-78,-81,-79,91,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,-26,-77,-80,91,-67,-73,-71,-75,-26,]),'EQUAL':([25,29,30,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,78,79,83,85,86,87,88,89,90,91,92,94,95,96,97,99,100,119,122,127,128,129,130,131,145,149,151,],[-26,-26,-26,-26,-26,81,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,81,-26,-26,-93,126,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,-26,-62,-26,-67,-73,-71,-75,-26,-65,]),'LESS':([25,29,30,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,78,79,85,86,87,88,89,90,91,92,94,95,96,97,99,100,119,122,127,128,129,130,131,145,149,151,],[-26,-26,-26,-26,-26,82,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,82,-26,-26,-93,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,-26,-62,-26,-67,-73,-71,-75,-26,-65,]),'LESSEQUAL':([25,29,30,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,78,79,85,86,87,88,89,90,91,92,94,95,96,97,99,100,119,122,127,128,129,130,131,145,149,151,],[-26,-26,-26,-26,-26,84,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,84,-26,-26,-93,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,-26,-62,-26,-67,-73,-71,-75,-26,-65,]),'GREATER':([25,29,30,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,78,79,82,85,86,87,88,89,90,91,92,94,95,96,97,99,100,119,122,127,128,129,130,131,145,149,151,],[-26,-26,-26,-26,-26,83,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-26,83,-26,-26,-93,125,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,-26,-62,-26,-67,-73,-71,-75,-26,-65,]),'TRUE':([29,30,60,],[62,62,62,]),'FALSE':([29,30,60,],[63,63,63,]),'SIMPLEQUOTE':([41,43,44,45,46,47,48,49,50,51,53,54,55,56,57,59,65,78,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,99,100,119,122,123,124,125,126,127,128,129,130,131,145,149,151,164,],[78,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-91,-92,-93,78,-26,-26,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-37,149,150,-61,-77,-80,-62,-26,-67,-73,-71,-75,-26,-65,171,]),'RPAREN':([41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,62,63,65,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,98,99,100,101,102,104,105,106,108,113,119,120,121,122,124,125,126,127,128,129,130,131,137,142,144,145,148,150,151,152,155,156,157,163,165,168,171,173,175,177,178,183,188,190,191,192,193,],[-26,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-26,-91,-92,-93,-26,-51,-52,-26,119,-26,-40,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,131,-72,-94,132,-47,-74,134,135,-26,-26,-37,-38,-41,-26,-61,-77,-80,-62,-26,-67,-73,-71,-53,161,-14,-75,-26,-26,-65,-48,-18,-19,-21,-42,-39,-26,-26,-13,-17,-26,-43,-12,-20,-26,-26,-16,-15,]),'COMMA':([41,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,65,67,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,99,100,104,119,122,124,125,126,127,128,129,130,131,133,140,145,148,150,151,155,156,157,168,171,177,188,190,191,],[-26,-60,-26,-26,-82,-83,-66,-68,-69,-70,-26,-26,-91,-92,-93,103,-26,-26,112,122,-93,-26,-76,-78,-81,-79,-26,-63,-64,-26,-84,-85,-86,-26,-87,-88,-89,-90,-72,-94,-74,-37,-26,-61,-77,-80,-62,-26,-67,-73,-71,103,112,-75,122,122,-65,-18,-19,-21,174,122,174,-20,174,174,]),'THEN':([55,56,57,61,62,63,65,81,82,83,84,100,108,125,126,137,],[-91,-92,-93,107,-51,-52,-26,-76,-78,-81,-79,-94,-26,-77,-80,-53,]),'DO':([55,56,57,62,63,65,66,81,82,83,84,100,108,125,126,137,],[-91,-92,-93,-51,-52,-26,109,-76,-78,-81,-79,-94,-26,-77,-80,-53,]),'COLON':([67,110,111,140,141,159,161,162,181,185,],[-26,139,-6,-26,160,-7,169,170,186,189,]),'SIZE':([93,],[130,]),'RBRACKET':([114,172,],[145,179,]),'INTEGER':([139,160,169,170,184,186,189,],[157,157,157,157,157,157,157,]),'ARRAY':([139,160,169,170,186,189,],[158,158,158,158,158,158,]),'OF':([179,],[184,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([4,6,38,107,109,115,153,182,],[5,17,17,17,17,146,17,187,]),'statement':([6,38,107,109,153,],[7,74,136,138,166,]),'simple_statement':([6,38,107,109,153,],[8,8,8,8,8,]),'structured_statement':([6,38,107,109,153,],[9,9,9,9,9,]),'declaration':([6,38,107,109,153,],[10,10,10,10,10,]),'assignment_statement':([6,38,107,109,153,],[11,11,11,11,11,]),'call':([6,25,38,40,41,44,52,53,59,78,80,88,92,107,109,122,149,153,],[12,49,12,49,49,49,49,49,49,49,49,49,49,12,12,49,49,12,]),'return_statement':([6,38,107,109,153,],[13,13,13,13,13,]),'read_statement':([6,38,107,109,153,],[14,14,14,14,14,]),'write_statement':([6,38,107,109,153,],[15,15,15,15,15,]),'assert_statement':([6,38,107,109,153,],[16,16,16,16,16,]),'if_statement':([6,38,107,109,153,],[18,18,18,18,18,]),'while_statement':([6,38,107,109,153,],[19,19,19,19,19,]),'var_declaration':([6,38,107,109,153,],[20,20,20,20,20,]),'procedure_declaration':([6,38,107,109,153,],[21,21,21,21,21,]),'function_declaration':([6,38,107,109,153,],[22,22,22,22,22,]),'variable':([6,25,38,40,41,44,52,53,58,59,78,80,88,92,103,107,109,122,133,149,153,],[23,50,23,50,50,50,50,50,102,50,50,50,50,50,133,23,23,50,102,50,23,]),'procedure_declaration2':([6,38,107,109,153,],[32,32,32,32,32,]),'empty':([6,7,25,29,30,38,40,41,44,45,52,53,54,59,60,65,67,74,77,78,80,85,88,92,107,108,109,113,122,128,140,148,149,150,153,168,171,177,190,191,],[33,39,57,57,57,33,57,79,57,87,57,57,57,79,57,57,111,39,121,57,57,87,57,57,33,57,33,144,57,87,111,121,57,121,33,175,121,175,175,175,]),'block2':([7,74,],[37,118,]),'expr':([25,40,41,52,59,78,122,149,],[42,75,77,98,77,123,148,164,]),'simple_expr':([25,40,41,52,59,78,80,122,149,],[43,43,43,43,43,43,124,43,43,]),'sign':([25,40,41,52,59,78,80,122,149,],[44,44,44,44,44,44,44,44,44,]),'term':([25,40,41,44,52,59,78,80,88,122,149,],[45,45,45,85,45,45,45,45,128,45,45,]),'factor':([25,40,41,44,52,53,59,78,80,88,92,122,149,],[48,48,48,48,48,99,48,48,48,48,129,48,48,]),'literal':([25,29,30,40,41,44,52,53,59,60,78,80,88,92,108,122,149,],[51,64,64,51,51,51,51,51,51,64,51,51,51,51,137,51,51,]),'string':([25,29,30,40,41,44,52,53,54,59,60,65,78,80,88,92,108,122,149,],[56,56,56,56,56,56,56,56,100,56,56,100,56,56,56,56,56,56,56,]),'boolean_expr':([29,30,60,],[61,66,106,]),'arguments':([41,59,],[76,105,]),'relational_operator':([43,64,],[80,108,]),'simple_expr2':([45,85,128,],[86,127,151,]),'adding_operator':([45,85,128,],[88,88,88,]),'multiplying_operator':([48,],[92,]),'read_statement2':([58,133,],[101,152,]),'var_declaration2':([67,140,],[110,159,]),'arguments2':([77,148,150,171,],[120,163,165,178,]),'parameters':([113,],[142,]),'type':([139,160,169,170,186,189,],[154,168,176,177,190,191,]),'simple_type':([139,160,169,170,184,186,189,],[155,155,155,155,188,155,155,]),'array_type':([139,160,169,170,186,189,],[156,156,156,156,156,156,]),'parameters2':([168,177,190,191,],[173,183,192,193,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON block','program',4,'p_program','miniPascal_Parser.py',9),
  ('declaration -> var_declaration','declaration',1,'p_declaration','miniPascal_Parser.py',13),
  ('declaration -> procedure_declaration','declaration',1,'p_declaration','miniPascal_Parser.py',14),
  ('declaration -> function_declaration','declaration',1,'p_declaration','miniPascal_Parser.py',15),
  ('var_declaration -> VAR ID var_declaration2 COLON type','var_declaration',5,'p_var_declaration','miniPascal_Parser.py',20),
  ('var_declaration2 -> empty','var_declaration2',1,'p_var_declaration2','miniPascal_Parser.py',23),
  ('var_declaration2 -> COMMA ID var_declaration2','var_declaration2',3,'p_var_declaration2','miniPascal_Parser.py',24),
  ('procedure_declaration -> procedure_declaration2 SEMICOLON','procedure_declaration',2,'p_procedure_declaration','miniPascal_Parser.py',29),
  ('procedure_declaration -> empty','procedure_declaration',1,'p_procedure_declaration','miniPascal_Parser.py',30),
  ('procedure_declaration2 -> PROCEDURE ID SEMICOLON block','procedure_declaration2',4,'p_procedure_declaration2','miniPascal_Parser.py',34),
  ('function_declaration -> FUNCTION ID LPAREN parameters RPAREN COLON type SEMICOLON block','function_declaration',9,'p_function_declaration','miniPascal_Parser.py',39),
  ('parameters -> VAR ID COLON type parameters2','parameters',5,'p_parameters','miniPascal_Parser.py',44),
  ('parameters -> ID COLON type parameters2','parameters',4,'p_parameters','miniPascal_Parser.py',45),
  ('parameters -> empty','parameters',1,'p_parameters','miniPascal_Parser.py',46),
  ('parameters2 -> COMMA VAR ID COLON type parameters2','parameters2',6,'p_parameters2','miniPascal_Parser.py',50),
  ('parameters2 -> COMMA ID COLON type parameters2','parameters2',5,'p_parameters2','miniPascal_Parser.py',51),
  ('parameters2 -> empty','parameters2',1,'p_parameters2','miniPascal_Parser.py',52),
  ('type -> simple_type','type',1,'p_type','miniPascal_Parser.py',57),
  ('type -> array_type','type',1,'p_type','miniPascal_Parser.py',58),
  ('array_type -> ARRAY LBRACKET NUMBER RBRACKET OF simple_type','array_type',6,'p_array_type','miniPascal_Parser.py',62),
  ('simple_type -> INTEGER','simple_type',1,'p_simple_type','miniPascal_Parser.py',66),
  ('block -> BEGIN statement block2 SEMICOLON END DOT','block',6,'p_block','miniPascal_Parser.py',71),
  ('block -> BEGIN statement block2 END DOT','block',5,'p_block','miniPascal_Parser.py',72),
  ('block2 -> empty','block2',1,'p_block2','miniPascal_Parser.py',76),
  ('block2 -> SEMICOLON statement block2','block2',3,'p_block2','miniPascal_Parser.py',77),
  ('empty -> <empty>','empty',0,'p_empty','miniPascal_Parser.py',82),
  ('statement -> simple_statement','statement',1,'p_statement','miniPascal_Parser.py',90),
  ('statement -> structured_statement','statement',1,'p_statement','miniPascal_Parser.py',91),
  ('statement -> declaration','statement',1,'p_statement','miniPascal_Parser.py',92),
  ('simple_statement -> assignment_statement','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',97),
  ('simple_statement -> call','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',98),
  ('simple_statement -> return_statement','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',99),
  ('simple_statement -> read_statement','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',100),
  ('simple_statement -> write_statement','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',101),
  ('simple_statement -> assert_statement','simple_statement',1,'p_simple_statement','miniPascal_Parser.py',102),
  ('assignment_statement -> variable ASSIGN expr','assignment_statement',3,'p_assignment_statement','miniPascal_Parser.py',105),
  ('call -> ID LPAREN arguments RPAREN','call',4,'p_call','miniPascal_Parser.py',109),
  ('arguments -> expr arguments2','arguments',2,'p_arguments','miniPascal_Parser.py',115),
  ('arguments -> SIMPLEQUOTE expr SIMPLEQUOTE arguments2','arguments',4,'p_arguments','miniPascal_Parser.py',116),
  ('arguments -> empty','arguments',1,'p_arguments','miniPascal_Parser.py',117),
  ('arguments2 -> empty','arguments2',1,'p_arguments2','miniPascal_Parser.py',120),
  ('arguments2 -> COMMA expr arguments2','arguments2',3,'p_arguments2','miniPascal_Parser.py',121),
  ('arguments2 -> COMMA SIMPLEQUOTE expr SIMPLEQUOTE arguments2','arguments2',5,'p_arguments2','miniPascal_Parser.py',122),
  ('return_statement -> RETURN','return_statement',1,'p_return_statement','miniPascal_Parser.py',127),
  ('return_statement -> RETURN expr','return_statement',2,'p_return_statement','miniPascal_Parser.py',128),
  ('read_statement -> READ LPAREN read_statement2 RPAREN','read_statement',4,'p_read_statement','miniPascal_Parser.py',133),
  ('read_statement2 -> variable','read_statement2',1,'p_read_statement2','miniPascal_Parser.py',136),
  ('read_statement2 -> COMMA variable read_statement2','read_statement2',3,'p_read_statement2','miniPascal_Parser.py',137),
  ('write_statement -> WRITELN LPAREN arguments RPAREN','write_statement',4,'p_write_statement','miniPascal_Parser.py',142),
  ('assert_statement -> ASSERT LPAREN boolean_expr RPAREN','assert_statement',4,'p_assert_statement','miniPascal_Parser.py',145),
  ('boolean_expr -> TRUE','boolean_expr',1,'p_boolean_expr','miniPascal_Parser.py',148),
  ('boolean_expr -> FALSE','boolean_expr',1,'p_boolean_expr','miniPascal_Parser.py',149),
  ('boolean_expr -> literal relational_operator literal','boolean_expr',3,'p_boolean_expr','miniPascal_Parser.py',150),
  ('structured_statement -> block','structured_statement',1,'p_structured_statement','miniPascal_Parser.py',159),
  ('structured_statement -> if_statement','structured_statement',1,'p_structured_statement','miniPascal_Parser.py',160),
  ('structured_statement -> while_statement','structured_statement',1,'p_structured_statement','miniPascal_Parser.py',161),
  ('if_statement -> IF boolean_expr THEN statement','if_statement',4,'p_if_statement','miniPascal_Parser.py',165),
  ('if_statement -> IF boolean_expr THEN statement ELSE statement','if_statement',6,'p_if_statement','miniPascal_Parser.py',166),
  ('while_statement -> WHILE boolean_expr DO statement','while_statement',4,'p_while_statement','miniPascal_Parser.py',170),
  ('expr -> simple_expr','expr',1,'p_expr','miniPascal_Parser.py',176),
  ('expr -> simple_expr relational_operator simple_expr','expr',3,'p_expr','miniPascal_Parser.py',177),
  ('simple_expr -> sign term simple_expr2','simple_expr',3,'p_simple_expr','miniPascal_Parser.py',181),
  ('simple_expr -> term simple_expr2','simple_expr',2,'p_simple_expr','miniPascal_Parser.py',182),
  ('simple_expr2 -> empty','simple_expr2',1,'p_simple_expr2','miniPascal_Parser.py',186),
  ('simple_expr2 -> adding_operator term simple_expr2','simple_expr2',3,'p_simple_expr2','miniPascal_Parser.py',187),
  ('term -> factor','term',1,'p_term','miniPascal_Parser.py',190),
  ('term -> factor multiplying_operator factor','term',3,'p_term','miniPascal_Parser.py',191),
  ('factor -> call','factor',1,'p_factor','miniPascal_Parser.py',195),
  ('factor -> variable','factor',1,'p_factor','miniPascal_Parser.py',196),
  ('factor -> literal','factor',1,'p_factor','miniPascal_Parser.py',197),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','miniPascal_Parser.py',198),
  ('factor -> NOT factor','factor',2,'p_factor','miniPascal_Parser.py',199),
  ('factor -> factor DOT SIZE','factor',3,'p_factor','miniPascal_Parser.py',200),
  ('variable -> ID','variable',1,'p_variable','miniPascal_Parser.py',206),
  ('variable -> LBRACKET ID NUMBER RBRACKET','variable',4,'p_variable','miniPascal_Parser.py',207),
  ('relational_operator -> EQUAL','relational_operator',1,'p_relational_operator','miniPascal_Parser.py',213),
  ('relational_operator -> LESS GREATER','relational_operator',2,'p_relational_operator','miniPascal_Parser.py',214),
  ('relational_operator -> LESS','relational_operator',1,'p_relational_operator','miniPascal_Parser.py',215),
  ('relational_operator -> LESSEQUAL','relational_operator',1,'p_relational_operator','miniPascal_Parser.py',216),
  ('relational_operator -> GREATER EQUAL','relational_operator',2,'p_relational_operator','miniPascal_Parser.py',217),
  ('relational_operator -> GREATER','relational_operator',1,'p_relational_operator','miniPascal_Parser.py',218),
  ('sign -> PLUS','sign',1,'p_sign','miniPascal_Parser.py',224),
  ('sign -> MINUS','sign',1,'p_sign','miniPascal_Parser.py',225),
  ('adding_operator -> PLUS','adding_operator',1,'p_adding_operator','miniPascal_Parser.py',231),
  ('adding_operator -> MINUS','adding_operator',1,'p_adding_operator','miniPascal_Parser.py',232),
  ('adding_operator -> OR','adding_operator',1,'p_adding_operator','miniPascal_Parser.py',233),
  ('multiplying_operator -> TIMES','multiplying_operator',1,'p_multiplying_operator','miniPascal_Parser.py',239),
  ('multiplying_operator -> DIVIDE','multiplying_operator',1,'p_multiplying_operator','miniPascal_Parser.py',240),
  ('multiplying_operator -> PERCENTAGE','multiplying_operator',1,'p_multiplying_operator','miniPascal_Parser.py',241),
  ('multiplying_operator -> AND','multiplying_operator',1,'p_multiplying_operator','miniPascal_Parser.py',242),
  ('literal -> NUMBER','literal',1,'p_literal','miniPascal_Parser.py',248),
  ('literal -> string','literal',1,'p_literal','miniPascal_Parser.py',249),
  ('string -> empty','string',1,'p_string','miniPascal_Parser.py',253),
  ('string -> ID string','string',2,'p_string','miniPascal_Parser.py',254),
]
