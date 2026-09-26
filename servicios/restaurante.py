from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

from servicios.archivo_servicio import (
    cargar_productos,
    guardar_productos,
    cargar_usuarios,
    guardar_usuarios,
    cargar_ventas,
    guardar_ventas
)


class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = cargar_productos()
        self.usuarios: list[Usuario] = cargar_usuarios()
        self.ventas: list[Venta] = cargar_ventas()

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def registrar_producto(self, nuevo: Producto) -> bool:

        for producto in self.productos:
            if producto.codigo == nuevo.codigo:
                return False

        self.productos.append(nuevo)
        guardar_productos(self.productos)

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        producto.nombre = nombre.strip()
        producto.categoria = categoria.strip()
        producto.precio = precio
        producto.stock = stock

        guardar_productos(self.productos)

        return True

    def eliminar_producto(self, codigo: str) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        guardar_productos(self.productos)

        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    # ==========================================
# USUARIOS
# ==========================================

def registrar_usuario(self, nuevo: Usuario) -> bool:

    for usuario in self.usuarios:
        if usuario.usuario == nuevo.usuario:
            return False

    self.usuarios.append(nuevo)
    guardar_usuarios(self.usuarios)

    return True


def buscar_usuario(self, usuario_ingresado: str) -> Usuario | None:

    for usuario in self.usuarios:
        if usuario.usuario == usuario_ingresado:
            return usuario

    return None


def validar_acceso(
    self,
    usuario_ingresado: str,
    contrasena: str
) -> bool:

    usuario = self.buscar_usuario(usuario_ingresado)

    if usuario is None:
        return False

    return usuario.contrasena == contrasena


def listar_usuarios(self) -> list[Usuario]:
    return self.usuarios

    # ==========================================
    # VENTAS
    # ==========================================

    def vender_producto(
        self,
        correo_usuario: str,
        codigo_producto: str,
        cantidad: int
    ) -> bool:

        # Validar cantidad
        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        # Buscar usuario
        usuario = self.buscar_usuario(correo_usuario)

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        # Buscar producto
        producto = self.buscar_producto(codigo_producto)

        if producto is None:
            raise ValueError(
                "El producto no existe."
            )

        # Validar stock
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente. "
                f"Disponible: {producto.stock}"
            )

        # Crear la venta
        venta = Venta(
            correo_usuario,
            codigo_producto,
            cantidad
        )

        # Disminuir stock
        producto.stock -= cantidad

        # Registrar venta
        self.ventas.append(venta)

        # Guardar cambios
        guardar_productos(self.productos)
        guardar_ventas(self.ventas)

        return True

    def ventas_por_usuario(
        self,
        correo_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self.ventas:
            if venta.correo_usuario == correo_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return self.ventas