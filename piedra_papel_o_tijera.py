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

computadora = random.choice (opciones)

if eleccio_jugador == computadora:
    resultado = "Empate"

    elif (
        (eleccion_jugador == "piedra" and computadora == "tijera") or
        (eleccion_jugador == "papel" and computadora == "piedra") or 
        (eleccion_jugador == "tijera" and computadora == "papel") or

    )
        resultado = "ganaste"
    
    else: 
        resultado = "perdiste"