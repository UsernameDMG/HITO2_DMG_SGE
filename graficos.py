import tkinter as tk
from tkinter import * 
from tkinter import ttk
import conexionBDD

def iramenu(raiz: Tk):
    from Menu import abrirMenu   
    raiz.destroy()
    abrirMenu()

def abrirGrafico():
    raiz = Tk()
    raiz.title("Mostrar graficos")
    raiz.geometry("400x100")
    raiz.resizable(False,False)
    ttk.Label(raiz, text="Elige el tipo de grafico").place(x=40, y=30)
    tabla = ttk.Combobox(values=["Grafico de barra", "Grafico de pastel"])
    tabla.place(x=40,y=50)
    ttk.Button(raiz, text="Ver grafico", command=lambda:conexionBDD.verGraficos(tabla.get())).place(x=200, y=50)
    ttk.Button(raiz, text="Volver", command=lambda:iramenu(raiz)).place(x=280,y=50)
    raiz.mainloop()

if (__name__ == "__main__"):
    abrirGrafico()
     
