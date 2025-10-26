#EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
print(precios_frutas)
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300
print(precios_frutas)

#EJERCICIO 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
print(precios_frutas)

precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300
print(precios_frutas)

#ACTUALIZAR PRECIO DE LA FRUTA
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800
print(precios_frutas)

#EJERCICIO 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
print(precios_frutas)

precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300
print(precios_frutas)

#ACTUALIZAR PRECIO DE LA FRUTA
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800
print(precios_frutas)

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#EJERCICIO 4
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = telefono
consulta = input("Ingrese el nombre del contacto que desea consultar: ")
if consulta in contactos:
    print(f"El número de teléfono de {consulta} es {contactos[consulta]}")
else:
    print(f"El contacto {consulta} no se encuentra en la agenda.")

#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
unicas = set(palabras)
print ("Palabras únicas :" , unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Recuento de palabras:", recuento)

#EJERCICIO 6
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple (notas)
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")

#EJERCICIO 7
Parcial1 = {1, 2, 3, 4, 5}
Parcial2 = {4, 5, 6, 7, 8}

#parcial1 = {ana, juan, luis, maria, carla}
#parcial2 = {maria, carla, pablo, sofia, lucas}

ambos_parciales = Parcial1 & Parcial2
solo_uno = Parcial1 ^ Parcial2
al_menos_uno = Parcial1 | Parcial2
print("Alumnos que aprobaron ambos parciales:", ambos_parciales)
print("Alumnos que aprobaron solo uno de los parciales:", solo_uno)
print("Alumnos que aprobaron al menos uno de los parciales:", al_menos_uno)

#EJERCICIO 8
productos = {"manzana": 10 , "banana": 15, "naranja":8}
producto = input ("Ingrese el nombre del producto: ").strip().lower()
if producto in productos:
   print (f"El stock de {producto} es: {productos[producto]} unidades.")
   agregar = int(input ("Ingrese la cantidad a agregar: "))
   productos [producto] += agregar
   print (f"Nuevo stock de {producto} es: {productos[producto]} unidades.")
else:
   nuevo_stock = int(input ( "Producto nuevo. Ingrese la cantidad de stock inicial: "))
   productos [producto] = nuevo_stock
   print (f"El producto {producto} ha sido agregado con un stock de {nuevo_stock} unidades.")
print("Stock final de productos:", productos)

#EJERCICIO 9
agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "14:00"): "Cita con el dentista",
    ("miércoles", "09:00"):"Clase de yoga"}
dia = input ("Ingrese el día : ").strip().lower()
hora = input ("Ingrese la hora (formato HH:MM): ")
clave = (dia, hora)
if clave in agenda:
    print (f"Actividad programada: {agenda[clave]}")
else:
    print ("No hay actividades programadas para esa fecha y hora.")

#EJERCICIO 10
paises = {
         "Argentina": "Buenos Aires",
         "Brasil": "Brasilia",
         "Chile": "Santiago",}
invertido = {}
for pais, capital in paises.items():
    invertido[capital] = pais
print ("Diccinario Original:", paises)
print ("Diccionario Invertido:", invertido)