#Ejercicio 2
productos = []
# Ingresar 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)
print("Lista de productos:")
for p in sorted(productos): #muestra la lista ordenada 
    print(p)
print("Productos ordenadados en forma de lista:", sorted(productos))
eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if eliminar in productos:
    # Esta parte se ejecuta si el producto SÍ está en la lista
    productos.remove(eliminar)
    print(f"Producto '{eliminar}' eliminado.")
    print("--- Lista Actualizada ---")
    print(sorted(productos))
else:
    # Esta parte se ejecuta si el producto NO está en la lista
    print(f"El producto '{eliminar}' no se encontró en la lista.")