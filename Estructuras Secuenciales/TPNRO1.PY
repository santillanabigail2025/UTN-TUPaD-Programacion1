# Ejercicio1
print("hola mundo!")

# Ejercicio2
nombre= input("Ingrese su nombre:")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre= input("Ingrese su nombre:")
apellido= input("Ingrese su apellido:")
edad= input("Ingrese su edad:")
residencia= input("Ingrese su residencia:")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
import math
radio_circulo= float(input("Por favor, ingrese el radio de un circulo: "))
area_circulo= math.pi * (radio_circulo)**2
perimetro_circulo= 2 * math.pi * radio_circulo
print(f"El area de un circulo es de {area_circulo} y el perimetro es de {perimetro_circulo}.")

# Ejercicio 5
segundos= int(input("Ingrese los segundos: "))
hora= segundos/3600
print(f" {segundos} seg equivale a {hora} hs")

#Ejercicio 6
numero = int(input("Por favor, ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
 resultado= numero*i
 print(f"{numero} * {i} = {resultado}")

#Ejercicio 7
num1= int(input("Ingrese el primer numero entero distinto de 0:"))
num2= int(input("Ingrese el segundo numero entero distinto de 0:"))
suma= num1+num2
resta= num1-num2
multiplicacion= num1*num2
division= num1/num2
print(f"La suma de {num1} + {num2} es: {suma}")
print(f"La resta de {num1} - {num2} es: {resta}")
print(f"La multiplicación de {num1} * {num2} es: {multiplicacion}")
print(f"La división de {num1} / {num2} es: {division}")

#Ejercicio 8
altura= int(input("Ingrese su altura:"))
peso= float(input("Ingrese su peso:"))
IMC= peso/((altura/100)**2)
print(f"Tu indice de masa corporal es {IMC}")

#Ejercicio 9
celsius= float(input("Por favor, ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

#Ejercicio 10
num1= int(input("Inserte el primer numero: "))
num2= int(input("Inserte el segundo numero: "))
num3= int(input("Inserte el tercer numero:"))
promedio= (num1+num2+num3)/3
print(f"El promedio es {promedio}")