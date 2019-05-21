*******************************************************************************
-------------------------GRAMMAR BNF------------------------------------------>
*******************************************************************************

program : decl_list

decl_list : decl_list decl
		| decl

decl : var_decl
		| fun_decl

var_decl : type_spec IDENT ;
		| type_spec IDENT [ ] ;

type_spec : VOID
		| BOOL
		| INT
		| FLOAT

fun_decl : type_spec IDENT ( params ) compound_stmt

params : param_list
		| VOID

param_list : param_list , param
		| param

param : type_spec IDENT
		| type_spec IDENT [ ]

compound_stmt : { local_decls stmt_list }

local_decls : local_decls local_decl
		| empty

local_decl : type_spec IDENT ;
		| type_spec IDENT [ ] ;

stmt_list : stmt_list stmt
		| empty

stmt : expr_stmt
		| compound_stmt
		| if_stmt
		| while_stmt
		| return_stmt
		| break_stmt

expr_stmt : expr ;
		| ;

while_stmt : WHILE ( expr ) stmt

if_stmt : IF ( expr ) stmt
		| IF ( expr ) stmt ELSE stmt

return_stmt : RETURN ;
		| RETURN expr ;

break_stamt : BREAK ;

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

arg_list : arg_list , expr
		| expr

args : arg_list
		| empty

********************************************************************************
*************************************DEBUGGING**********************************
********************************************************************************

Rule 0     S' -> program
Rule 1     program -> decl_list
Rule 2     decl_list -> decl
Rule 3     decl_list -> decl_list decl
Rule 4     decl -> fun_decl
Rule 5     decl -> var_decl
Rule 6     var_decl -> type_spec IDENT SLBRAK SRBRAK
Rule 7     var_decl -> type_spec IDENT
Rule 8     type_spec -> FLOAT
Rule 9     type_spec -> INT
Rule 10    type_spec -> BOOL
Rule 11    type_spec -> VOID
Rule 12    fun_decl -> type_spec IDENT LPAREN params RPAREN compound_stmt
Rule 13    params -> VOID
Rule 14    params -> param_list
Rule 15    param_list -> param
Rule 16    param_list -> param_list COMMA param
Rule 17    param -> type_spec IDENT SLBRAK SRBRAK
Rule 18    param -> type_spec IDENT
Rule 19    compound_stmt -> LBRAK local_decls stmt_list RBRAK
Rule 20    local_decls -> empty
Rule 21    local_decls -> local_decls local_decl
Rule 22    local_decl -> type_spec IDENT SLBRAK SRBRAK SEMI
Rule 23    local_decl -> type_spec IDENT SEMI
Rule 24    stmt_list -> empty
Rule 25    stmt_list -> stmt_list stmt
Rule 26    stmt -> break_stmt
Rule 27    stmt -> return_stmt
Rule 28    stmt -> while_stmt
Rule 29    stmt -> if_stmt
Rule 30    stmt -> compound_stmt
Rule 31    stmt -> expr_stmt
Rule 32    expr_stmt -> SEMI
Rule 33    expr_stmt -> expr SEMI
Rule 34    while_stmt -> WHILE LPAREN expr RPAREN stmt
Rule 35    if_stmt -> IF LPAREN expr RPAREN stmt ELSE stmt
Rule 36    if_stmt -> IF LPAREN expr RPAREN stmt
Rule 37    return_stmt -> RETURN expr SEMI
Rule 38    return_stmt -> RETURN SEMI
Rule 39    break_stmt -> BREAK SEMI
Rule 40    expr -> NEW type_spec SLBRAK expr SRBRAK
Rule 41    expr -> FLOAT_LIT
Rule 42    expr -> INT_LIT
Rule 43    expr -> BOOL_LIT
Rule 44    expr -> IDENT POINT SIZE
Rule 45    expr -> IDENT LPAREN args RPAREN
Rule 46    expr -> IDENT SLBRAK expr SRBRAK
Rule 47    expr -> IDENT
Rule 48    expr -> LPAREN expr RPAREN
Rule 49    expr -> PLUS expr  [precedence=left, level=2]
Rule 50    expr -> MINUS expr  [precedence=left, level=2]
Rule 51    expr -> NEG expr
Rule 52    expr -> expr MOD expr
Rule 53    expr -> expr DIVIDE expr  [precedence=left, level=3]
Rule 54    expr -> expr TIMES expr  [precedence=left, level=3]
Rule 55    expr -> expr MINUS expr  [precedence=left, level=2]
Rule 56    expr -> expr PLUS expr  [precedence=left, level=2]
Rule 57    expr -> expr GT expr  [precedence=nonassoc, level=1]
Rule 58    expr -> expr GE expr
Rule 59    expr -> expr LT expr  [precedence=nonassoc, level=1]
Rule 60    expr -> expr LE expr
Rule 61    expr -> expr NE expr
Rule 62    expr -> expr EQ expr
Rule 63    expr -> expr AND expr
Rule 64    expr -> expr OR expr
Rule 65    expr -> IDENT SLBRAK expr SRBRAK ASSIGN expr
Rule 66    expr -> IDENT ASSIGN expr
Rule 67    arg_list -> expr
Rule 68    arg_list -> arg_list COMMA expr
Rule 69    args -> empty
Rule 70    args -> arg_list
Rule 71    empty -> <empty>
