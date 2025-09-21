#EJERCICIO 9
# 1.Se crea una lista de listas de 3x3 con guiones.
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# --- 2. Lógica del Juego ---
jugador_actual = "X" # El jugador X siempre empieza

# El juego tiene un máximo de 9 turnos
for turno in range(9):
    # -- Mostrar el tablero actual --
    print("\n--- TA - TE - TI ---")
    for fila in tablero:
        print(" ".join(fila))
    print("-------------------")
    
    print(f"Turno del jugador '{jugador_actual}'")
    
    # Pedir al usuario que ingrese su jugada
    # Se resta 1 porque las listas en Python empiezan en el índice 0
    fila_ingresada = int(input("Ingresa la fila (1, 2, o 3): ")) - 1
    columna_ingresada = int(input("Ingresa la columna (1, 2, o 3): ")) - 1
    
    # Validar si la casilla está vacía antes de colocar la ficha
    if tablero[fila_ingresada][columna_ingresada] == "-":
        tablero[fila_ingresada][columna_ingresada] = jugador_actual
        
        # Cambiar de jugador para el siguiente turno
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("¡Esa casilla ya está ocupada! Pierdes el turno.")
        # El jugador pierde el turno, no se cambia de jugador

# --- 3. Mostrar el tablero final al terminar el juego ---
print("\n--- TABLERO FINAL ---")
for fila in tablero:
    print(" ".join(fila))
print("-------------------")
print("¡Juego terminado!")