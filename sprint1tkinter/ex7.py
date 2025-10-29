import tkinter as tk

def crear_canvas():
    canvas.create_rectangle(50, 50, f"{entrada1.get()}", f"{entrada2.get()}", outline="red")

root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, width=300, height=150, bg="white")
canvas.pack()

etiqueta1 = tk.Label(root, text="Inroduce x1:")
etiqueta1.pack()

entrada1 = tk.Entry(root)
entrada1.pack()

etiqueta2 = tk.Label(root, text="Inroduce y1:")
etiqueta2.pack()

entrada2 = tk.Entry(root)
entrada2.pack()

etiqueta3 = tk.Label(root, text="Inroduce x2:")
etiqueta3.pack()

entrada3 = tk.Entry(root)
entrada3.pack()

etiqueta4 = tk.Label(root, text="Inroduce y2:")
etiqueta4.pack()

entrada4 = tk.Entry(root)
entrada4.pack()

boton = tk.Button(root, text="Crear formas", command=crear_canvas())
boton.pack()



root.mainloop()