#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo") 
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"
nombre = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)   

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
 print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
#Definicion Global de Variables
PI = 3.1416
#Definicion de las funciones    
def calcular_area_circulo(radio):
   return PI * radio ** 2
def calcular_perimetro_circulo(radio):
   return 2 * PI * radio
# --- Programa Principal ---
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")    
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
# Definición de la función
def segundos_a_horas(segundos):
  horas = segundos / 3600
  return horas
# --- Programa Principal ---
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#Ejercicio 6
# Definición de la función
def tabla_multiplicar(numero):
  print(f"Tabla de multiplicar del {numero}")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")   
# --- Programa Principal ---
numero= int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
# Definición de la función
def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  # Se comprueba que b no sea cero para evitar errores en la división
  division = a / b if b != 0 else "Indefinida (división por cero)"
  return (suma, resta, multiplicacion, division)
# --- Programa Principal ---
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
# Se llama a la función y se desempaqueta la tupla en variables
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#Ejercicio 8
# Definición de la función
def calcular_imc(peso, altura):
  #Calcula el Índice de Masa Corporal (IMC)
  return peso / (altura ** 2)
# --- Programa Principal ---
peso_usuario = float(input("Ingresa tu peso en kilogramos (kg): "))
altura_usuario = float(input("Ingresa tu altura en metros (m): "))
imc = calcular_imc(peso_usuario, altura_usuario)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
# Definición de la función
def celsius_a_fahrenheit(celsius):
#Convierte grados Celsius a Fahrenheit.
  return (celsius * 9/5) + 32
# --- Programa Principal ---
celsius_usuario = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius_usuario)
print(f"{celsius_usuario}°C equivalen a {fahrenheit:.2f}°F.")

#Ejercicio 10
# Definición de la función
def calcular_promedio(a, b, c):
  #Calcula el promedio de tres números.
  return (a + b + c) / 3
# --- Programa Principal ---
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")