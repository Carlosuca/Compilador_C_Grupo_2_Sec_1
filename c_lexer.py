import ply.lex as lex
from utils.reservadas import reservadas
from utils.tokens import *

# Ignorar espacios y tabs
t_ignore = ' \t'

# Definición de operadores y delimitadores
t_mas = r'\+'
t_menos = r'\-'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_asignacion = r'='
t_menor = r'<'
t_mayor = r'>'
t_menor_igual_que = r'<='
t_mayor_igual_que = r'>='
t_igual_que = r'=='
t_operador_y = r'&&'
t_operador_o = r'\|\|'


# Delimitadores
t_punto = r'\.'
t_coma = r','
t_punto_coma = r';'
t_parentesis_de_inicio = r'\('
t_parentesis_de_cierre = r'\)'
t_llave_de_inicio = r'\{'
t_llave_de_cierre = r'\}'

# Manejo de comentarios
def t_comentario(token):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass  # Ignorar los comentarios

def t_linea_comentario(token):
    r'//.*'
    pass  # Ignorar los comentarios de línea

# Manejo de constantes
def t_constante_flotante(token):
    r'\d+\.\d*([eE][+-]?\d+)?'
    token.value = float(token.value)
    return token

def t_constante_entera(token):
    r'\d+'
    token.value = int(token.value)
    return token

def t_constante_caracter(token):
    r"'([^\\]|\\.)'"
    token.value = token.value[1:-1]  # Remover comillas simples
    return token

# Manejo de cadenas
def t_string(token):
    r'"([^\\"]|\\.)*"'
    return token

# Manejo de identificadores y palabras reservadas
def t_identificador(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'identificador')
    return token

# Manejo de saltos de línea
def t_salto_de_linea(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

# Manejo de errores léxicos
def t_error(token):
    print(f"Carácter ilegal: {token.value[0]} en la línea {token.lexer.lineno}")
    token.lexer.skip(1)

# Construcción del analizador léxico
analizador = lex.lex()

# Función para leer archivos
def leer_fichero(txt):
    with open(txt, 'r', encoding="utf8") as archivo_c:
        contenido = archivo_c.read()
    return contenido

def imprimir_tokens(lista):
    for token in lista:
        print("Linea {:6} Posicion: {:12} Tipo: {:24} Valor: {:40}".format(
                str(token.lineno), str(token.lexpos), str(token.type), str(token.value)))


def identificar_tokens(analizador, txt):
    print("\n")
    analizador.input(str(leer_fichero(txt)))
    print('Dirección del archivo cargado: ' + txt)
    lista_token = []
    tabla_simbolos = {}
    
    while True:
        token = analizador.token()
        if not token:
            break
        lista_token.append(token)
        tabla_simbolos[token.lexpos] = {
            'Linea': token.lineno,
            'Posicion': token.lexpos,
            'Tipo': token.type,
            'Valor': token.value
        }
    return lista_token, tabla_simbolos    
    
    