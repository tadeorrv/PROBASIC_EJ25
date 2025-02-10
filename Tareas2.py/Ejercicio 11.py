#Ejercicio 11 
def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    if palabra == palabra[::-1]:
        return True
    else:
        return False
palabra1 = input("Introduce una palabra: ")
if palindromo(palabra1):
    print(f"La palabra '{palabra1}' es un palíndromo.")
else:
    print(f"La palabra '{palabra1}' no es un palíndromo.")


