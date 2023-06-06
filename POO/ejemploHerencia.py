class Deporte:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print("Nombre del deporte:", self.nombre)


class DeporteIndividual(Deporte):
    def __init__(self, nombre, jugador):
        super().__init__(nombre)
        self.jugador = jugador
    
    def mostrar_jugador(self):
        print("Jugador:", self.jugador)


class DeporteColectivo(Deporte):
    def __init__(self, nombre, equipo):
        super().__init__(nombre)
        self.equipo = equipo
    
    def mostrar_equipo(self):
        print("Equipo:", self.equipo)


class DeporteColectivoConPelota(DeporteColectivo):
    def __init__(self, nombre, equipo, tipo_pelota):
        super().__init__(nombre, equipo)
        self.tipo_pelota = tipo_pelota
    
    def mostrar_tipo_pelota(self):
        print("Tipo de pelota:", self.tipo_pelota)


# Ejemplo de uso
futbol = DeporteColectivoConPelota("Fútbol", "11 jugadores por equipo", "Balón de fútbol")
futbol.mostrar_nombre()
futbol.mostrar_equipo()
futbol.mostrar_tipo_pelota()

tenis = DeporteIndividual("Tenis", "2 jugadores")
tenis.mostrar_nombre()
tenis.mostrar_jugador()
