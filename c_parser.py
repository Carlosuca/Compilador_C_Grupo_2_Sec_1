tabla = []
pila = ['eof', 0]

def construir_arbol(lista_tokens):

    for token in lista_tokens:
        top = pila[-1]
        if top == token.type and top == 'eof':
            print('Terminado exitosamente')
            return
        if top == token.type and top != 'eof':
            pila.pop()
            continue
        if top in tokens and top != token.type:                
            print("Error: se esperaba ", top)
            print('en la posicion: ', token.lexpos)
            return

