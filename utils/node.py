
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

    def print_values(self): 
        
        print([
        self.type,
        self.value,
        self.scope])
    
    def __repr__(self):

        if self.value == "":
            return self.type
        else: 
            return str(self.type) + " -> " + str(self.value) + str(self.scope)

