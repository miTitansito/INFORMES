from math import dist
from itertools import accumulate
#Determine el par de puntos que se encuentran más cercanos.
#Almacene la respuesta en un string llamado parCercano. Ejemplo:
#parCercano = "P1-P9" 
#"""
#print("------------------------ EJERCICIO 1 --------------------------------")
### Se transcriben los puntos a listas, puesto que estas son iterables y se pueden operar
P1=list((2, 2, 3))
P6=list((1, 0.5, 1))
P2=list((2, 3, 4))
P7=list((3, 2, 0.5))
P3=list((1, 1, 3))
P8=list((3, 1, 2))
P4=list((0.5, 0.5, 2))
P9=list((0, 0, 0))
P5=list((1, 2, 1))
P1=list((2, 0, 0.5))
P10=list((2, 0, 0.5))
## Se crea una lista de puntos
Puntos=[P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]
## Para encontrar que puntos son los mas cercanos se debe hallar la distancia entre los mismos
## Para hallar la longitud del segmento XY se aplica que se restan cada una de sus componentes, se elevan al cuadrado
## y se les saca la raiz, de este modo se crea un vector de estos datos y se obtiene el minimo.

## Se crea una lista vacia que vaya a contener todos los datos de las distancias
dist=[]
## Nos piden que se determine cual es la pareja mas cercana de puntos, por lo tanto se creará una lista
## que vaya guardando los puntos evaluados y la pareja de puntos
pareval=[]

#Se recorre toda la lista de puntos determinando el punto x del segmento a evaluar
for x in Puntos:
    #Se recorre toda la lista de puntos determinando el punto x del segmento a evaluar
    for y in Puntos:
        #Se recorren las coordenadas de cada punto, del tamaño de cada punto
        #Como se restan entre ellos mismos, se debe poner la condicion de que sean diferentes uno de otro
        if x!=y:
            for coordenadas in range(len(P1)):
                #Se aplica la formula
                segmento=((x[0]-y[0])**2 + (x[1]-y[1])**2+(x[2]-y[2])**2)**(1/2)
                #print(segmento)
            #Lista de coordenadas
            pareval.append([x,y])
            #Lista de distancias
            dist.append([segmento])
## 
minimo=(min(dist))
#print(minimo)
#Para saber cual es la pareja de la distancia mas pequeña se ocupa index, este determina su ubicacion 
# Se evalua para el par evaluado
ptos=pareval[dist.index(minimo)]
#print(ptos)
## Para saber la etiqueta de cada par de numeros se utiliza nuevamente index
## Se agrega un 1 puesto la posicion se retrasa en 1, ya que el contador del for toma 
## la operacion de su mismo numero, retrasandola en 1 posicion
## Se debe tener en STR
cual=("la pareja de puntos es: "+"P"+str(Puntos.index(ptos[0])+1)+"-"+"P"+str(Puntos.index(ptos[1])+1))
parCercano="P"+str(Puntos.index(ptos[0])+1)+"-"+"P"+str(Puntos.index(ptos[1])+1)
#print("parCercano = ",parCercano)

#print(cual)
        
        

        #Se recorre las coordenadas de cada punto
      


#------------------------ EJERCICIO 2 --------------------------------
"""
Cree las siguientes listas utilizando el ciclo while: lista1 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
   lista2 = [100, -1, 99, -1, 98, -1, 97, -1, 96, -1, ... 3, -1, 2, -1, 1, -1]
   lista3 = [2, 4, 5, 6, 8, 10,12, 14,15, 16,18, 20, 22, 24, 25 ... 592, 594, 595 ,596 ,598, 600]
Después de lograr los listados, almacenelos de la siguiente manera:
listaDeListas = [lista1, lista2, lista3]
"""
#print("-----------------Ejercicio 2--------------")
#print(" ")
#print("Creando la lista 1")
#lista0 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
#print("La longitud de la primera lista es",len(lista0)," por lo tanto se crea la lista de esa longitud")
#print(" ")
i=14
while i>0:    
    i-=1
    if i!=1:
        lista1=print("1,","-1",end=", ")

#print(" ")
#
#print(" ")
#print("Creando la lista 2")
#print(" ")
k=101
while k>1:
    k-=1
    lista2=print(k,-1,end=" ")
#print(" ")
#i=0
#while i<=27:
#    print(i,end="")
#rint("Creando la lista 3")
#print(" ")
n=0
while n<600:
    n+=2
    lista3=print(n,end=" ")

listadelistas=[lista1,lista2,lista3]

#
#print(" ")
#print(" ")
#
#print("------------------------ EJERCICIO 3 --------------------------------")

#Se ordenan los datos que se dan en el ejercicio
N1=list((1.0, 1.1, 2.3, 1.1 ))
N2=list((3.1, 3.1, 1.2, 3.0 ))
N3=list((5.0 ,4.0 ,2.5 ,5.0))
N4=list((3.1 ,1.0 ,2.6 ,1.0))
N5=list((3.2 ,4.0 ,1.1 ,3.0))
N6=list((5.0 ,5.0 ,5.0 ,3.9))
N7=list((3.4 ,4.0 ,2.6 ,3.2))
N8=list((2.0 ,2.2 ,2.1 ,4.2))
N9=list((3.7 ,4.1 ,4.7 ,4.0))
N10=list((4.1, 4.7, 4.4, 5.0))
N11=list((5.0, 5.0, 1.0, 3.2))
N12=list((5.0, 4.2, 2.1, 5.0))
N13=list((3.2, 4.1, 2.2, 3.3))
calificaion=[]# creacion de lista con notas con porcentajes ya aplicados
estudiante=[] #creacion de lista con las notas y el codigo de estudiante
#Se crea una nueva lista con los conjuntos de datos dados.
codigo=[]
notas=[N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12,N13]
multi=[0.1,0.2,0.15,0.2]

for individual in notas:
    total=0
    for x in range(1):
        calificaion=list(map(lambda x, y: x*y, individual,multi))
        #print(calificaion)
        a=sum(calificaion)
        estudiante.append(a)
        codigo.append([a,individual])     
pasa=[]
no_se_sabe=[]
[pasa.append(x) for x in estudiante if x>=3]     
paso=(len(pasa))
#rint("Aunque saque la nota más baja, pasan ", paso ," estudiantes")

[no_se_sabe.append(x) for x in estudiante if x<=3]
#print(no_se_sabe)
#print(len(no_se_sabe))
#Se suma 0.35*5=1.75 que seria la maxima nota que puede sacar para pasar la materia
xd=[]
for v in no_se_sabe:
    no_se_sabe=v+1.75
    xd.append(no_se_sabe)
#print(xd)

pasaa=[]
no_pasa=[]
[pasaa.append(x) for x in xd if x>=3] 
#print(pasaa)    
pas0=(len(pasaa))
#print("Si logra sacar la nota mas alta, pasan ", pas0 ," estudiantes")

[no_pasa.append(x) for x in xd if x<=3]
pas1=(len(no_pasa))
#print("Si logra sacar la nota mas alta, no pasan ", pas1 ," estudiantes")
#print(" ")
estudiantes=[pas1,paso,pas0]
#print("------------------------ EJERCICIO 5 --------------------------------")
#print(" ")
## SE ARREGLAN TODOS LOS DATOS DADOS
 
S001=(20, 22, 30, 2, 40 ,20 ,3 )
S002=(31, 14, 32, 15, 13 ,20 ,11)
S010=(24, 32, 40, 9, 12 ,50 ,13)
S020=(42, 12, 33, 24, 22 ,32 ,23)
S021=(51, 21, 25, 10, 19 ,14 ,2 )
S022=(22, 31, 51, 21, 35 ,15 ,11)
S023=(21, 36, 22, 32, 39 ,32 ,15)
S024=(22, 33, 41, 21, 43 ,31 ,36)
S025=(33, 31, 20, 42, 33 ,42 ,35)
S031=(22, 47, 5 ,28, 37 ,31 ,32)
S032=(24, 38, 33, 21, 41 ,31 ,16)
S033=(21, 18, 32, 37, 39 ,22 ,12)
S041=(33, 31, 21, 21, 33 ,39 ,25)
S042=(25, 39, 20, 48, 15 ,30 ,32)
S043=(27, 32, 29, 28, 37 ,35 ,16)
S121=(24, 12, 31, 21, 39 ,32 ,13)
S122=(31, 31, 50, 22, 13 ,30 ,21)
S123=(23, 35, 35, 39, 31 ,19 ,19)
S351=(26, 36, 39, 27, 35 ,32 ,16)
S352=(25, 31, 21, 21, 25 ,37 ,15)
S353=(23, 34, 35, 32, 37 ,20 ,49)
S368=(31, 14, 29, 39, 25 ,37 ,16)
S369=(26, 31, 31, 27, 37 ,32 ,41)
S461=(40, 42, 23, 11, 21 ,15 ,19)
S466=(27, 31, 39, 21, 31 ,32 ,25)
S469=(38, 32, 19, 29 ,35 ,50, 16)

empleados=[S001, S002, S010, S020, S021, S022, S023, S024, S025, S031, S032, S033, S041, S042, S043, S121, S122, S123, S351, S352, S353, S368, S369, S461, S466,S469,]
nombres=["S001","S002,","S010","S020","S021","S022","S023","S024","S025","S031","S032","S033","S041","S042,","S043","S121,","S122","S123","S351","S352","S353","S368","S369","S461","S466","S469"]
bono=[2500,2800,2400,1750,1750,2400,1800]

ganancia=[]
ganancia1=[]
cuales=[]
for vendedor in empleados:
    for x in range(1):
        total=list(map(lambda x, y: x*y, vendedor,bono))
        #print(calificaion)
        b=sum(total)
        ganancia1.append(b)
        ganancia.append(b)
        cuales.append([b,vendedor])
codigosAltosSalario=[]
for l in range(3):
    mejores=max(ganancia)
    codigosAltosSalario.append(mejores)
    eliminar=ganancia.remove(mejores)

#print(codigosAltosSalario)
#a=codigosAltosSalarios[0]
#o=codigosAltosSalarios[1]
#p=codigosAltosSalarios[2]
posicion2=ganancia1.index(codigosAltosSalario[1])
posicion1=ganancia1.index(codigosAltosSalario[0])
posicion3=ganancia1.index(codigosAltosSalario[2])
#print(posicion1)
#print(posicion2)
#print(posicion3)
#print(ganancia)
#print(ganancia1)
#quien=cuales[ganancia1.index(codigosAltosSalarios)]
#print(cuales)
#print("los empleados con mayor salario fueron: ",nombres[posicion1],nombres[posicion2],nombres[posicion3])
codigosAltosSalarios=[nombres[posicion1],nombres[posicion2],nombres[posicion3]]
