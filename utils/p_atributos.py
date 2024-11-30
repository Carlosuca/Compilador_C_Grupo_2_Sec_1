def Pop(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.pop()

def DcT(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.append(token)

def DcI(pila_semantica, token, arbol, tabla_simbolos):
    id_s = tabla_simbolos.is_declared(token.value,0)
    if id_s == True:
        print("VARIABLE YA DECLARADA\n")
    pila_semantica.append(token)
    tabla_simbolos.addEntry(pila_semantica[-1].value,pila_semantica[-2].value)

def DcF(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.symbols[pila_semantica[-1].value]
    func.type = "funcion " + pila_semantica[-2].value
    func.ivalue = "@" + pila_semantica[-1].value
    func.parameters = []

def BBl(pila_semantica, token, arbol, tabla_simbolos):
    tabla_simbolos.addScope("block_" + str(tabla_simbolos.block_counter))
    tabla_simbolos.block_counter += 1
    return tabla_simbolos.children["block_" + str(tabla_simbolos.block_counter-1)]

def BFB(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.symbols[pila_semantica[-1].value]
    tabla_simbolos.addScope(func.ivalue)
    return tabla_simbolos.children[func.ivalue]

def EBl(pila_semantica, token, arbol, tabla_simbolos):
    return tabla_simbolos.parent

def RgP(pila_semantica, token, arbol, tabla_simbolos):
    func = tabla_simbolos.parent.symbols[pila_semantica[-3].value]
    func.parameters.append(pila_semantica[-2].value)

def Ref(pila_semantica, token, arbol, tabla_simbolos):
    id_s = tabla_simbolos.is_declared(token.value)
    if id_s == False:
        print("VARIABLE NO DECLARADA\n")

def Psh(pila_semantica, token, arbol, tabla_simbolos):
    pila_semantica.append(token)

operando_integral = {
    'constante_entera': 'int',
    'constante_flotante': 'float',
    'constante_caracter': 'char',
    'constante_boleano': 'bool' 
}

def Cmp(pila_semantica, token, arbol, tabla_simbolos):
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
        print("TERMINO NO COMPATIBLE\n")
        pila_semantica.pop()
        pila_semantica.pop()
        pila_semantica.append("#INVALID")
        return
    pila_semantica.pop()
    pila_semantica.pop()
    pila_semantica.append(a)

def CmA(pila_semantica, token, arbol, tabla_simbolos):
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
        print("EXPRESION NO ASIGNABLEf\n")
        pila_semantica.pop()
        return
    pila_semantica.pop()

def CPI(pila_semantica, token, arbol, tabla_simbolos):
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
    

def CmP(pila_semantica, token, arbol, tabla_simbolos):
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
        print("PARAMETROS NO ENCAJA\n")
        pila_semantica.pop()
        return
    pila_semantica.pop()

def CmR(pila_semantica, token, arbol, tabla_simbolos):
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
        print("PARAMETROS NO ENCAJA\n")
        pila_semantica.pop()
        return
    pila_semantica.pop()

def DcC(pila_semantica, token, arbol, tabla_simbolos):

    tabla_simbolos.addEntry("const_" + str(tabla_simbolos.const_counter),operando_integral[token.type],token.value)
    tabla_simbolos.const_counter += 1
    pila_semantica.append('operando_integral')
    token.type = 'identificador'
    token.value = "const_" + str(tabla_simbolos.const_counter-1)
    
    
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
}