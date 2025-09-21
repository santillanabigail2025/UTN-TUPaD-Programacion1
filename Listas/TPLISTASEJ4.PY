#EJERCICIO 4
# Eliminar duplicados de una lista
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicados = []
for d in datos:
    if d not in sin_duplicados:
        sin_duplicados.append(d)
print("Lista original:", datos) #Muestra la lista original
for d in datos:
    print(d, end=" ")
print()
print("Lista sin duplicados:", sin_duplicados)  
for d in sin_duplicados:
    print(d, end=" ")
print()