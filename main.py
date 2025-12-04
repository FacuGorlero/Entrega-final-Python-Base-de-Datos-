import sys
from database import *
from ui import *

def accion_registrar():
    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip() or None
    cantidad = solicitar_entero("Cantidad: ")
    precio = solicitar_float("Precio: ")
    categoria = input("Categoría: ").strip() or None
    nuevo_id = registrar_producto(nombre, descripcion, cantidad, precio, categoria)
    print(c(f"Producto registrado con ID {nuevo_id}", Fore.GREEN))

def accion_ver_todos():
    filas = obtener_todos()
    for f in filas:
        imprimir_producto_tuple(f)

def accion_buscar_id():
    pid = solicitar_entero("ID: ")
    prod = obtener_por_id(pid)
    if prod:
        imprimir_producto_tuple(prod)
    else:
        print(c("Producto no encontrado", Fore.RED))

def accion_buscar_nombre_categoria():
    texto = input("Buscar: ").strip()
    filas = buscar_por_nombre_o_categoria(texto)
    for f in filas:
        imprimir_producto_tuple(f)

def accion_actualizar():
    pid = solicitar_entero("ID: ")
    nombre = input("Nuevo nombre: ").strip() or None
    descripcion = input("Nueva descripción: ").strip() or None
    cantidad = solicitar_entero("Nueva cantidad: ", True)
    precio = solicitar_float("Nuevo precio: ", True)
    categoria = input("Nueva categoría: ").strip() or None
    actualizar_producto(pid, nombre, descripcion, cantidad, precio, categoria)
    print(c("Producto actualizado", Fore.GREEN))

def accion_eliminar():
    pid = solicitar_entero("ID: ")
    eliminar_producto(pid)
    print(c("Producto eliminado", Fore.GREEN))

def accion_reporte_bajo_stock():
    umbral = solicitar_entero("Umbral: ")
    filas = reporte_bajo_stock(umbral)
    for f in filas:
        imprimir_producto_tuple(f)

def main():
    crear_tabla()
    while True:
        op = menu_principal()
        if op == "1": accion_registrar()
        elif op == "2": accion_ver_todos()
        elif op == "3": accion_buscar_id()
        elif op == "4": accion_buscar_nombre_categoria()
        elif op == "5": accion_actualizar()
        elif op == "6": accion_eliminar()
        elif op == "7": accion_reporte_bajo_stock()
        elif op == "8": sys.exit()
        else: print(c("Opción inválida", Fore.RED))

if __name__ == "__main__":
    main()
