import random
import sqlite3

conexion = sqlite3.connect("piedra_papel_tijera.db")
cursor = conexion.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jugador TEXT NOT NULL,
        eleccion_jugador TEXT NOT NULL,
        eleccion_computadora TEXT NOT NULL,
        resultado TEXT
    )
    """
)

opciones = ["piedra", "papel", "tijera"]

jugador = input("Escribe tu nombre: ").strip()

while True:
    eleccion_jugador = input("Elige una opción (piedra, papel o tijera): ").strip().lower()
    if eleccion_jugador in opciones:
        break
    print("Opción inválida. Intenta de nuevo.")

eleccion_computadora = random.choice(opciones)

if eleccion_jugador == eleccion_computadora:
    resultado = "Empate"
elif (
    (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
    (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
    (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
):
    resultado = "Ganaste"
else:
    resultado = "Perdiste"

print(f"Tu elección: {eleccion_jugador}")
print(f"La computadora eligió: {eleccion_computadora}")
print(f"Resultado: {resultado}")

cursor.execute(
    "INSERT INTO resultados (jugador, eleccion_jugador, eleccion_computadora, resultado) VALUES (?, ?, ?, ?)",
    (jugador, eleccion_jugador, eleccion_computadora, resultado),
)
conexion.commit()
conexion.close()