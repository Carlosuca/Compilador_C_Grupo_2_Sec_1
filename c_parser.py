from utils.tokens import tokens
from utils.tabla_parser import tabla_parser

tabla = []
pila = ['eof', 0]

def construir_arbol(lista_tokens):

    for token in lista_tokens:
        top = pila[-1]
        if top == token.type:
            if top == 'eof':

                print('Terminado exitosamente')
                return
            
            pila.pop()
            continue
        if top in tokens:               
            print("Error: se esperaba ", top)
            print('en la posicion: ', token.lexpos)
            return
        produccion = buscar_produccion(top, token.type)
        if produccion is None:
            print("Error: NO se esperaba", token.type)
            print('en la posicion: ', token.lexpos)
            return
        pila.pop()
        agregar_produccion(pila, produccion)

def buscar_produccion(terminal, no_terminal):
    if terminal not in tabla_parser:
        return None
    if no_terminal not in tabla_parser[terminal]:
        return None
    return tabla_parser[terminal][no_terminal]

def agregar_produccion(pila, produccion):
    for i in produccion:
        pila.append(i)
        

