#Ejercicio 14
# Método de ordenamiento por burbuja 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Método de ordenamiento por inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Método de ordenamiento por selección 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    arr = list(map(int, input("Introduce una lista de números separados por espacios: ").split()))
    print("\nMétodos de Ordenamiento Disponibles:")
    print("1. Burbuja (Bubble Sort)")
    print("2. Inserción (Insertion Sort)")
    print("3. Selección (Selection Sort)")
    
    opcion = int(input("\nElige el número del método de ordenamiento: "))
    
    if opcion == 1:
        print("\nOrdenando con el método Burbuja...")
        sorted_arr = bubble_sort(arr)
    elif opcion == 2:
        print("\nOrdenando con el método Inserción...")
        sorted_arr = insertion_sort(arr)
    elif opcion == 3:
        print("\nOrdenando con el método Selección...")
        sorted_arr = selection_sort(arr)
    else:
        print("Opción no válida.")
        return
    
    print("Lista ordenada:", sorted_arr)
if __name__ == "__main__":
    main()