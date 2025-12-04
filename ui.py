try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    USE_COLOR = True
except:
    USE_COLOR = False
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = RESET = ""
    class Style:
        BRIGHT = NORMAL = RESET_ALL = ""

def c(text, color=Fore.CYAN, bright=False):
    if USE_COLOR:
        style = Style.BRIGHT if bright else Style.NORMAL
        return f"{style}{color}{text}{Style.RESET_ALL}"
    return text

def imprimir_producto_tuple(t):
    pid, nombre, descripcion, cantidad, precio, categoria = t
    print(f"[{pid}] {nombre} | cat: {categoria or '-'} | cant: {cantidad} | precio: {precio:.2f} | desc: {descripcion or '-'}")

def solicitar_entero(prompt, permitir_vacio=False):
    while True:
        val = input(prompt).strip()
        if permitir_vacio and val == "":
            return None
        try:
            return int(val)
        except ValueError:
            print(c("Ingrese un número entero válido.", Fore.RED))

def solicitar_float(prompt, permitir_vacio=False):
    while True:
        val = input(prompt).strip()
        if permitir_vacio and val == "":
            return None
        try:
            return float(val)
        except ValueError:
            print(c("Ingrese un número válido.", Fore.RED))

def menu_principal():
    opciones = [
        ("1", "Registrar producto"),
        ("2", "Ver productos"),
        ("3", "Buscar por ID"),
        ("4", "Buscar por nombre o categoría"),
        ("5", "Actualizar producto"),
        ("6", "Eliminar producto"),
        ("7", "Reporte bajo stock"),
        ("8", "Salir"),
    ]
    print(c("\n--- MENÚ PRINCIPAL ---", Fore.MAGENTA, True))
    for k, desc in opciones:
        print(c(f"{k}) ", Fore.YELLOW, True) + desc)
    return input(c("Seleccione una opción: ", Fore.CYAN)).strip()
