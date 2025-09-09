#EJERCICIO 1
for i in range(101):
    print(i)

#EJERCICIO 2
try:
    numero = int(input("Ingresa un número entero para contar sus dígitos: "))
    # Convierte el número a cadena de texto para contar los caracteres
    cantidad_digitos = len(str(abs(numero)))
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

#EJERCICIO 3
try:
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
     # Asegura que el rango sea de menor a mayor
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1 
    suma = 0
    # Se suman los números entre los dos valores, excluyendo los extremos
    for i in range(valor1 + 1, valor2):
        suma += i
    print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números enteros.")

#EJERCICIO 4
total = 0
print("Ingresa números para sumarlos. Ingresa 0 para detener el programa.")
while True:
    try:
        numero = int(input("Ingresa un número: "))
        if numero == 0:
            break 
        total += numero
        print(f"Total acumulado: {total}")   
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
print(f"\nSuma final de todos los números ingresados: {total}")

#EJERCICIO 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False
print("¡Adivina el número secreto! Está entre 0 y 9.")
while not adivinado:
        adivinanza = int(input("Tu suposición: "))
        intentos += 1
        if adivinanza < numero_secreto:
            print("Demasiado bajo. ¡Inténtalo de nuevo!")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicitaciones! Adivinaste el número {numero_secreto}.")
            adivinado = True        
print(f"Te tomó {intentos} intentos para adivinar el número.")

#EJERCICIO 6
for i in range(100, -1, -2):
    print(i)

#EJERCICIO 7
try:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        suma = 0
        for i in range(numero + 1):
            suma += i
        print(f"La suma de todos los números desde 0 hasta {numero} es: {suma}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

#EJERCICIO 8
CANTIDAD_NUMEROS = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Ingresa {CANTIDAD_NUMEROS} números enteros.")
for i in range(CANTIDAD_NUMEROS):
    try:
        numero = int(input(f"Ingresa el número {i + 1}: "))
        # Clasifica el número
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1    
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1      
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        # Se decrementa el contador para que se le pida el número de nuevo
        i -= 1
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#EJERCICIO 9
CANTIDAD_NUMEROS = 100
suma = 0
print(f"Ingresa {CANTIDAD_NUMEROS} números enteros para calcular su media.")
for i in range(CANTIDAD_NUMEROS):
    try:
        numero = int(input(f"Ingresa el número {i + 1}: "))
        suma += numero
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        # Se decrementa el contador para que se le pida el número de nuevo
        i -= 1
media = suma / CANTIDAD_NUMEROS
print(f"\nLa media de los números ingresados es: {media:.2f}")

#EJERCICIO 10
numero_str = input("Ingresa un número para invertir sus dígitos: ")
# Invierte la cadena de texto usando slicing
numero_invertido = numero_str[::-1]
print(f"El número invertido es: {numero_invertido}")