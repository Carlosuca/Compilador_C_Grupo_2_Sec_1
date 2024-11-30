# from no_terminales import no_terminales as NT
# from utils.gramatica.no_terminales import no_terminales_instruccion as NT

tabla_inst = {

    'INSTRUCCION' :
    {
            'identificador': ['identificador', '#Ref', '#Psh', 'OPERACION', '#Pop', 'punto_coma'] ,
            'void': ['void', '#DcT', 'identificador', '#DcI', '#BFB', 'parentesis_de_inicio', 'PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA', '#EBl', '#Pop', '#Pop'] ,
            'int': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION', '#Pop', '#Pop'] ,
            'float': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION', '#Pop', '#Pop'] ,
            'char': ['TIPO', '#DcT', 'identificador', '#DcI', 'DECLARACION', '#Pop', '#Pop'] ,
            'return': ['RETORNO', 'punto_coma'] ,
    },

    'DECLARACION' :
    {
            'punto_coma': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'parentesis_de_inicio': [ 'parentesis_de_inicio', '#DcF', '#BFB','PARAMETROS', 'parentesis_de_cierre', 'FUNCION_COLA', '#EBl'] ,
            'coma': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'asignacion': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
            'eof': ['ASIGNACION', '_DECLARACION_CONT', 'punto_coma'] ,
    },

    'FUNCION_COLA' :
    {
            'punto_coma': ['punto_coma'] ,
            'llave_de_inicio': ['llave_de_inicio', 'BLOQUE', 'llave_de_cierre'] ,
    },

    '_DECLARACION_CONT' :
    {
            'punto_coma': [] ,
            'coma': ['coma', 'DECLARACION_CONT', '_DECLARACION_CONT'] ,
    },

    'DECLARACION_CONT' :
    {
            'identificador': ['identificador', '#Pop', '#DcI', 'ASIGNACION'] ,
    },

    'ASIGNACION' :
    {
            'punto_coma': [] ,
            'coma': [] ,
            'asignacion': ['asignacion', 'EXPRESION', '#CmA'] ,
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
            'parentesis_de_inicio': ['#CPI', 'parentesis_de_inicio', 'ARGUMENT', 'parentesis_de_cierre', '#Pop'] ,
    },

    'ARGUMENT' :
    {
            'parentesis_de_cierre': [] ,
            '*': ['EXPRESION', '#CmP', '_ARGUMENT'] ,
    },

    '_ARGUMENT' :
    {
            'parentesis_de_cierre': [] ,
            'coma': ['coma', 'EXPRESION', '#CmP', '_ARGUMENT'] ,
    },
}

# INSTRUCCION -> identificador EXPRESION punto_coma
# INSTRUCCION -> RETORNO punto_coma

# INSTRUCCION -> TIPO identificador DECLARACION
# INSTRUCCION -> void identificador parentesis_de_inicio #DecF PARAMETROS parentesis_de_cierre FUNCION_COLA
# DECLARACION -> ASIGNACION #DecVI _DECLARACION_CONT #DecVC punto_coma
# DECLARACION -> parentesis_de_inicio #DecF PARAMETROS parentesis_de_cierre FUNCION_COLA 
# FUNCION_COLA -> punto_coma #ClsScp
# FUNCION_COLA -> llave_de_inicio BLOQUE llave_de_cierre #ClsScp

# _DECLARACION_CONT -> coma DECLARACION_CONT _DECLARACION_CONT
# _DECLARACION_CONT -> ''
# DECLARACION_CONT -> identificador ASIGNACION

# ASIGNACION -> asignacion EXPRESION
# ASIGNACION -> ''

# PARAMETROS -> TIPO identificador _PARAMETROS
# PARAMETROS -> ''
# _PARAMETROS -> coma TIPO identificador _PARAMETROS
# _PARAMETROS -> ''

# TIPO -> int
# TIPO -> float
# TIPO -> char

# RETORNO -> return EXPRESION

# EXPRESION -> ASIGNACION
# EXPRESION -> LLAMAR_FUNCION
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
