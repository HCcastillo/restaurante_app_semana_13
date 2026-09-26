from modelos.producto import Producto
from modelos.usuario import Usuario

from servicios.archivo_servicio import (
    cargar_productos,
    cargar_usuarios,
    guardar_productos,
    guardar_usuarios
)


class RestauranteServicio:

    def __init__(self):
        self.productos: list[Producto] = cargar_productos()
        self.usuarios: list[Usuario] = cargar_usuarios()

    # ==========================================
    # ACCESO
    # ==========================================

    def buscar_usuario(self, usuario_ingresado: str) -> Usuario | None:

        for usuario in self.usuarios:
            if usuario.usuario == usuario_ingresado.strip():
                return usuario

        return None

    def validar_acceso(
        self,
        usuario_ingresado: str,
        contrasena: str
    ) -> Usuario | None:

        usuario = self.buscar_usuario(usuario_ingresado)

        if usuario is None:
            return None

        if usuario.contrasena == contrasena.strip():
            return usuario

        return None

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

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def registrar_producto(self, nuevo: Producto) -> bool:

        for producto in self.productos:
            if producto.codigo == nuevo.codigo:
                return False

        self.productos.append(nuevo)
        guardar_productos(self.productos)

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        for producto in self.productos:
            if producto.codigo == codigo.strip():
                return producto

        return None

    def eliminar_producto(self, codigo: str) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        guardar_productos(self.productos)

        return True