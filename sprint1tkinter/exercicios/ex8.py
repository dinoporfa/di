import tkinter as tk

def borrar():
    etiqueta3.config(text="")

def mostrar():
    etiqueta3.config(text=f"{entrada1.get()}")

root = tk.Tk()
root.geometry("400x400")

frame1 = tk.Frame(root, bg="lightgrey",bd="2", relief="sunken")
frame1.pack(padx=20, pady=20, fill="both", expand=True)

etiqueta1 = tk.Label(frame1, text="Ola", bg="lightgrey")
etiqueta1.pack()

etiqueta2 = tk.Label(frame1, text="Inroduce algo:", bg="lightgrey")
etiqueta2.pack()

entrada1 = tk.Entry(frame1)
entrada1.pack()

frame2 = tk.Frame(frame1,bd="2", relief="raised")
frame2.pack(padx=20, pady=20, fill="both", expand=True)

boton1 = tk.Button(frame2, text="Ver algo", command=mostrar)
boton1.pack(pady=10)

etiqueta3 = tk.Label(frame2, text="")
etiqueta3.pack()

boton2 = tk.Button(frame2, text="borrar", command=borrar)
boton2.pack(pady=10)


root.mainloop()