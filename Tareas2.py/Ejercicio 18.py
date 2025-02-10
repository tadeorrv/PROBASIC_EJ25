#Ejercicio 18
print("Resolver la ecuación cuadrática ax^2 + bx + c = 0")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

if a == 0:
    print("El valor de 'a' no puede ser 0 en una ecuación cuadrática.")
else:
    discriminante = b**2 - 4*a*c
    
    solucion1 = (-b + (discriminante**1/2)) / (2 * a)
    solucion2 = (-b - (discriminante**1/2)) / (2 * a)
    print(f"Las soluciones son: {solucion1} y {solucion2}")