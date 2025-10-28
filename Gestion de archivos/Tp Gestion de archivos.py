# --- PUNTO 1: CREAR ARCHIVO INICIAL ---
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.50,30\n")
    archivo.write("Cuaderno,350.00,15\n")
    archivo.write("Goma,80.75,50\n")

print("Archivo 'productos.txt' creado con éxito.")
print("Ahora puedes ejecutar el programa principal.")

# --- PUNTOS 2 y 4: Cargar productos en lista y mostrarlos ---

def cargar_productos():
    """
    Lee el archivo, lo muestra (Punto 2) y lo carga en una
    lista de diccionarios (Punto 4).
    """
    # Lista del PUNTO 4
    productos = [] 
    
    with open("productos.txt", "r") as archivo:
        print("--- Productos Cargados desde 'productos.txt' ---")
        
        for linea in archivo:
            # 1. Se procesa la línea
            nombre, precio, cantidad = linea.strip().split(',')
            
            # --- PUNTO 2 ---
            print(f"Producto: {nombre} | Precio: ${float(precio):.2f} | Cantidad: {int(cantidad)}")

            # --- PUNTO 4 ---
            # 2. Crea el diccionario
            producto_dic = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            # 3. Se le agrega a la lista
            productos.append(producto_dic)
            
    # Devuelve la lista completa para usarla en el resto del programa
    return productos

# --- PUNTO 3: Agregar productos desde teclado ---

def agregar_producto(lista_productos):
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    # 1. Agrega el producto a la LISTA en memoria
    nuevo_producto_dic = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    lista_productos.append(nuevo_producto_dic)

    # 2. Agrega el producto al ARCHIVO TXT
    # Se abre en modo "a" (append - añadir)
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"¡Producto '{nombre}' agregado con éxito!")


# --- PUNTO 5: Buscar producto por nombre ---

def buscar_producto(lista_productos):
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
    
    encontrado = False
    # Recorremos la LISTA de diccionarios (no el archivo)
    for producto in lista_productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("\n¡Producto encontrado!")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']:.2f}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break 
    if not encontrado:
        print(f"Error: El producto '{nombre_buscar}' no se encontró en la lista.")

# --- PUNTO 6: Guardar los productos actualizados ---

def guardar_productos(lista_productos):
    with open("productos.txt", "w") as archivo:
        for producto in lista_productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    
    print("\nTodos los productos han sido guardados en 'productos.txt'.")

# --- Función auxiliar para ver la lista en memoria ---

def mostrar_productos_memoria(lista_productos):
    """
    Muestra los productos que están actualmente en la lista de memoria.
    """
    print("\n--- Lista Actual de Productos (en memoria) ---")
    if not lista_productos:
        print("No hay productos cargados en memoria.")
        return
        
    for producto in lista_productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")


# --- Menú Interactivo ---

# 1. Cargamos los productos del archivo a la lista 'lista_de_productos'
lista_de_productos = cargar_productos()

# 2. Iniciamos el menú interactivo
while True:
    print("\n===== MENÚ DE GESTIÓN DE PRODUCTOS =====")
    print("1. Agregar nuevo producto (Punto 3)")
    print("2. Buscar producto por nombre (Punto 5)")
    print("3. Mostrar todos los productos actuales (de la memoria)")
    print("4. Guardar y Salir (Punto 6)")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Llama a la función del Punto 3
        agregar_producto(lista_de_productos)
    
    elif opcion == "2":
        # Llama a la función del Punto 5
        buscar_producto(lista_de_productos)
    
    elif opcion == "3":
        # Llama a la función auxiliar
        mostrar_productos_memoria(lista_de_productos)

    elif opcion == "4":
        # Llama a la función del Punto 6 y sale
        guardar_productos(lista_de_productos)
        print("Datos guardados. ¡Adiós!")
        break
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")