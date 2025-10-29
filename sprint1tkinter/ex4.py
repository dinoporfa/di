import tkinter as tk

root = tk.Tk()
root.geometry("300x150")

def mostrar_seleccion():
    seleccion1 = var_check1.get()
    seleccion2 = var_check2.get()
    seleccion3 = var_check3.get()
    estado1 = " escoitar música" if seleccion1 else ""
    estado2 = ", facer deporte" if seleccion2 else ""
    estado3 = ", ler" if seleccion3 else ""
    etiqueta.config(text= f"Gústame: {estado1} {estado2} {estado3}")


var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()

check1 = tk.Checkbutton(root, text = "Música", variable = var_check1, command = mostrar_seleccion)
check1.pack()
check2 = tk.Checkbutton(root, text = "Deporte", variable = var_check2, command = mostrar_seleccion)
check2.pack()
check3 = tk.Checkbutton(root, text = "Ler", variable = var_check3, command = mostrar_seleccion)
check3.pack()

etiqueta = tk.Label(root, text= "Gústame: ")
etiqueta.pack(pady=10)

root.mainloop()