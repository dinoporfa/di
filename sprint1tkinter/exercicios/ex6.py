import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()
    elementos = [listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Seleccionaches: {', '.join(elementos)}")

root = tk.Tk()
root.geometry("300x250")

opcions = ["Mazá", "Plátano", "Laranxa"]

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for opcion in opcions:
    listbox.insert(tk.END, opcion)
listbox.pack(pady=10)

boton = tk.Button(root, text="Mostrar selección", command = mostrar_seleccion)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="Seleccionaches: Ningún")
etiqueta.pack(pady=10)

root.mainloop()