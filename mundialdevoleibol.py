# Registro de resultados de los partidos
resultados = {
    "Grupo A": [
        ("Brasil", "Italia", 3, 1),
        ("Estados Unidos", "Alemania", 3, 0),
        ("Italia", "Estados Unidos", 2, 3),
        ("Brasil", "Alemania", 3, 0),
        ("Italia", "Alemania", 3, 2),
        ("Brasil", "Estados Unidos", 3, 1)
    ],
    "Grupo B": [
        ("Rusia", "Polonia", 3, 2),
        ("Serbia", "Francia", 3, 1),
        ("Polonia", "Serbia", 0, 3),
        ("Rusia", "Francia", 3, 0),
        ("Polonia", "Francia", 2, 3),
        ("Rusia", "Serbia", 3, 1)
    ]
}

# Descripción de los equipos
equipos = {
    "Brasil": "Equipo de voleibol de Brasil, conocido por su técnica y juego poderoso.",
    "Italia": "Selección italiana de voleibol, con una sólida defensa y juego estratégico.",
    "Estados Unidos": "Equipo estadounidense de voleibol, destacado por su potencia y habilidad atlética.",
    "Alemania": "Selección alemana de voleibol, con un juego disciplinado y táctico.",
    "Rusia": "Equipo de voleibol de Rusia, reconocido por su fuerza física y bloqueo efectivo.",
    "Polonia": "Selección polaca de voleibol, con una destacada técnica y versatilidad en el ataque.",
    "Serbia": "Equipo serbio de voleibol, con una sólida defensa y potencia en el saque.",
    "Francia": "Selección francesa de voleibol, con jugadores hábiles y una estrategia de juego inteligente."
}

# Función para calcular los puntos de cada equipo en la fase de grupos
def calcular_puntos(resultados):
    puntos = {}
    for grupo, partidos in resultados.items():
        for equipo1, equipo2, set_equipo1, set_equipo2 in partidos:
            # Ganador del partido
            if set_equipo1 > set_equipo2:
                puntos[equipo1] = puntos.get(equipo1, 0) + 3
                puntos[equipo2] = puntos.get(equipo2, 0) + 0
            else:
                puntos[equipo1] = puntos.get(equipo1, 0) + 0
                puntos[equipo2] = puntos.get(equipo2, 0) + 3
    return puntos

# Calcular los puntos de cada equipo en la fase de grupos
puntos = calcular_puntos(resultados)

# Obtener el equipo con más puntos (ganador del campeonato)
ganador = max(puntos, key=puntos.get)

# Imprimir resultados y descripción del ganador
print("Resultados del último Campeonato Mundial de Voleibol:\n")
for grupo, partidos in resultados.items():
    print(f"
