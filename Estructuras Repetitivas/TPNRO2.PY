#Ejercicio 1
Edad= int(input("Ingrese su edad:"))
if (Edad >= 18):
    print("Es mayor de edad")

#Ejercicio 2
Nota =int(input("Ingrese su nota:"))
if (Nota >=6):
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
Num = int(input("Ingrese un numero:"))
if (Num% 2 ==0):
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercio 4
Edad1= int(input("Ingrese su edad:"))
if (Edad1 < 12):
    print("Sos un niño")
elif (Edad1 >= 12 and Edad1 < 18):
    print("Sos un adolescente")
elif (Edad1 >= 18 and Edad1 < 30):
    print("Sos adulto/joven")
else:
    print("Sos adulto")

#Ejercicio 5
Contraseña= input("Ingrese una contraseña:")
if (len(Contraseña) >= 8) and (len(Contraseña)<=14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
import statistics
from collections import Counter
numeros_aleatorios= [random.randint(1, 100) for i in range (50)]
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
conteo = Counter(numeros_aleatorios)
moda = conteo.most_common(1)[0][0]
if media > mediana > moda:
    resultado_sesgo = "Hay sesgo POSITIVO (asimétrica a la derecha)."
elif media < mediana < moda:
    resultado_sesgo = "Hay sesgo NEGATIVO (asimétrica a la izquierda)."
else:
    resultado_sesgo = "NO hay sesgo (distribución simétrica)."
print(f"Lista de números generada:\n{numeros_aleatorios}\n")
print("Medidas de tendencia central")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}\n")
print("Análisis de Sesgo")
print(f"Comparación: Media ({media:.2f}) vs. Mediana ({mediana:.2f})")
print(f"Resultado: {resultado_sesgo}")

#Ejercicio 7
vocales = "aeiouáéíóú"
frase = input("Por favor, ingresa una frase: ").strip()
ultimo_caracter = frase[-1].lower()
if ultimo_caracter in vocales:
    print(f"{frase}!")
else:
    print(frase)

#Ejercicio 8
nombre = input("Por favor, ingresa tu nombre: ").strip()
print("\nElige una opción para formatear tu nombre:")
print("1. Si quiere su nombre en mayúsculas. (Usando .upper())")
print("2. Si quiere su nombre en minúsculas. (Usando .lower())")
print("3. Si quiere su nombre con la primera letra mayúscula. (Usando .title())")
opcion = input("Ingresa el número de tu elección (1, 2 o 3): ")
print("\nResultado")
if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
 print(nombre.title())
else:
     print("Opción no válida. Por favor, ejecuta de nuevo el programa y elige 1, 2 o 3.")

#Ejercicio 9
magnitud_str = input("Por favor, ingrese la magnitud del terremoto: ")
Magnitud_Terremoto = float(magnitud_str)
if Magnitud_Terremoto < 3:
    categoria= "Muy leve (imperceptible)"
elif Magnitud_Terremoto < 4:
   categoria= "Leve (ligeramente perceptible)"
elif Magnitud_Terremoto < 5:
    categoria= "Moderado (sentido por personas, pero generalmente no causa daños)"
elif Magnitud_Terremoto < 6:
    categoria= "Fuerte (puede causar daños en estructuras débiles)"
elif Magnitud_Terremoto < 7:
    categoria= "Muy Fuerte (puede causar daños significativos)"
else:
    categoria= "Extremo (puede causar graves daños a gran escala)"
print(f"\nUna magnitud de {Magnitud_Terremoto} en la escala de Richter se clasifica como:")
print(f"-> {categoria}")

#Ejercicio 10
print("Este programa determina la estación del año según la fecha y el hemisferio.")
hemisferio_input = input("¿En qué hemisferio se encuentra? (N/S): ")
mes_input = input("Ingrese el mes del año (1-12): ")
dia_input = input("Ingrese el día del mes (1-31): ")
try:
    mes = int(mes_input)
    dia = int(dia_input)
    hemisferio = hemisferio_input.upper().strip()
    if hemisferio == 'N' or hemisferio == 'S':
        if 1 <= mes <= 12:
            if 1 <= dia <= 31:
                fecha_numerica = mes * 100 + dia
                estacion_norte = ""
                if 321 <= fecha_numerica <= 620:
                    estacion_note = "Primavera"
                elif 621 <= fecha_numerica <= 920:
                    estacion_norte = "Verano"
                elif 921 <= fecha_numerica <= 1220:
                    estacion_norte = "Otoño"
                else: # Si no es ninguna de las anteriores, es invierno
                    estacion_norte = "Invierno"
                if hemisferio == 'N':
                    estacion_final = estacion_norte
                else: # El hemisferio es 'S'
                    if estacion_norte == "Invierno":
                        estacion_final = "Verano"
                    elif estacion_norte == "Primavera":
                        estacion_final = "Otoño"
                    elif estacion_norte == "Verano":
                        estacion_final = "Invierno"
                    else: # Otoño en el norte
                        estacion_final = "Primavera"
                print(f"La estación para el día {dia} del mes {mes} en el hemisferio {hemisferio} es: {estacion_final}")
            else:
                print("\nError: El día debe ser un número entre 1 y 31.")
        else:
            print("\nError: El mes debe ser un número entre 1 y 12.")
    else:
        print("\nError: El hemisferio debe ser 'N' o 'S'.")
except ValueError:
    print("\nError: El mes y el día deben ser ingresados como números.")
