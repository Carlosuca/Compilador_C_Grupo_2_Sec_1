import argparse
from c_lexer import *
from c_parser import *
from c_semantic import *
from utils.s_table import *

def main(input_file, show_arbol, show_tabla, show_lista):
    # Procesar el archivo proporcionado como argumento
    lista, tabla = identificar_tokens(analizador, input_file)

    if show_lista:
        print('Lista de tokens....')
        print("\n")
        imprimir_tokens(lista)
        print("\n")
    
    arbol, tabla = construir_arbol(lista)

    if show_arbol:
        print("Árbol construido:")
        print(arbol)

    # TODO: FALTAN COMENTARIOS

    # tabla = construir_tabla(arbol)

    if show_tabla:
        print("Tabla de símbolos...")
        print("\n")
        print(tabla)

    #analisis_semantico(arbol, tabla)

    print('\n')
    # input("Presiona enter para salir")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analizador de código en C")
    parser.add_argument(
        "input_file", type=str, help="Ruta al archivo fuente en C que será analizado"
    )
    parser.add_argument(
        "--show-arbol", action="store_true", help="Mostrar el árbol construido"
    )
    parser.add_argument(
        "--show-tabla", action="store_true", help="Mostrar la tabla de símbolos"
    )
    parser.add_argument(
        "--show-lista", action="store_true", help="Mostrar la lista de tokens"
    )
    args = parser.parse_args()
    main(args.input_file, args.show_arbol, args.show_tabla, args.show_lista)


    # from c_lexer import *
# from c_parser import *
# from c_semantic import *
# from utils.s_table import *

# if __name__ == '__main__':
#     lista, tabla = identificar_tokens(analizador, 'test/test1.c')

#     print('Lista de tokens....')
#     print("\n")
#     # imprimir_tokens(lista)
#     print("\n")
#     arbol = construir_arbol(lista)
#     # print(arbol)

#     #TODO: FALTAN COMENTARIOS

#     print("Tabla de simbolos...")
#     print("\n")
#     tabla = construir_tabla(arbol)
#     print(tabla)
#     # print(arbol)

#     analisis_semantico(arbol, tabla)

#     print('\n')
#     input("Presiona enter para salir")
