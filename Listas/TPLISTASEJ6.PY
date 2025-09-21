#EJERCICIO 6
# Mover el último elemento al principio de la lista
numeros = list(range(1, 8))
print("Lista original:", numeros)
for n in numeros:
    print(n, end=" ")
print()
ultimo = numeros.pop(-1)
numeros.insert(0, ultimo)
print("Lista modificada:", numeros)