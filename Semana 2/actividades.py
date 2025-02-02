#Problema 1
print("hola mundo")

#Problema 2
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
print("adicion= ",a+b)
print("sustraccion= ",a-b)
print("multiplicacion= ",a*b)
print("division= ",a/b)

#Problema 3
num=int(input("ingrese el numero: "))
fact=1
for i in range(1, num+1):
    fact*=i
print("el factorial de ",num, "es: ",fact)

#Problema 4
n=int(input("ingrese la cantidad de numeros: "))
a=0
b=1
for i in range(n):
   c=a+b
   a=b
   b=c
print(b)