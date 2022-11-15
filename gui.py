from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

root = Tk()
root.config(width=850, height=400)
root.title("Ferretería")


frame = Frame(root)
frame.pack(pady = 5)
frame.place(x = 25, y = 50)

vista = ttk.Treeview(frame)

ttk.Label(root, text = "Selecciona filtro: ").place(x=25, y=5)

# menuFiltro = ttk.Combobox(root, state="readonly", values=["", ""])
# menuFiltro.place (x =25, y = 25)

btnFiltro = ttk.Button(root, text = "Filtrar", command='')
btnFiltro.place(x=25, y= 300)

btnTabla = ttk.Button(root, text = "Todo", command='')
btnTabla.place(x=150, y= 300)

root.mainloop()