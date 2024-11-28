'expresion'
# PROGRAM -> A PROGRAM
# PROGRAM -> ''

# A -> TypeSpecifier B
# B -> identificador GlobalDeclaration 

# GlobalDeclaration -> VariableDeclaration
# GlobalDeclaration -> VariableInit
# GlobalDeclaration -> FunctionDeclaration

# VariableDeclaration -> punto_coma
# VariableInit -> coma B

# FunctionDeclaration -> ( ParameterList ) punto_coma

# TypeSpecifier -> int
# TypeSpecifier -> float
# TypeSpecifier -> char

# ParameterList -> Parameter ParameterRest
# ParameterList -> void
# ParameterList -> ''

# Parameter -> TypeSpecifier Identifier
# ParameterRest -> coma Parameter ParameterRest
# ParameterRest -> ''

tabla_program =  {
    
'PROGRAMA' :
{
'identificador': ['B'] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'llave_de_cierre': ['llave_de_cierre', 'PROGRAMA'],
'bloque': [] ,
'int': ['A', 'PROGRAMA'] ,
'float': ['A', 'PROGRAMA'] ,
'char': ['A', 'PROGRAMA'] ,
'void': ['A', 'PROGRAMA'] ,
'Identifier': [] ,
'eof': ['eof'] ,
},

'A' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': ['TypeSpecifier', 'B'] ,
'float': ['TypeSpecifier', 'B'] ,
'char': ['TypeSpecifier', 'B'] ,
'void': ['TypeSpecifier', 'B'] ,
'Identifier': [] ,
'eof': [] ,
},

'B' :
{
'identificador': ['identificador', 'GlobalDeclaration'] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'GlobalDeclaration' :
{
'identificador': [] ,
'punto_coma': ['punto_coma'] ,
'coma': ['coma', 'B'] ,
'asignacion': ['VariableInit', 'C'] ,
'expresion': [] ,
'parentesis_de_inicio': ['FunctionDeclaration'] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'C' :
{
'identificador': [] ,
'punto_coma': ['punto_coma'] ,
'coma': ['coma', 'B'] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'VariableInit' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': ['asignacion', 'EXPRESION'] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'FunctionDeclaration' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': ['parentesis_de_inicio', 'ParameterList', 'parentesis_de_cierre', 'FunctionStruct'] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'FunctionStruct' :
{
'identificador': [] ,
'llave_de_inicio': ['BLOQUE'],
'punto_coma': ['punto_coma'] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,

'bloque': ['bloque'] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

'TypeSpecifier' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': ['int'] ,
'float': ['float'] ,
'char': ['char'] ,
'void': ['void'] ,
'Identifier': [] ,
'eof': [] ,
},

'ParameterList' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': ['e'] ,
'bloque': [] ,
'int': ['Parameter', 'ParameterRest'] ,
'float': ['Parameter', 'ParameterRest'] ,
'char': ['Parameter', 'ParameterRest'] ,
'void': ['Parameter', 'ParameterRest'] ,
'Identifier': [] ,
'eof': [] ,
},

'Parameter' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': [] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': [] ,
'bloque': [] ,
'int': ['TypeSpecifier', 'Identifier'] ,
'float': ['TypeSpecifier', 'Identifier'] ,
'char': ['TypeSpecifier', 'Identifier'] ,
'void': ['TypeSpecifier', 'Identifier'] ,
'Identifier': [] ,
'eof': [] ,
},

'ParameterRest' :
{
'identificador': [] ,
'punto_coma': [] ,
'coma': ['coma', 'Parameter', 'ParameterRest'] ,
'asignacion': [] ,
'expresion': [] ,
'parentesis_de_inicio': [] ,
'parentesis_de_cierre': ['e'] ,
'bloque': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'void': [] ,
'Identifier': [] ,
'eof': [] ,
},

}