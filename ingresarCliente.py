import tkinter as tk
from tkinter import * 
from tkinter import ttk
import conexionBDD

def iramenu(raiz: Tk):
    from Menu import abrirMenu   
    raiz.destroy()
    abrirMenu()

def abrirIngresarCliente():
    raiz = Tk()
    raiz.title("Ingresar Cliente")
    raiz.geometry("400x200")
    raiz.resizable(False,False)
    dni = tk.StringVar()
    nombre = tk.StringVar()
    correo = tk.StringVar()
    direccion = tk.StringVar()
    ttk.Label(raiz, text="DNI").place(x=40, y=30)
    ttk.Entry(raiz, textvariable=dni).place(x=80, y=30)
    ttk.Label(raiz, text="Nombre").place(x=40, y=60)
    ttk.Entry(raiz, textvariable=nombre).place(x=100, y=60)
    ttk.Label(raiz, text="Correo").place(x=40, y=90)
    ttk.Entry(raiz, textvariable=correo).place(x=100, y=90)
    ttk.Label(raiz, text="Direccion").place(x=40, y=120)
    ttk.Entry(raiz, textvariable=direccion).place(x=100, y=120)
    ttk.Button(raiz, text="Agregar", command=lambda:conexionBDD.ingresarRegistroCliente(dni.get(),nombre.get(),correo.get(),direccion.get())).place(x=280, y=60)
    ttk.Button(text="Modificar", command=lambda:conexionBDD.modificarRegistroCliente(dni.get(),nombre.get(),correo.get(),direccion.get())).place(x=280, y=90)
    ttk.Button(raiz, text="Volver", command=lambda:iramenu(raiz)).place(x=280,y=120)
    raiz.mainloop()

if (__name__ == "__main__"):
    abrirIngresarCliente()
     
