import tkinter as tk
from tkinter import *
from tkinter import ttk
import conexionBDD
from Menu import Menu

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def datosTablaElegida(tabla, campo, orden):
    if(tabla.get()!=""): 
        if (tabla.get()=="Cliente"):
            campo['values'] = ["id_cliente", "nombre", "correo", "direccion"]
            orden['values'] = ["id_cliente", "nombre", "correo", "direccion"]
        elif (tabla.get()=="Categoria"):
            campo['values'] = ["id_categoria","nombre", "descripcion"]
            orden['values'] = ["id_categoria","nombre", "descripcion"]
        elif (tabla.get()=="Producto"):
            campo['values'] = ["id_producto","nombre", "id_categoria", "precio_unitario", "stock_actual"]
            orden['values'] = ["id_producto","nombre", "id_categoria", "precio_unitario", "stock_actual"]
        elif (tabla.get()=="Pedido"):
            campo['values'] = ["id_pedido","id_cliente", "estado"]
            orden['values'] = ["id_pedido","id_cliente", "estado"]
        elif (tabla.get()=="Detalles"):
            campo['values'] = ["id_detalle", "id_pedido", "id_producto", "cantidad", "precio_unitario"]
            orden['values'] = ["id_detalle", "id_pedido", "id_producto", "cantidad", "precio_unitario"]

def mostrarDatos():
    raiz = Tk()
    raiz.title("Mostrar datos")
    raiz.geometry("700x800")
    tk.Label(text="Elige la tabla (obligatorio)").place(x=270,y=30)
    tabla = ttk.Combobox(values=["Cliente", "Producto", "Pedido", "Detalle", "Categoria"])
    tabla.place(x=270,y=60)
    ttk.Button(text="Seleccionar tabla (Obligatorio)",command=lambda:datosTablaElegida(tabla, campo, orden)).place(x=260,y=90)
    tk.Label(text="Buscar por:").place(x=270,y=120)
    campo = ttk.Combobox(values=[])
    campo.place(x=270,y=150)
    tk.Label(text="Ordenar por:").place(x=270,y=180)
    orden = ttk.Combobox(values=[])
    orden.place(x=270,y=210)
    tk.Label(text="Escribe el dato:").place(x=270,y=240)
    dato = tk.StringVar()
    datos = tk.Entry(textvariable=dato)
    datos.place(x=270,y=270)
    mostrarTodosRegistros = tk.Text()
    mostrarTodosRegistros.place(x=30,y=360)
    Enviar = tk.Button(text="Mostrar", command=lambda:conexionBDD.verRegistros(mostrarTodosRegistros, tabla.get(), campo.get(), dato.get(), orden.get())).place(x=270,y=310)
    Volver = tk.Button(text="Volver", command=lambda:irMenu(raiz)).place(x=350,y=310)
    Excel = tk.Button(text="Exportar a excel", command=lambda:conexionBDD.exportarExcel()).place(x=430,y=310)

    raiz.mainloop()
if (__name__=="__main__"):
    mostrarDatos()