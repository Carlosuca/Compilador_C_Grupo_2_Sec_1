tabla_parser = {
    '<_BLOQUE>': {
        'llave_de_inicio': ['<BLOQUE>', '<_BLOQUE>'],
        'llave_de_cierre': [],
        'identificador': ['<BLOQUE>', '<_BLOQUE>'],
        'bucle_while': ['<BLOQUE>', '<_BLOQUE>'],
        'bucle_do': ['<BLOQUE>', '<_BLOQUE>'],
        'bucle_for': ['<BLOQUE>', '<_BLOQUE>'],
        'condicion_if': ['<BLOQUE>', '<_BLOQUE>'],
        'eof': []
    },
    '<BLOQUE>': {
        'llave_de_inicio': ['<INSTRUCCION>'],
        'identificador': ['<INSTRUCCION>'],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>'],
        'bucle_do': ['bucle_do', '<INSTRUCCION_CERRADA>', 'bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'identificador', 'punto_coma', 'identificador', 'punto_coma', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>', '<BLOQUE_ELSE>'],
    },
    '<INSTRUCCION_CERRADA>': {
        'llave_de_inicio': ['<INSTRUCCION>'],
        'identificador': ['<INSTRUCCION>'],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>'],
        'bucle_do': ['bucle_do', '<INSTRUCCION_CERRADA>', 'bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'identificador', 'punto_coma', 'identificador', 'punto_coma', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<INSTRUCCION_CERRADA>', 'condicion_else', '<INSTRUCCION_CERRADA>'],
    },
    '<BLOQUE_ELSE>': {
        'llave_de_inicio': [],
        'llave_de_cierre': [],
        'identificador': [],
        'bucle_while': [],
        'bucle_do': [],
        'bucle_for': [],
        'condicion_if': [],
        'condicion_else': ['condicion_else', '<COLA_ELSE>'],
        'eof': []
    },
    '<COLA_ELSE>': {
        'llave_de_inicio': ['<INSTRUCCION>'],
        'identificador': ['<INSTRUCCION>'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<COLA_ELSE>'],
    },
    '<INSTRUCCION>': {
        'llave_de_inicio': ['llave_de_inicio', '<_BLOQUE>', 'llave_de_cierre'],
        'identificador': ['identificador', 'punto_coma'],
    }
}