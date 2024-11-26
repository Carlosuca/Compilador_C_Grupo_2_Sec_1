from no_terminales import no_terminales as NT

tabla_parser = {
    NT._BLOQUE: {
        'llave_de_inicio': [NT.BLOQUE, NT._BLOQUE],
        'llave_de_cierre': [],
        'identificador': [NT.BLOQUE, NT._BLOQUE],
        'bucle_while': [NT.BLOQUE, NT._BLOQUE],
        'bucle_do': [NT.BLOQUE, NT._BLOQUE],
        'bucle_for': [NT.BLOQUE, NT._BLOQUE],
        'condicion_if': [NT.BLOQUE, NT._BLOQUE],
        'eof': []
    },
    NT.BLOQUE: {
        'llave_de_inicio': [NT.INSTRUCCION],
        'identificador': [NT.INSTRUCCION],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA],
        'bucle_do': ['bucle_do', NT.INSTRUCCION_CERRADA, 'bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'identificador', 'punto_coma', 'identificador', 'punto_coma', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA, NT.BLOQUE_ELSE],
    },
    NT.INSTRUCCION_CERRADA: {
        'llave_de_inicio': [NT.INSTRUCCION],
        'identificador': [NT.INSTRUCCION],
        'bucle_while': ['bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA],
        'bucle_do': ['bucle_do', NT.INSTRUCCION_CERRADA, 'bucle_while', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre'],
        'bucle_for': ['bucle_for', 'parentesis_de_inicio', 'identificador', 'punto_coma', 'identificador', 'punto_coma', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', NT.INSTRUCCION_CERRADA, 'condicion_else', NT.INSTRUCCION_CERRADA],
    },
    NT.BLOQUE_ELSE: {
        'llave_de_inicio': [],
        'llave_de_cierre': [],
        'identificador': [],
        'bucle_while': [],
        'bucle_do': [],
        'bucle_for': [],
        'condicion_if': [],
        'condicion_else': ['condicion_else', NT.COLA_ELSE],
        'eof': []
    },
    NT.COLA_ELSE: {
        'llave_de_inicio': [NT.INSTRUCCION],
        'identificador': [NT.INSTRUCCION],
        'condicion_if': ['condicion_if', 'parentesis_de_inicio', 'identificador', 'parentesis_de_cierre', NT.COLA_ELSE],
    },
    NT.INSTRUCCION: {
        'llave_de_inicio': ['llave_de_inicio', NT._BLOQUE, 'llave_de_cierre'],
        'identificador': ['identificador', 'punto_coma'],
    }
}