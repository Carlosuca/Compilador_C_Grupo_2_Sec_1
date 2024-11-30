def Pop(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    pila_semantica.pop()

def DcT(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    pila_semantica.append(token)

def DcI(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    id_s = tabla_simbolos.is_declared(token.value,0)
    if id_s == True:
        lista_errores.append("\n\nError: la variable " + token.value + ' ya esta declarada\nen la linea: ' + str(token.lineno) + ', posicion: ' + str(token.lexpos))
        return
    pila_semantica.append(token)
    tabla_simbolos.addEntry(pila_semantica[-1].value,pila_semantica[-2].value,str(pila_semantica[-1].lineno),None,None)

def DcF(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    func = tabla_simbolos.symbols[pila_semantica[-1].value]
    func.usage_count+=1
    func.type = "funcion " + pila_semantica[-2].value
    func.ivalue = "@" + pila_semantica[-1].value
    func.parameters = []

def BBl(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    tabla_simbolos.addScope("block_" + str(tabla_simbolos.block_counter))
    tabla_simbolos.block_counter += 1
    return tabla_simbolos.children["block_" + str(tabla_simbolos.block_counter-1)]

def BFB(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    func = tabla_simbolos.symbols[pila_semantica[-1].value]
    tabla_simbolos.addScope(func.ivalue)
    return tabla_simbolos.children[func.ivalue]

def EBl(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    return tabla_simbolos.parent

def RgP(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    func = tabla_simbolos.parent.symbols[pila_semantica[-3].value]
    func.parameters.append(pila_semantica[-2].value)

def Ref(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    id_s = tabla_simbolos.find_symbol(token.value)
    if id_s is None:
        lista_errores.append("\n\nError: la variable " + token.value + ' no ha sido declarada\nen la linea: ' + str(token.lineno) + ', posicion: ' + str(token.lexpos))
        return
    id_s.usage_count +=1

def Psh(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    pila_semantica.append(token)

operando_integral = {
    'constante_entera': 'int',
    'constante_flotante': 'float',
    'constante_caracter': 'char',
    'constante_boleano': 'bool' 
}

def Cmp(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    a = pila_semantica[-1]
    if not isinstance(a, str):
        aa = tabla_simbolos.find_symbol(a.value)
        if aa is None:
            pila_semantica.pop()
            pila_semantica.pop()
            pila_semantica.append("#INVALID")
            return
        a = aa.type
    elif a == "#INVALID":
        return
    b = pila_semantica[-2]
        
    if not isinstance(b, str):
        bb = tabla_simbolos.find_symbol(b.value)
        if bb is None:
            pila_semantica.pop()
            pila_semantica.pop()
            pila_semantica.append("#INVALID")
            return
        b = bb.type
    
    if a in operando_integral or a in operando_integral.values():
        a = 'operando_integral'
    if b in operando_integral or b in operando_integral.values():
        b = 'operando_integral'

    if a != b:
        pila_semantica.pop()
        pila_semantica.pop()
        pila_semantica.append("#INVALID")
        lista_errores.append("\n\nError: la expresion incluye does valores que no son convertibles por defecto\nen la linea: " + str(token.lineno) + ', posicion: ' + str(token.lexpos))
        return
    pila_semantica.pop()
    pila_semantica.pop()
    pila_semantica.append(a)

def CmA(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    a = pila_semantica[-1]
    b = pila_semantica[-2]
    if not isinstance(a, str):
        aa = tabla_simbolos.find_symbol(a.value)
        if aa is None:
            return
        a = aa.type
    if not isinstance(b, str):
        bb = tabla_simbolos.find_symbol(b.value)
        if bb is None:
            return
        b = bb.type
    if a in operando_integral or a in operando_integral.values():
        a = 'operando_integral'
    if b in operando_integral or b in operando_integral.values():
        b = 'operando_integral'
    if a != b:
        pila_semantica.pop()
        lista_errores.append("\n\nError: el valor de la expresion no se puede asignar a la variable " + b.value + '\nen la linea: ' + str(b.lineno) + ', posicion: ' + str(b.lexpos))
        return
    pila_semantica.pop()

def CPI(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    a = pila_semantica[-1]
    if not isinstance(a, str):
        aa = tabla_simbolos.find_symbol(a.value)
        if aa is None:
            pila_semantica.append("#INVALID")
            return
        a = aa.parameters
        pila_semantica.extend(reversed(a))
    else:
        pila_semantica.append("#INVALID")
    

def CmP(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    a = pila_semantica[-1]
    b = pila_semantica[-2]
    if b == "#INVALID":
        return
    if not isinstance(a, str):
        aa = tabla_simbolos.find_symbol(a.value)
        if aa is None:
            return
        a = aa.type
    if a in operando_integral or a in operando_integral.values():
        a = 'operando_integral'
    if b in operando_integral or b in operando_integral.values():
        b = 'operando_integral'
    if a != b:
        pila_semantica.pop()
        lista_errores.append("\n\nError: los parametros proporcionadoes no encajan con la declaracion de " + b.value + ' ya esta declarada\nen la linea: ' + str(b.lineno) + ', posicion: ' + str(b.lexpos))
        return
    pila_semantica.pop()

def CmR(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    a = pila_semantica[-1]
    
    if not isinstance(a, str):
        if not a.type == 'return':
            aa = tabla_simbolos.find_symbol(a.value)
            if aa is None:
                pila_semantica.pop()
                pila_semantica.pop()
                pila_semantica.append("#INVALID")
                return
            a = aa.type
            pila_semantica.pop()
            pila_semantica.pop()
        else:
            a = 'void'
            pila_semantica.pop()
    elif a == "#INVALID":
        pila_semantica.pop()
        pila_semantica.pop()
        return
    b = tabla_simbolos.find_symbol(tabla_simbolos.scope[1:]).type[8:]
    bb = b
    if a in operando_integral or a in operando_integral.values():
        a = 'operando_integral'
    if b in operando_integral or b in operando_integral.values():
        b = 'operando_integral'
    if a != b:
        print("RETORNO INVALIDO\n")
        lista_errores.append("\n\nError: el valor de retorno no es el esperado por la funcion " + bb + ' ya esta declarada\nen la linea: ' + str(token.lineno) + ', posicion: ' + str(token.lexpos))
        return

def DcC(pila_semantica, token, arbol, tabla_simbolos, lista_errores):

    tabla_simbolos.addEntry("const_" + str(tabla_simbolos.const_counter),operando_integral[token.type],token.lineno,token.value)
    tabla_simbolos.symbols["const_" + str(tabla_simbolos.const_counter)].usage_count+=1
    tabla_simbolos.const_counter += 1
    pila_semantica.append('operando_integral')
    token.type = 'identificador'
    token.value = "const_" + str(tabla_simbolos.const_counter-1)
    
def Snc(pila_semantica, token, arbol, tabla_simbolos, lista_errores):
    pila_semantica.append('#SYNC')
    
procesos_atributos = {
    '#DcT': DcT,
    '#DcI': DcI,
    '#Pop': Pop,
    '#Psh': Psh,
    '#DcF': DcF,
    '#BBl': BBl,
    '#EBl': EBl,
    '#BFB': BFB,
    '#RgP': RgP,
    '#Ref': Ref,
    '#Cmp': Cmp,
    '#CmA': CmA,
    '#CmP': CmP,
    '#DcC': DcC,
    '#CPI': CPI,
    '#CmR': CmR,
    '#Snc': Snc
}