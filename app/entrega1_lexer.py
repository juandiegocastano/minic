# ----------------------------------------------------------------------
# El siguiente import carga una función error(lineno,msg) que se debe
# utilizar para informar de todos los mensajes de error emitidos por su
# lexer.
from errors import error
# El paquete SLY. https://github.com/dabeaz/sly
from sly import Lexer

class Tokenizer(Lexer):
        # -------
        # Conjunto de palabras reservadas
        keywords = {
                'int', 'if', 'while', 'else', 'return',
                'break', 'new', 'size', 'void', 'bool',
                'float'
        }
        # ----------------------------------------------------------------------
        # Conjunto de tokens
        tokens = {
                # keywords en MAYUSCULAS son tokens. Ej: kw: int, token: INT
                * { kw.upper() for kw in keywords },
                # Identificador
                LE, GE, EQ, NE, OR, AND, INT_LIT, FLOAT_LIT, IDENT, ASSIGN, LT,
                GT, MOD, PLUS, MINUS, TIMES, DIVIDE, COMMA, SEMI, LBRAK, RBRAK,
                LPAREN, RPAREN, NEG, SLBRAK, SRBRAK, POINT, BOOL_LIT
        }
        literals = {
                '+', '-', '*', '/', '%', ',', ';', '{', '}', '(', ')',
                '[', ']', '<=', '>=', '==', '<', '>', '=', '!', '.'
        }

        ignore = ' \t\r'
        #Define un error para los comentarios anidados. BUG: No suma lineno.
        #+Ver README para mas informacion.
        @_(r'(\*/).*\n*(\*/)+.*',r'(/\*).*\n*(/\*)+.*')
        def error_comentario(self, t):
                error(self.lineno, 'ERROR: Comentarios anidados no permitidos')
                self.index += 1

        #Ignora los comentarios legales. BUG: No suma lineno.
        @_(r'/\*[\w\W]*?\*/',r'//.*')
        def ignore_comment(self,t):
                t.lineno += t.value.count('\n')

        #Ignora newline
        @_(r'\n+')
        def ignore_newline(self, t):
                self.lineno += len(t.value)

        #Declaracion para reconocimiento de tokens por expresiones
        #regulares para los literales.
        LE  = r'<='
        GE  = r'>='
        AND = r'\&\&'
        OR = r'\|\|'
        PLUS = r'\+'
        MINUS = r'-'
        TIMES = r'\*'
        DIVIDE = r'/'
        EQ = r'=='
        ASSIGN = r'='
        LT = r'<'
        GT = r'>'
        NE = r'!='
        NEG = r'!'
        MOD = r'%'
        COMMA = r','
        SEMI = r';'
        LBRAK = r'{'
        RBRAK = r'}'
        LPAREN = r'\('
        RPAREN = r'\)'
        SLBRAK = r'\['
        SRBRAK = r'\]'
        POINT = r'\.'
        IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
        #STRING = r'"[^"]*"'
        FLOAT_LIT = r'\d*\.\d*(e[+-]?\d*)?'
        INT_LIT = r'[0-9]+'
        BOOL_LIT = r'True|False'


        #Decorador para IDENT.
        #Añade funcionalidad para reconocer los identificadores que pertenecen
        #a las keywords. Ej: int es de tipo(type) INT. Todas las keywords tienen
        #un token con el mismo String pero en MAYUSCULA.
        @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
        def IDENT(self, t):
            if t.value in self.keywords:
                t.type = t.value.upper()
            if t.value in [True, False]:
                t.type = BOOL_LIT
            return t

        #Decorador para INT_LIT
        #Agrega funcionalidad a los INT_LIT (Enteros como tal. Ej: 14252, 23536, etc.)
        #para que se reconozca que son de tipo int en el compilador y no una cadena.
        #NOTA: No se debe especificar expresion regular ya que esta declarada en la zona
        #de definicion de los literales.
        @_(r'[0-9]+')
        def INT_LIT(self,t):
            t.type = int(t.value)

        #No se hace conversion de FLOAT por los conflictos con las diferentes bases,
        #y ademas no se especificó en las instrucciones. Pero seria algo asi (sin
        #contar con que se debe tener en cuenta cada caso para las diferentes bases)
        def FLOAT_LIT(self,t):
        #    if t.value r''
            t.type = float(t.value)
            return t

        # Manejo de errores de caracteres incorrectos
        def error(self, t):
                error(self.lineno, 'Caracter Ilegal %r' % t.value[0])
                self.index += 1



# ----------------------------------------------------------------------
#---------------------------ESPECIFICACIONES----------------------------
# ----------------------------------------------------------------------
#
#Para correr el Lexer--->
#   Una vez posicionado en la carpeta ~/RUTA_RELATIVA/minic/app
#           python3 -m entrega1_lexer ../test/prueba.c
#   Para correr peuba de comentarios:
#           python3 -m entrega1_lexer ../test/testComentarios
#   Para correr peuba de numeros:
#           python3 -m entrega1_lexer ../test/testNumeros
# ----------------------------------------------------------------------
def main():
        '''
        main. Para propósitos de depuracion
        '''
        import sys

        if len(sys.argv) != 2:
                sys.stderr.write('Uso: python3 -m minic.tokenizer filename\n')
                raise SystemExit(1)

        lexer = Tokenizer()
        text = open(sys.argv[1]).read()
        for tok in lexer.tokenize(text):
                print(tok)

if __name__ == '__main__':
        main()
