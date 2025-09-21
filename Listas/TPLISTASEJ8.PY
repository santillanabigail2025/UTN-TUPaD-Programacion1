#EJERCICIO 8
notas = [
    [7, 8, 9], 
    [6, 5, 4], 
    [8, 9, 10], 
    [3, 4, 5],
    [8, 9, 7]
    ]
for i   in range(len(notas)):
   promedio = sum(notas[i]) / len(notas[i])
   print(f"El promedio del estudiante {i + 1} es: {promedio:.2f}")

num_alumnos = len(notas)
num_materias = len(notas[0])

# Bucle externo: recorre las columnas (cada materia)
for j in range(num_materias):
    suma_materia = 0
    # Bucle interno: recorre las filas para sumar su nota en esa materia
    for i in range(num_alumnos):
        suma_materia += notas[i][j] # Se accede a la nota del estudiante 'i' en la materia 'j'
    promedio = suma_materia / num_alumnos
    print(f"El promedio de la materia {j + 1} es: {promedio:.2f}")