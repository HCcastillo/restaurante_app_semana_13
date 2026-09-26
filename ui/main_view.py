import tkinter as tk


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(root, padx=30, pady=30)
        self.frame.pack(fill="both", expand=True)

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=(0, 20))

        subtitulo = tk.Label(
            self.frame,
            text="Menú principal"
        )
        subtitulo.pack(pady=(0, 15))

        botones = tk.Frame(self.frame)
        botones.pack()

        tk.Button(
            botones,
            text="Ver productos",
            width=20,
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            botones,
            text="Ver usuarios",
            width=20,
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            botones,
            text="Ventas (pendiente)",
            width=20,
            command=self.mostrar_ventas
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            botones,
            text="Cerrar sesión",
            width=20,
            command=self.salir
        ).grid(row=1, column=1, padx=5, pady=5)

        self.contenido = tk.Text(
            self.frame,
            width=70,
            height=15
        )
        self.contenido.pack(pady=20)

    def mostrar_productos(self):
        self.contenido.delete("1.0", tk.END)

        productos = self.servicio.listar_productos()

        self.contenido.insert(
            tk.END,
            "=== LISTA DE PRODUCTOS ===\n\n"
        )

        if not productos:
            self.contenido.insert(
                tk.END,
                "No existen productos registrados."
            )
            return

        for producto in productos:
            self.contenido.insert(
                tk.END,
                f"Código: {producto.codigo}\n"
                f"Nombre: {producto.nombre}\n"
                f"Categoría: {producto.categoria}\n"
                f"Precio: ${producto.precio:.2f}\n"
                f"Stock: {producto.stock}\n"
                f"{'-' * 40}\n"
            )

    def mostrar_usuarios(self):
        self.contenido.delete("1.0", tk.END)

        usuarios = self.servicio.listar_usuarios()

        self.contenido.insert(
            tk.END,
            "=== LISTA DE USUARIOS ===\n\n"
        )

        if not usuarios:
            self.contenido.insert(
                tk.END,
                "No existen usuarios registrados."
            )
            return

        for usuario in usuarios:
            self.contenido.insert(
                tk.END,
                f"Identificador: {usuario.identificador}\n"
                f"Nombre: {usuario.nombre}\n"
                f"Usuario: {usuario.usuario}\n"
                f"{'-' * 40}\n"
            )

    def mostrar_ventas(self):
        self.contenido.delete("1.0", tk.END)

        self.contenido.insert(
            tk.END,
            "=== VENTAS ===\n\n"
            "El módulo de ventas queda pendiente\n"
            "para una futura implementación."
        )

    def salir(self):
        self.frame.destroy()
        self.cerrar_sesion()