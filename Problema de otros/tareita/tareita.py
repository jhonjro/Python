
nombre = str(input('Ingrese su nombre: '))
apellido_paterno = str(input('Ingrese su apellido paterno: '))
apellido_materno = str(input('Ingrese su apellido materno: '))
fecha = str(input('Ingrese su fecha de nacimiento (dd/mm/aaaa): '))
dni = str(input('Ingrese su dni(al menos 3 digitos): '))

nombre = nombre.upper()
apellido_paterno = apellido_paterno.upper()
apellido_materno = apellido_materno.upper()

fecha = fecha.split('/')

# * año

if (len(fecha[2]) != 4):
    print('Ingreso el año de manera incorrecta')
else:
    aa = fecha[2][-2:]

# * mes

if (len(fecha[1]) > 2):
    print('Ingreso el mes de manera incorrecta')

elif (len(fecha[1]) == 1):
    mm = '0' + fecha[1]
else:
    mm = fecha[1]

# * día

if (len(fecha[0]) > 2):
    print('Ingreso el día de manera incorrecta')


elif (len(fecha[0]) == 1):
    dd = '0' + fecha[0]
else:
    dd = fecha[0]

# * Apellido paterno

if (len(apellido_paterno) > 0):
    A = str(len(apellido_paterno))
    P = apellido_paterno[0]

    if(len(apellido_paterno) < 4):
        Z = apellido_paterno[-1]
    else:
        Z = apellido_paterno[3]
else:
    print('Ingreso el apellido paternp de manera incorrecta')


# * Apellido materno

if (len(apellido_materno) > 0):

    M = apellido_paterno[0]

    if(len(apellido_materno) < 3):
        Y = apellido_materno[-1]
    else:
        Y = apellido_paterno[2]
else:
    print('Ingreso el apellido materno de manera incorrecta')


if (len(nombre) > 0):
    N = nombre[0]
else:
    print('Ingreso el nombre de manera incorrecta')


# * nombre

if (len(nombre) > 0):
    N = nombre[0]
else:
    print('Ingreso el nombre de manera incorrecta')


# * dni

if (len(dni) > 3):
    DDD = dni[:3]
else:
    print('Ingreso el dni de manera incorrecta')

print(type(aa))
print(type(mm))
print(type(dd))
print(type(A))
print(type(P))
print(type(Z))
print(type(M))
print(type(Y))
print(type(N))
print(type(DDD))
print(aa+mm+dd+A+P+Z+M+Y+N+DDD)
