#Ejercicio 19
from random import randint
listP=list()
listN=list()
elementos=int(input("Introduce la cantidad de elementos: "))
for cont in range(-elementos,elementos):
    if cont<0:
        listN.append(randint(-100,0))
    elif cont>0:
        listP.append(randint(0,100))
    else:
        listP.append(randint(0,1))

listaCompleta=listN+listP
listP.extend(listN)
print(listP)
num=int(input("Ingrese el numero a buscar: "))
for int in listaCompleta:
    if int==num:
        print("el numero se encontraba en la posicion",listaCompleta.index(int))
    else:
        print("El numero no se encuentra en la lista")
        break