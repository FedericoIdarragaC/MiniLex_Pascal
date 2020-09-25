import ply.lex as lex
import sys

 


# list of tokens
tokens = (
    # Reserverd words
    #'AUTO',
    'AND',	
    'ARRAY',
    'BEGIN',	
    'CASE',
    'CONST',
    'DIV',
    'DO',
    'DOWNTO',	
    'ELSE',
    'END',
    'FILE',
    'FOR',
    'FUNCTION',	
    'GOTO',
    'IF',
    'IN',
    'LABEL',
    'MOD',
    'NIL',
    'NOT',
    'OF',
    'OR',
    'PACKED',	
    'PROCEDURE',	
    'PROGRAM',
    'RECORD',
    'REPEAT',	
    'SET',
    'THEN',
    'TO',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'WITH',
   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    #'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    #'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LSQBRACKET',
    'RSQBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'TILDE',
    'ASSIGN',

    # Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LSQBRACKET = r'\{'
t_RSQBRACKET = r'\}'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_TILDE = r'`'




#RULES OF TOKENS

def t_AND(t):    
    r'and'
    return t	
def t_ARRAY(t):    
    r'array'
    return t	
def t_BEGIN(t):    
    r'begin'
    return t	
def t_CASE(t):    
    r'case'
    return t	
def t_CONST(t):    
    r'const'
    return t
def t_DIV(t):    
    r'div'
    return t	
def t_DO(t):    
    r'do'
    return t	
def t_DOWNTO(t):    
    r'downto'
    return t	
def t_ELSE(t):    
    r'else'
    return t	
def t_END(t):    
    r'end'
    return t
def t_FILE(t):    
    r'file'
    return t	
def t_FOR(t):    
    r'for'
    return t	
def t_FUNCTION(t):    
    r'function'
    return t	
def t_GOTO(t):    
    r'goto'
    return t	
def t_IF(t):    
    r'if'
    return t
def t_IN(t):    
    r'in'
    return t	
def t_LABEL(t):    
    r'label'
    return t
def t_MOD(t):    
    r'mod'
    return t	
def t_NIL(t):    
    r'nil'
    return t	
def t_NOT(t):    
    r'not'
    return t
def t_OF(t):    
    r'of'
    return t	
def t_OR(t):    
    r'or'
    return t	
def t_PACKED(t):    
    r'packed'
    return t	
def t_PROCEDURE(t):    
    r'procedure'
    return t	
def t_PROGRAM(t):    
    r'program'
    return t

def t_RECORD(t):    
    r'record'
    return t	
def t_REPEAT(t):    
    r'repeat'
    return t	
def t_SET(t):    
    r'set'
    return t	
def t_THEN(t):    
    r'then'
    return t	
def t_TO(t):    
    r'to'
    return t
def t_TYPE(t):    
    r'type'
    return t	
def t_UNTIL(t):    
    r'until'
    return t	
def t_VAR(t):    
    r'var'
    return t	
def t_WHILE(t):    
    r'while'
    return t	
def t_WITH(t):    
    r'with'
    return t

##-----------------------------------------------------------------------------------------------
def t_ASSIGN(t):
    r':='
    return t
    
def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t

#Var Names and Numbers


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t
def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
