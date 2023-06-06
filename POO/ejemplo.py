class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self) -> str:
        return f"Soy {self.nombre}, tengo {self.edad} y estudio {self.carrera}"

    def habilidad(self):
        return f"mi habilidad es: ?"

estudiante1 = Estudiante("Gabriel", 21, "TICS")
print(estudiante1)
print(estudiante1.habilidad())
