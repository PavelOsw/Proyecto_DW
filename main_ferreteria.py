from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import pandas as pd

win2 = Tk()
win2.config(width=850, height=400)
win2.title("Ferretería")
    
productos = pd.read_csv('data/producto.csv')
pedidos = pd.read_csv('data/pedido.csv')
clientes = pd.read_csv('data/cliente.csv')
empleados = pd.read_csv('data/empleado.csv')

frame = Frame(win2)
frame.pack(pady = 2)
frame.place(x = 25, y = 100)

vista = ttk.Treeview(frame)

def clear():
    vista.delete(*vista.get_children())

def tabla():
    clear()

    #############################################
    filPedido = pedidos[['fecha']]
        
    vista["column"] = list(filPedido.columns)
    vista["show"] = "headings"
    
    for column in vista["column"]:
        vista.heading(column, text=column) 
        
    data_rows = filPedido.to_numpy().tolist()
    for row in data_rows:
        vista.insert("", "end", values = row)
    
def filtros():
    clear()
    seleccion = menuFiltro.get()
    
    ###################################################
    if seleccion == "Producto":
        rowsProducto = productos[['codigo','nombre_Producto']]
        rowsPedido = pedidos[['codigo','fecha']]
        
        Union = pd.merge(rowsProducto, rowsPedido, left_on = 'codigo', right_on = 'codigo')
        
        vista["column"] = list(Union.columns)
        vista["show"] = "headings"

        for column in vista["column"]:
            vista.heading(column, text=column) 
            
        data_rows = Union.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
        graph = Union.nombre_Producto.value_counts()
        graph.plot.barh()
        plt.show()
    ###################################################                    
    if seleccion == "Montos":
        rowsPedido = pedidos[['codigo', 'monto', 'fecha']]
        
        Union = rowsPedido
        
        vista["column"] = list(Union.columns)
        vista["show"] = "headings"

        for column in vista["column"]:
            vista.heading(column, text=column) 
            
        data_rows = Union.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
        
        graph = Union.monto.value_counts()
        graph.plot.barh()
        plt.show()
    
    ###################################################
    if seleccion == "Compras":
        rowsProducto = productos[['codigo','nombre_Producto']]
        rowsCliente = clientes[['codigo','nombre_Cliente']]
        
        Union = pd.merge(rowsCliente, rowsProducto, left_on = 'codigo', right_on = 'codigo')
        
        vista["column"] = list(Union.columns)
        vista["show"] = "headings"

        for column in vista["column"]:
            vista.heading(column, text=column) 
            
        data_rows = Union.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
        graph = Union.nombre_Cliente.value_counts()
        graph.plot.barh()
        plt.show()
            
    ###################################################
    if seleccion == "Ventas":
        rowsEmpleado = empleados[['codigo','id','nombre']]
        rowsPedido = pedidos[['codigo','descripcion']]
        
        Union = pd.merge(rowsEmpleado, rowsPedido, left_on = 'codigo', right_on = 'codigo')
        
        vista["column"] = list(Union.columns)
        vista["show"] = "headings"

        for column in vista["column"]:
            vista.heading(column, text=column) 
            
        data_rows = Union.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
        graph = Union.nombre.value_counts()
        graph.plot.barh()
        plt.show()    
            
    ###################################################        
    if seleccion == "Artículos":
        rowsPedido = pedidos[['codigo', 'fecha']]
        rowsProducto = productos[['codigo','nombre_Producto']]
        rowsCliente = clientes[['codigo','nombre_Cliente']]
        
        Union_1 = pd.merge(rowsCliente, rowsProducto, left_on = 'codigo', right_on = 'codigo')
        Union_2 = pd.merge(rowsPedido, Union_1, left_on = 'codigo', right_on = 'codigo')
        
        vista["column"] = list(Union_2.columns)
        vista["show"] = "headings"

        for column in vista["column"]:
            vista.heading(column, text=column) 
            
        data_rows = Union_2.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
        graph = Union.nombre_Producto.value_counts()
        graph.plot.barh()
        plt.show()
    
    
tabla()
vista.pack()

# Logo
img_1 = Image.open("img/logo_2.png")
img_1 = img_1.resize((75, 75), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img_1)
logo1 = ttk.Label(image=test)
logo1.image = test
logo1.place(x=25, y=1)

# Labels
ttk.Label(win2, text = "Selecciona filtro: ").place(x=400, y= 25)
ttk.Label(win2, text = "Selecciona período: ").place(x=600, y= 25)

# Combobox
menuFiltro = ttk.Combobox(win2, 
                          state =   "readonly", 
                          values = ["Producto", 
                                    "Montos",
                                    "Compras",
                                    "Ventas",
                                    "Artículos"]
                          )
menuFiltro.place (x =400, y = 45)
menuTiempo = ttk.Combobox(win2, 
                          state = "readonly", 
                          values = ["Último mes", 
                                    "Últimos 3 meses",
                                    "Primer semestre",
                                    "Últimos 5 años"]
                          )
menuTiempo.place (x =600, y = 45)

# Botones
btnFiltro = ttk.Button(win2, 
                       text = "Filtrar", 
                       command=filtros
                       )
btnFiltro.place(x=25, y= 350)
btnTabla = ttk.Button(win2, 
                      text = "Todo", 
                      command=tabla
                      )
btnTabla.place(x=150, y= 350)

win2.mainloop()