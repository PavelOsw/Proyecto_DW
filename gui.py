from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

# from filtros import win2

win1 = Tk()
win1.config(width=400, height=500)
win1.title("Ferretería")


frame = Frame(win1)
frame.pack(pady = 5)
frame.place(x = 25, y = 50)

vista = ttk.Treeview(frame)

# ttk.Label(win1, text = "Ferretaría").place(x=25, y=5)

img_1 = Image.open("img/logo_2.png")
img_1 = img_1.resize((150, 150), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img_1)
logo1 = ttk.Label(image=test)
logo1.image = test
logo1.place(x=25, y=5)

# menuFiltro = ttk.Combobox(win1, state="readonly", values=["", ""])
# menuFiltro.place (x =25, y = 25)

def clear():
    vista.delete(*vista.get_children())

# def win_reportes():
#     clear()
#     # win2

btnAccion1 = ttk.Button(win1, text = "Base de datos", command='')
btnAccion1.place(x=150, y= 200)

btnAccion2 = ttk.Button(win1, text = "Reportes", command='win_reportes')
btnAccion2.place(x=150, y= 300)

btnSalir = ttk.Button(win1, text = "Salir", command='exit')
btnSalir.place(x=150, y= 400)


def exit():
    win1.destroy

win1.mainloop()