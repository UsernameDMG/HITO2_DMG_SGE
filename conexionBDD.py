import sqlite3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt


def crearTablas():
    con = sqlite3.connect("BDD_DMG.db")
    con.execute("CREATE TABLE IF NOT EXISTS Categoria (id_categoria INT PRIMARY KEY,nombre VARCHAR(50),descripcion VARCHAR(255))")
    con.execute("CREATE TABLE IF NOT EXISTS Cliente (id_cliente INT PRIMARY KEY,nombre VARCHAR(100),correo VARCHAR(100),direccion VARCHAR(255))")
    con.execute("CREATE TABLE IF NOT EXISTS Producto (id_producto INT PRIMARY KEY,nombre VARCHAR(100),id_categoria INT,precio_unitario DECIMAL(10, 2),stock_actual INT,FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria));")
    con.execute("CREATE TABLE IF NOT EXISTS Pedido (id_pedido INT PRIMARY KEY,id_cliente INT,fecha_pedido VARCHAR(70),estado VARCHAR(50),FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente));")
    con.execute("CREATE TABLE IF NOT EXISTS Detalle (id_detalle INT PRIMARY KEY,id_pedido INT,id_producto INT,cantidad INT,precio_unitario DECIMAL(10, 2),FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),FOREIGN KEY (id_producto) REFERENCES Producto(id_producto));")
    con.close()
crearTablas()

def verGraficos(opcion):
    if opcion == "":
        messagebox.showerror("Error", "Hay algún campo vacío")
    else:
        con = sqlite3.connect("BDD_DMG.db")

        try:
            if opcion == "Grafico de barra":
                cursor = con.execute("SELECT direccion, COUNT(*) as TotalClientes FROM Cliente GROUP BY direccion")
                datos = cursor.fetchall()

                if not datos:
                    messagebox.showinfo("Info", "No hay datos para generar el gráfico.")
                    return
                df = DataFrame(datos, columns=['Direccion', 'TotalClientes'])

                plt.bar(df['Direccion'], df['TotalClientes'])
                plt.title('Clientes por Dirección')
                plt.xlabel('Dirección')
                plt.ylabel('Número de Clientes')

            elif opcion == "Grafico de pastel":
                cursor = con.execute("SELECT COUNT(*) as TotalClientes, direccion FROM Cliente GROUP BY direccion")
                datos = cursor.fetchall()

                if not datos:
                    messagebox.showinfo("Info", "No hay datos para generar el gráfico.")
                    return
                df = DataFrame(datos, columns=['TotalClientes', 'Direccion'])
                plt.pie(df['TotalClientes'], labels=df['Direccion'], autopct='%1.1f%%', startangle=140)
                plt.title('Porcentaje de Clientes por Dirección')

            else:
                messagebox.showerror("Error", "Opción no válida")
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error al generar el gráfico: {str(e)}")

        finally:
            con.close()


    
def borrar_tabla(nombre_tabla):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        con.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
        con.commit()
    except:
        messagebox.showerror("Error", "No se pudo borrar la tabla")
        con.close()
        return
    messagebox.showinfo("Éxito", "Tabla borrada correctamente.")
    con.close()

def crear_tabla(nombre_tabla, columnas):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        columns_str = ", ".join(f"{col['nombre']} {col['tipo']}" for col in columnas)
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({columns_str})"
        con.execute(create_table_sql)
        con.commit()
        
    except:
        messagebox.showerror("Error","No se pudo crear la tabla")
        con.close()
        return
    messagebox.showinfo("Éxito","Tabla creada correctamente")
    con.close()


def exportarExcel():
    con = sqlite3.connect("BDD_DMG.db")
    try:
        cursor = con.execute("Select * from Cliente")
        datos = cursor.fetchall()
        df = DataFrame(datos, columns=[desc[0] for desc in cursor.description])
        df.to_excel('consulta_cliente.xlsx')    
    except:
        messagebox.showerror("Error","Se ha producido un error al exportar los datos a excel")
        return
    messagebox.showinfo("Correcto", "Datos importados a excel con exito")
    x = ["1 de enero de 2021", "1 de julio de 2020", "1 de enero de 2020"]
    y = [35.564, 47.344, 23.318]
    plt.bar(x, y)
    plt.title('Gráfico de Barras')
    plt.xlabel('Etiqueta del Eje X')
    plt.ylabel('Etiqueta del Eje Y')
    plt.show()


def ingresarRegistroCategoria(id_categoria, nombre, descripcion):
    con = sqlite3.connect("BDD_DMG.db")
    secuencia = "Insert into Categoria(id_categoria, nombre, descripcion) VALUES (?,?,?)"
    try:
        sql = (id_categoria, nombre, descripcion)
        con.execute(secuencia, sql)
    except:
        messagebox.showerror("Error","Se ha producido un error al insertar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro añadido")

def ingresarRegistroCliente(DNI, nombre, correo, direccion):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = "Insert into Cliente(id_cliente, nombre, correo, direccion) VALUES (?,?,?,?)"
        sql = (DNI, nombre, correo, direccion)
        con.execute(secuencia, sql)
    except:
        messagebox.showerror("Error","Se ha producido un error al insertar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro añadido")

def ingresarRegistroPedido(id_pedido, id_cliente, fecha_pedido, estado):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = "Insert into Pedido(id_pedido, id_cliente, fecha_pedido, estado) VALUES (?,?,?,?)"
        sql = (id_pedido, id_cliente, fecha_pedido, estado)
        con.execute(secuencia, sql)
    except:
        messagebox.showerror("Error","Se ha producido un error al insertar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro añadido")

def ingresarRegistroProducto(id_producto, nombre, id_categoria, precio_unitario, stock_actual):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = "Insert into Producto(id_producto, nombre, id_categoria, precio_unitario, stock_actual) VALUES (?,?,?,?,?)"
        sql = (id_producto, nombre, id_categoria, precio_unitario, stock_actual)
        con.execute(secuencia, sql)
    except:
        messagebox.showerror("Error","Se ha producido un error al insertar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro añadido")

def ingresarRegistroDetalle(id_detalle, id_pedido, id_producto, cantidad, precio_unitario):
    try:
        con = sqlite3.connect("BDD_DMG.db")
        secuencia = "Insert into Detalle(id_detalle, id_pedido, id_producto, cantidad, precio_unitario) VALUES (?,?,?,?,?)"
        sql = (id_detalle, id_pedido, id_producto, cantidad, precio_unitario)
        con.execute(secuencia, sql)
    except:
        messagebox.showerror("Error","Se ha producido un error al insertar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro añadido")

def modificarRegistroCategoria(id_categoria, nombre, descripcion):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = f"update Categoria set id_categoria = '{id_categoria}', nombre = '{nombre}', descripcion = '{descripcion}' where id_categoria = '{id_categoria}'"
        con.execute(secuencia)
    except:
        messagebox.showerror("Error","Se ha producido un error al modificar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro modificado")

def modificarRegistroCliente(DNI, nombre, correo, direccion):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = f"update Cliente set id_cliente = '{DNI}', nombre = '{nombre}', correo = '{correo}', direccion = '{direccion}' where direccion = '{direccion}'"
        con.execute(secuencia)
    except:
        messagebox.showerror("Error","Se ha producido un error al modificar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro modificado")

def modificarRegistroPedido(id_pedido, id_cliente, fecha_pedido, estado):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = f"update Pedido set id_pedido = '{id_pedido}', id_cliente = '{id_cliente}', fecha_pedido = '{fecha_pedido}', estado='{estado}' where id_pedido = '{id_pedido}'"
        con.execute(secuencia)
    except:
        messagebox.showerror("Error","Se ha producido un error al modificar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro modificado")

def modificarRegistroProducto(id_producto, nombre, id_categoria, precio_unitario, stock_actual):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = f"update Producto set id_producto = '{id_producto}', nombre = '{nombre}', id_categoria = '{id_categoria}', precio_unitario='{precio_unitario}', stock_actual = '{stock_actual}' where id_producto = '{id_producto}'"
        con.execute(secuencia)
    except:
        messagebox.showerror("Error","Se ha producido un error al modificar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro modificado")

def modificarRegistroDetalle(id_detalle, id_pedido, id_producto, cantidad, precio_unitario):
    con = sqlite3.connect("BDD_DMG.db")
    try:
        secuencia = f"update Detalle set id_detalle = '{id_detalle}', id_pedido = '{id_pedido}', id_producto = '{id_producto}', cantidad = '{cantidad}', precio_unitario='{precio_unitario}' where id_detalle = '{id_detalle}'"
        con.execute(secuencia)
    except:
        messagebox.showerror("Error","Se ha producido un error al modificar el registro")
        con.close()
        return
    con.commit()
    con.close()
    messagebox.showinfo("Correcto", "Registro modificado")


def eliminarRegistros(tabla, clave, datos):
    con = sqlite3.connect("BDD_DMG.db")
    if (tabla != "" and clave != "" and datos != ""):
        try:
            secuencia = f"DELETE FROM {tabla} WHERE {clave} = '{datos}'"
            con.execute(secuencia)
        except:
            messagebox.showerror("Error", "No se ha podido eliminar el registro")
            con.close()
            return
        messagebox.showinfo("Correcto", "Registro borrado")
        con.commit()
        con.close()
    else:
        messagebox.showwarning("Atencion", "Hay algun campo sin rellenar")

def verRegistros(texto: tk.Text,tabla, campo, dato, orden):
    texto.config(state="normal")
    con = sqlite3.connect("BDD_DMG.db")
    cur = con.cursor()
    texto.delete("1.0", "end")
    if(tabla!=""):

        if (campo == "" and orden == ""):
            secuencia = f"SELECT * FROM {tabla}"
            cur.execute(secuencia)
        elif (campo != "" and orden =="" and dato != "") :
            try:
                secuencia = f"SELECT * FROM {tabla} where {campo}='{dato}'"
                cur.execute(secuencia)
            except:
                messagebox.showerror("Error","Se ha producido un error en la búsqueda")
        elif (campo == "" and orden !=""):
            try:
                secuencia = f"SELECT * FROM {tabla} order by {orden}"
                cur.execute(secuencia)
            except:
                messagebox.showerror("Error","Se ha producido un error en la búsqueda")
        elif (campo != "" and orden !="" and dato != ""):
            try:
                secuencia = f"SELECT * FROM {tabla} WHERE {campo} = '{dato}' order by {orden}"
                cur.execute(secuencia)
            except:
                messagebox.showerror("Error","Se ha producido un error en la búsqueda")

        rows = cur.fetchall()
        if(rows != []):
            for row in rows:
                texto.insert(tk.INSERT,row)
                texto.insert(tk.INSERT, "\n")
            texto.config(state="disabled")