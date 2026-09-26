class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ):
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = precio
        self.stock = stock

    def to_dict(self) -> dict:
        """Convierte el producto en un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        """Reconstruye un objeto Producto desde un diccionario."""
        try:
            return cls(
                str(datos["codigo"]),
                str(datos["nombre"]),
                str(datos["categoria"]),
                float(datos["precio"]),
                int(datos["stock"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Datos de producto inválidos: {e}")