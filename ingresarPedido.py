import tkinter as tk
from tkinter import * 
from tkinter import ttk
import conexionBDD
from Menu import Menu

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def abrirIngresarPedido():
    raiz = Tk()
    raiz.title("Ingresar Pedido")
    raiz.geometry("400x200")
    raiz.resizable(False,False)
    id_pedido = tk.StringVar()
    id_cliente = tk.StringVar()
    fecha_pedido = tk.StringVar()
    estado = tk.StringVar()
    ttk.Label(text="id_pedido").place(x=40, y=30)
    ttk.Entry(textvariable=id_pedido).place(x=100, y=30)
    ttk.Label(text="id_cliente").place(x=40, y=60)
    ttk.Entry(textvariable=id_cliente).place(x=100, y=60)
    ttk.Label(text="fecha_pedido").place(x=40, y=90)
    ttk.Entry(textvariable=fecha_pedido).place(x=120, y=90)
    ttk.Label(text="estado").place(x=40, y=120)
    ttk.Entry(textvariable=estado).place(x=85, y=120)
    ttk.Button(text="Agregar", command=lambda:conexionBDD.ingresarRegistroPedido(id_pedido.get(),id_cliente.get(),fecha_pedido.get(),estado.get())).place(x=280, y=60)
    ttk.Button(text="Modificar", command=lambda:conexionBDD.modificarRegistroPedido(id_pedido.get(),id_cliente.get(),fecha_pedido.get(),estado.get())).place(x=280, y=90)
    ttk.Button(text="Volver", command=lambda:irMenu(raiz)).place(x=280, y=120)    

    raiz.mainloop()

if(__name__=="__main__"):
    abrirIngresarPedido()