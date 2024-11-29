import pandas as pd
from utils.node import Nodo


#TODO LO COMENTADO AUN ESTA EN PROCESO


# Función principal de análisis semántico
def analisis_semantico(syntax_tree, symbol_table):

    # Procesar nodos recursivamente
    def process_node(node, current_scope, errors):

        if node.scope != "":
            current_scope = node.scope
        # if node.type == "identificador":
        #     process_declaration(node, current_scope, errors)
        # elif node.type == "INSTRUCCION":
        #     process_assignment(node, current_scope, errors)
        # elif node.type == "identificador":
        if node.type == "identificador":
            process_variable_usage(node, current_scope, errors)

        # Procesar hijos recursivamente
        for child in node.children:
            process_node(child, current_scope, errors)


    # # Procesar declaración de variables
    # def process_declaration(node, current_scope, errors):
    #     var_name = node.children[0].value  # Nombre de la variable
    #     var_type = node.children[1].value  # Tipo de la variable

    #     if var_name in current_scope.symbols:
    #         errors.append(f"Error: Variable '{var_name}' ya declarada en el ámbito '{current_scope.scope}'.")
    #     else:
    #         current_scope.addEntry(var_name, var_type)


    # # Procesar asignaciones
    # def process_assignment(node, current_scope, errors):
    #     var_name = node.children[0].value  # Nombre de la variable
    #     assigned_value = node.children[1]  # Nodo con el valor asignado

    #     var_entry = find_in_scope(var_name, current_scope)

    #     if var_entry is None:
    #         errors.append(f"Error: Variable '{var_name}' no declarada antes de ser asignada.")
    #     else:
    #         if not check_type_compatibility(var_entry.type, assigned_value.type):
    #             errors.append(f"Error: Tipo incompatible en la asignación de '{var_name}'. Esperado '{var_entry.type}', encontrado '{assigned_value.type}'.")


    # Procesar uso de variables
    def process_variable_usage(node, current_scope, errors):
        var_name = node.value  # Nombre de la variable
        
        
        if symbol_table.exists_in_scope(current_scope, var_name):
            symbol_table.increment_usage(var_name)
            #  print(var_name, current_scope, symbol_table.increment_usage(var_name))
        else: 
            print(f"Error: variable {var_name} is used but never declared in current scope")

    # # Búsqueda en la tabla de símbolos
    # def find_in_scope(var_name, scope):
    #     current_scope = scope
    #     while current_scope:
    #         if var_name in current_scope.symbols:
    #             return current_scope.symbols[var_name]
    #         current_scope = current_scope.parent
    #     return None


    # # Verificación de compatibilidad de tipos
    # def check_type_compatibility(expected_type, actual_type):
    #     type_compatibility = {
    #         "int": ["int"],
    #         "float": ["float", "int"],
    #         "char": ["char"],
    #     }
    #     return actual_type in type_compatibility.get(expected_type, [])
    
    def process_table(symbol_table): 

        for child in symbol_table.children:
            for id in symbol_table.symbols:
                sym = symbol_table.symbols[id]
                if  sym.usage_count == 1 and sym.name != 'main':
                    
                    print(f"Warning: {sym.type or 'variable'} {sym.name} declared but never used ")
            

    errors = []
    process_node(syntax_tree, symbol_table.scope, errors)
    process_table(symbol_table)
    return errors
