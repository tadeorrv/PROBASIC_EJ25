#Ejercicio 16
cadena = input("Introduce una cadena de texto: ")
vocales = 0
consonantes = 0
for char in cadena:
    char = char.lower()
    if char in 'aeiou':
        vocales += 1
    elif char.isalpha():
        consonantes += 1
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")