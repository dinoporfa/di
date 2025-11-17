import tkinter as tk
from tkinter import messagebox

def axuda():
    messagebox.showinfo("Axuda", "Mensaxe de axuda")

def abrir_arquivo():
    messagebox.showinfo("Arquivo", "Arquivo aberto")

def sair():
    root.quit()

root = tk.Tk()
root.geometry("200x100")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)


menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Arquivo", command=abrir_arquivo)
menu_arquivo.add_command(label="Saír", command=sair)


menu_axuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Axuda", menu=menu_axuda)
menu_axuda.add_command(label="Acerca de", command=axuda)


root.mainloop()