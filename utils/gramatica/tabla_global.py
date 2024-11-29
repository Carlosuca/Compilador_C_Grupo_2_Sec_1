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
            'void': ['void', 'identificador', 'parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCIONG_COLA'] ,
            'int': ['TIPO', 'identificador', 'DECLARACION_GLBL'] ,
            'float': ['TIPO', 'identificador', 'DECLARACION_GLBL'] ,
            'char': ['TIPO', 'identificador', 'DECLARACION_GLBL'] ,
    },

    'DECLARACION_GLBL' :
    {
            'void': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'parentesis_de_inicio': ['parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCIONG_COLA'] ,
            'punto_coma': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'coma': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'asignacion': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'int': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'float': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'char': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
            'eof': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
    },

    'FUNCIONG_COLA' :
    {
            'punto_coma': ['punto_coma'] ,
            'llave_de_inicio': ['llave_de_inicio', 'BLOQUE', 'llave_de_cierre'] ,
    },

    '_ASIGNACION_CONST' :
    {
            'punto_coma': [] ,
            'coma': ['coma', 'ASIGNACION_CONST', '_ASIGNACION_CONST'] ,
    },

    'ASIGNACION_CONST' :
    {
            'identificador': ['identificador', 'ASIGNACION'] ,
    },

    'EXPRESION_CONST' :
    {
            'constante_entera': ['constante_entera'] ,
            'constante_character': ['constante_character'] ,
            'constante_flotante': ['constante_flotante'] ,
    },

    'ASIGNACION' :
    {
            'void': [] ,
            'punto_coma': [] ,
            'coma': [] ,
            'asignacion': ['asignacion', 'EXPRESION_CONSTANTE'] ,
            'int': [] ,
            'float': [] ,
            'char': [] ,
            'eof': [] ,
    },

    'PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'int': ['TIPO', 'identificador', '_PARAMETROS'] ,
            'float': ['TIPO', 'identificador', '_PARAMETROS'] ,
            'char': ['TIPO', 'identificador', '_PARAMETROS'] ,
    },

    '_PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'coma': ['coma', 'TIPO', 'identificador', '_PARAMETROS'] ,
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

# GLOBAL -> TIPO identificador DECLARACION_GLBL
# GLOBAL -> void identificador parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCIONG_COLA
# DECLARACION_GLBL -> ASIGNACION _ASIGNACION_CONST punto_coma
# DECLARACION_GLBL -> parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCIONG_COLA 
# FUNCIONG_COLA -> punto_coma
# FUNCIONG_COLA -> llave_de_inicio BLOQUE llave_de_cierre

# _ASIGNACION_CONST -> coma ASIGNACION_CONST _ASIGNACION_CONST
# _ASIGNACION_CONST -> ''
# ASIGNACION_CONST -> identificador ASIGNACION
# EXPRESION_CONST -> constante_entera
# EXPRESION_CONST -> constante_character
# EXPRESION_CONST -> constante_flotante

# ASIGNACION -> asignacion EXPRESION_CONSTANTE
# ASIGNACION -> ''

# PARAMETROS -> TIPO identificador _PARAMETROS
# PARAMETROS -> ''
# _PARAMETROS -> coma TIPO identificador _PARAMETROS
# _PARAMETROS -> ''

# TIPO -> int
# TIPO -> float
# TIPO -> char

# BLOQUE -> b