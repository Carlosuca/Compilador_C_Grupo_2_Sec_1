
# PROGRAM -> A PROGRAM
# PROGRAM -> ''


# A -> TypeSpecifier I GlobalDeclaration 

# GlobalDeclaration -> VariableDeclaration
# GlobalDeclaration -> FunctionDeclaration

# VariableDeclaration -> ;

# FunctionDeclaration -> ( ParameterList ) ;

# ParameterList ) ;

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
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': ['A', 'PROGRAM'] ,
    'float': ['A', 'PROGRAM'] ,
    'char': ['A', 'PROGRAM'] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'A' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'float': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'char': ['TypeSpecifier', 'identificador', 'GlobalDeclaration'] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'GlobalDeclaration' :
    {
    'identificador': [] ,
    ';': ['VariableDec'] ,
    '=': ['VariableAsi'] ,
    'expresion': [] ,
    '(': ['Function'] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'VariableDec' :
    {
    'identificador': [] ,
    ';': [';'] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'VariableAsi' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': ['=', 'EXPRESION', ';'] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'Function' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': ['(', 'ParameterList', ')', 'FunctionDeclaration'] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'FunctionDeclaration' :
    {
    'identificador': [] ,
    ';': [';'] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': ['_BLOQUE'] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'TypeSpecifier' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': ['int'] ,
    'float': ['float'] ,
    'char': ['char'] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'ParameterList' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': ["''"] ,
    'bloque_funcion': [] ,
    'int': ['Parameter', 'ParameterRest'] ,
    'float': ['Parameter', 'ParameterRest'] ,
    'char': ['Parameter', 'ParameterRest'] ,
    'void': ['void'] ,
    ',': [] ,
    '$': [] ,
    },

    'Parameter' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': [] ,
    'bloque_funcion': [] ,
    'int': ['TypeSpecifier', 'identificador'] ,
    'float': ['TypeSpecifier', 'identificador'] ,
    'char': ['TypeSpecifier', 'identificador'] ,
    'void': [] ,
    ',': [] ,
    '$': [] ,
    },

    'ParameterRest' :
    {
    'identificador': [] ,
    ';': [] ,
    '=': [] ,
    'expresion': [] ,
    '(': [] ,
    ')': ["''"] ,
    'bloque_funcion': [] ,
    'int': [] ,
    'float': [] ,
    'char': [] ,
    'void': [] ,
    ',': [',', 'Parameter', 'ParameterRest'] ,
    '$': [] ,
    },

}