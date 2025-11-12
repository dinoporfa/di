import tkinter as tk

def mostrar_seleccion():
    seleccion = var_radio.get()
    root.configure(bg=f"{seleccion}")

root = tk.Tk()
root.geometry("300x150")


var_radio = tk.StringVar()
var_radio.set("Azul")

radio1 = tk.Radiobutton(root, text = "Azul", variable = var_radio, value = "blue", command = mostrar_seleccion)
radio1.pack(pady = 5)
radio2 = tk.Radiobutton(root, text = "Vermello", variable = var_radio, value = "red", command = mostrar_seleccion)
radio2.pack(pady = 5)
radio3 = tk.Radiobutton(root, text = "Verde", variable = var_radio, value = "green", command = mostrar_seleccion)
radio3.pack(pady = 5)

root.mainloop()