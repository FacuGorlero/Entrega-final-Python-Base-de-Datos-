import sqlite3

DB_FILE = "inventario.db"

def conectar_db():
    return sqlite3.connect(DB_FILE)

def crear_tabla():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        );
    """)
    conn.commit()
    conn.close()

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    nuevo_id = cur.lastrowid
    conn.close()
    return nuevo_id

def obtener_todos():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos ORDER BY id;")
    filas = cur.fetchall()
    conn.close()
    return filas

def obtener_por_id(prod_id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE id = ?;", (prod_id,))
    fila = cur.fetchone()
    conn.close()
    return fila

def buscar_por_nombre_o_categoria(texto):
    term = f"%{texto}%"
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM productos
        WHERE nombre LIKE ? COLLATE NOCASE OR categoria LIKE ? COLLATE NOCASE
        ORDER BY id;
    """, (term, term))
    filas = cur.fetchall()
    conn.close()
    return filas

def actualizar_producto(prod_id, nombre=None, descripcion=None, cantidad=None, precio=None, categoria=None):
    actual = obtener_por_id(prod_id)
    if not actual:
        return False

    nuevo_nombre = nombre if nombre is not None else actual[1]
    nueva_desc = descripcion if descripcion is not None else actual[2]
    nueva_cant = cantidad if cantidad is not None else actual[3]
    nuevo_precio = precio if precio is not None else actual[4]
    nueva_cat = categoria if categoria is not None else actual[5]

    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?;
    """, (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_cat, prod_id))
    conn.commit()
    conn.close()
    return True

def eliminar_producto(prod_id):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM productos WHERE id = ?;", (prod_id,))
    cambios = cur.rowcount
    conn.commit()
    conn.close()
    return cambios > 0

def reporte_bajo_stock(umbral):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM productos
        WHERE cantidad <= ?
        ORDER BY cantidad ASC;
    """, (umbral,))
    filas = cur.fetchall()
    conn.close()
    return filas
