#Ejercicio 1
def factorial_recursivo(n):
    # Caso Base: El factorial de 0 es 1.
    if n == 0:
        return 1
    # Paso Recursivo: n! = n * (n-1)!
    else:
        return n * factorial_recursivo(n - 1)
numero_usuario = int(input("Ingresa un número entero para calcular factoriales: "))

print(f"\nCalculando los factoriales desde 1 hasta {numero_usuario}:\n")

# Usamos un bucle 'for' para iterar desde 1 hasta el número del usuario
# range(1, numero_usuario + 1) asegura que incluyamos el número final
for i in range(1, numero_usuario + 1):
    # Calculamos el factorial de 'i' usando nuestra función recursiva
    resultado = factorial_recursivo(i)
    print(f"El factorial de {i} es {resultado}")

#Ejercicio 2
def fibonacci_recursivo(n):
    # Caso Base 1: F(0) = 0
    if n == 0:
        return 0
    # Caso Base 2: F(1) = 1
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
# Solicitud al usuario
posicion = int(input("Ingresa hasta qué posición de la serie deseas ver: "))

print(f"\n--- Serie de Fibonacci hasta la posición {posicion} ---")

# Usamos un bucle 'for' para mostrar la serie completa.
a, b = 0, 1
serie_completa = []

# Iteramos 'posicion + 1' veces para incluir F(0) hasta F(n)
for _ in range(posicion + 1):
    serie_completa.append(a)
    # Actualizamos los valores de la serie
    a, b = b, a + b
# Imprimimos la lista con la serie
print(serie_completa)
#Mostramos el valor final usando la función recursiva
valor_final = fibonacci_recursivo(posicion)
print(f"\nEl valor final en la posición {posicion} (calculado recursivamente) es: {valor_final}")

#Ejercicio 3
def potencia_recursiva(base, exponente):
    # Caso Base: n^0 = 1
    if exponente == 0:
        return 1
    # Paso Recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia_recursiva(base, exponente - 1)
    
# --- Algoritmo General ---
print("Calculadora de Potencia Recursiva")
# 1. Solicitar al usuario la base y el exponente
base_usuario = float(input("Ingresa el número base: "))
# Usamos int() para el exponente, ya que la fórmula se basa en restar 1
exponente_usuario = int(input("Ingresa el exponente (entero no negativo): "))

# 2. Validamos la entrada
if exponente_usuario < 0:
    print("\nError: Esta función recursiva solo acepta exponentes 0 o positivos.")
else:
    resultado = potencia_recursiva(base_usuario, exponente_usuario)
    print(f"\nEl resultado de {base_usuario} elevado a la {exponente_usuario} es: {resultado}")

#Ejercicio 4
def decimal_a_binario(n):
    # Aseguramos que n sea un entero
    n = int(n)
    # Caso Base: Cuando el número a dividir es 0 o 1,su representación binaria es él mismo.
    if n < 2:
        return str(n)
    
    # Paso Recursivo:
    # 1. Obtenemos el cociente (la parte entera de la división)
    cociente = n // 2
    
    # 2. Obtenemos el residuo (el 0 o 1 que irá al final)
    residuo = n % 2
    
    # 3. Devolvemos la conversión del *cociente* + el *residuo* como string
    return decimal_a_binario(cociente) + str(residuo)

# --- Algoritmo de prueba ---

# Solicitamos el número al usuario
numero_decimal = int(input("Ingresa un número entero positivo: "))

if numero_decimal < 0:
    print("El número debe ser positivo.")
else:
    # Llamamos a la función recursiva
    resultado_binario = decimal_a_binario(numero_decimal)
    print(f"El número {numero_decimal} en binario es: {resultado_binario}")

#Ejercicio 5
def es_palindromo(palabra):
    # --- 1. Caso Base ---
    # Si la palabra tiene 1 letra o está vacía, es un palíndromo.
    if len(palabra) <= 1:
        return True
    
    # --- 2. Caso de Falla ---
    # Si la primera letra es distinta a la última, no es palíndromo.
    if palabra[0] != palabra[-1]:
        return False
        
    # --- 3. Paso Recursivo ---
    # Si son iguales, llamamos a la función con la palabra "interna".
    return es_palindromo(palabra[1:-1])

# --- Algoritmo principal ---

print("--- Verificador de Palíndromos Recursivo ---")
# 1. Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

# 2. Llamar a la función con esa palabra
es_un_palindromo = es_palindromo(palabra_ingresada)

# 3. Mostrar el resultado (True o False)
print(f"¿La palabra '{palabra_ingresada}' es palíndromo? {es_un_palindromo}")

#Ejercicio 6
def suma_digitos(n):
    # --- 1. Caso Base ---
    # Si 'n' tiene un solo dígito (es menor que 10), la suma es 'n' mismo.
    if n < 10:
        return n
    # --- 2. Paso Recursivo ---
    # Si 'n' tiene más de un dígito:
    # 1. Obtenemos el último dígito (ej: 1234 % 10 = 4)
    # 2. Obtenemos el resto del número (ej: 1234 // 10 = 123)
    # 3. Retornamos el último dígito + la suma de los dígitos del resto
    else:
        return (n % 10) + suma_digitos(n // 10)

# --- Algoritmo de prueba ---
print("--- Suma de Dígitos Recursiva ---")
numero = int(input("Ingresa un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7
def contar_bloques(n):
    # --- 1. Caso Base ---
    # Si la base es 1, la pirámide tiene un solo bloque.
    if n == 1:
        return 1   
    # --- 2. Paso Recursivo ---
    # El total es 'n' (la capa base) + el total de la pirámide
    # que se construiría sobre ella (cuya base es n-1).
    else:
        return n + contar_bloques(n - 1)

# --- Algoritmo de prueba ---

print("--- Calculadora de Bloques de Pirámide ---")
numero_base = int(input("Ingresa el número de bloques en el nivel más bajo (n): "))
# Validamos que sea positivo
if numero_base <= 0:
    print("El número debe ser un entero positivo.")
else:
    # Llamamos a la función recursiva
    total = contar_bloques(numero_base)
    print(f"\nPara una base de {numero_base} bloques,")
    print(f"se necesitan un total de {total} bloques para toda la pirámide.")

#Ejercicio 8
def contar_digito(numero, digito):
    # --- 1. Caso Base ---
    # Si el número tiene un solo dígito.
    if numero < 10:
        # Devuelve 1 si son iguales, 0 si no
        return 1 if numero == digito else 0
    
    # --- 2. Paso Recursivo ---
    # Comparamos el último dígito
    if numero % 10 == digito:
        # Coincide: Contamos 1 y sumamos el conteo del resto del número
        return 1 + contar_digito(numero // 10, digito)
    else:
        # No coincide: Solo devolvemos el conteo del resto del número
        return contar_digito(numero // 10, digito)

# --- Algoritmo principal ---

print("--- Contador de Dígitos Recursivo ---")

# 1. Pedir el número entero
numero_ingresado = int(input("Ingresa un número entero positivo: "))
# 2. Pedir el dígito a contar
digito_ingresado = int(input("Ingresa el dígito que quieres contar (0-9): "))

# 3. Validamos entradas
if numero_ingresado < 0:
    print("Error: El número debe ser positivo.")
elif not (0 <= digito_ingresado <= 9):
    print("Error: El dígito debe estar entre 0 y 9.")
else:
    total = contar_digito(numero_ingresado, digito_ingresado)
    print(f"\nEl dígito {digito_ingresado} aparece {total} veces en el número {numero_ingresado}.")