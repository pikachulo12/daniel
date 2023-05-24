# Historial de enfrentamientos entre River Plate y Flamengo en la Copa Libertadores 2019
enfrentamientos = [
    {"rival": "Flamengo", "local": "River Plate", "puntos_local": 2, "puntos_rival": 1},
    {"rival": "River Plate", "local": "Flamengo", "puntos_local": 1, "puntos_rival": 2},
    # Agrega más enfrentamientos aquí según la historia de la Copa Libertadores 2019
]

# Variables para los puntajes totales
river_puntaje = 0
flamengo_puntaje = 0

# Simulación de los partidos
for enfrentamiento in enfrentamientos:
    local = enfrentamiento["local"]
    rival = enfrentamiento["rival"]
    puntos_local = enfrentamiento["puntos_local"]
    puntos_rival = enfrentamiento["puntos_rival"]
    
    # Actualización de los puntajes totales
    if local == "River Plate":
        river_puntaje += puntos_local
        flamengo_puntaje += puntos_rival
    else:
        river_puntaje += puntos_rival
        flamengo_puntaje += puntos_local

# Imprimir resultados
print("Historia de enfrentamientos en la Copa Libertadores 2019 entre River Plate y Flamengo:")
for enfrentamiento in enfrentamientos:
    local = enfrentamiento["local"]
    rival = enfrentamiento["rival"]
    puntos_local = enfrentamiento["puntos_local"]
    puntos_rival = enfrentamiento["puntos_rival"]
    
    print(f"{local} {puntos_local} - {puntos_rival} {rival}")

print("\nPuntaje total:")
print(f"River Plate: {river_puntaje} puntos")
print(f"Flamengo: {flamengo_puntaje} puntos")
