import tkinter as tk
from tkinter import messagebox

class RexistroApp:
    def __init__(self, root):
        self.root = root

        def gardar():
            messagebox.showinfo("Gardar lista", "Lista gardada")

        def cargar():
            messagebox.showinfo("Cargar lista", "Lista cargada")

        self.menu_principal = tk.Menu(root)
        self.root.config(menu=self.menu_principal)
        self.menu_lista = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Lista", menu=self.menu_lista)
        self.menu_lista.add_command(label="Gardar lista", command=gardar)
        self.menu_lista.add_command(label="Cargar lista", command=cargar)

        self.etiqueta1 = tk.Label(root, text="Introduce teu nome:")
        self.etiqueta1.pack(pady=10)

        self.entrada_nome = tk.Entry(root)
        self.entrada_nome.pack()

        def actualizar_valor(i):
            self.etiqueta3.config(text=f"{i} anos")

        self.etiqueta2 = tk.Label(root, text="Introduce túa idade")
        self.etiqueta2.pack(pady=10)

        self.scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
        self.scale.pack()

        self.etiqueta3 = tk.Label(root, text="0 anos")
        self.etiqueta3.pack()

        self.etiqueta4 = tk.Label(root, text="Introduce teu xénero")
        self.etiqueta4.pack(pady=10)

        self.var_radio = tk.StringVar()
        self.var_radio.set("Outro")

        self.radio1 = tk.Radiobutton(root, text="Masculino", variable=self.var_radio, value="Masculino")
        self.radio1.pack(pady=5)
        self.radio2 = tk.Radiobutton(root, text="Femenino", variable=self.var_radio, value="Femenino")
        self.radio2.pack(pady=5)
        self.radio3 = tk.Radiobutton(root, text="Outro", variable=self.var_radio, value="Outro")
        self.radio3.pack(pady=5)

        self.boton_añadir = tk.Button(root, text="Añadir usuarix", command=self.añadir_usuarix)
        self.boton_añadir.pack()

        self.boton_borrar = tk.Button(root, text="Borrar usuarix", command=self.eliminar_usuarix)
        self.boton_borrar.pack(pady=5)

        self.boton_sair = tk.Button(root, text="Saír", command=self.salir)
        self.boton_sair.pack()

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)

        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.listbox.pack(pady=10, fill="both", expand=True)

    def añadir_usuarix(self):
        self.usuarix = f"{self.entrada_nome.get()}, {self.etiqueta3.cget("text")}, {self.var_radio.get()}"
        self.listbox.insert(tk.END, self.usuarix)

    def eliminar_usuarix(self):
        self.listbox.delete(self.listbox.curselection())

    def salir(self):
        self.root.quit()

root = tk.Tk()
root.geometry("400x600")
app = RexistroApp(root)
root.mainloop()