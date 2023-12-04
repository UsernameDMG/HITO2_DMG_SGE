import tkinter as tk
from tkinter import *
from tkinter import ttk
import conexionBDD
from Menu import Menu

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def abrirIngresarCategoria():
    raiz = Tk()
    raiz.title("Ingresar Categoria")
    raiz.geometry("400x200")
    raiz.resizable(False,False)
    nombre = tk.StringVar()
    descripcion = tk.StringVar()
    categoria = tk.StringVar()
    ttk.Label(text="Id categoria").place(x=40, y=50)
    ttk.Entry(textvariable=categoria).place(x=120 , y=50)
    ttk.Label(text="Nombre").place(x=40, y=90)
    ttk.Entry(textvariable=nombre).place(x=100 , y=90)
    ttk.Label(text="Descripcion").place(x=40, y=130)
    ttk.Entry(textvariable=descripcion).place(x=120, y=130)
    ttk.Button(text="Agregar", command=lambda:conexionBDD.ingresarRegistroCategoria(categoria.get(), nombre.get(), descripcion.get())).place(x=280, y=60)
    ttk.Button(text="Modificar", command=lambda:conexionBDD.modificarRegistroCategoria(categoria.get(), nombre.get(), descripcion.get())).place(x=280, y=90)
    ttk.Button(text="Volver", command=lambda:irMenu(raiz)).place(x=280, y=120)
    raiz.mainloop()
if(__name__=="__main__"):
    abrirIngresarCategoria()