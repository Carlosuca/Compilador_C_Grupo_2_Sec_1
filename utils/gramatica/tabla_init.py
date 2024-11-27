
# PROGRAM -> A PROGRAM
# PROGRAM -> ''


# A -> TypeSpecifier I GlobalDeclaration 

# GlobalDeclaration -> VariableDeclaration
# GlobalDeclaration -> FunctionDeclaration

# VariableDeclaration -> punto_coma

# FunctionDeclaration -> ( ParameterList ) punto_coma

# ParameterList ) punto_coma

# TypeSpecifier -> int
# TypeSpecifier -> float
# TypeSpecifier -> char

# ParameterList -> Parameter ParameterRest
# ParameterList -> void
# ParameterList -> ''

# Parameter -> TypeSpecifier Identifier
# ParameterRest -> , Parameter ParameterRest
# ParameterRest -> ''

tabla_program = {
    'PROGRAM' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'llave_de_cierre': ['e'] ,
    'bloque_funcion': [] ,
    'int': ['A', 'PROGRAM'] ,
    'float': ['A', 'PROGRAM'] ,
    'char': ['A', 'PROGRAM'] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'A' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'float': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'char': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'GlobalDeclaration' :
    {
    'identificador': [] ,
    'punto_coma': ['VariableDec'] ,
    'asignacion': ['VariableAsi'] ,
    'expresion': [] ,
    'parentesis_de_inicio': ['Function'] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'VariableDec' :
    {
    'identificador': [] ,
    'punto_coma': ['punto_coma'] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'VariableAsi' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': ['asignacion', 'EXPRESION', 'punto_coma'] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'Function' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': ['parentesis_de_inicio', 'ParameterList', 'parentesis_de_cierre', 'FunctionDeclaration'] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'FunctionDeclaration' :
    {
    'identificador': [] ,
    'punto_coma': ['punto_coma'] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'llave_de_inicio': ['llave_de_inicio', 'INSTRUCCION'] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'TypeSpecifier' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': ['int'] ,
    'float': ['float'] ,
    'char': ['char'] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'ParameterList' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': ['e'] ,
    'bloque_funcion': [] ,
    'int': ['Parameter', 'ParameterRest'] ,
    'float': ['Parameter', 'ParameterRest'] ,
    'char': ['Parameter', 'ParameterRest'] ,
    'void': ['void'] ,
    'coma': [] ,
    'eof': [] ,
    },

    'Parameter' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': [] ,
    'bloque_funcion': [] ,
    'int': ['TypeSpecifier', 'identificador'] ,
    'float': ['TypeSpecifier', 'identificador'] ,
    'char': ['TypeSpecifier', 'identificador'] ,
    'void': [] ,
    'coma': [] ,
    'eof': [] ,
    },

    'ParameterRest' :
    {
    'identificador': [] ,
    'punto_coma': [] ,
    'asignacion': [] ,
    'expresion': [] ,
    'parentesis_de_inicio': [] ,
    'parentesis_de_cierre': ['e'] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    'coma': ['coma', 'Parameter', 'ParameterRest'] ,
    'eof': [] ,
    },


    

}