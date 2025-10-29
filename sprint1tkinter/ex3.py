import tkinter as tk

def ex3():
    etiqueta1.config(text=f"Ola {entrada.get()}")

root = tk.Tk()
root.geometry("300x150")

etiqueta1 = tk.Label(root, text="Escribe teu nome:")
etiqueta1.pack()

entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text="Saudar", command=ex3)
boton.pack()

root.mainloop()