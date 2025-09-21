#EJERCICIO 5
# Lista de asistencia
asistencia = ["Micaela", "Macarena", "Gabriela", "Antonella", "Aixa", "Yanina", "Agustina", "Pamela"]
print("Lista de asistencia:")
for a in asistencia:
    print (a)
# Agregar o eliminar un nombre
opcion = input("Desea agregar o eliminar un nombre? (A/E): ").upper()
if opcion == "A":
    nuevo_nombre = input("Ingrese el nombre que desea agregar: ")
    if nuevo_nombre in asistencia:
        print(f"El nombre '{nuevo_nombre}' ya está en la lista.")
    else:
        asistencia.append(nuevo_nombre)
        print(f"Nombre '{nuevo_nombre}' agregado.")
elif opcion == "E":
    nombre_eliminar = input("Ingrese el nombre que desea eliminar: ")
    if nombre_eliminar in asistencia:
        asistencia.remove(nombre_eliminar)
        print(f"Nombre '{nombre_eliminar}' eliminado.")
    else:
        print(f"El nombre '{nombre_eliminar}' no se encontró en la lista.")
# Mostrar la lista actualizada
print("--- Lista Actualizada ---")
for a in asistencia:
    print(a)