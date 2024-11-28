# from no_terminales import no_terminales as NT
# from utils.gramatica.no_terminales import no_terminales_instruccion as NT

tabla_inst = {

    'INSTRUCCION' :
    {
            'identificador': ['identificador', 'OPERACION', 'punto_coma'] ,
            'void': ['void', 'identificador', 'parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA'] ,
            'int': ['TYPO', 'identificador', 'DECLARACION'] ,
            'float': ['TYPO', 'identificador', 'DECLARACION'] ,
            'char': ['TYPO', 'identificador', 'DECLARACION'] ,
            'return': ['RETORNO', 'punto_coma'] ,
    },

    'DECLARACION' :
    {
            'punto_coma': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'parentesis_de_inicio': ['parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA'] ,
            'coma': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'asignacion': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'eof': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
    },

    'FUNCION_COLA' :
    {
            'punto_coma': ['punto_coma'] ,
            'llave_de_inicio': ['llave_de_inicio', '_BLOQUE', 'llave_de_cierre'] ,
    },

    '_DECLARACION_CONT' :
    {
            'punto_coma': [] ,
            'coma': ['coma', 'DECLARACION_CONT', '_DECLARACION_CONT'] ,
    },

    'DECLARACION_CONT' :
    {
            'identificador': ['identificador', 'ASIGNACION'] ,
    },

    'ASIGNACION' :
    {
            'punto_coma': [] ,
            'coma': [] ,
            'asignacion': ['asignacion', 'EXPRESION'] ,
            'eof': [] ,
    },

    'PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'int': ['TYPO', 'identificador', '_PARAMETROS'] ,
            'float': ['TYPO', 'identificador', '_PARAMETROS'] ,
            'char': ['TYPO', 'identificador', '_PARAMETROS'] ,
    },

    '_PARAMETROS' :
    {
            'parentesis_de_cierre': [] ,
            'coma': ['coma', 'TYPO', 'identificador', '_PARAMETROS'] ,
    },

    'TYPO' :
    {
            'int': ['int'] ,
            'float': ['float'] ,
            'char': ['char'] ,
    },

    'RETORNO' :
    {
            'return': ['return', 'EXPRESION'] ,
    },

    'OPERACION' :
    {
            'punto_coma': ['ASIGNACION'] ,
            'parentesis_de_inicio': ['LLAMAR_FUNCION'] ,
            'asignacion': ['ASIGNACION'] ,
    },

    'LLAMAR_FUNCION' :
    {
            'parentesis_de_inicio': ['parentesis_de_inicio', 'ARGUMENT', 'parentesis_de_cierre'] ,
    },

    'ARGUMENT' :
    {
            'parentesis_de_cierre': [] ,
            '*': ['EXPRESION', '_ARGUMENT'] ,
    },

    '_ARGUMENT' :
    {
            'parentesis_de_cierre': [] ,
            'coma': ['coma', 'EXPRESION', '_ARGUMENT'] ,
    },
}

# S -> INSTRUCCION _INSTRUCCION
# _INSTRUCCION -> INSTRUCCION _INSTRUCCION
# _INSTRUCCION -> ''

# INSTRUCCION -> identificador OPERACION punto_coma
# INSTRUCCION -> RETORNO punto_coma

# INSTRUCCION -> TYPO identificador DECLARACION
# INSTRUCCION -> void identificador parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCION_COLA
# DECLARACION -> ASIGNACION _DECLARACION_CONT punto_coma
# DECLARACION -> parentesis_de_inicio PARAMETROS parentesis_de_cierre FUNCION_COLA 
# FUNCION_COLA -> punto_coma
# FUNCION_COLA -> llave_de_inicio _BLOQUE llave_de_cierre

# _DECLARACION_CONT -> coma DECLARACION_CONT _DECLARACION_CONT
# _DECLARACION_CONT -> ''
# DECLARACION_CONT -> identificador ASIGNACION

# ASIGNACION -> asignacion EXPRESION
# ASIGNACION -> ''

# PARAMETROS -> TYPO identificador _PARAMETROS
# PARAMETROS -> ''
# _PARAMETROS -> coma TYPO identificador _PARAMETROS
# _PARAMETROS -> ''

# TYPO -> int
# TYPO -> float
# TYPO -> char

# RETORNO -> return EXPRESION

# OPERACION -> ASIGNACION
# OPERACION -> LLAMAR_FUNCION
# LLAMAR_FUNCION -> parentesis_de_inicio ARGUMENT parentesis_de_cierre

# ARGUMENT -> EXPRESION _ARGUMENT
# ARGUMENT -> ''

# _ARGUMENT -> coma EXPRESION _ARGUMENT
# _ARGUMENT -> ''

# EXPRESION -> e

#----------------------------------------------------------------------------

# INSTRUCCION -> _INSTRUCCION INSTRUCCION
# INSTRUCCION -> ''


# _INSTRUCCION -> DECLARACION punto_coma
# _INSTRUCCION -> identificador ID punto_coma
# _INSTRUCCION -> RETURN_I punto_coma

# ID -> D_INIT
# ID -> FUNTION_CALL

# TIPO -> int
# TIPO -> float
# TIPO -> char
# TIPO -> void

# RETURN_I -> return EXPRESION

# FUNTION_CALL -> ( ARGUMENT )

# ARGUMENT -> EXPRESION A_ARGUMENT
# ARGUMENT -> ''

# A_ARGUMENT -> , EXPRESION A_ARGUMENT
# A_ARGUMENT -> ''


# DECLARACION -> TIPO identificador D_INIT
# D_INIT -> = EXPRESION
# D_INIT -> ''
