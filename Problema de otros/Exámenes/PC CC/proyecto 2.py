fans = open("Licenciamiento Institucional_6.csv", "r")
a = dict()
b = dict()
c = dict()
d = dict()
e = dict()
f = dict()
g = dict()
h = dict()
i = dict()
j = dict()

for line in fans:
    if line != "":
        line = line.replace('\n', '')
        line = line.replace('|', ',')
        line_data = line.split(",")
        a[line_data[0]] = line_data[1]
        b[line_data[0]] = line_data[2]
        c[line_data[0]] = line_data[3]
        d[line_data[0]] = line_data[4]
        e[line_data[0]] = line_data[5]
        f[line_data[0]] = line_data[6]
        g[line_data[0]] = line_data[7]
        h[line_data[0]] = line_data[8]
        i[line_data[0]] = line_data[9]


def matriz():
    p = list(b.values())
    o = list(e.values())
    Public = []
    Private = []
    for i in range(len(p)):
        if p[i] == 'PÚBLICO':
            Public.append(o[i])
        elif p[i] == 'PRIVADO':
            Private.append(o[i])
    h = list(set(o))
    h.sort()
    print(h)
    A = []
    for y in range(len(h)):
        c = list()
        c.append(h[y])
        c.append(Private.count(h[y]))
        c.append(Public.count(h[y]))
        c.append(int(Private.count(h[y]) + Public.count(h[y])))
        A.append(c)
    print(A)


def mergesort(lista, columna):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]
        mergesort(L, columna)
        mergesort(R, columna)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][columna] < R[j][columna]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1


def busqueda_binaria(lista, buscar, columna):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der)//2
        if lista[medio][columna] == buscar:
            return medio
        elif lista[medio][columna] > buscar:
            der = medio - 1
        else:
            izq = medio + 1
    return -1


def busqueda():
    lista = []
    fans_archivo = open("Licenciamiento Institucional_6.csv", "r")
    for linea in fans_archivo.readlines():
        fila = linea.split('|')
        lista.append({
            'CODIGO_ENTIDAD' : fila[0],
            'NOMBRE' : fila[1],
            'TIPO_GESTION': fila[2],
            'ESTADO_LICENCIAMIENTO' : fila[3],
            'PERIODO_LICENCIAMIENTO' : fila[4],
            'DEPARTAMENTO_LOCAL' : fila[5],
            'PROVINCIA_LOCAL': fila[6],
            'DISTRITO_LOCAL':fila[7],
            'LATITUD_UBICACION':fila[8],
            'LONGITUD_UBICACION':fila[9]
        })
    print("1. Buscar por nombre de universidad")
    print("2. Buscar por departamento")
    print("3. Buscar por distrito")

    opcion = input("Ingrese opcion : ")
    if opcion == "1":
        mergesort(lista, "NOMBRE")
        buscar = input("Nombre de universidad : ").upper()
        posicion = busqueda_binaria(lista, buscar, "NOMBRE")
        if posicion == -1 :
            print("Nombre no encontrado")
        else:
            for key, value in lista[posicion].items():
                print(key, " : ", value)

    elif opcion == "2":
        mergesort(lista, "DEPARTAMENTO_LOCAL")
        buscar = input("Nombre Departamento Local : ").upper()
        posicion = busqueda_binaria(lista, buscar, "DEPARTAMENTO_LOCAL")
        if posicion == -1:
            print("Departamento no encontrado")
        else:
            for key, value in lista[posicion].items():
                print(key, " : ", value)

    elif opcion == "3":
        mergesort(lista, "DISTRITO_LOCAL")
        mergesort(lista, "DISTRITO_LOCAL")
        buscar = input("Nombre de Distrito Local : ").upper()
        posicion = busqueda_binaria(lista, buscar, "DISTRITO_LOCAL")
        if posicion == -1:
            print("Distrito no encontrado")
        else:
            for key, value in lista[posicion].items():
                print(key, " : ", value)
def PDF():
    k = open('a.pdf', 'a')
    k.close()


PDF()


def menu():
    while True:
        print("1. Leer Archivo")
        print("2. Guardar como pdf")
        print("3. Busqueda")
        print("4. Matriz")
        opcion = input("Opcion : ")
        if opcion == "1":
            PDF()
        elif opcion == "3":
            busqueda()
        elif opcion == "4":
            matriz()



menu()
