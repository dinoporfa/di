import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x600")

def gardar():
    messagebox.showinfo("Gardar lista", "Lista gardada")

def cargar():
    messagebox.showinfo("Cargar lista", "Lista cargada")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_lista = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Lista", menu=menu_lista)
menu_lista.add_command(label="Gardar lista", command=gardar)
menu_lista.add_command(label="Cargar lista", command=cargar)



etiqueta1 = tk.Label(root, text="Introduce teu nome:")
etiqueta1.pack(pady=10)

entrada_nome = tk.Entry(root)
entrada_nome.pack()

def actualizar_valor(i):
    etiqueta3.config(text=f"{i} anos")

etiqueta2 = tk.Label(root, text="Introduce túa idade")
etiqueta2.pack(pady=10)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack()

etiqueta3 = tk.Label(root, text="0 anos")
etiqueta3.pack()

etiqueta4 = tk.Label(root, text="Introduce teu xénero")
etiqueta4.pack(pady=10)

var_radio = tk.StringVar()
var_radio.set("Outro")

radio1 = tk.Radiobutton(root, text = "Masculino", variable = var_radio, value = "Masculino")
radio1.pack(pady = 5)
radio2 = tk.Radiobutton(root, text = "Femenino", variable = var_radio, value = "Femenino")
radio2.pack(pady = 5)
radio3 = tk.Radiobutton(root, text = "Outro", variable = var_radio, value = "Outro")
radio3.pack(pady = 5)



listbox = tk.Listbox(root, selectmode=tk.SINGLE)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

def añadir():
    usuarix = f"{entrada_nome.get()}, {etiqueta3.cget("text")}, {var_radio.get()}"
    listbox.insert(tk.END, usuarix)

boton_añadir = tk.Button(root, text="Añadir usuarix", command=añadir)
boton_añadir.pack()

def borrar():
    listbox.delete(listbox.curselection())

boton_borrar = tk.Button(root, text="Borrar usuarix", command=borrar)
boton_borrar.pack(pady=5)

def sair():
    root.quit()

boton_sair = tk.Button(root, text="Saír", command=sair)
boton_sair.pack()

listbox.pack(pady=10, fill="both", expand=True)
root.mainloop()


root.mainloop()