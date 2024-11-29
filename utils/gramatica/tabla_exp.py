# tabla_exp = {
#     'EXPRESION' :
#         {
#         'identificador': ['identificador'] ,
#         'constante_entera': ['constante_entera'] ,
#         'constante_caracter': ['constante_caracter'] ,
#         },
# }


tabla_exp = {
	'EXPRESION' :
	{
		'constante_entera': ['Term', 'Expr_P'] ,
		'constante_caracter': ['constante_caracter'] ,
		'constante_flotante': ['Term', 'Expr_P'] ,
		'constante_boleano': ['Term', 'Expr_P'] ,
		'identificador': ['Term', 'Expr_P'] ,
		'parentesis_de_inicio': ['Term', 'Expr_P'] ,
	},

	'Expr_P' :
	{
		'mas': ['PlusExpr_P'] ,
		'menos': ['MinusExpr_P'] ,
		'parentesis_de_cierre': [] ,
		'operador_y': ['LogicalExpr'] ,
		'operador_o': ['LogicalExpr'] ,
		'igual_que': ['LogicalExpr'] ,
		'punto_coma': [] ,
	},

	'PlusExpr_P' :
	{
		'mas': ['mas', 'Term', 'Expr_P'] ,
	},

	'MinusExpr_P' :
	{
		'menos': ['menos', 'Term', 'Expr_P'] ,
	},

	'Term' :
	{
		'constante_entera': ['Factor', 'Term_P'] ,
		'constante_flotante': ['Factor', 'Term_P'] ,
		'constante_boleano': ['Factor', 'Term_P'] ,
		'identificador': ['Factor', 'Term_P'] ,
		'parentesis_de_inicio': ['Factor', 'Term_P'] ,
	},

	'Term_P' :
	{
		'mas': [] ,
		'menos': [] ,
		'multiplicacion': ['MultTerm_P'] ,
		'division': ['DivTerm_P'] ,
		'modulo': ['ModTerm_P'] ,
		'parentesis_de_cierre': [] ,
		'operador_y': [] ,
		'operador_o': [] ,
		'igual_que': [] ,
		'punto_coma': [] ,
	},

	'MultTerm_P' :
	{
		'multiplicacion': ['multiplicacion', 'Factor', 'Term_P'] ,
	},

	'DivTerm_P' :
	{
		'division': ['division', 'Factor', 'Term_P'] ,
	},

	'ModTerm_P' :
	{
		'modulo': ['modulo', 'Factor', 'Term_P'] ,
	},

	'Factor' :
	{
		'constante_entera': ['constante_entera'] ,
		'constante_flotante': ['constante_flotante'] ,
		'identificador': ['identificador'] ,
		'constante_boleano': ['constante_boleano'] ,
		'parentesis_de_inicio': ['OpenExpr'] ,
	},

	'OpenExpr' :
	{
		'parentesis_de_inicio': ['parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre'] ,
	},

	'LogicalExpr' :
	{
		'operador_y': ['operador_y', 'EXPRESION'] ,
		'operador_o': ['operador_o', 'EXPRESION'] ,
		'igual_que': ['igual_que', 'EXPRESION'] ,
	},
}