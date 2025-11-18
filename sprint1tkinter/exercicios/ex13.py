import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

def debuxar(event):
    canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, outline="red")

def borrar():
    canvas.delete("all")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", debuxar)
canvas.bind("<c>", borrar)

root.mainloop()