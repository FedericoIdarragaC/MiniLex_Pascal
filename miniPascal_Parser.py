import ply.yacc as yacc
from MiniPascal import tokens
import MiniPascal
import sys

VERBOSE = 1

def p_program(p):
    'program : PROGRAM ID SEMICOLON block '
    pass

def p_declaration(p):
	'''declaration : var_declaration
            | procedure_declaration
            | function_declaration'''
	pass
#--------------
#Variable's
def p_var_declaration(p):
	'''var_declaration : VAR ID var_declaration2 COLON type'''
	pass
def p_var_declaration2(p):
	'''var_declaration2 : empty	
			| COMMA ID var_declaration2 '''
	pass
#--------------
#Procedure's
def p_procedure_declaration(p):
	'''procedure_declaration : procedure_declaration2 SEMICOLON
			| empty'''
	pass
			
def p_procedure_declaration2(p):
	'''procedure_declaration2 : PROCEDURE ID SEMICOLON block'''
	pass
#--------------
#Function
def p_function_declaration(p):
	'function_declaration : FUNCTION ID LPAREN parameters RPAREN COLON type SEMICOLON block'
	pass
#--------------
#Parametros
def p_parameters(p):
	''' parameters : VAR ID COLON type parameters2 
			| ID COLON type parameters2 
			| empty '''  
	pass

def p_parameters2(p):
	''' parameters2 : COMMA VAR ID COLON type parameters2 
			| COMMA ID COLON type parameters2 
			| empty '''
	pass
#---------------
#Tipos
def p_type(p):
	'''type :  simple_type 
			| array_type'''
	pass

def p_array_type(p):
	'array_type : ARRAY LBRACKET NUMBER RBRACKET OF simple_type'
	pass

def p_simple_type(p):
	''' simple_type : INTEGER'''
	pass
#---------------
#Block's
def p_block(p):
	'''block : BEGIN statement block2 SEMICOLON END DOT 
			| BEGIN statement block2 END DOT'''
	pass

def p_block2(p):
	'''block2 : empty 
				| SEMICOLON statement block2'''
	pass
#---------------
#Vacio
def p_empty(p):
	'empty : '
	pass
#--------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Statements's
def p_statement(p):
	'''statement : simple_statement
			| structured_statement
			| declaration'''
	pass


def p_simple_statement(p):
	'''simple_statement : assignment_statement
			| call
			| return_statement
			| read_statement
			| write_statement
			| assert_statement'''
	pass
def p_assignment_statement(p):
	'assignment_statement : variable ASSIGN expr'
#--------------
#Call
def p_call(p):
	'call : ID LPAREN arguments RPAREN'
	pass

#--------------
#Argument
def p_arguments(p):
	'''arguments : expr arguments2 
			| SIMPLEQUOTE expr SIMPLEQUOTE arguments2
			| empty'''
	pass
def p_arguments2(p):
	'''arguments2 : empty
			| COMMA expr arguments2
			| COMMA SIMPLEQUOTE expr SIMPLEQUOTE arguments2'''
	pass
#--------------
#Return 
def p_return_statement(p):
	'''return_statement : RETURN
			| RETURN expr'''
	pass
#--------------
#Read
def p_read_statement(p):
	'''read_statement : READ LPAREN read_statement2 RPAREN'''
	pass
def p_read_statement2(p):
	'''read_statement2 : variable
			| COMMA variable read_statement2 '''
	pass
#--------------
#Write
def p_write_statement(p):
	'''write_statement : WRITELN LPAREN arguments RPAREN'''
	pass
def p_assert_statement(p):
	'''assert_statement : ASSERT LPAREN boolean_expr RPAREN'''
	pass
def p_boolean_expr(p):
	'''boolean_expr : TRUE 
			| FALSE
			| literal relational_operator literal
'''
	pass



#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Expresiones estructuradas
def p_structured_statement(p):
	'''structured_statement : block 
			| if_statement 
			| while_statement'''
	pass

def p_if_statement(p):
	'''if_statement : IF boolean_expr THEN statement 
					| IF boolean_expr THEN statement ELSE statement'''
	pass

def p_while_statement(p):
	'''while_statement : WHILE boolean_expr DO statement'''
	pass
#--------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def p_expr(p):
	'''expr : simple_expr 
			| simple_expr relational_operator simple_expr'''
	pass

def p_simple_expr(p):
	'''simple_expr : sign term simple_expr2 
			| term simple_expr2'''
	pass

def p_simple_expr2(p):
	''' simple_expr2 : empty 
			| adding_operator term simple_expr2 '''
	pass
def p_term(p):
	'''term : factor
			| factor multiplying_operator factor'''

#factor's
def p_factor(p):
	'''factor : call 
			| variable 
			| literal 
			| LPAREN expr RPAREN
			| NOT factor
			| factor DOT SIZE'''
	pass
#--------------

#variables's
def p_variable(p):
	'''variable : ID 
			| LBRACKET ID NUMBER RBRACKET '''
	pass
#--------------

#relational_operator's
def p_relational_operator(p):
	'''relational_operator : EQUAL 
	| LESS GREATER 
	| LESS
	| LESSEQUAL 
	| GREATER EQUAL 
	| GREATER '''
	pass
#--------------

#sign's
def p_sign(p):
	'''sign : PLUS 
			| MINUS '''
	pass
#--------------

#adding_operator's
def p_adding_operator(p):
	'''adding_operator : PLUS
			| MINUS 
			| OR'''
	pass
#--------------

#multiplying_operator's
def p_multiplying_operator(p):
	'''multiplying_operator : TIMES 
			| DIVIDE
			| PERCENTAGE 
			| AND'''
	pass
#--------------

#Literal
def p_literal(p):
	'''literal : NUMBER 
			| string'''
	pass
#--------------
def p_string(p):
	'''string : empty	
				| ID string'''
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(MiniPascal.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'calculadora.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("COMPILA")
	#input()