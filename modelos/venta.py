class Venta:
    def __init__(
        self,
        correo_usuario: str,
        codigo_producto: str,
        cantidad: int
    ):
        if not correo_usuario.strip():
            raise ValueError("El correo del usuario no puede estar vacío.")

        if not codigo_producto.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.correo_usuario = correo_usuario.strip()
        self.codigo_producto = codigo_producto.strip()
        self.cantidad = cantidad

    def to_dict(self) -> dict:
        """Convierte la venta en un diccionario compatible con JSON."""
        return {
            "correo_usuario": self.correo_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        """Reconstruye una venta desde un diccionario."""
        try:
            return cls(
                str(datos["correo_usuario"]),
                str(datos["codigo_producto"]),
                int(datos["cantidad"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Datos de venta inválidos: {e}")