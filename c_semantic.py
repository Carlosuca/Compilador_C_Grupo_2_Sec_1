import pandas as pd
import ast
from utils.node import ASTNode
from utils.s_table import find_node_by_type

#TODO LO COMENTADO AUN ESTA EN PROCESO


# Función principal de análisis semántico
def analisis_semantico(syntax_tree, symbol_table):

    # Procesar nodos recursivamente
    def process_node(node, current_scope, process, errors):

        er = None

        if node.scope != "":
            current_scope = node.scope

        if process == "ASIGNMENT" and node.type == "INSTRUCCION":
            er = process_assignment(node)          
        
        if process == "USAGE" and node.type == "identificador":
             er = process_variable_usage(node, current_scope)

        # Procesar hijos recursivamente
        if er is not None:
            errors.add(er)

        for child in node.children:
            process_node(child, current_scope, process, errors)


    # # Procesar declaración de variables
    # def process_declaration(node, current_scope, errors):
    #     var_name = node.children[0].value  # Nombre de la variable
    #     var_type = node.children[1].value  # Tipo de la variable

    #     if var_name in current_scope.symbols:
    #         errors.append(f"Error: Variable '{var_name}' ya declarada en el ámbito '{current_scope.scope}'.")
    #     else:
    #         current_scope.addEntry(var_name, var_type)


    # # Procesar asignaciones
    def process_assignment(node):

        value_node = find_node_by_type(node, "EXPRESION")
        
        if(value_node is not None):
            # print(value_node.print_values())
            exp = get_expresion(value_node)
            # print(exp)

           
        # Define a helper function to convert the list to an expression
        def list_to_expression(input_list):
            operators = {
                'mas': '+',
                'resta': '-',
                'division': '/',
                'multiplicacion': '*',
                'operador_y': '&&',
                'operador_o': '||',
                'igual_que': '==',
            }

            types = {
                'int': "1", 
                'float': "1.0",
                'char': "1",
                'bool': "1"
            }

            expression = ""
            for item in input_list:
                if item in types:
                    expression += types[item]  # Use sample values for types
                elif item in operators:
                    expression += f" {operators[item]} "
                else:
                    raise ValueError(f"Unknown item: {item}")
            return expression

        # Define a function to evaluate the AST and determine the result type
        def evaluate_ast(node):
            if isinstance(node, ast.BinOp):
                # Recursively evaluate left and right nodes
                left_type = evaluate_ast(node.left)
                right_type = evaluate_ast(node.right)
                
                # Determine the result type based on the operation
                if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
                    return 'float' if 'float' in (left_type, right_type) else 'int'
                elif isinstance(node.op, ast.Div):
                    return 'float'  # Division always results in float
            elif isinstance(node, ast.Constant):
                # Check the constant's type
                return 'float' if isinstance(node.value, float) else 'int'
            else:
                raise ValueError(f"Unsupported AST node: {type(node)}")

        # Input list
        input_list = exp

        # Convert list to expression
        expression = list_to_expression(input_list)
        # print(expression)

        # Parse the expression into an AST
        parsed_ast = ast.parse(expression, mode='eval')

        # Evaluate the AST and determine the type
        value_type  = evaluate_ast(parsed_ast.body)

        type_node = find_node_by_type(node, "TIPO")
    
        if(type_node is not None):
            
            id_node = find_node_by_type(node, "identificador")
            id_value = id_node.value
            
            type_name = type_node.children[0].type  # Nombre de la variable

            # print(value_type, type_name)

            if not check_type_compatibility(type_name, value_type):
                # return "No", type_name, value_type)
                return f"Error: var {id_value} type {type_name} received invalid type {value_type}"
            else:
                return 
    # Procesar uso de variables
    def process_variable_usage(node, current_scope):
        var_name = node.value  # Nombre de la variable
        
        
        if symbol_table.exists_in_scope(current_scope, var_name):
            symbol_table.increment_usage(var_name)
            return 
            #  print(var_name, current_scope, symbol_table.increment_usage(var_name))
        else: 
            return f"Error: variable {var_name} is used but never declared in current scope"

    def get_expresion(node):
        
        values = []
        
        if node.type == "identificador":
            return [symbol_table.get_symbol(node.value).type]
        elif node.type == "constante_entera":
            return ["int"]
        elif node.type == "constante_caracter":
            return["char"]
        elif node.type == "boleano":
            return["int"]
        elif node.type == "constante_flotante":
            return ["float"]
        elif node.type in ["mas", "menos", "multiplicacion", "division", "operador_o", "operador_y", "igual_que"]:
            return [node.type]
           
        else:
           None

        for child in node.children:
            exp = get_expresion(child)
            if exp != []:
                values = values + exp

        return values
                



    # # Búsqueda en la tabla de símbolos
    # def find_in_scope(var_name, scope):
    #     current_scope = scope
    #     while current_scope:
    #         if var_name in current_scope.symbols:
    #             return current_scope.symbols[var_name]
    #         current_scope = current_scope.parent
    #     return None


    # Verificación de compatibilidad de tipos
    def check_type_compatibility(expected_type, actual_type):
        type_compatibility = {
            "int": ["int"],
            "float": ["float", "int"],
            "char": ["char", "int"],
            "bool": ["int", "bool", "char"],
        }
        return actual_type in type_compatibility[expected_type]
    
    def process_table(symbol_table, errors): 

        for child in symbol_table.children:
            for id in symbol_table.symbols:
                sym = symbol_table.symbols[id]
                if  sym.usage_count == 1 and sym.name != 'main':
                    
                    errors.add( f"Warning: {sym.type or 'variable'} {sym.name} declared but never used ")
            

    errors = set()
    warnings = set()

    process_node(syntax_tree, symbol_table.scope, "USAGE", errors)
    
    if(len(errors) == 0):
        process_node(syntax_tree, symbol_table.scope, "ASIGNMENT", errors)
        
    if(len(errors) == 0):
        process_table(symbol_table, warnings)
    
    for er in errors:
        print(er)
        print("\n Terminado con errores")
        return

    for er in warnings:
        print(er)
        print("\n Terminado con advertencias")
        return
    
    print("\n Terminado exitosamente")

     
