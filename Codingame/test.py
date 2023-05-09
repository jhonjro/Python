str = input("ingrese la ecuacion:")

igual = str.find("=")
mas_a = str.find("+", 0, igual)
menos_a = str.find("-", 0, igual)
mas_d = str.find("+", igual, len(str)-1)
menos_d = str.find("-", igual, len(str)-1)
por_a = str.find("*", 0, igual)
por_d = str.find("*", igual, len(str) - 1)
entre_a = str.find("/", 0, igual)
entre_d = str.find("/", igual, len(str) - 1)

x = str.find("x", 0, len(str))
l = list(str)

if mas_a > 0:
    # reemplazamos el simbolo por une espacio
    l[mas_a] = ' '
    str = "".join(l)
    # guadamos el valor en caso esta sea correcta
    s_a = 1
if mas_d > 0:
    l[mas_d] = ' '
    str = "".join(l)
    s_d = 1
if menos_a > 0:
    l[menos_a] = ' '
    str = "".join(l)
    s_a = 0
if menos_d > 0:
    l[menos_d] = ' '
    str = "".join(l)
    s_d = 0

if por_a > 0:
    # reemplazamos el simbolo por une espacio
    l[por_a] = ' '
    str = "".join(l)
    # guadamos el valor en caso esta sea correcta
    s_a = 2
if por_d > 0:
    l[por_d] = ' '
    str = "".join(l)
    s_d = 2
if entre_a > 0:
    # reemplazamos el simbolo por une espacio
    l[entre_a] = ' '
    str = "".join(l)
    # guadamos el valor en caso esta sea correcta
    s_a = 3
if entre_d > 0:
    l[entre_d] = ' '
    str = "".join(l)
    s_d = 3

if igual > 0:
    l[igual] = ' '
    str = "".join(l)

# ubicamos los numeros
numeros = [int(temp) for temp in str.split() if temp.isdigit()]
if x > igual:
    # invertimos el sentido en caso x este en el lado derecho de la ecuacion
    aux = numeros[2]
    numeros[2] = numeros[1]
    numeros[1] = numeros[0]
    numeros[0] = aux
    if x == igual+1:
        x = 0
    else:
        x = 1
    aux = s_d
    s_d = s_a
    s_a = aux

# despeja al lado derecho
if s_d == 0:
    x_val = numeros[1] - numeros[2]
if s_d == 1:
    x_val = numeros[1] + numeros[2]
if s_d == 2:
    x_val = numeros[1] * numeros[2]
if s_d == 3:
    if numeros[2] != 0:
        x_val = numeros[1] / numeros[2]
    else:
        print("error de sintaxis...")
        quit()
if x == 0:
    if s_a == 0:
        x_val = x_val + numeros[0]
    if s_a == 1:
        x_val = x_val - numeros[0]
    if s_a == 2:
        if numeros[0] != 0:
            x_val = x_val / numeros[0]
        else:
            print("error de sintaxis...")
            quit()
    if s_a == 3:
        if numeros[0] != 0:
            x_val = x_val * numeros[0]
        else:
            print("error de sintaxis...")
            quit()
else:
    if s_a == 0:
        x_val = -x_val + numeros[0]
    if s_a == 1:
        x_val = x_val - numeros[0]
    if s_a == 2:
        if numeros[0] != 0:
            x_val = x_val / numeros[0]
        else:
            print("error de sintaxis...")
            quit()
    if s_a == 3:
        if numeros[0] != 0:
            x_val = numeros[0]/x_val
        else:
            print("error de sintaxis...")
            quit()

print("el valor de x es: ", x_val)
