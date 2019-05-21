# coding: utf-8
r'''
Proyecto 2: Escribir un analizador
==================================
En este proyecto, escribes el shell básico de un analizador para MiniC.
A continuación se incluye la forma BNF del lenguaje. Su tarea es escribir
las reglas de análisis y construir el AST para esta gramática usando SLY.
La siguiente gramática es parcial. Se agregan más características en
proyectos posteriores.


Para hacer el proyecto, siga las instrucciones que siguen a continuación.
'''
# ----------------------------------------------------------------------
# Analizadores son definidos usando SLY.  Se hereda de la clase Parser
#
# vea http://sly.readthedocs.io/en/latest/
# ----------------------------------------------------------------------
import sly

# ----------------------------------------------------------------------
# El siguiente import carga la función error(lineno, msg) que se debe
# usar para informar todos los mensajes de error emitidos por su analizador.
# Las pruebas unitarias y otras características del compilador se basarán
# en esta función. Consulte el archivo errors.py para obtener más
# documentación sobre el mecanismo de manejo de errores.
from errors import error

# ------------------------------------------------- ---------------------
# Importar la clase lexer. Su lista de tokens es necesaria para validar y
# construir el objeto analizador.
from clex import Lexer

# ----------------------------------------------------------------------
# Obtener los nodos AST.
# Lea las instrucciones en ast.py
from cast import *

class Parser(sly.Parser):
	#debugfile = 'parser.txt'

	tokens = Lexer.tokens

	precedence = (
	)

	program : decl_list

	@_("decl_list")
	def program(self, p):
		pass

	decl_list : decl_list decl
			| decl

	@_("decl_list decl")
	def decl_list(self, p):
		pass

	@_("decl")
	def decl_list(self, p):
		pass


	decl : var_decl
			| fun_decl

	@_("var_decl")
	def decl(self, p):
		pass

	@_("fun_decl")
	def decl(self, p):
		pass

	var_decl : type_spec IDENT ;
			| type_spec IDENT [ ] ;

	@_("type_spec IDENT") //////////////¿type_spec es propio de mi lexer?
	def var_decl(self, p):
		pass

	@_("type_spec IDENT SLBRAK SRBRAK")
	def var_decl(self, p):
		pass

	type_spec : VOID
			| BOOL
			| INT
			| FLOAT

	@_("VOID") ///////
	def type_spec(self, p):
		pass

	@_("BOOL") /////
	def type_spec(self, p):
		pass

	@_("INT") /////
	def type_spec(self, p):
		pass

	@_("FLOAT")
	def type_spec(self, p):
		pass

	fun_decl : type_spec IDENT ( params ) compound_stmt

	@_("type_spec IDENT LPAREN params RPAREN compound_stmt")  ////////////////
	def fun_decl(self, p):
		pass

	params : param_list
			| VOID

	@_("param_list")
	def params(self, p):
		pass

	@_("VOID")
	def params(self, p):
		pass


	param_list : param_list , param
			| param

	@_("param_list COMMA param")  ///////////////////
	def param_list(self, p):
		pass

	@_("param")
	def param_list(self, p):
		pass

	param : type_spec IDENT
			| type_spec IDENT [ ]

	@_("type_spec IDENT")
	def param(self, p):
		pass

	@_("type_spec IDENT SLBRAK SRBRAK")  //////////////////
	def param(self, p):
		pass

	compound_stmt : { local_decls stmt_list }

	@_("LBRAK local_decls stmt_list RBRAK") //////////////////
	def compound_stmt(self, p):
		pass

	local_decls : local_decls local_decl
			| empty

	@_("local_decls local_dec")
	def local_decls(self, p):
		pass

	@_("empty")
	def local_decls(self, p):
		pass

	local_decl : type_spec IDENT ;
			| type_spec IDENT [ ] ;

	@_("type_spec IDENT SEMI")
	def local_decl(self, p):
		pass

	@_("type_spec IDENT SLBRAK SRBRAK SEMI")  //////////////////
	def local_decl(self, p):
		pass

	stmt_list : stmt_list stmt
			| empty

	@_("stmt_list stmt")
	def stmt_list(self, p):
		pass

	@_("empty")
	def stmt_list(self, p):
		pass

	stmt : expr_stmt
			| compound_stmt
			| if_stmt
			| while_stmt
			| return_stmt
			| break_stmt

					///////////////7 ¿depende de tokens definidos?
	@_("expr_stmt")
	def stmt(self, p):
		pass

	@_("compound_stmt")
	def stmt(self, p):
		pass

	@_("if_stmt")
	def stmt(self, p):
		pass

	@_("while_stmt")
	def stmt(self, p):
		pass

	@_("return_stmt")
	def stmt(self, p):
		pass

	@_("break_stmt")
	def stmt(self, p):
		pass

	expr_stmt : expr ;
			| ;


	@_("expr SEMI")
	def expr_stmt(self, p):
		pass

	@_("SEMI")
	def expr_stmt(self, p):
		pass

	while_stmt : WHILE ( expr ) stmt

	@_("WHILE LPAREN expr RPAREN stmt") /////////////
	def while_stmt(self, p):
		pass

	if_stmt : IF ( expr ) stmt
			| IF ( expr ) stmt ELSE stmt


	@_("IF LPAREN expr RPAREN stmt") ////////////////////
	def if_stmt(self, p):
		pass

	@_("IF LPAREN expr RPAREN stmt ELSE stmt")  ///////////////
	def if_stmt(self, p):
		pass


	return_stmt : RETURN ;
			| RETURN expr ;

	@_("RETURN SEMI")
	def return_stmt(self, p):
		pass

	@_("RETURN expr SEMI")
	def return_stmt(self, p):
		pass

	break_stamt : BREAK ;

	@_("BREAK SEMI")
	def break_stamt(self, p):
		pass


	expr : IDENT = expr | IDENT[ expr ] = expr
			| expr OR expr
			| expr AND expr
			| expr EQ expr | expr NE expr
			| expr LE expr | expr < expr | expr GE expr | expr > expr
			| expr + expr | expr - expr
			| expr * expr | expr / expr | expr % expr
			| ! expr | - expr | + expr
			| ( expr )
			| IDENT | IDENT[ expr ] | IDENT( args ) | IDENT . size
			| BOOL_LIT | INT_LIT | FLOAT_LIT | NEW type_spec [ expr ]


	@_("IDENT ASSIGN expr")
	def expr(self, p):
		pass

	@_("IDENT SLBRAK expr SRBRAK ASSIGN expr") ////////
	def expr(self, p):
		pass

	@_("expr OR expr")
	def expr(self, p):
		pass

	@_("expr AND expr")
	def expr(self, p):
		pass

	@_("expr EQ expr")
	def expr(self, p):
		pass

	@_("expr NE expr")
	def expr(self, p):
		pass

	@_("expr LE expr")
	def expr(self, p):
		pass

	@_("expr LT expr")
	def expr(self, p):
		pass

	@_("expr GE expr")
	def expr(self, p):
		pass

	@_("expr GT expr")
	def expr(self, p):
		pass

	@_("expr PLUS expr")
	def expr(self, p):
		pass

	@_("expr MINUS expr")
	def expr(self, p):
		pass

	@_("expr TIMES expr")
	def expr(self, p):
		pass

	@_("expr DIVIDE expr")
	def expr(self, p):
		pass

	@_("expr MOD expr")
	def expr(self, p):
		pass

	@_("NEG expr")
	def expr(self, p):
		pass

	@_("MINUS expr")
	def expr(self, p):
		pass

	@_("PLUS expr")
	def expr(self, p):
		pass

	| ( expr )
	| IDENT | IDENT[ expr ] | IDENT( args ) | IDENT . size
	| BOOL_LIT | INT_LIT | FLOAT_LIT | NEW type_spec [ expr ]
	@_("LPAREN expr RPAREN") ///////////////////
	def expr(self, p):
		pass

	@_("IDENT")
	def expr(self, p):
		pass

	@_("IDENT SLBRAK expr SRBRAK ") /////////////////
	def expr(self, p):
		pass

	@_("IDENT LPAREN args RPAREN") //////////////
	def expr(self, p):
		pass

	@_("IDENT POINT SIZE")
	def expr(self, p):
		pass

	@_("BOOL_LIT")
	def expr(self, p):
		pass

	@_("INT_LIT")
	def expr(self, p):
		pass

	@_("FLOAT_LIT")
	def expr(self, p):
		pass

	@_("NEW type_spec SLBRAK expr SRBRAK") /////////////////
	def expr(self, p):
		pass

	arg_list : arg_list , expr
			| expr


	@_("arg_list COMMA expr") //////////???
	def arg_list(self, p):
		pass

	@_("expr")
	def arg_list(self, p):
		pass


	args : arg_list
			| empty

	@_("arg_list")
	def args(self, p):
		pass

	@_("empty")
	def args(self, p):
		pass


	# ----------------------------------------------------------------------
	# NO MODIFIQUE
	#
	# manejo de errores catch-all. Se llama a la siguiente función en
	# cualquier entrada incorrecta. p es el token ofensivo o None si
	# el final de archivo (EOF).
	def error(self, p):
		if p:
			error(p.lineno, "Error de sintaxis en la entrada en el token '%s'" % p.value)
		else:
			error('EOF','Error de sintaxis. No mas entrada.')

# ----------------------------------------------------------------------
#                  NO MODIFIQUE NADA A CONTINUACIÓN
# ----------------------------------------------------------------------

def parse(source):
	'''
	Parser el código fuente en un AST. Devuelve la parte superior del árbol AST.
	'''
	lexer  = Lexer()
	parser = Parser()
	ast = parser.parse(lexer.tokenize(source))
	return ast

def main():
	'''
	Programa principal. Usado para probar.
	'''
	import sys

	if len(sys.argv) != 2:
		sys.stderr.write('Uso: python -m minic.parser filename\n')
		raise SystemExit(1)

	# Parse y crea el AST
	ast = parse(open(sys.argv[1]).read())

	# Genera el árbol de análisis sintáctico resultante
	for depth, node in flatten(ast):
		print('%s: %s%s' % (getattr(node, 'lineno', None), ' '*(4*depth), node))

if __name__ == '__main__':
	main()
