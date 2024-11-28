from utils.tokens import tokens
from utils.gramatica.no_terminales import *
from utils.gramatica.tabla_inst import *
from utils.gramatica.tabla_bloque import *
from utils.gramatica.tabla_exp import *
from utils.gramatica.tabla_init import *
from utils.node import Nodo


def construir_arbol(lista_tokens):
    pila = ['eof', 'PROGRAMA']
    arbol = Nodo('PROGRAMA', "")
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
            top = pila[-1]
            pila_arbol[-1].value = token.value 
            # print(1.5, pila_arbol[-1])
            pila_arbol.pop()
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
        if produccion is None:
            print("Error: NO se esperaba", token.type)
            print('en la posicion: ', token.lexpos)
            return
        nodos = list(map(lambda i: Nodo(i, ""), produccion))
        pila_arbol[-1].children = nodos
        pila.pop()
        pila_arbol.pop()
        

        agregar_produccion(pila, produccion)


        if produccion != ['e']:
            agregar_produccion_arbol(pila_arbol, nodos)
        top = pila[-1]
    
       

def buscar_produccion(no_terminal, terminal):
    # if terminal not in no_terminales:
    #     return None

    print(2, "-> ", no_terminal, terminal, "\n")

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

def agregar_produccion_arbol(pila_arbol, nodos):
    for i in reversed(nodos):
        if(i != 'e'):
            pila_arbol.append(i)

  