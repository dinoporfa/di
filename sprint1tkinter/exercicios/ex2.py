import tkinter as tk

def ex2():
    etiqueta1.config(text="Texto")

def ex():
    root.quit()

root = tk.Tk()
root.geometry("300x150")

etiqueta1 = tk.Label(root, text="")
etiqueta1.pack()

boton1 = tk.Button(root, text="Mostrar texto", command=ex2)
boton1.pack()

boton2 = tk.Button(root, text="Pechar", command=ex)
boton2.pack()

root.mainloop()