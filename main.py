import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Restaurante App")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()

        self.login_view = None
        self.main_view = None

        self.mostrar_login()

    def mostrar_login(self):

        if self.main_view is not None:
            self.main_view.destroy()
            self.main_view = None

        self.login_view = LoginView(
            self.root,
            self.servicio,
            self.mostrar_principal
        )

        self.login_view.pack(
            fill="both",
            expand=True
        )

    def mostrar_principal(self, usuario):

        if self.login_view is not None:
            self.login_view.destroy()
            self.login_view = None

        self.main_view = MainView(
            self.root,
            self.servicio,
            self.mostrar_login
        )

        self.main_view.pack(
            fill="both",
            expand=True
        )

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()