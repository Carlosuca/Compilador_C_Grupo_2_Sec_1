no_terminales_bloque = {
    '_BLOQUE',
    'BLOQUE',
    'INSTRUCCION_CERRADA',
    'BLOQUE_ELSE',
    'COLA_ELSE'
}

no_terminales_instruccion = {
    'INSTRUCCION',
    '_INSTRUCCION',
    'ID',
    'TIPO',
    'RETURN_I',
    'FUNTION_CALL',
    'ARGUMENT',
    'A_ARGUMENT',
    'DECLARACION',
    'D_INIT',
}

no_terminales_exp = {
    'EXPRESION'
}

no_terminales_ini = {
'PROGRAMA',
'A',
'B',
'C',
'GlobalDeclaration',
'VariableDeclaration',
'VariableInit',
'FunctionDeclaration',
'FunctionStruct',
'TypeSpecifier',
'ParameterList',
'Parameter',
'ParameterRest',
}

no_terminales = no_terminales_bloque.union(no_terminales_instruccion).union(no_terminales_exp).union(no_terminales_ini)

# print(no_terminales_ini["PROGRAM"])