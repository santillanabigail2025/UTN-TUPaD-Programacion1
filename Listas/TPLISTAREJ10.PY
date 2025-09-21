#EJERCICIO 10
ventas = [
    # Lun Mar Mie Jue Vie Sab Dom
    [10, 15, 20, 12, 25, 30, 18],  # Producto 1
    [5,  8,  10, 7,  12, 15, 11],  # Producto 2
    [25, 30, 35, 28, 40, 45, 38],  # Producto 3
    [12, 18, 22, 15, 28, 32, 25]   # Producto 4
]

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# --- 1. Mostrar el total vendido por cada producto ---
print("Total vendido por producto")
max_venta_producto = -1
producto_mas_vendido = ""

# Bucle externo: recorre cada producto (fila)
for i in range(len(ventas)):
    total_producto = 0
    # Bucle interno: recorre cada venta diaria de ese producto y la suma
    for venta_diaria in ventas[i]:
        total_producto += venta_diaria
    
    print(f"{productos[i]}: {total_producto} unidades")
    
    # Comprobar si este es el producto más vendido hasta ahora
    if total_producto > max_venta_producto:
        max_venta_producto = total_producto
        producto_mas_vendido = productos[i]

print("-" * 30)

# --- 2. Mostrar el día con mayores ventas totales ---
print("Día con mayores ventas")
max_venta_dia = -1
dia_mayor_venta = ""

# Iterar por columnas (j representa el índice del día)
for j in range(len(dias)):
    suma_del_dia = 0
    # Iterar por filas (i representa el índice del producto)
    for i in range(len(ventas)):
        suma_del_dia += ventas[i][j]
    
    # Comprobar si este día tuvo más ventas que el máximo registrado
    if suma_del_dia > max_venta_dia:
        max_venta_dia = suma_del_dia
        dia_mayor_venta = dias[j]

print(f"El día con mayores ventas totales fue el {dia_mayor_venta} ({max_venta_dia} unidades).")

print("-" * 30)

# --- 3. Indicar cuál fue el producto más vendido ---
print("Producto más vendido de la semana")
print(f"El producto estrella fue el {producto_mas_vendido} ({max_venta_producto} unidades).")