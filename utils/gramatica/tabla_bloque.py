tabla_bloque = {
        'BLOQUE' :
        {
                'condicion_if': ['INSTRUCCION_B', 'BLOQUE'] ,
                'bucle_while': ['INSTRUCCION_B', 'BLOQUE'] ,
                'bucle_do': ['INSTRUCCION_B', 'BLOQUE'] ,
                'bucle_for': ['INSTRUCCION_B', 'BLOQUE'] ,
                '*': ['INSTRUCCION_B', 'BLOQUE'] ,
                'llave_de_inicio': ['INSTRUCCION_B', 'BLOQUE'] ,
                'llave_de_cierre': [] ,
                'eof': [] ,
        },

        'INSTRUCCION_B' :
        {
                'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C', 'BLOQUE_ELSE'] ,
                'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C'] ,
                'bucle_do': ['bucle_do', 'INSTRUCCION_C', 'bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'punto_coma'] ,
                'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'INSTRUCCION',  'EXPRESION', 'punto_coma',  'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C'] ,
                '*': ['INSTRUCCION'] ,
                'llave_de_inicio': ['INSTRUCCION'] ,
        },

        'INSTRUCCION_C' :
        {
                'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C', 'condicion_else', 'INSTRUCCION_C'] ,
                'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C'] ,
                'bucle_do': ['bucle_do', 'INSTRUCCION_C', 'bucle_while', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'punto_coma'] ,
                'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'INSTRUCCION',  'EXPRESION', 'punto_coma',  'EXPRESION', 'parentesis_de_cierre', 'INSTRUCCION_C'] ,
                '*': ['INSTRUCCION'] ,
                'llave_de_inicio': ['INSTRUCCION'] ,
        },

        'BLOQUE_ELSE' :
        {
                'condicion_if': [] ,
                'bucle_while': [] ,
                'bucle_do': [] ,
                'bucle_for': [] ,
                'condicion_else': ['condicion_else', 'COLA_ELSE'] ,
                '*': [] ,
                'llave_de_inicio': [] ,
                'llave_de_cierre': [] ,
                'eof': [] ,
        },

        'COLA_ELSE' :
        {
                'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre', 'COLA_ELSE'] ,
                '*': ['INSTRUCCION'] ,
                'llave_de_inicio': ['INSTRUCCION'] ,
        },

        'INSTRUCCION' :
        {
                'llave_de_inicio': ['llave_de_inicio', 'BLOQUE', 'llave_de_cierre'] ,
        },

        'EXPRESION' :
        {
                'parentesis_de_cierre': [] ,
                'punto_coma': [] ,
        },
}

# BLOQUE -> INSTRUCCION_B BLOQUE
# BLOQUE -> ''
# INSTRUCCION_B -> INSTRUCCION
# INSTRUCCION_B -> condicion_if parentesis_de_inicio EXPRESION parentesis_de_cierre INSTRUCCION_C BLOQUE_ELSE
# INSTRUCCION_B -> bucle_while parentesis_de_inicio EXPRESION parentesis_de_cierre INSTRUCCION_C
# INSTRUCCION_B -> bucle_do INSTRUCCION_C bucle_while parentesis_de_inicio EXPRESION parentesis_de_cierre punto_coma
# INSTRUCCION_B -> bucle_for parentesis_de_inicio INSTRUCCION identificador EXPRESION punto_coma identificador EXPRESION parentesis_de_cierre INSTRUCCION_C
# INSTRUCCION_C -> condicion_if parentesis_de_inicio EXPRESION parentesis_de_cierre INSTRUCCION_C condicion_else INSTRUCCION_C
# INSTRUCCION_C -> bucle_while parentesis_de_inicio EXPRESION parentesis_de_cierre INSTRUCCION_C
# INSTRUCCION_C -> bucle_do INSTRUCCION_C bucle_while parentesis_de_inicio EXPRESION parentesis_de_cierre punto_coma
# INSTRUCCION_C -> bucle_for parentesis_de_inicio INSTRUCCION identificador EXPRESION punto_coma identificador EXPRESION parentesis_de_cierre INSTRUCCION_C
# INSTRUCCION_C -> INSTRUCCION
# BLOQUE_ELSE -> condicion_else COLA_ELSE
# BLOQUE_ELSE -> ''
# COLA_ELSE -> condicion_if parentesis_de_inicio EXPRESION parentesis_de_cierre COLA_ELSE
# COLA_ELSE -> INSTRUCCION
# INSTRUCCION -> i
# INSTRUCCION -> llave_de_inicio BLOQUE llave_de_cierre
# EXPRESION -> o
# EXPRESION -> ''



# programa - bloque

# bloque - "{" lista_instrucciones "}"
# lista_instrucciones - instruccion lista_instrucciones
# lista_instrucciones - ε

# instruccion - if_statement
# instruccion - while_statement
# instruccion - do_while_statement
# instruccion - for_statement
# instruccion - instruccion

# if_statement - "if" "(" exp_bool ")" bloque
# if_statement -  "if" "(" exp_bool ")" bloque "else" bloque

# while_statement - "while" "(" exp_bool ")" bloque

# do_while_statement - "do" bloque "while" "(" exp_bool ")" ";"

# for_statement - "for" "(" instruccion ";" exp_bool ";" instruccion ")" bloque
