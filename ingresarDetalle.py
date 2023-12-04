import tkinter as tk
from tkinter import *
from tkinter import ttk
import conexionBDD

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def abrirIngresarDetalle():
    raiz = Tk()
    raiz.title("Ingresar Detalle")
    raiz.geometry("400x200")
    raiz.resizable(False,False)
    id_detalle = tk.StringVar()
    id_pedido = tk.StringVar()
    id_producto = tk.StringVar()
    cantidad = tk.StringVar()
    precio_unitario = tk.StringVar()
    ttk.Label(text="id_detalle").place(x=40, y=30)
    ttk.Entry(textvariable=id_detalle).place(x=100, y=30)
    ttk.Label(text="id_pedido").place(x=40, y=60)
    ttk.Entry(textvariable=id_pedido).place(x=100, y=60)
    ttk.Label(text="id_producto").place(x=40, y=90)
    ttk.Entry(textvariable=id_producto).place(x=110, y=90)
    ttk.Label(text="cantidad").place(x=40, y=120)
    ttk.Entry(textvariable=cantidad).place(x=95, y=120)
    ttk.Label(text="precio_unitario").place(x=40, y=150)
    ttk.Entry(textvariable=precio_unitario).place(x=125, y=150)
    ttk.Button(text="Agregar", command=lambda:conexionBDD.ingresarRegistroDetalle(id_detalle.get(),id_pedido.get(),id_producto.get(),cantidad.get(), precio_unitario.get())).place(x=280, y=60)
    ttk.Button(text="Modificar", command=lambda:conexionBDD.modificarRegistroDetalle(id_detalle.get(),id_pedido.get(),id_producto.get(),cantidad.get(), precio_unitario.get())).place(x=280, y=90)
    ttk.Button(text="Volver", command=lambda:irMenu(raiz)).place(x=280, y=120)

    raiz.mainloop()

if (__name__ == "__main__"):
    abrirIngresarDetalle()