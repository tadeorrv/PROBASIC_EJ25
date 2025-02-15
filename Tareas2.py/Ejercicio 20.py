#Ejercicio 20
class Busquedas:
    
    # Búsqueda Lineal
    
    def busqueda_lineal(lista, objetivo):
        for indice, valor in enumerate(lista):
            if valor == objetivo:
                return indice  # Retorna el índice donde se encuentra el valor
        return -1  # Retorna -1 si el valor no se encuentra
    
    # Búsqueda Binaria
    
    def busqueda_binaria(lista, objetivo):
        inicio = 0
        fin = len(lista) - 1
        
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if lista[medio] == objetivo:
                return medio  # Retorna el índice si el valor es encontrado
            elif lista[medio] < objetivo:
                inicio = medio + 1  # El objetivo está en la mitad derecha
            else:
                fin = medio - 1  # El objetivo está en la mitad izquierda
        
        return -1  # Retorna -1 si no encuentra el valor
