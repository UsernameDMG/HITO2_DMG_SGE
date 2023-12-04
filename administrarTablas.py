import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import conexionBDD

def irMenu(raiz):
    raiz.destroy()
    from Menu import abrirMenu
    abrirMenu()

def administrarTablas():
    
    raiz = tk.Tk()
    raiz.title('Administrar Tablas')
    raiz.geometry("300x300")
    raiz.resizable(False, False)
    
    boton_crear = tk.Button(raiz, text="Crear tabla", command=lambda:mostrar_ventana_crear_tabla()).place(x=100, y=50)

    boton_borrar_tabla = tk.Button(raiz, text="Borrar Tabla", command=lambda: mostrar_ventana_borrar_tabla()).place(x=100, y=100)

    boton_volver = tk.Button(raiz, text="Volver", command=lambda:irMenu(raiz)).place(x=100, y=150)

    raiz.mainloop()

def mostrar_ventana_borrar_tabla():
    
    ventana_borrar_tabla = tk.Toplevel()
    ventana_borrar_tabla.title('Borrar Tabla')
    ventana_borrar_tabla.geometry("350x350")
    ventana_borrar_tabla.resizable(False,False)

    espacio_superior = tk.Frame(ventana_borrar_tabla, height=40)
    espacio_superior.pack()

    etiqueta_nombre_tabla = tk.Label(ventana_borrar_tabla, text="Nombre de la Tabla:")
    etiqueta_nombre_tabla.pack(pady=5)

    entry_nombre_tabla = tk.Entry(ventana_borrar_tabla)
    entry_nombre_tabla.pack(pady=5)

    boton_borrar = tk.Button(ventana_borrar_tabla, text="Borrar", command=lambda: conexionBDD.borrar_tabla(entry_nombre_tabla.get()))
    boton_borrar.pack(pady=5)

    boton_volver = tk.Button(ventana_borrar_tabla, text="Volver", command=ventana_borrar_tabla.destroy)
    boton_volver.pack(pady=5)

def mostrar_ventana_crear_tabla():
    ventana_crear_tabla = Tk()
    ventana_crear_tabla.title('Crear Tabla')
    ventana_crear_tabla.geometry("400x500")
    ventana_crear_tabla.resizable(False,False)

    tk.Label(ventana_crear_tabla, text="Nombre de la Tabla:").place(x=120, y=20)
    entry_nombre_tabla = tk.Entry(ventana_crear_tabla)
    entry_nombre_tabla.place(x=120, y=40)
    columnas = []

        
    def agregar_columna(nombre, tipo, columnas):
        if nombre == "" or  tipo=="":
            messagebox.showerror("Error", "Hay campos vacíos")
        else:
            columnas.append({'nombre': nombre, 'tipo': tipo})
            messagebox.showinfo("Correcto", "Se ha agregado la columna")
        

    tk.Label(ventana_crear_tabla, text="Nombre de la columna").place(x=120, y=70)
    entry_nombre_columna = tk.Entry(ventana_crear_tabla)
    entry_nombre_columna.place(x=120, y=90)
    tk.Label(ventana_crear_tabla, text="Tipo de la columna").place(x=120, y=110)
    entry_tipo_columna = tk.Entry(ventana_crear_tabla)
    entry_tipo_columna.place(x=120, y=130)

    button_agregar = tk.Button(ventana_crear_tabla, text="Agregar Columna", command=lambda:agregar_columna(entry_nombre_columna.get(), entry_tipo_columna.get(), columnas))
    button_agregar.place(x=120, y=160)

    ttk.Button(ventana_crear_tabla, text="Crear tabla", command=lambda:conexionBDD.crear_tabla(entry_nombre_tabla.get(), columnas)).place(x=120, y=200)

    ttk.Button(ventana_crear_tabla, text="Volver", command=ventana_crear_tabla.destroy).place(x=200, y=200)

if __name__ == "__main__":
    administrarTablas()