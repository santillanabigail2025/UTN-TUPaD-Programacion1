#Ejercicio 1
Notas = [7, 5, 4, 3, 8, 9, 7, 8, 10, 9]
print("Notas")
for n in Notas:
    print(n, end=" ")
    print()
#Promedio, nota mas alta y nota mas baja
Promedio = sum(Notas)/len(Notas)
print("El promedio es: ", Promedio)
print("Notas mas alta", max(Notas))
print("Notas mas baja", min(Notas))

