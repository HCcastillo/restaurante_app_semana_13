class Usuario:
    def __init__(
        self,
        identificador: str,
        nombre: str,
        usuario: str,
        contrasena: str
    ):
        if not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío.")

        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía.")

        self.identificador = identificador.strip()
        self.nombre = nombre.strip()
        self.usuario = usuario.strip()
        self.contrasena = contrasena.strip()

    def to_dict(self) -> dict:
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contrasena": self.contrasena
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        try:
            return cls(
                str(datos["identificador"]),
                str(datos["nombre"]),
                str(datos["usuario"]),
                str(datos["contrasena"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Datos de usuario inválidos: {e}")