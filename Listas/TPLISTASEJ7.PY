#EJERCICIO 7
# Datos de temperaturas mínimas y máximas para cada día de la semana
temperaturas = [
    [15, 25],  # Lunes
    [12, 22],  # Martes
    [10, 24],  # Miércoles
    [14, 30],  # Jueves
    [18, 30],  # Viernes
    [20, 32],  # Sábado
    [19, 29]   # Domingo
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# --- Calcular promedios ---
suma_minimas = 0
suma_maximas = 0

for temp_dia in temperaturas:
    suma_minimas += temp_dia[0]  # Acumula la temperatura mínima (índice 0)
    suma_maximas += temp_dia[1]  # Acumula la temperatura máxima (índice 1)

promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

print(f"El promedio de las temperaturas mínimas es: {promedio_minimas:.2f}°C")
print(f"El promedio de las temperaturas máximas es: {promedio_maximas:.2f}°C")

# --- Calcular mayor amplitud térmica ---
mayor_amplitud = -1
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima
    
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[i]

print(f"El día con la mayor amplitud térmica fue el {dia_mayor_amplitud} con {mayor_amplitud}°C.")