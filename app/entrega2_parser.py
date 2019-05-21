import sly
from errors import error
from entrega1_lexer import Tokenizer
from cast import *

class Parser(sly.Parser):
	debugfile = 'parser.out'
	tokens = Tokenizer.tokens
	precedence = (
		('nonassoc', 'LOWER'),   ###CAMBIO1
		('nonassoc', ELSE),      ###CAMBIO1
			('right', ASSIGN),
			('left', OR),
			('left', AND),
			('left', EQ,NE),
			('left', LE,LT,GE,GT),
			('left', PLUS, MINUS),
			('left', TIMES, DIVIDE, MOD),
			('right', UNARY)
	)

	####PREGUNTAR:
	# En el AST esta definido Program asi:
	# class Program(Statement):
	# 	'''
	# 	program : decl_list
	# 	'''
	# 	decl_list: [Statement]

	@_("decl_list")
	def program(self, p):
		return Program(p.decl_list) ###¿Como sabe que p.decl_list es del tipo Statement?

	@_('NEG expr %prec UNARY','MINUS expr %prec UNARY','PLUS expr %prec UNARY')
	def expr(p):
	 	return UnaryOp(-p.expr)


	@_("decl_list decl")
	def decl_list(self, p):
		p.decl_list.append(p.decl)
		return p.decl_list

	@_("decl")
	def decl_list(self, p):
		return [p.decl] ###PREGUNTAR: ¿Como se en que estructura retornarlo?
						### si solo p.decl o si [p.decl]

	@_("var_decl")
	def decl(self, p):
		return p.var_decl

	@_("fun_decl")
	def decl(self, p):
		return p.fun_decl

	@_("type_spec IDENT SEMI")
	def var_decl(self, p):
		return VarDeclaration(p.IDENT, p.type_spec, None,lineno=p.lineno)###PREGUNTAR: ¿Que es None?

	@_("type_spec IDENT SLBRAK SRBRAK")
	def var_decl(self, p):
		return VarDeclaration(p.IDENT, p.type_spec,None,lineno=p.lineno)

	@_("VOID","BOOL","INT","FLOAT")
	def type_spec(self, p):
		return SimpleType(p[0])

	@_("type_spec IDENT LPAREN params RPAREN compound_stmt")
	def fun_decl(self, p):
		return FuncDeclaration(p.IDENT, [p.params],p.type_spec,[p.compound_stmt])

	@_("param_list")
	def params(self, p):
		return p.param_list

	@_("VOID")
	def params(self, p):
		p.VOID

	@_("param_list COMMA param")
	def param_list(self, p):
		p.param_list.append(p.param)
		return p.param_list

	@_("param")
	def param_list(self, p):
		return [p.param]

	@_("type_spec IDENT")
	def param(self, p):
		return FuncParameter(p.IDENT, p.type_spec)

	@_("type_spec IDENT SLBRAK SRBRAK")
	def param(self, p):
		return FuncParameter(p.IDENT, p.type_spec)

	@_("LBRAK local_decls stmt_list RBRAK")
	def compound_stmt(self, p):
		pass ###PREGUNTAR: ¿En que funcion del AST se llama?

	@_("local_decls local_decl")
	def local_decls(self, p):
		p.local_decls.append(p.local_decl)
		return p.local_decls

	@_("empty")
	def local_decls(self, p):
		return p.empty ###PREGUNTAR: ¿Esto busca def de empty y retorna " "?

	@_("type_spec IDENT SEMI")
	def local_decl(self, p):
		return VarDeclaration(p.IDENT, p.type_spec, None)

	@_("type_spec IDENT SLBRAK SRBRAK SEMI")
	def local_decl(self, p):
		return VarDeclaration(p.IDENT, p.type_spec, None)

	@_("stmt_list stmt")
	def stmt_list(self, p):
		pass

	@_("empty")
	def stmt_list(self, p):
		pass

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

	@_("expr SEMI")
	def expr_stmt(self, p):
		pass

	@_(" SEMI")
	def expr_stmt(self, p):
		pass

	@_("WHILE LPAREN expr RPAREN stmt")
	def while_stmt(self, p):
		return WhileStatement(p.expr, [p.stmt])

	@_("IF LPAREN expr RPAREN stmt")
	def if_stmt(self, p):
		#return IfStatement(p.expr, p.stmt, ?, lineno=p.lineno) ### Solo recibe Statement, ¿Como hacer para que lo reciba bien?
		###PREGUNTAR:
		# Esta funcion retorna basado en la clase de AST:
		# class IfStatement(Statement):
		# Pero ¿Que significa Statement?
		# ¿Donde esta definido?
		# ¿Como se que estructura tiene?
		# ¿Lista, pila, de cuantos elementos?
		# ¿Como se en que orden se le pasan los args?
		pass

	@_("IF LPAREN expr RPAREN stmt ELSE stmt")
	def if_stmt(self, p):
		#return IfStatement(p.expr, [p.stmt0],[p.stmt1],lineno=p.lineno, ?) ###PREGUNTAR: ¿Pq nos dijo que lo miraramos?
		pass

	@_("RETURN SEMI")
	def return_stmt(self, p):
		#return  ###PREGUNTAR: ¿Se devuelve vacio ya que en cast no tiene param None?

	@_("RETURN expr SEMI")
	def return_stmt(self, p):
		return ReturnStatement(p.expr)

	@_("BREAK SEMI") ###PREGUNTAR: ¿Donde esta BreakStatement en cast.py?
	def break_stmt(self, p):
		pass

	@_("IDENT ASSIGN expr")
	def expr(self, p):
		pass

	@_("IDENT SLBRAK expr SRBRAK ASSIGN expr")
	def expr(self, p):
		pass

	@_("expr OR expr","expr AND expr""expr EQ expr","expr NE expr",
	"expr LE expr","expr LT expr","expr GE expr","expr GT expr",
	"expr PLUS expr","expr MINUS expr","expr TIMES expr",
	"expr DIVIDE expr","expr MOD expr")
	def expr(self, p):
		pass

	@_("LPAREN expr RPAREN")
	def expr(self, p):
		pass

	@_("IDENT")
	def expr(self, p):
		pass

	@_("IDENT SLBRAK expr SRBRAK ")
	def expr(self, p):
		pass

	@_("IDENT LPAREN args RPAREN")
	def expr(self, p):
		pass

	@_("IDENT POINT SIZE")
	def expr(self, p):
		pass

	@_("BOOL_LIT")
	def expr(self, p):
		return BoolLiteral(p.BOOL_LIT, lineno=p.lineno) ###### En simbolos no terminales se pone lineno

	@_("INT_LIT")
	def expr(self, p):
		return IntegerLiteral(p.INT_LIT, lineno=p.lineno)

	@_("FLOAT_LIT")
	def expr(self, p):
		return FloatLiteral(p.FLOAT_LIT, lineno=p.lineno)

	@_("NEW type_spec SLBRAK expr SRBRAK")
	def expr(self, p):
		pass

	@_("arg_list COMMA expr")
	def arg_list(self, p):
		p.arg_list.append(p.expr)
		return p.arg_list

	@_("expr")
	def arg_list(self, p):
		return [p.expr]

	@_("arg_list")
	def args(self, p):
		return p.arg_list

	@_("empty")
	def args(self, p):
		return p.empty

	@_(" ")
	def empty(self, p):
		return ###PREGUNTAR: ¿Se deja así?

	def error(self, p):
		if p:
			error(p.lineno, "Error de sintaxis en la entrada en el token '%s'" % p.value)
		else:
			error('EOF','Error de sintaxis. No mas entrada.')

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
