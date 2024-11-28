tabla_bloque = {
    '_BLOQUE': {
        'llave_de_inicio': ['llave_de_inicio', 'BLOQUE', '_BLOQUE'],
        'llave_de_cierre': ['e'],
        'bucle_while': ['BLOQUE', '_BLOQUE'],
        'bucle_do': ['BLOQUE', '_BLOQUE'],
        'bucle_for': ['BLOQUE', '_BLOQUE'],
        'condicion_if': ['BLOQUE', '_BLOQUE'],
        'eof': []
    },
    'BLOQUE': {
        'llave_de_inicio': ['llave_de_inicio', 'INSTRUCCION', 'llave_de_cierre', 'INSTRUCCION'],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA'],
        'bucle_do': ['bucle_do', 'INSTRUCCION_CERRADA', 'bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'EXPRESION', 'punto_coma', 'EXPRESION', 'punto_coma', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA', 'BLOQUE_ELSE'],
    },
    'INSTRUCCION_CERRADA': {
        'llave_de_inicio': ['llave_de_inicio', 'INSTRUCCION'],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA'],
        'bucle_do': ['bucle_do', 'INSTRUCCION_CERRADA', 'bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'EXPRESION', 'punto_coma', 'EXPRESION', 'punto_coma', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_CERRADA', 'condicion_else', 'INSTRUCCION_CERRADA'],
    },
    'BLOQUE_ELSE': {
        'llave_de_inicio': ['llave_de_inicio', ],
        'llave_de_cierre': ['e'],
        'identificador': [],
        'bucle_while': [],
        'bucle_do': [],
        'bucle_for': [],
        'condicion_if': [],
        'condicion_else': ['condicion_else', 'COLA_ELSE'],
        'eof': []
    },
    'COLA_ELSE': {
        'llave_de_inicio': ['llave_de_inicio', 'INSTRUCCION'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'COLA_ELSE'],
    },
}


# programa -> bloque

# bloque -> "{" lista_instrucciones "}"
# lista_instrucciones -> instruccion lista_instrucciones
# lista_instrucciones -> ε

# instruccion -> if_statement
# instruccion -> while_statement
# instruccion -> do_while_statement
# instruccion -> for_statement
# instruccion -> instruccion

# if_statement -> "if" "(" exp_bool ")" bloque
# if_statement ->  "if" "(" exp_bool ")" bloque "else" bloque

# while_statement -> "while" "(" exp_bool ")" bloque

# do_while_statement -> "do" bloque "while" "(" exp_bool ")" ";"

# for_statement -> "for" "(" instruccion ";" exp_bool ";" instruccion ")" bloque
