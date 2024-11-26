tabla_parser = {
    '<_BLOQUE>': {
        'llave_de_inicio': ['<BLOQUE>','<_BLOQUE>'],
        'llave_de_cierre': [],
        'identificador': ['<BLOQUE>','<_BLOQUE>'],
        'bucle_while': ['<BLOQUE>','<_BLOQUE>'],
        'bucle_do': ['<BLOQUE>','<_BLOQUE>'],
        'bucle_for': ['<BLOQUE>','<_BLOQUE>'],
        'condicion_if': ['<BLOQUE>','<_BLOQUE>'],
        'condicion_else': ['<BLOQUE>','<_BLOQUE>'],
        'eof': []
    },
    '<BLOQUE>': {
        'llave_de_inicio': ['<BLOQUE>','<_BLOQUE>'],
        'identificador': ['identificador','punto_coma'],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<BLOQUE>'],
        'bucle_do': ['bucle_do', '<BLOQUE>', 'bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'identificador', 'punto_coma', 'identificador', 'punto_coma', 'identificador', 'parentesis_de_cierre', '<BLOQUE>'],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', '<BLOQUE>'],
        'condicion_else': ['condicion_else', '<BLOQUE>'],
    }
}