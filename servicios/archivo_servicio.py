import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


RUTA_PRODUCTOS = "datos/productos.json"
RUTA_USUARIOS = "datos/usuarios.json"
RUTA_VENTAS = "datos/ventas.json"


def guardar_productos(lista: list[Producto]) -> bool:
    try:
        os.makedirs("datos", exist_ok=True)

        datos = [producto.to_dict() for producto in lista]

        with open(RUTA_PRODUCTOS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        return True

    except PermissionError:
        print("Error: no existen permisos para guardar productos.")
        return False

    except OSError as e:
        print(f"Error al guardar productos: {e}")
        return False


def cargar_productos() -> list[Producto]:
    if not os.path.exists(RUTA_PRODUCTOS):
        return []

    try:
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        productos = []

        for item in datos:
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, ValueError) as e:
                print(f"Advertencia: producto inválido: {e}")

        return productos

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: productos.json no contiene JSON válido.")
        return []

    except PermissionError:
        print("Error: no existen permisos para leer productos.")
        return []


# =====================================================
# USUARIOS
# =====================================================

def guardar_usuarios(lista: list[Usuario]) -> bool:
    try:
        os.makedirs("datos", exist_ok=True)

        datos = [usuario.to_dict() for usuario in lista]

        with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        return True

    except PermissionError:
        print("Error: no existen permisos para guardar usuarios.")
        return False

    except OSError as e:
        print(f"Error al guardar usuarios: {e}")
        return False


def cargar_usuarios() -> list[Usuario]:
    if not os.path.exists(RUTA_USUARIOS):
        return []

    try:
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        usuarios = []

        for item in datos:
            try:
                usuarios.append(Usuario.from_dict(item))
            except (KeyError, ValueError) as e:
                print(f"Advertencia: usuario inválido: {e}")

        return usuarios

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: usuarios.json no contiene JSON válido.")
        return []

    except PermissionError:
        print("Error: no existen permisos para leer usuarios.")
        return []


# =====================================================
# VENTAS
# =====================================================

def guardar_ventas(lista: list[Venta]) -> bool:
    try:
        os.makedirs("datos", exist_ok=True)

        datos = [venta.to_dict() for venta in lista]

        with open(RUTA_VENTAS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        return True

    except PermissionError:
        print("Error: no existen permisos para guardar ventas.")
        return False

    except OSError as e:
        print(f"Error al guardar ventas: {e}")
        return False


def cargar_ventas() -> list[Venta]:
    if not os.path.exists(RUTA_VENTAS):
        return []

    try:
        with open(RUTA_VENTAS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        ventas = []

        for item in datos:
            try:
                ventas.append(Venta.from_dict(item))
            except (KeyError, ValueError) as e:
                print(f"Advertencia: venta inválida: {e}")

        return ventas

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: ventas.json no contiene JSON válido.")
        return []

    except PermissionError:
        print("Error: no existen permisos para leer ventas.")
        return []