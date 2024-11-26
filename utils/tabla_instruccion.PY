# from no_terminales import no_terminales as NT
from no_terminales import no_terminales as NT
tabla_parser = {
    NT.INSTRUCCION :
{
';': [] ,
'id': ['INSTRUCCION', '_INTRUCCION'] ,
'int': ['INSTRUCCION', '_INTRUCCION'] ,
'float': ['INSTRUCCION', '_INTRUCCION'] ,
'char': ['INSTRUCCION', '_INTRUCCION'] ,
'return': ['INSTRUCCION', '_INTRUCCION'] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT._INTRUCCION :
{
';': [] ,
'id': ['_INTRUCCION', 'id', ';'] ,
'int': ['_INTRUCCION', 'DECLARACION'] ,
'float': ['_INTRUCCION', 'DECLARACION'] ,
'char': ['_INTRUCCION', 'DECLARACION'] ,
'return': ['_INTRUCCION', 'RETURN_I'] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.ID :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': [] ,
'expresion': [] ,
'(': ['ID', 'FUNTION_CALL'] ,
')': [] ,
',': [] ,
'=': ['ID', 'D_INIT'] ,
'$': [] ,
},

NT.TIPO :
{
';': [] ,
'id': [] ,
'int': ['TIPO', 'int'] ,
'float': ['TIPO', 'float'] ,
'char': ['TIPO', 'char'] ,
'return': [] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.RETURN_I :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': ['RETURN_I', 'return'] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.FUNTION_CALL :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': [] ,
'expresion': [] ,
'(': ['FUNTION_CALL', '(', ')'] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.ARGUMENT :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': [] ,
'expresion': ['ARGUMENT', '"expresion"'] ,
'(': [] ,
')': ['ARGUMENT', "''"] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.A_ARGUMENT :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': [] ,
'expresion': [] ,
'(': [] ,
')': ['A_ARGUMENT', "''"] ,
',': ['A_ARGUMENT', ',', 'A_ARGUMENT'] ,
'=': [] ,
'$': [] ,
},

NT.DECLARACION :
{
';': [] ,
'id': [] ,
'int': ['DECLARACION', 'TIPO', 'D_INIT'] ,
'float': ['DECLARACION', 'TIPO', 'D_INIT'] ,
'char': ['DECLARACION', 'TIPO', 'D_INIT'] ,
'return': [] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': [] ,
'$': [] ,
},

NT.D_INIT :
{
';': [] ,
'id': [] ,
'int': [] ,
'float': [] ,
'char': [] ,
'return': [] ,
'expresion': [] ,
'(': [] ,
')': [] ,
',': [] ,
'=': ['D_INIT', '='] ,
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

# RETURN_I -> return "expresion"

# FUNTION_CALL -> ( ARGUMENT )

# ARGUMENT -> "expresion" A_ARGUMENT
# ARGUMENT -> ''

# A_ARGUMENT -> , "expresion" A_ARGUMENT
# A_ARGUMENT -> ''


# DECLARACION -> TIPO id D_INIT
# D_INIT -> = "expresion"
# D_INIT -> = ''
