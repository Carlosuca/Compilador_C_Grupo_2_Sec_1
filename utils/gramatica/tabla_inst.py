# from no_terminales import no_terminales as NT
# from utils.gramatica.no_terminales import no_terminales_instruccion as NT

tabla_inst = {

    '_INTRUCCION' :
    {
        ';': [] ,
        'id': ['id', 'ID', ';'] ,
        'int': ['DECLARACION', ';'] ,
        'float': ['DECLARACION', ';'] ,
        'char': ['DECLARACION', ';'] ,
        'return': ['RETURN_I', ';'] ,
        'expresion': [] ,
        '(': [] ,
        ')': [] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'ID' :
    {
        ';': ['D_INIT'] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': [] ,
        'expresion': [] ,
        '(': ['FUNTION_CALL'] ,
        ')': [] ,
        ',': [] ,
        '=': ['D_INIT'] ,
        '$': [] ,
    },

    'TIPO' :
    {
        ';': [] ,
        'id': [] ,
        'int': ['int'] ,
        'float': ['float'] ,
        'char': ['char'] ,
        'return': [] ,
        'expresion': [] ,
        '(': [] ,
        ')': [] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'RETURN_I' :
    {
        ';': [] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': ['return', 'EXPRESION'] ,
        'expresion': [] ,
        '(': [] ,
        ')': [] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'FUNTION_CALL' :
    {
        ';': [] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': [] ,
        'expresion': [] ,
        '(': ['(', 'ARGUMENT', ')'] ,
        ')': [] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'ARGUMENT' :
    {
        ';': [] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': [] ,
        'expresion': ['EXPRESION', 'A_ARGUMENT'],
        '(': [] ,
        ')': ['e'] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'A_ARGUMENT' :
    {
        ';': [] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': [] ,
        'expresion': [] ,
        '(': [] ,
        ')': ['e'] ,
        ',': [',', 'EXPRESION', 'A_ARGUMENT'] ,
        '=': [] ,
        '$': [] ,
    },

    'DECLARACION' :
    {
        ';': [] ,
        'id': [] ,
        'int': ['TIPO', 'id', 'D_INIT'] ,
        'float': ['TIPO', 'id', 'D_INIT'] ,
        'char': ['TIPO', 'id', 'D_INIT'] ,
        'return': [] ,
        'expresion': [] ,
        '(': [] ,
        ')': [] ,
        ',': [] ,
        '=': [] ,
        '$': [] ,
    },

    'D_INIT' :
    {
        ';': ['e'] ,
        'id': [] ,
        'int': [] ,
        'float': [] ,
        'char': [] ,
        'return': [] ,
        'expresion': [] ,
        '(': [] ,
        ')': [] ,
        ',': [] ,
        '=': ['=', 'EXPRESION'] ,
        '$': [] ,
    },
}

# INSTRUCCION -> _INTRUCCION INSTRUCCION
# INSTRUCCION -> ''


# _INTRUCCION -> DECLARACION ;
# _INTRUCCION -> id ID ;
# _INTRUCCION -> RETURN_I ;

# ID -> D_INIT
# ID -> FUNTION_CALL

# TIPO -> int
# TIPO -> float
# TIPO -> char
# TIPO -> void

# RETURN_I -> return "expresion"

# FUNTION_CALL -> ( ARGUMENT )

# ARGUMENT -> "expresion" A_ARGUMENT
# ARGUMENT -> ''

# A_ARGUMENT -> , "expresion" A_ARGUMENT
# A_ARGUMENT -> ''


# DECLARACION -> TIPO id D_INIT
# D_INIT -> = "expresion"
# D_INIT -> ''
