import tkinter as tk
from tkinter import *
from tkinter import ttk
import conexionBDD

def iramenu(raiz: Tk):
    from Menu import abrirMenu   
    raiz.destroy()
    abrirMenu()

def datosTablaElegida(tabla, clave):
    if(tabla.get()!=""): 
        if (tabla.get()=="Cliente"):
            clave['values'] = ["id_cliente"]
        elif (tabla.get()=="Categoria"):
            clave['values'] = ["id_categoria"]
        elif (tabla.get()=="Producto"):
            clave['values'] = ["id_producto"]
        elif (tabla.get()=="Pedido"):
            clave['values'] = ["id_pedido"]
        elif (tabla.get()=="Detalle"):
            clave['values'] = ["id_detalle"]

def eliminarRegistro():
    raiz = Tk()
    raiz.title("Eliminar registro")
    raiz.resizable(False, False)
    raiz.geometry("350x250")
    dato = tk.StringVar()
    tk.Label(text="Selecciona la tabla a eliminar").place(x=30, y=30)
    tabla = ttk.Combobox(values=["Cliente", "Producto", "Pedido", "Detalle", "Categoria"])
    tabla.place(x=30, y=60)
    ttk.Button(text="Seleccionar tabla", command=lambda:datosTablaElegida(tabla, clave)).place(x=220,y=90)
    tk.Label(text="Selecciona el registro a eliminar").place(x=30, y=90)
    clave = ttk.Combobox()
    clave.place(x=30, y=120)
    tk.Label(text="Indica la clave a eliminar").place(x=30, y=150)
    tk.Entry(textvariable=dato).place(x=30, y=180)
    ttk.Button(text="Eliminar", command=lambda:conexionBDD.eliminarRegistros(tabla.get(), clave.get(), dato.get())).place(x=220,y=130)
    ttk.Button(text="Volver", command=lambda:iramenu(raiz)).place(x=220,y=170)
    raiz.mainloop()

if(__name__ == "__main__"):
    eliminarRegistro()

    