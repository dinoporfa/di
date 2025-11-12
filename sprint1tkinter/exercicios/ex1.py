import tkinter as tk

def ex1():
    etiqueta3.config(text="Caramba")

root = tk.Tk()
root.title("Miña primeira app en Tkinter")
root.geometry("300x150")

etiqueta1 = tk.Label(root, text="Ola")
etiqueta1.pack()
etiqueta2 = tk.Label(root, text="Lois")
etiqueta2.pack()
etiqueta3 = tk.Label(root, text = "Este texto vai cambiar")
etiqueta3.pack()

boton = tk.Button(root, text="Cambiar texto", command=ex1)
boton.pack()

root.mainloop()