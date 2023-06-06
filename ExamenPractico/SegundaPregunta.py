class Pila(list):
    def esta_vacia(self):
        return not bool(self)

# Crear una instancia de la pila
pila = Pila()

pila.extend([1, 2, 3, 4, 5])

while not pila.esta_vacia():
    elemento = pila.pop()
    print("Elemento desapilado:", elemento)

if pila.esta_vacia():
    print("La pila está vacía")
else:
    print("La pila no está vacía")