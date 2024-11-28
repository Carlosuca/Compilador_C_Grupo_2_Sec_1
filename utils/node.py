
#https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
class Nodo:
    def __init__(self, type, value, children = []):
        self.type = type
        self.value = value
        self.children = children

    def __str__(self, level=0):

        val = ""

        if self.value == "":
            val = self.type
        else: 
            val =  self.type + " -> " + str(self.value) 

        ret = "\t"*level+repr(val)+"\n"

        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def __repr__(self):

        if self.value == "":
            return self.type
        else: 
            return self.type + "->" + self.value 

