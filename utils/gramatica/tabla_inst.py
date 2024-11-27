# from no_terminales import no_terminales as NT
# from utils.gramatica.no_terminales import no_terminales_instruccion as NT

tabla_inst = {

'INSTRUCCION' :
{
'punto_coma': [] ,
'identificador': ['_INSTRUCCION', 'INSTRUCCION'] ,
'int': ['_INSTRUCCION', 'INSTRUCCION'] ,
'float': ['_INSTRUCCION', 'INSTRUCCION'] ,
'char': ['_INSTRUCCION', 'INSTRUCCION'] ,
'void': ['_INSTRUCCION', 'INSTRUCCION'] ,
'return': ['_INSTRUCCION', 'INSTRUCCION'] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'llave_de_cierre': ['e'] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'_INSTRUCCION' :
{
'punto_coma': [] ,
'identificador': ['identificador', 'ID', 'punto_coma'] ,
'int': ['DECLARACION', 'punto_coma'] ,
'float': ['DECLARACION', 'punto_coma'] ,
'char': ['DECLARACION', 'punto_coma'] ,
'void': ['DECLARACION', 'punto_coma'] ,
'return': ['RETURN_I', 'punto_coma'] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'ID' :
{
'punto_coma': ['D_INIT'] ,
'identificador': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': ['FUNTION_CALL'] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': ['D_INIT'] ,
'EOF': [] ,
},

'TIPO' :
{
'punto_coma': [] ,
'identificador': [] ,
'int': ['int'] ,
'float': ['float'] ,
'char': ['char'] ,
'void': ['void'] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'RETURN_I' :
{
'punto_coma': [] ,
'identificador': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': ['return', 'EXPRESION'] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'FUNTION_CALL' :
{
'punto_coma': [] ,
'identificador': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': ['parentesis_de_inicio', 'ARGUMENT', 'parentesis_de_cierre'] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'ARGUMENT' :
{
'punto_coma': [] ,
'identificador': ['EXPRESION', 'A_ARGUMENT'] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': [] ,
'constante_caracter': ['EXPRESION', 'A_ARGUMENT'] ,
'constante_entera': ['EXPRESION', 'A_ARGUMENT'] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': ['e'] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'A_ARGUMENT' :
{
'punto_coma': [] ,
'identificador': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': ['e'] ,
'coma': ['coma', 'EXPRESION', 'A_ARGUMENT'] ,
'asignacion': [] ,
'EOF': [] ,
},

'DECLARACION' :
{
'punto_coma': [] ,
'identificador': [] ,
'int': ['TIPO', 'identificador', 'D_INIT'] ,
'float': ['TIPO', 'identificador', 'D_INIT'] ,
'char': ['TIPO', 'identificador', 'D_INIT'] ,
'void': ['TIPO', 'identificador', 'D_INIT'] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': [] ,
'EOF': [] ,
},

'D_INIT' :
{
'punto_coma': ['e'] ,
'identificador': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'return': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'coma': [] ,
'asignacion': ['asignacion', 'EXPRESION'] ,
'EOF': [] ,
},
}

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
