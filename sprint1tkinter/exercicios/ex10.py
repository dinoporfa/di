import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

cadro_texto = tk.Text(frame, wrap="none")
cadro_texto.grid(row=0, column=0, sticky="nsew")

scroll = tk.Scrollbar(frame, orient="vertical", command=cadro_texto.yview)
scroll.grid(row=0, column=1, sticky="ns")
cadro_texto.configure(yscrollcommand=scroll.set)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

def insertar_texto():
    cadro_texto.insert(tk.END, f"A Galipedia é o nome co que se coñece\npopularmente a Wikipedia en lingua galega.\nComezou a publicarse o 8 de marzo de 2003,\n é unha enciclopedia en liña de acceso libre,\ncon todos os seus contidos en aberto\ne editados de forma colectiva en\nlingua galega. O 4 de marzo de 2013, catro\ndías antes do décimo aniversario, superou os\n100 000 artigos, e actualmente ten un total de\n227.691. A comezos do ano 2013 usábanse\nxa 101 305 imaxes distintas."
                                    "\nO primeiro usuario rexistrouse o 8 de\nmarzo de 2003, ILVI, quen axiña comezou a\ntraballar na que sería a primeira versión da\nPortada. Catro días despois creou o primeiro\nartigo da base de datos: grupo.\nSeguiría con outras entradas como ou,\ncal, ciencias naturais, ciencias humanas,\nciencias ocultas, ciencias aplicadas e botánica.")

insertar_texto()


root.mainloop()