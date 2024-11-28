
import pandas as pd
from utils.node import Nodo

def imprimir_tabla(tree):
    # Tabla de símbolos
    symbol_table = pd.DataFrame()

    scope_stack = ['global']

    def find_node_by_type(node, target_type):
    # Verifica si el nodo actual tiene el tipo deseado
        # print(node.type)
        if node.type == target_type:
            return node

        # Recurre en los hijos del nodo actual
        for child in node.children:
            result = find_node_by_type(child, target_type)
            if result is not None:  # Si se encuentra, se devuelve
                return result

        return None # Retorna None si no se encuentra el nodo

    def build_symbol_table(node, scope="global"):
           
        # print(find_node_by_type(node, 'DECLARACION'))
        if node.type == "DECLARACION":
            type_node = find_node_by_type(node, "TIPO").children[0].value
            id_node = find_node_by_type(node, 'identificador').value
            # print(find_node_by_type(node, 'EXPRESION'))

            symbol_table[id_node] = {
                "type": type_node,
                "value": None,
                # "value": value_node if value_node else None,
                "scope": scope
            }

        elif node.type == "A":
            type_node = find_node_by_type(node, "TypeSpecifier").children[0].value
            id_node = find_node_by_type(node, 'identificador').value
            # print(find_node_by_type(node, 'EXPRESION')) 

            symbol_table[id_node] = {
                "type": type_node,
                "value": None,
                # "value": value_node if value_node else None,
                "scope": scope
            }

        # print(node.type)
        if node.type == 'A' :
            scope = "global"

        elif node.type == 'BLOQUE' and node.children[0].type == 'llave_de_inicio' :
            scope_stack.append("FunctionStruct")
            
        elif node.type == 'BLOQUE' :
            scope_stack.append(node.children[0].type)
        
        elif node.type == 'llave_de_cierre':
            scope_stack.pop()

        for child in node.children:
            build_symbol_table(child, scope_stack[-1])

    # Construir la tabla
    build_symbol_table(tree, scope_stack[-1])

    # Imprime la tabla
    
    print(symbol_table.transpose())
    # # Imprimir usando tabulate
    # print(tabulate(symbol_table.transpose(), headers="keys", tablefmt="grid"))

