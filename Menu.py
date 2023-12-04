import tkinter as tk
from tkinter import *
from tkinter import ttk

def agregarModificar(tabla, raiz):
    from ingresarDetalle import abrirIngresarDetalle
    from ingresarCliente import abrirIngresarCliente
    from ingresarProducto import abrirIngresarProducto
    from ingresarCategoria import abrirIngresarCategoria
    from ingresarPedido import abrirIngresarPedido

    if(tabla.get()!=""): 
        raiz.destroy()
        if (tabla.get()=="Cliente"):
            abrirIngresarCliente()
        elif (tabla.get()=="Categoria"):
            abrirIngresarCategoria()
        elif (tabla.get()=="Producto"):
            abrirIngresarProducto()
        elif (tabla.get()=="Pedido"):
            abrirIngresarPedido()
        elif (tabla.get()=="Detalle"):
            abrirIngresarDetalle()

def mostrar(raiz):
    from mostrarDatos import mostrarDatos
    raiz.destroy()
    mostrarDatos()
def eliminar(raiz):
    from eliminarRegistros import eliminarRegistro
    raiz.destroy()
    eliminarRegistro()
def administrarTabla(raiz):
    from administrarTablas import administrarTablas
    raiz.destroy()
    administrarTablas()
def verGraficos(raiz):
    from graficos import abrirGrafico
    raiz.destroy()
    abrirGrafico()
def abrirMenu():
    raiz = Tk()
    raiz.title("Menu")
    raiz.geometry("400x260")
    raiz.resizable(False, False)
    tabla = tk.StringVar()
    ttk.Combobox(raiz, textvariable=tabla, values=["Cliente", "Producto", "Pedido", "Detalle", "Categoria"]).place(x=130, y=20)
    ttk.Button(raiz, text="Agregar/Modificar", command=lambda:agregarModificar(tabla, raiz)).place(x=130, y=60)
    ttk.Button(raiz, text="Mostrar", command=lambda:mostrar(raiz)).place(x=130, y=100)
    ttk.Button(raiz, text="Eliminar", command=lambda:eliminar(raiz)).place(x=130, y=140)
    ttk.Button(raiz, text="Administrar tablas", command=lambda:administrarTabla(raiz)).place(x=130, y=180)
    ttk.Button(raiz, text="Mostrar graficos", command=lambda:verGraficos(raiz)).place(x=130, y=220)
    ttk.Button(raiz, text="Salir", command=lambda:raiz.destroy()).place(x=300, y=220)

    raiz.mainloop()
if(__name__ == "__main__"):
    abrirMenu()
