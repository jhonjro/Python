# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 07:09:23 2020

@author: Cristian Candia
"""

#Este es nuestro primer script
"""
------------------------
Saludos desde Colombia,
¡Bienvenidos al curso introductorio de Python 3.x desde cero!
------------------------
"""

print ("¡Hola mundo!")
print ("saludos desde Colombia")

# =============================================================================
# DEFINICIÓN Y OPERACIÓN DE VARIABLES EN PYTHON
# =============================================================================
import math

#Variables string
variable_str = "La Cartilla"
tutorial = "Python 3.x"
print(variable_str + " " + tutorial)

print(type(variable_str))
type(variable_str)
len(variable_str)

#Variables int
variable_int = 10
variable_int2 = 10
mult = variable_int * variable_int2
variable_int2//2.724638

print(variable_str + " " + tutorial + str(mult) )
print(type(variable_int))

#Variables float
variable_foat = 3.1416

#Variables bool
variable_t = True
variable_f = False
type(variable_f)

pi_10 = variable_int*math.pi
pi_10 = round(pi_10, 4)

print(variable_str*10)

# =============================================================================
# IMPORTAR MÓDULOS/PAQUETES/LIBRERÍAS EN PYTHON
# =============================================================================
#import math
#import pandas as pd
#from sklearn.decomposition import PCA as pca

# =============================================================================
# MÉTODOS DE STRINGS Ó CADENAS DE TEXTO
# =============================================================================

string1 = "la cartilla"
string2 = "123"
string3 = "La Cartilla - Curso de Python 3 desde Cero"

#Descriptivos o de análisis
string1.count("cartilla")
string3.find("Curso")
string1.islower()
string3.islower()
string3.isupper()
string2.isnumeric()

#Métodos de transformación
string1.upper()
string1.title()
string1.replace("a","e")
string3.split("-")

# =============================================================================
# OPERADORES EN PYTHON
#https://www.w3schools.com/python/python_operators.asp
# =============================================================================

#OPERADORES ARITMÉTICOS
x = 10
x//3
x%3
x**2

#OPERADORES DE ASIGNACIÓN
y = "la cartilla"
x+=5 #x= x+5
x-=10
x/=5
y+=" python 3"

#OPERADORES DE COMPARACIÓN
x == y #x es igual a y?
x == 1
y == y #y es igual a y? 
x != y 
x != 1
True != False
10.5638230 < 11.23243
len(y) > x #20 es mayor a 1?
10 <= 10

#OPERADORES LÓGICOS EN PYTHON
x<5 and x<10
x>3 and x<10
x>3 or x<10
not(0.5 < 1)
not(x<10)

#OPERADORES DE IDENTIDAD 
x is x #x es x ? 
y is not x #y no es x ? 
y is not y 

#OPERADORES DE PERTENENCIA
lista1 = [1,2,3,4,5]
3 in lista1 #3 está en la lista 1?
10 not in lista1 #10 no está en la lista 1
"la" in y #la está en la variable y?

(x<5) & (x>-5)
x<5 and x>-5

# =============================================================================
# COLECCIONES/ARREGLOS BÁSICOS EN PYTHON
# =============================================================================

#LISTAS: colecciones ordenadas, no indexadas, mutables.
lista1 = [1,2,3,4,"la cartilla",[True,False,True]]
lista1[0]
lista1[5]
lista1[0:4]
lista1[3:]
lista1[-1]
lista1[-2:]
lista1[-6:]
lista1[5][1:]

lista1[0] = 10
lista1[-1][0] = 0.234
del(lista1[-1])
del(lista1[-1])

lista1 = sorted(lista1,reverse=True)
lista1.append([True,False,True])

#TUPLAS: colecciones ordenados, no indexadas que son inmutables.
tupla1 = (True, False, 1, 2, 3,5, ["a","b","c"])
tupla1[-1]
tupla1[3:]

#SETS: colecciones no ordenadas, no indexadas, mutables, que no permiten elementos duplicados. 
set1 = {1,2,3,4,"la cartilla",1,2,10}
set1.add("python")
set1.update(["a","b",True, False])
set1.discard("la cartilla")

#DICCIONARIOS: colecciones no ordenadas, indexadas, mutables,que no permiten índices duplicados.
carro = {"marca":"ford","modelo":"mustang","año":"1964"}
carro.get("modelo")
carro.keys()
carro.values()
carro.update({"color":"rojo"})

lista_marcas = ["ford","audi","jaguar"]
carro2 = {"marcas":lista_marcas}
carro2.update({"colores":["rojo","negro","plata"]})

# =============================================================================
#SENTENCIAS IF-ELIF-ELSE
# =============================================================================

numero = int(input("Introduzca un número: "))

if numero%2==0:
    print("El número introducido es par")
else:
    print("El número introducido no es par")
    
numero = int(input("Introduzca un número: "))
if numero%2==0:
    print("El número introducido es par")
    if numero <=20:
        print("El número es menor o igual a 20")
    else:
        print("El número es mayor o igual a 20")
else:
    print("El número introducido no es par")
    if numero<20:
        print("El número es menor a 20")
    elif numero>20 and numero<=30:
        print("El número es mayor a 20 y menor o igual a 30")
    else:
        print("El número es mayor a 30 ")
    

if numero<100:
    numero = numero**2

string = "La Cartilla"
if len(string)>4:
    print(string)
else:
    "El número de caracteres del string es inferior a 4"

# =============================================================================
#CICLOS FOR EN PYTHON
# =============================================================================

rango = range(10,20,2)
for elemento in rango:
    print(elemento)

rango2 = [2,4,6,8,10]
for ix,elemento in enumerate(rango):
    print("índice: " + str(ix) + ", elemento: " + str(elemento) + ", mult: " + str(elemento*rango2[ix]))


lista = [["La","Cartilla"],("Python","3.x","desde cero")]
for elemento in lista:
    print(elemento)
    for zoom_elemento in elemento:
        print(zoom_elemento)
    

for elemento in lista:
    print(elemento)
    for zoom_elemento in elemento:
        if len(zoom_elemento)>3:
            print(zoom_elemento)

detalles = []
for ix in range(len(lista)):
    for elemento in lista[ix]:
        detalles.append([elemento,len(elemento)])
    
# =============================================================================
#CICLOS WHILE EN PYTHON
# =============================================================================
numero_usuario = int(input("Ingrese un número mayor a 50: "))
while numero_usuario <= 50:
    numero_usuario = int(input("Número errado, por favor ingrese otro número: "))
else:
    print("Gracias, su número ha sido almacenado")

numero=1
while numero<10:
    print("El número es menor a 10")
    numero += 1

numero=2
while numero<10000000000000:
    print("El número es menor a 10000000000000")
    numero+=1
    if numero > 100:
        print("El número ha superado el valor de 100")
        break

# =============================================================================
#FUNCIONES EN PYTHON
# =============================================================================
        
def y_x2(numero):
    valor_funcion = numero**2
    return valor_funcion

valor = y_x2(10)

def utilidad_neta(ingresos_brutos,egresos,tasa_impuestos):
    utilidad_net = (ingresos_brutos-egresos)*(1-tasa_impuestos)
    return utilidad_net

utilidad = utilidad_neta(1000,300,tasa_impuestos=0.25)
print(utilidad_neta(tasa_impuestos = 0.25, egresos = 300, ingresos_brutos = 1000))

# =============================================================================
#ARGUMENTOS ARBITRARIOS EN FUNCIONES
# =============================================================================
def tipo_datos(*datos):
    tipos_datos = []
    for valor in datos:
        tipos_datos.append(type(valor).__name__)
    return tipos_datos

tipos_datos = tipo_datos(1,10,50,0.50,True,"La Cartilla",0.80,20,30)

def utilidad_neta(**valores):
    utilidad_net = (valores["ingresos_brutos"]-valores["egresos"])*(1-valores["tasa_impuestos"])
    return utilidad_net

import matplotlib.pyplot as plt


def parabola(minimo,maximo,step):
    x=[]
    y=[]
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**2)   
    plt.plot(x,y)
    return x,y

def cubica(minimo,maximo,step):
    x=[]
    y=[]
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**3)   
    plt.plot(x,y)
    return x,y

#valoresx, valoresy = parabola(0,50,2)

def obtener_grafica(minimo,maximo,step,tipo_funcion):
    if tipo_funcion ==1:
        return parabola(minimo,maximo,step)
    elif tipo_funcion==2:
        return cubica(minimo,maximo,step)
    else:
        return print("El tipo de función ingresada es incorrecta")
    
x,y = obtener_grafica(-10,20,1,2)

# =============================================================================
#EJERCICIO DE ALGORITMIA - CIFRADO CESAR
# =============================================================================
import string

alfabeto = list(string.ascii_lowercase)

def cifrado_cesar(alfabeto,n,texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado

frase = "hola a todos, bienvenidos al curso de python 3 desde cero orientado por la cartilla"
frase_cifrada = cifrado_cesar(alfabeto,3,frase)

def decodificar(alfabeto,n,texto):
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - n
            if indice_original <0 :
                indice_original += 25
            texto_decodificado += alfabeto[indice_original]
        else:
            texto_decodificado += letra
    return texto_decodificado

frase_decodificada = decodificar(alfabeto,3,frase_cifrada)

# =============================================================================
#LIST COMPREHENSION EN PYTHON
# =============================================================================

pares = []
for numero in range(100):
    if numero%2==0:
        pares.append(numero)


pares_lc = [numero for numero in range(100) if numero%2==0]

pares_dc = {"id: "+str(numero):numero for numero in range(100) if numero%2==0}

generador = (numero for numero in range(100) if numero%2==0)
generador = list(generador)

generador =  (1 for numero in range(100) if numero%2==0)

import matplotlib.pyplot as plt
import numpy as np

parabola = np.array([[x,x**2] for x in range(-10,10,1)])
plt.plot(parabola[:,0],parabola[:,1])

frases = ["La Cartilla","Curso python 3 desde cero", "list comprehension en python"]
tokens = [palabra.split(" ") for palabra in frases]

# =============================================================================
#FUNCIONES LAMBDA EN PYTHON
# =============================================================================
mensaje = lambda numero: "el número ingresado es: " + str(numero)
mensaje(2)

binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
binomio_cuadrado(2,3)

def cubos(numero):
    str_numero = str(numero)
    cubos = (int(valor)**3 for valor in str_numero)
    return sum(cubos)

valores_buscados = []
for numero in range(100,1000):
    if numero == cubos(numero):
        valores_buscados.append(numero)
        

suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))
numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]

# =============================================================================
#FUNCIONES DE ORDEN SUPERIOR EN PYTHON
# =============================================================================
frase = "hola a todos bienvenidos a un nuevo tutorial del curso de python 3 desde cero orientado por la cartilla"
tokens = frase.split()            

def caracteres(palabra):
    if len(palabra) >3:
        return True

list(filter(caracteres,tokens))

list(filter(lambda palabra: len(palabra)>3,frase.split() ))

numeros = [1,3,5,9,15,25]
list(filter(lambda numero: numero%5==0,numeros))

list(map(lambda palabra: palabra.upper(),tokens))

list(map(lambda numero: numero**2,numeros))

# =============================================================================
#INTRODUCCIÓN A NUMPY PARTE 1 - VECTORES, MATRICES Y SLICING
# =============================================================================

import sys
import time

import numpy as np

tamaño = 10000000

print("vector numpy")
t_vector = time.time()
vector_numpy = np.arange(tamaño,dtype="int64")
suma_vector = vector_numpy.sum()
print("Tipo objeto: " + str(type(vector_numpy)))
print("suma: "+ str(suma_vector))
print("Tamaño vector: " +  str(sys.getsizeof(vector_numpy)/1024))
print("Tiempo ejecución: " + str(time.time()-t_vector))

print("----------------------------")

print("lista")
t_lista = time.time()
lista = list(range(tamaño))
suma_lista = sum(lista)
print("Tipo objeto: " + str(type(lista)))
print("suma: "+ str(suma_lista))
print("Tamaño lista: " +  str(sys.getsizeof(lista)/1024))
print("Tiempo ejecución: " + str(time.time()-t_lista))

#Dimensionalidad
#0D
escalar_0d = 10
#1D
vector_1d = np.array([1,2,3,4,5])
#2D
matriz_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
#3D
matriz_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,11,13],[14,15,16],[17,18,19]]])

#Slicing numpy
vector_1d[0]
vector_1d[-1]
vector_1d[0:3]

matriz_2d[1,0]
matriz_2d[:,1]
matriz_2d[2,:]

matriz_3d[1]
matriz_3d[1,:,2]

# =============================================================================
#INTRODUCCIÓN A NUMPY PARTE 2 - OPERACIONES, APLICACIONES A.L Y ALEATORIOS
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

#Operaciones básicas con numpy arrays
vector_a = np.arange(100)
vector_b = np.arange(100)**(1/2)

suma_v = vector_a + vector_b
mult_v = vector_a* vector_b

#calculo con matrices
matriz = np.array([[1,2],[3,4]])
matriz.sum()
matriz.mean()
matriz.std()
matriz**2
inversa = np.linalg.inv(matriz)
np.dot(matriz,inversa)

#Ajuste polinómico
x= np.arange(-2,2,0.1)
y = np.array([np.sin(valor * (180/np.pi)) for valor in x])
plt.plot(x,y)
coeficientes = np.polyfit(x,y,39)
y_estimada = np.polyval(coeficientes,x)
plt.plot(x,y_estimada)

#Números aleatorios en numpy
cantidad = 100000

uniformes = np.random.uniform(20,80,cantidad)
plt.subplot(2,2,1)
plt.hist(uniformes, bins = 100)

normales = np.random.normal(50,10,cantidad)
plt.subplot(2,2,2)
plt.hist(normales,bins=100)

triangular = np.random.triangular(20,30,80,cantidad)
plt.subplot(2,2,3)
plt.hist(triangular,bins=100)

exponenciales = np.random.exponential(100,cantidad)
plt.subplot(2,2,4)
plt.hist(exponenciales,bins=100)


# =============================================================================
#INTRODUCCIÓN A PANDAS - LECTURA DE ARCHIVOS
# =============================================================================

import pandas as pd
import requests

#EXCEL - CANCER MAMA
# cancer_mama = pd.read_excel("breast_cancer.xlsx")

#CSV (COMMA SEPARATED VALUES) TITANIC Y VINO ROJO
titanic = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
vino_rojo = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",sep=";")

#JSON - COVID19
json_covid = requests.get("https://api.covid19api.com/summary").json()
datos_coronoravirus = pd.DataFrame.from_dict(json_covid["Countries"])
# datos_coronoravirus = pd.read_csv("covid_20200430.csv")

datos_coronoravirus.info()
vino_rojo.describe()
sample_cancer = cancer_mama.head(10)
titanic_sample = titanic.tail(50)


# =============================================================================
#INTRODUCCIÓN A PANDAS - ACCESO A ELEMENTOS EN UN DATAFRAME
# =============================================================================

#Shape dataframe
type(vino_rojo)
vino_rojo.shape

#Columnas dataframe
list(titanic.columns)

#índices dataframe
titanic.index

#Cómo seleccionar una columna?
nombres = titanic["Name"]
nombres_ = list(titanic.Name)

#Seleccionar varias columnas y reordenar un dataframe
titanic = titanic[[
 'Name',
 'Sex',
 'Age',
 'Siblings/Spouses Aboard',
 'Parents/Children Aboard',
 'Fare','Survived',
 'Pclass']]

nombre_sexo = titanic[["Name","Sex"]]

#Cómo re-asignar índices en un dataframe
cancer_mama.index = cancer_mama["id"]
cancer_mama.drop(["id"],axis = 1, inplace=True)

#Filtrando las columnas de un dataframe
cols_cancer = list(cancer_mama.columns)
cols_cancer.remove("radius_mean")
cancer_mama = cancer_mama[cols_cancer]

#Acceder a valores específicos en un dataframe

#Uso de LOC
cancer_mama.loc[842302]
cancer_mama.loc[842302,"diagnosis"]
cancer_mama.loc[[842302,842517],["diagnosis","radius_mean"]]
cancer_mama.loc[[842302,842517]]

titanic_50 = titanic.loc[0:49]
titanic.head(50)

#Uso de ILOC
datos_coronoravirus.iloc[1,0]
datos_coronoravirus.iloc[:20,:4]
datos_coronoravirus.iloc[-50:-1,-1]

#Filtrando dataframes con operadores lógicos
calidad_5 = vino_rojo["quality"]==5
registros_calidad5 = vino_rojo[calidad_5]

calidad_5_6 = (vino_rojo["quality"]==5) | (vino_rojo["quality"]==6)
registros_calidad5_6 = vino_rojo[calidad_5_6]

# =============================================================================
#INTRODUCCIÓN A PANDAS - MEDIDAS DERIVADAS Y APLICACIÓN DE FUNCIONES
# =============================================================================

#Medidas aritméticas para columna/variable/atributo/descriptores
vino_rojo.mean()
vino_rojo.std()
vino_rojo.median()
#Conteo de valores en una columna
vino_rojo["quality"].value_counts()
titanic["Survived"].value_counts()
cancer_mama["diagnosis"].value_counts()

#Creando nuevas columnas derivadas
datos_coronoravirus["DeathRate"] = 1
datos_coronoravirus["DeathRate"] = datos_coronoravirus["TotalDeaths"] / datos_coronoravirus["TotalConfirmed"]
datos_coronoravirus.sort_values("DeathRate",ascending=False,inplace=True)

#Aplicando funciones a la medida sobre series (una columna)
titanic["SurvivedLabel"] = titanic["Survived"].map({0:"Murió",1:"Sobrevivió"})
titanic["SurvivedLabel"].value_counts()

series_upper = lambda x: x.upper()
name_upper = titanic["Name"].map(series_upper)

name_upper_ = titanic["Name"].str.upper()

#Aplicando funciones a la medida sobre dataframes (varias columnas)
name_sex = titanic[["Name","Sex"]].applymap(series_upper)

df_lower = lambda x: x.lower() if type(x) == str else x
titanic = titanic.applymap(df_lower)

vino_rojo.apply(np.sum,axis=1)
titanic_ = titanic.apply(df_lower)

import datetime

# =============================================================================
# MANEJO DE FECHAS EN PYTHON CON DATETIME Y PANDAS
# =============================================================================
import pandas as pd

#FECHAS CON DATETIME
fecha_ejecucion = datetime.datetime.now()
print(type(fecha_ejecucion))
print(fecha_ejecucion)

fecha_ejecucion.year
fecha_ejecucion.day
fecha_ejecucion.date()
str(fecha_ejecucion.date())

fecha_ejecucion.strftime("%x")
fecha_ejecucion.strftime("%X")
fecha_ejecucion.strftime("%A")

fecha_ejecucion.date() + datetime.timedelta(days=10)
str(fecha_ejecucion.date() + datetime.timedelta(days=-2))

#FECHAS CON PANDAS

pd.to_datetime("05/15/2020")
pd.to_datetime("2020-05-15")
pd.to_datetime("20200515")
pd.to_datetime("20201205")
pd.to_datetime("20201205", format="%Y%d%m")

energy = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")

type(energy.iloc[0,0])
energy.index = energy["Date"]
type(energy.index[0])
energy.drop("Date",axis=1, inplace=True)

energy = energy.loc["2014":]
energy = energy.loc["2014-06":]
energy = energy.loc["2014-06":"2017-06"]
energy.reset_index(inplace=True)
energy = energy[energy["Date"] > "2015"]

energy["Date"] = pd.to_datetime(energy["Date"] )
energy.plot(x="Date")

energy["year"] = energy["Date"].dt.year
energy["dayofweek"] = energy["Date"].dt.dayofweek
energy["dayofweek_name"] = energy["Date"].dt.strftime("%A")


energy = energy.drop(["year","dayofweek","dayofweek_name"],axis =1)

m_energy = energy.resample("M",on="Date").sum()
m_energy.plot()

# =============================================================================
# AGRUPACIONES Y PIVOTEOS EN PANDAS
# =============================================================================
import pandas as pd

#Carga y revisión datos
historic_sales = pd.read_csv("OnlineRetail.csv",encoding = "latin1")
historic_sales.info()

historic_sales.isna().sum()
sample = historic_sales.sample(5000)

historic_sales.describe()

#Cálculo de fecha mensual
historic_sales["InvoiceDate"] = pd.to_datetime(historic_sales["InvoiceDate"])
sample = historic_sales.sample(5000)
anio_mes = lambda x: x[:7]
historic_sales["FechaMes"] = historic_sales["InvoiceDate"].astype(str).map(anio_mes)

#Cálculo del monto económico de ventas
historic_sales["Ventas"] = historic_sales["UnitPrice"] * historic_sales["Quantity"]
historic_sales = historic_sales[historic_sales["Ventas"]>0]

#Cuál es el monto de ventas histórico por mes (fecha mes, $ventas)
ventas_mensuales = historic_sales.groupby(["FechaMes"],as_index=False).agg({"Ventas":"sum"})
ventas_mensuales.plot(x="FechaMes")

#Cuál es el monto de ventas histórico mensual por país (fecha mes,país,$ventas)
ventas_mensuales_pais = historic_sales.groupby(["FechaMes","Country"],as_index=False).agg({"Ventas":"sum"})

#Cuál es el número de órdenes histórico mensual por país (fecha mes, país, órdenes)
ordenes_mensuales_pais = historic_sales.groupby(["FechaMes","Country"],as_index=False).agg({"InvoiceNo":"nunique"})

#Histórico ve ventas de manera amigable para quien no está relacionado con formato tidy
ventas_producto = historic_sales.pivot_table(index = "StockCode",columns = ["FechaMes"],values="Ventas",aggfunc="sum",fill_value=0)

#Haga un pivote de las ventas mensuales por país, para que cada país sea una columna
ordenes_mensuales_pais_pivote = ordenes_mensuales_pais.pivot_table(index = "FechaMes",columns="Country",values="InvoiceNo",aggfunc = "sum",fill_value=0).reset_index()























