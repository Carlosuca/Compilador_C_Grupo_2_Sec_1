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
		'constante_caracter': ['Term', 'Expr_P'] ,
		'constante_flotante': ['Term', 'Expr_P'] ,
		'constant_caracter': ['Term', 'Expr_P'] ,
		'identificador': ['Term', 'Expr_P'] ,
		'parentesis_de_inicio': ['Term', 'Expr_P'] ,
	},

	'Expr_P' :
	{
		'mas': ['PlusExpr_P'] ,
		'menos': ['MinusExpr_P'] ,
		'parentesis_de_cierre': [] ,
		'parentesis_de_inicio': [] ,
		'operador_y': ['LogicalExpr'] ,
		'operador_o': ['LogicalExpr'] ,
		'igual_que': ['LogicalExpr'] ,
		'*': [] ,
	},

	'PlusExpr_P' :
	{
		'mas': ['mas', 'Term', '#Cmp', 'Expr_P'] ,
	},

	'MinusExpr_P' :
	{
		'menos': ['menos', 'Term', '#Cmp', 'Expr_P'] ,
	},

	'Term' :
	{
		'constante_entera': ['Factor', 'Term_P'] ,
		'constante_flotante': ['Factor', 'Term_P'] ,
		'constante_caracter': ['Factor', 'Term_P'] ,
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
		'parentesis_de_inicio': ['LLAMAR_FUNCION'] ,
		'operador_y': [] ,
		'operador_o': [] ,
		'igual_que': [] ,
		'*': [] ,
	},

	'MultTerm_P' :
	{
		'multiplicacion': ['multiplicacion', 'Factor', '#Cmp', 'Term_P'] ,
	},

	'DivTerm_P' :
	{
		'division': ['division', 'Factor', '#Cmp', 'Term_P'] ,
	},

	'ModTerm_P' :
	{
		'modulo': ['modulo', 'Factor', '#Cmp', 'Term_P'] ,
	},

	'Factor' :
	{
		'constante_entera': ['constante_entera', '#DcC'] ,
		'constante_flotante': ['constante_flotante', '#DcC'] ,
		'identificador': ['identificador', '#Ref', '#Psh'] ,
		'constante_caracter': ['constante_caracter', '#DcC'] ,
		'parentesis_de_inicio': ['OpenExpr'] ,
	},

	'OpenExpr' :
	{
		'parentesis_de_inicio': ['parentesis_de_inicio', 'EXPRESION', 'parentesis_de_cierre'] ,
	},

	'LogicalExpr' :
	{
		'operador_y': ['operador_y', 'EXPRESION', '#Cmp'] ,
		'operador_o': ['operador_o', 'EXPRESION', '#Cmp'] ,
		'igual_que': ['igual_que', 'EXPRESION', '#Cmp'] ,
	},
}