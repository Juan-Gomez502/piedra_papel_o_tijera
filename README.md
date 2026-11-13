# piedra_papel_o_tijera
Un repositorio para realizar la actividad de piedra papel 
Equipo:Rocio Farias Gigena, Patricio Rodriguez, Juan Simón Gomez y Alan Souberbielle

No cumple con el requisito de clases en archivos separados. Todo está en piedra_papel_o_tijera.py.

Clases y objetos propios:	No define clases ni crea objetos propios.
Archivos separados:	Toda la implementación está en un único archivo Python.
Organización:	Mezcla ingreso de datos, menús, lógica del juego y consultas SQL.


Además:
1. Acepta nombres vacíos. Si se ingresa Enter o espacios, permite jugar y guarda las partidas sin nombre. Lo comprobé ejecutándolo.
2. Las estadísticas distinguen mayúsculas y minúsculas. «Juan» y «juan» se consideran jugadores diferentes, por lo que pueden quedar estadísticas separadas para la misma persona.
3. No permite cambiar de jugador durante la ejecución. Para ingresar otro nombre hay que cerrar y volver a ejecutar el programa.
4. El README está incompleto. Identifica al equipo, pero no explica cómo ejecutar el juego ni consultar las estadísticas.
5. Hay un archivo vacío sobrante, llamado piedra_papel_o_tijera, sin extensión.

La corrección principal es implementar las clases y separarlas en archivos, distribuyendo las responsabilidades del jugador, el juego y la base de datos. Repartir el código actual entre archivos, sin crear y utilizar clases, no cumpliría la consigna.
