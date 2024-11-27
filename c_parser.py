from utils.tokens import tokens
from utils.gramatica.no_terminales import *
from utils.gramatica.tabla_inst import *
from utils.gramatica.tabla_bloque import *
from utils.gramatica.tabla_exp import *
from utils.gramatica.tabla_init import *

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
    pila = ['eof', 'PROGRAM']
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
    
       

def buscar_produccion(no_terminal, terminal):
    # if terminal not in no_terminales:
    #     return None

    print("-> ", no_terminal, terminal, "\n")

    if no_terminal not in no_terminales:
        return None
    
    if no_terminal in no_terminales_ini: 
        return tabla_program[no_terminal][terminal]

    if no_terminal in no_terminales_bloque: 
        return tabla_bloque[no_terminal][terminal]

    if no_terminal in no_terminales_instruccion: 
        return tabla_inst[no_terminal][terminal]

    if no_terminal in no_terminales_exp: 
        return tabla_exp[no_terminal][terminal]

def agregar_produccion(pila, produccion):
    for i in reversed(produccion):
        if(i != 'e'):
            pila.append(i)

        

