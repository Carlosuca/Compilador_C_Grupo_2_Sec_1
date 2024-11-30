tabla_global = {
        'PROGRAMA' :
    {
            'void': ['_GLOBAL'] ,
            'int': ['_GLOBAL'] , 
            'float': ['_GLOBAL'] ,
            'char': ['_GLOBAL'] ,
            'eof': ['_GLOBAL'] ,
    },

    '_GLOBAL' :
    {
            'void': ['GLOBAL', '_GLOBAL'] ,
            'int': ['GLOBAL', '_GLOBAL'] ,
            'float': ['GLOBAL', '_GLOBAL'] ,
            'char': ['GLOBAL', '_GLOBAL'] ,
            'eof': [] ,
    },

    'GLOBAL' :
    {
            'void': ['void', '#DcT', 'identificador', '#DcI', 'parentesis_de_inicio', '#DcF', '#BFB','PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA', '#EBl', '#Pop', '#Pop'] ,
            'int': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION_CONST', '#Pop', '#Pop'] ,
            'float': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION_CONST', '#Pop', '#Pop'] ,
            'char': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION_CONST', '#Pop', '#Pop'] ,
    },

    'DECLARACION_CONST' :
    {
            'void': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'parentesis_de_inicio': ['parentesis_de_inicio', '#DcF', '#BFB', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA', '#EBl'] ,
            'punto_coma': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'coma': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'asignacion': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'int': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'float': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'char': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
            'eof': ['ASIGNACION_CONST', '_DECLARACION_CONST_CONT', 'punto_coma'] ,
    },

    'FUNCION_COLA' :
    {
            'punto_coma': ['punto_coma'] ,
            'llave_de_inicio': ['llave_de_inicio', 'BLOQUE', 'llave_de_cierre'] ,
    },

    '_DECLARACION_CONST_CONT' :
    {
            'punto_coma': [] ,
            'coma': ['coma', 'DECLARACION_CONST_CONT', '_DECLARACION_CONST_CONT'] ,
    },

    'DECLARACION_CONST_CONT' :
    {
            'identificador': ['identificador', '#Pop', '#DcI', 'ASIGNACION_CONST'] ,
    },

    'EXPRESION_CONST' :
    {
            'constante_entera': ['constante_entera'] ,
            'constante_character': ['constante_character'] ,
            'constante_flotante': ['constante_flotante'] ,
    },

    'ASIGNACION_CONST' :
    {
            'void': [] ,
            'punto_coma': [] ,
            'coma': [] ,
            'asignacion': ['asignacion', 'EXPRESION'] ,
            'int': [] ,
            'float': [] ,
            'char': [] ,
            'eof': [] ,
    },

    'PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'int': ['TIPO', '#DcT', 'identificador', '#DcI','#RgP', '#Pop', '#Pop', '_PARAMETROS'] ,
            'float': ['TIPO', '#DcT', 'identificador', '#DcI','#RgP', '#Pop', '#Pop', '_PARAMETROS'] ,
            'char': ['TIPO', '#DcT', 'identificador', '#DcI','#RgP', '#Pop', '#Pop', '_PARAMETROS'] ,
    },

    '_PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'coma': ['coma', 'TIPO', '#DcT', 'identificador', '#DcI','#RgP', '#Pop', '#Pop', '_PARAMETROS'] ,
    },

    'TIPO' :
    {
            'int': ['int'] ,
            'float': ['float'] ,
            'char': ['char'] ,
    },
}

# PROGRAMA -> _GLOBAL
# _GLOBAL -> GLOBAL _GLOBAL
# _GLOBAL -> ''

# GLOBAL -> TIPO identificador DECLARACION_CONST
# GLOBAL -> void identificador parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCION_COLA
# DECLARACION_CONST -> ASIGNACION_CONST _DECLARACION_CONST_CONT punto_coma
# DECLARACION_CONST -> parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCION_COLA 
# FUNCION_COLA -> punto_coma
# FUNCION_COLA -> llave_de_inicio BLOQUE llave_de_cierre

# _DECLARACION_CONST_CONT -> coma DECLARACION_CONST_CONT _DECLARACION_CONST_CONT
# _DECLARACION_CONST_CONT -> ''
# DECLARACION_CONST_CONT -> identificador ASIGNACION_CONST
# EXPRESION_CONST -> constante_entera
# EXPRESION_CONST -> constante_character
# EXPRESION_CONST -> constante_flotante

# ASIGNACION_CONST -> asignacion EXPRESION_CONST
# ASIGNACION_CONST -> ''

# PARAMETROS -> TIPO identificador _PARAMETROS
# PARAMETROS -> ''
# _PARAMETROS -> coma TIPO identificador _PARAMETROS
# _PARAMETROS -> ''

# TIPO -> int
# TIPO -> float
# TIPO -> char

# BLOQUE -> b