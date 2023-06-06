class Cola(list):
    def encolar(self, elemento):
        self.append(elemento)

    def desencolar(self):
        if self:
            return self.pop(0)
        return "La cola está vacía"

# Crear una instancia de la cola
cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

while cola:
    elemento = cola.desencolar()
    print("Elemento desencolado:", elemento)

if not cola:
    print("La cola está vacía")
else:
    print("La cola no está vacía")