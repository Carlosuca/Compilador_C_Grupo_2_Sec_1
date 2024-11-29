
#https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
class Nodo:
    def __init__(self, type, value, scope='' ,children = []):
        self.type = type
        self.value = value
        self.children = children
        self.scope = scope

    def __str__(self, level=0):

        val = self.scope

        # if self.value == "":
        #     val = self.type + "@" + self.scope
        # else: 
        #     val =  self.type + " -> " + str(self.value) + "@" + self.scope
        
        ret = "\t"*level+repr(self)+"\n"

        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addScope(self, scope):
        self.scope = scope

    def print_values(self, level=0): 
        ret = "\t"*level+repr(self)+"\n"

        for child in self.children:

            # if child.children != []:
            ret += child.print_values(level+1)
            # ret += child.print_values(level+1)
        return ret
        
    
    def __repr__(self):

        if self.value == "":
            return self.type
        else: 
            return str(self.type) + " -> " + str(self.value) + str(self.scope)


class ASTNode:
    def __init__(self, type_, value=None, left=None, right=None):
        self.type = type_  # Tipo de nodo, como "operador", "identificador", "numero"
        self.value = value  # Valor del nodo (por ejemplo, "x" para un identificador o 5 para un número)
        self.left = left  # Hijo izquierdo (para operaciones binarias)
        self.right = right  # Hijo derecho (para operaciones binarias)

    def __str__(self):
        if self.type in ['+', '-', '*', '/', '=']:  # Operadores
            return f"({str(self.left)} {self.value} {str(self.right)})"
        return str(self.value)

# Clases para identificadores y números
class Identifier(ASTNode):
    def __init__(self, name):
        super().__init__('identificador', name)

class Number(ASTNode):
    def __init__(self, value):
        super().__init__('numero', value)