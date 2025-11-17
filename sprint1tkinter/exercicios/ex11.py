import tkinter as tk

def actualizar_valor(i):
    etiqueta.config(text=f"Valor: {i}")

root = tk.Tk()
root.geometry("300x300")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack(pady=20)

etiqueta = tk.Label(root, text="Valor: 0")
etiqueta.pack(pady=10)

root.mainloop()