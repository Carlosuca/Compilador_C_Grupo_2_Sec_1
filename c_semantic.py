
import pandas as pd
from utils.node import Nodo

## Tabla de Simbolos extendida, incluyendo ambitos y valores iniciales (algunos)


class Identifier:
    def __init__(self,name,type,ivalue=None):
        self.name = name
        self.type = type
        self.ivalue = ivalue

    def __str__(self):
        return "ID {:16} Tipo: {:16} Inicial: {:32}".format(
                str(self.name), str(self.type), str(self.ivalue))

## Estructura de tabla de simbolos. Una tabla se crea por ambito y se enlazan.
## Almacena simbolos en un hash table y hace referencias al ambito superior e inferiores.
class SymbolTable:
    def __init__(self, scope, parent):
        self.scope = scope
        self.parent = parent ##Ambito superio
        self.symbols = {} ##Simbolos en el ambito actual
        self.children = {} ##Sub-ambitos

    ## REvisa si la variable no existe. De ser el caso, la crea y almacena
    def addEntry(self,name,type,ivalue=None):
        if name in self.symbols: return
        self.symbols[name] = Identifier(name,type,ivalue)

    def addScope(self,scope):
        if scope in self.children: return
        self.children[scope] = SymbolTable(scope,self)

    #Formateo para vizualizar niveles de ambito
    def printString(self,l):
        out = ''
        for i in range(0,l-1):
                out += '\t'

        out += f"scope of {self.scope}\n"
        for s in self.symbols.keys():
            for e in range(0,l):
                out += '\t'
            out += str(self.symbols[s]) + '\n'
        for c in self.children:
            out += self.children[c].printString(l+1)
        return out

    def __str__(self):
        return self.printString(0)
    
block_counter = 0

def find_node_by_type(node, target_type, depth=-1):
    # Verifica si el nodo actual tiene el tipo deseado
        # print(node.type)
        if node is None:
            return None
        if node.type == target_type:
            return node

        if depth == 0:
            return None
        # Recurre en los hijos del nodo actual
        for child in node.children:
            result = find_node_by_type(child, target_type, depth-1)
            if result is not None:  # Si se encuentra, se devuelve
                return result

        return None # Retorna None si no se encuentra el nodo

def build_symbol_table(node, symbol_table):
        # TODO: Parametros y valores inicialse de variables
        # print(find_node_by_type(node, 'DECLARACION'))
        if node is None:
            return
        if node.type == "INSTRUCCION_B" or node.type == "GLOBAL":
            type_node = find_node_by_type(node, "INSTRUCCION", 1)
            source = node
            if type_node is not None:
                source = type_node
                type_node = find_node_by_type(type_node, "TIPO", 1)
            else:
                type_node = find_node_by_type(node, "TIPO", 1)
            data_type = ""
            if type_node is not None:
                data_type = type_node.children[0].type
            else:
                type_node = find_node_by_type(source, "void", 1)
                data_type = 'void'
            if type_node is not None:
                id_node = find_node_by_type(source, 'identificador',1).value
                func = find_node_by_type(source, "FUNCIONG_COLA", 2)
                if func is None:
                    func = find_node_by_type(source, "FUNCION_COLA", 2)
                if func is not None:
                    symbol_table.addEntry(id_node, "function " + data_type, "@" + id_node)
                    func_def = find_node_by_type(func, "BLOQUE", 1)
                    if func_def is not None:
                        symbol_table.addScope(symbol_table.symbols[id_node].ivalue)
                        build_symbol_table(func_def,symbol_table.children[symbol_table.symbols[id_node].ivalue])
                else:
                    if type_node.type != "void":
                        symbol_table.addEntry(id_node,data_type)

        if node.type == "INSTRUCCION_B" or node.type == "INSTRUCCION_C":
            inst_node = find_node_by_type(node, "INSTRUCCION_C", 1)
            if inst_node is not None:
                global block_counter
                block_counter += 1
                symbol_table.addScope("@blk"+str(block_counter))
                blk_node = find_node_by_type(inst_node, "BLOQUE", 2)
                if blk_node is not None:
                    build_symbol_table(blk_node,symbol_table.children["@blk"+str(block_counter)])
                else:
                    build_symbol_table(find_node_by_type(inst_node, "INSTRUCCION", 1),symbol_table.children["@blk"+block_counter])
        if node.type == "_GLOBAL" or node.type == "BLOQUE":
            for child in node.children:
                build_symbol_table(child, symbol_table)
        return symbol_table

def imprimir_tabla(tree):
    # Tabla de símbolos
    pdsymbol_table = pd.DataFrame()

    scope_stack = ['global']

    
    
        


    # Construir la tabla
    global block_counter
    block_counter = 0
    symbol_table = build_symbol_table(find_node_by_type(tree, "_GLOBAL", 1), SymbolTable('global', None))

    # Imprime la tabla
    
    print(symbol_table)
    # # Imprimir usando tabulate
    # print(tabulate(symbol_table.transpose(), headers="keys", tablefmt="grid"))

