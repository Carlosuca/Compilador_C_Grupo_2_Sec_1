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
    'void': ['void', 'identificador', 'PARAMETROS', 'FUNCIONG_COLA'] ,
    'int': ['TYPO', 'identificador', 'DECLARACION_GLBL'] ,
    'float': ['TYPO', 'identificador', 'DECLARACION_GLBL'] ,
    'char': ['TYPO', 'identificador', 'DECLARACION_GLBL'] ,
    },

    'DECLARACION_GLBL' :
    {
    'void': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
    'punto_coma': ['ASIGNACION', '_ASIGNACION_CONST', 'punto_coma'] ,
    'parentesis_de_inicio': ['parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCIONG_COLA'] ,
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
    'punto_coma': [] ,
    'parentesis_de_cierre': [] ,
    'llave_de_inicio': [] ,
    'int': ['TYPO', 'identificador', '_PARAMETROS'] ,
    'float': ['TYPO', 'identificador', '_PARAMETROS'] ,
    'char': ['TYPO', 'identificador', '_PARAMETROS'] ,
    },

    '_PARAMETROS' :
    {
    'punto_coma': [] ,
    'parentesis_de_cierre': [] ,
    'llave_de_inicio': [] ,
    'coma': ['coma', 'TYPO', 'identificador', '_PARAMETROS'] ,
    },

    'TYPO' :
    {
    'int': ['int'] ,
    'float': ['float'] ,
    'char': ['char'] ,
    },
}

# PROGRAMA -> _GLOBAL
# _GLOBAL -> GLOBAL _GLOBAL
# _GLOBAL -> ''

# GLOBAL -> TYPO identificador DECLARACION_GLBL
# GLOBAL -> void identificador PARAMETROS FUNCIONG_COLA
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

# PARAMETROS -> TYPO identificador _PARAMETROS
# PARAMETROS -> ''
# _PARAMETROS -> coma TYPO identificador _PARAMETROS
# _PARAMETROS -> ''

# TYPO -> int
# TYPO -> float
# TYPO -> char

# BLOQUE -> b