#Ejercicio 15
anio = int(input("Introduce un año para verificar si es bisiesto: "))
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")