tokens = [
    # Identificadores y palabras reservadas
    'identificador',
    'palabra_reservada',
    'return',
    'condicion_if',        # Condicional if
    'condicion_else',      # Condicional else
    'bucle_while',
    'bucle_do',
    'bucle_for',       # Iteración for
    'scanf',     # Lectura desde teclado
    'printf',    # Escritura en consola

    # Operadores relacionales
    'mayor',             # >
    'mayor_igual_que',   # >=
    'menor',             # <
    'menor_igual_que',   # <=
    'igual_que',         # ==

    # Operadores aritméticos
    'mas',               # +
    'menos',             # -
    'multiplicacion',    # *
    'division',          # /
    'modulo',            # %

    # Operadores lógicos
    'operador_y',        # &&
    'operador_o',        # ||

    # Asignación
    'asignacion',        # =

    # Constantes
    'constante_entera',    # Números enteros
    'constante_flotante',  # Números de punto flotante
    'constante_caracter',  # Caracteres individuales

    # Tipos de datos
    'int',                # Tipo entero
    'double',             # Tipo doble precisión
    'float',              # Tipo flotante
    'char',               # Tipo carácter
    'bool',               # Tipo booleano
    'string',             # Tipo cadena de texto

    # Delimitadores
    'punto',              # .
    'coma',               # ,
    'punto_coma',         # ;
    'parentesis_de_inicio',  # (
    'parentesis_de_cierre',  # )
    'llave_de_inicio',       # {
    'llave_de_cierre',       # }
    'numeral',              # #

    # Comentarios
    'comentario',          # Bloque de comentario
    'linea_comentario',    # Línea de comentario

    'e', #vacia
    # Otros
    'error',              # Token para errores léxicos
]