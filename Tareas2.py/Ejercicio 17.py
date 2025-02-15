#Ejercicio 17
class EstructurasDeDatos:
    class Pila:
        def __init__(self):
            self.items = []
        
        def esta_vacia(self):
            return len(self.items) == 0
        
        def apilar(self, item):
            self.items.append(item)
        
        def desapilar(self):
            if not self.esta_vacia():
                return self.items.pop()
            return None
        
        def cima(self):
            if not self.esta_vacia():
                return self.items[-1]
            return None
        
        def tamanio(self):
            return len(self.items)

        def __str__(self):
            return str(self.items)

    class Cola:
        def __init__(self):
            self.items = []
        
        def esta_vacia(self):
            return len(self.items) == 0
        
        def encolar(self, item):
            self.items.append(item)
        
        def desencolar(self):
            if not self.esta_vacia():
                return self.items.pop(0)
            return None
        
        def frente(self):
            if not self.esta_vacia():
                return self.items[0]
            return None
        
        def tamanio(self):
            return len(self.items)

        def __str__(self):
            return str(self.items)

    class ListaEnlazada:
        class Nodo:
            def __init__(self, dato):
                self.dato = dato
                self.siguiente = None

        def __init__(self):
            self.cabeza = None
        
        def esta_vacia(self):
            return self.cabeza is None
        
        def agregar_inicio(self, dato):
            nuevo_nodo = self.Nodo(dato)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        
        def eliminar_inicio(self):
            if not self.esta_vacia():
                self.cabeza = self.cabeza.siguiente
        
        def recorrer(self):
            elementos = []
            actual = self.cabeza
            while actual:
                elementos.append(actual.dato)
                actual = actual.siguiente
            return elementos
        
        def __str__(self):
            return "->".join(map(str, self.recorrer()))
    
