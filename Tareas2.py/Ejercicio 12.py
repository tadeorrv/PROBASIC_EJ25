#Ejercicio 12
n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: "))
if n1>n2 and n1>n3:
    print(n1,"es el mayor")
if n2>n1 and n2>n3:
    print(n2,"es el mayor")
if n3>n1 and n3>n2:
    print(n3,"es el mayor")