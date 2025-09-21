#EJERCICIO 3
import random   
# Generar 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
# Separar en pares e impares
pares=[]
impares=[]
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Números generados:", numeros)
for n in numeros:
    print(n, end=" ")
print()
# Mostrar pares e impares y su cantidad
print("Números pares:", pares)
for p in pares:
    print(p, end=" ")
print("/nCantidad de números pares:", len(pares))

print("Números impares:", impares)
for ip in impares:
    print(ip, end=" ")
print("/nCantidad de números impares:", len(impares))