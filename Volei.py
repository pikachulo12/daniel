class JuegoVoleibol:
    def __init__(self):
        self.puntaje_equipo_a = 0
        self.puntaje_equipo_b = 0

    def anotar_equipo_a(self, puntos):
        self.puntaje_equipo_a += puntos

    def anotar_equipo_b(self, puntos):
        self.puntaje_equipo_b += puntos

    def obtener_puntaje_equipo_a(self):
        return self.puntaje_equipo_a

    def obtener_puntaje_equipo_b(self):
        return self.puntaje_equipo_b

# Ejemplo de uso:
juego = JuegoVoleibol()

# Anotar 3 puntos para el equipo A
juego.anotar_equipo_a(3)

# Anotar 2 puntos para el equipo B
juego.anotar_equipo_b(2)

# Obtener el puntaje actual de cada equipo
puntaje_equipo_a = juego.obtener_puntaje_equipo_a()
puntaje_equipo_b = juego.obtener_puntaje_equipo_b()

print("Puntaje equipo A:", puntaje_equipo_a)
print("Puntaje equipo B:", puntaje_equipo_b)
