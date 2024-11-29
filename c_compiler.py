from c_lexer import *
from c_parser import *
from c_semantic import *
from utils.s_table import *

if __name__ == '__main__':
    lista, tabla = identificar_tokens(analizador, 'test/test1.c')

    print('Lista de tokens....')
    print("\n")
    # imprimir_tokens(lista)
    print("\n")
    arbol = construir_arbol(lista)
    print(arbol)

    #TODO: FALTAN COMENTARIOS

    print("Tabla de simbolos...")
    print("\n")
    tabla = construir_tabla(arbol)
    # print(tabla)
    # print(arbol)

    analisis_semantico(arbol, tabla)

    print('\n')
    input("Presiona enter para salir")