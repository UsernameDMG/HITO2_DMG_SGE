import tkinter as tk
from tkinter import *
from tkinter import ttk
import conexionBDD
from Menu import Menu

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def abrirIngresarProducto():
    raiz = Tk()
    raiz.title("Ingresar Producto")
    raiz.geometry("400x200")
    raiz.resizable(False,False)
    id_producto = tk.StringVar()
    nombre = tk.StringVar()
    id_categoria = tk.StringVar()
    precio = tk.StringVar()
    stock = tk.StringVar()
    ttk.Label(text="Id producto").place(x=40, y=30)
    ttk.Entry(textvariable=id_producto).place(x=120, y=30)
    ttk.Label(text="Nombre").place(x=40, y=60)
    ttk.Entry(textvariable=nombre).place(x=100, y=60)
    ttk.Label(text="Id categoria").place(x=40, y=90)
    ttk.Entry(textvariable=id_categoria).place(x=120, y=90)
    ttk.Label(text="Precio unitario").place(x=40, y=120)
    ttk.Entry(textvariable=precio).place(x=130, y=120)
    ttk.Label(text="Stock actual").place(x=40, y=150)
    ttk.Entry(textvariable=stock).place(x=120, y=150)
    ttk.Button(text="Agregar", command=lambda:conexionBDD.ingresarRegistroProducto(id_producto.get(), nombre.get(), id_categoria.get(), precio.get(), stock.get())).place(x=280, y=60)
    ttk.Button(text="Modificar", command=lambda:conexionBDD.modificarRegistroProducto(id_producto.get(), nombre.get(), id_categoria.get(), precio.get(), stock.get())).place(x=280, y=90)
    ttk.Button(text="Volver", command=lambda:irMenu(raiz)).place(x=280, y=120)

    raiz.mainloop()

if (__name__=="__main__"):
    abrirIngresarProducto()