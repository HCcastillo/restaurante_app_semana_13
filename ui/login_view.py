import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):

    def __init__(self, master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#eef3f8")

        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Login.TButton",
            background="#25ebe8",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(14, 8)
        )

    def construir_interfaz(self):

        contenedor = tk.Frame(
            self,
            bg="#ffffff",
            padx=32,
            pady=28
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            contenedor,
            text="Restaurante",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold")
        ).pack(pady=(0, 6))

        tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11)
        ).pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11)
        )
        self.usuario_entry.pack(pady=(4, 14), ipady=4)

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )
        self.contrasena_entry.pack(pady=(4, 14), ipady=4)

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10)
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton"
        )
        boton.pack(fill="x")

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_error.config(
                text="Ingrese usuario y contraseña."
            )
            return

        usuario_valido = self.restaurante_servicio.validar_acceso(
            usuario,
            contrasena
        )

        if usuario_valido:
            print("Inicio de sesión correcto:", usuario_valido.nombre)
            self.al_iniciar_sesion(usuario_valido)
        else:
            self.mensaje_error.config(
                text="Credenciales incorrectas."
            )