def Pop(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.pop()

def DcT(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.append(token.type)

def DcI(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.append(token.value)
    tabla_simbolos.addEntry(pila_semantica[-1],pila_semantica[-2])

def DcF(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.symbols[pila_semantica[-1]]
    func.type = "funcion " + func.type
    func.ivalue = "@" + func.name
    func.parameters = []

def BBl(pila_semantica, token, arbol, tabla_simbolos):
    tabla_simbolos.addScope("block_" + str(tabla_simbolos.block_counter))
    tabla_simbolos.block_counter += 1
    return tabla_simbolos.children["block_" + str(tabla_simbolos.block_counter-1)]

def BFB(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.symbols[pila_semantica[-1]]
    tabla_simbolos.addScope(func.ivalue)
    return tabla_simbolos.children[func.ivalue]

def EBl(pila_semantica, token, arbol, tabla_simbolos):
    return tabla_simbolos.parent

def RgP(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.parent.symbols[pila_semantica[-3]]
    func.parameters.append(pila_semantica[-2])


    
procesos_atributos = {
    '#DcT': DcT,
    '#DcI': DcI,
    '#Pop': Pop,
    '#DcF': DcF,
    '#BBl': BBl,
    '#EBl': EBl,
    '#BFB': BFB,
    '#RgP': RgP,
}