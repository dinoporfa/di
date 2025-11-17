import tkinter as tk

def crear_canvas():
    if entrada1.get()=="":
        float1 = 0.0
    else:
        float1 = float(entrada1.get())
    if entrada2.get()=="":
        float2 = 0.0
    else:
        float2 = float(entrada2.get())
    if entrada3.get()=="":
        float3 = 0.0
    else:
        float3 = float(entrada3.get())
    if entrada4.get()=="":
        float4 = 0.0
    else:
        float4 = float(entrada4.get())
    canvas.create_rectangle(float1, float2, float3, float4, outline="red")
    canvas.create_oval(float1, float2, float3, float4, outline="blue")

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

boton = tk.Button(root, text="Crear formas", command=crear_canvas)
boton.pack()



root.mainloop()