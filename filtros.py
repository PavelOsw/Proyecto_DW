from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import pandas as pd

win2 = Tk()
win2.config(width=850, height=400)
win2.title("Ferretería")

data = pd.read_csv('datos.csv')

frame = Frame(win2)
frame.pack(pady = 2)
frame.place(x = 25, y = 100)

vista = ttk.Treeview(frame)

img_1 = Image.open("img/logo_2.png")
img_1 = img_1.resize((75, 75), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img_1)
logo1 = ttk.Label(image=test)
logo1.image = test
logo1.place(x=25, y=1)

def clear():
    vista.delete(*vista.get_children())

def tabla():
    clear()
    
    vista["column"] = list(data.columns)
    vista["show"] = "headings"
    
    for column in vista["column"]:
        vista.heading(column, text=column)
       
    data_rows = data.to_numpy().tolist()
    for row in data_rows:
        vista.insert("", "end", values=row)
        
    
def filtros():
    clear()
    
    seleccion = menuFiltro.get()
    
    if seleccion == "Edad":
        Edades = data[['edad']].sort_values('edad')
        recuentoEdad = pd.crosstab(index = data['edad'], columns = 'Recuento de edades').sort_values('edad')
        filtroEdad = pd.merge(Edades, recuentoEdad, left_on='edad', right_on='edad')
        
        vista["column"] = list(filtroEdad.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text = column)
            
        data_rows = filtroEdad.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
    if seleccion == "Ocupación":
        Ocupaciones = data[['ocupacion']].sort_values('ocupacion')
        recuentoOcup = pd.crosstab(index = data['ocupacion'], columns = 'Recuento de ocupaciones').sort_values('ocupacion')
        filtroOcup = pd.merge(Ocupaciones, recuentoOcup, left_on='ocupacion', right_on='ocupacion')
        
        vista["column"] = list(filtroOcup.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text = column)
            
        data_rows = filtroOcup.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
    
tabla()
vista.pack()

ttk.Label(win2, text = "Selecciona filtro: ").place(x=600, y= 25)

menuFiltro = ttk.Combobox(win2, state="readonly", values=["Edad", "Ocupación"])
menuFiltro.place (x =600, y = 45)

btnFiltro = ttk.Button(win2, text = "Filtrar", command=filtros)
btnFiltro.place(x=25, y= 350)

btnTabla = ttk.Button(win2, text = "Todo", command=tabla)
btnTabla.place(x=150, y= 350)

win2.mainloop()