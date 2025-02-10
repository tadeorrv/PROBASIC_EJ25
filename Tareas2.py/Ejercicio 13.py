#Ejercicio 13
temperatura = float(input("Introduce la temperatura: "))
escala = input("Introduce la escala de la temperatura (Celsius, Fahrenheit, Kelvin): ")
if escala.lower() == 'celsius':
    fahrenheit = (temperatura * 9/5) + 32
    kelvin = temperatura + 273.15
    print(f"{temperatura}°C es igual a {fahrenheit}°F y {kelvin} K.")
    
elif escala.lower() == 'fahrenheit':
    celsius = (temperatura - 32) * 5/9
    kelvin = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura}°F es igual a {celsius}°C y {kelvin} K.")
    
elif escala.lower() == 'kelvin':
    celsius = temperatura - 273.15
    fahrenheit = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura} K es igual a {celsius}°C y {fahrenheit}°F.")
    
else:
    print("Escala no válida")