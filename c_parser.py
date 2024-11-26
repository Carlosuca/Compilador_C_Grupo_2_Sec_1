from utils.tokens import tokens
from utils.tabla_parser import tabla_parser

#https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
class Nodo:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def __repr__(self):
        return '<tree node representation>'



def construir_arbol(lista_tokens):
    pila = ['eof', '<_BLOQUE>']
    arbol = Nodo('<PROGRAMA>')
    pila_arbol = [arbol]
    iterador_token = iter(lista_tokens)
    token = next(iterador_token)
    top = pila[-1]
    while True:
        print(pila)
        if top == token.type:
            if top == 'eof':
                print('Terminado exitosamente')
                return arbol
            pila.pop()
            pila_arbol.pop()
            top = pila[-1]
            try:
                token = next(iterador_token)
            except StopIteration:
                token.type = 'eof'
            continue
        if top in tokens:               
            print("Error: se esperaba ", top)
            print('en la posicion: ', token.lexpos)
            return
        # print(top+'\t'+token.type)
        produccion = buscar_produccion(top, token.type)
        # print(produccion)
        if produccion is None:
            print("Error: NO se esperaba", token.type)
            print('en la posicion: ', token.lexpos)
            return
        nodos = list(map(lambda i: Nodo(i), produccion))
        pila_arbol[-1].children = nodos
        pila.pop()
        pila_arbol.pop()
        agregar_produccion(pila, produccion)
        agregar_produccion(pila_arbol, nodos)
        top = pila[-1]
    
       

def buscar_produccion(terminal, no_terminal):
    if terminal not in tabla_parser:
        return None
    if no_terminal not in tabla_parser[terminal]:
        return None
    return tabla_parser[terminal][no_terminal]

def agregar_produccion(pila, produccion):
    for i in reversed(produccion):
        pila.append(i)

        

