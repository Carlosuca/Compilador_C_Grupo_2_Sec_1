from utils.tokens import tokens
from utils.gramatica.no_terminales import *
from utils.gramatica.tabla_inst import *
from utils.gramatica.tabla_bloque import *
from utils.gramatica.tabla_exp import *
from utils.gramatica.tabla_global import *
import copy

tabla_parser = {}

for tabla in [tabla_global, tabla_bloque, tabla_inst, tabla_exp]:
    for no_terminal in tabla:
        if no_terminal not in tabla_parser:
            tabla_parser[no_terminal] = tabla[no_terminal]
        else:
            tabla_parser[no_terminal] = tabla_parser[no_terminal] | tabla[no_terminal]
            
from utils.node import Nodo


def construir_arbol(lista_tokens):
    pila = ['eof', 'PROGRAMA']
    arbol = Nodo('PROGRAMA', "")
    pila_arbol = [arbol]
    iterador_token = iter(lista_tokens)
    token = next(iterador_token)
    top = pila[-1]
    buffer = []
    while True:
        # print(pila)
        if top == token.type:
            if top == 'eof':
                print('Terminado exitosamente')
                return arbol
            pila.pop()
            top = pila[-1]
            pila_arbol[-1].value = token.value 
            # print(1.5, pila_arbol[-1])
            pila_arbol.pop()
            if buffer:
                token = buffer.pop(0)
                continue
            try:
                token = next(iterador_token)
            except StopIteration:
                token.type = 'eof'
            continue

        # Manejador de errores de recuperacion
        if top in tokens:               
            print("\nError de sintaxis: se esperaba ", top)
            print('en la linea: ' + str(token.lineno), ', posicion: ', str(token.lexpos))
            
            buffer.append(copy.copy(token))
            token.type = top
            token.value = top
            continue
        # print(top+'\t'+token.type)
        produccion = buscar_produccion(top, token.type)

        # Manejador de errores des simbolos de sincronismo
        if produccion is None:
            print("\nError de sintaxis: NO se esperaba", token.type)
            print('en la linea: ' + str(token.lineno), ', posicion: ', str(token.lexpos))
            while True:
                if top == "_GLOBAL" or top == "BLOQUE":
                    break
                pila.pop()
                pila_arbol.pop()
                top = pila[-1]
            while True:
                try:
                    token = next(iterador_token)
                except StopIteration:
                    return
                if token.type == "punto_coma":
                    try:
                        token = next(iterador_token)
                    except StopIteration:
                        return
                    break
            continue

        nodos = list(map(lambda i: Nodo(i, ""), produccion))
        pila_arbol[-1].children = nodos
        pila.pop()
        pila_arbol.pop()
        
        agregar_produccion(pila, produccion)
        agregar_produccion(pila_arbol, nodos)
        top = pila[-1]
        

def buscar_produccion(no_terminal, terminal):
    # if terminal not in no_terminales:
    #     return None

    # print(2, "-> ", no_terminal, terminal, "\n")

    if no_terminal not in tabla_parser:
        return None
    if terminal not in tabla_parser[no_terminal]:
        if '*' in tabla_parser[no_terminal]:
            return tabla_parser[no_terminal]['*']
        return None
    return tabla_parser[no_terminal][terminal]

def agregar_produccion(pila, produccion):
    for i in reversed(produccion):
        if(i != 'e'):
            pila.append(i)
