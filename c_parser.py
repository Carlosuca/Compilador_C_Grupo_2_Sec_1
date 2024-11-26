from utils.tokens import tokens
from utils.tabla_parser import tabla_parser

tabla = []
pila = ['eof', '<_BLOQUE>']

def construir_arbol(lista_tokens):
    print(pila)
    iterador_token = iter(lista_tokens)
    token = next(iterador_token)
    print(token)
    top = pila[-1]
    while True:
        print(pila)
        if top == token.type:
            if top == 'eof':
                print('Terminado exitosamente')
                return
            pila.pop()
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
        print(top+'\t'+token.type)
        produccion = buscar_produccion(top, token.type)
        print(produccion)
        if produccion is None:
            print("Error: NO se esperaba", token.type)
            print('en la posicion: ', token.lexpos)
            return
        pila.pop()
        agregar_produccion(pila, produccion)
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

        

