import tkinter as tk
from tkinter import messagebox

from modelos.venta import Venta
from servicios.venta_servicio import VentaServicio


class MainView:

    def __init__(self, root):

        self.root = root
        self.root.title("Restaurante App - Semana 15")

        self.servicio = VentaServicio()

        titulo = tk.Label(
            root,
            text="Registro de ventas"
        )
        titulo.pack()

        self.usuario = tk.Entry(root)
        self.usuario.pack()
        self.usuario.insert(0, "Usuario")

        self.producto = tk.Entry(root)
        self.producto.pack()
        self.producto.insert(0, "Producto")

        self.cantidad = tk.Entry(root)
        self.cantidad.pack()
        self.cantidad.insert(0, "Cantidad")

        boton = tk.Button(
            root,
            text="Registrar venta",
            command=self.registrar_venta
        )
        boton.pack()

        self.lista = tk.Listbox(root)
        self.lista.pack()


    def registrar_venta(self):

        venta = Venta(
            "V001",
            self.producto.get(),
            self.cantidad.get(),
            0
        )

        self.servicio.guardar(venta)

        self.lista.insert(
            tk.END,
            str(venta)
        )

        messagebox.showinfo(
            "Venta",
            "Venta registrada correctamente"
        )
