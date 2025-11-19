import customtkinter as ctk

class MainView:
    def __init__(self, root):
        self.root = root

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame
        self.lista_usuarios_scrollable.grid(column=0, row=0, pady=10, padx=10)
        self.label1 = ctk.CTkLabel
        self.label1.grid(column=1, row=0, pady=10, padx=10)
        self.label2 = ctk.CTkLabel
        self.label2.grid(column=1, row=1, pady=10, padx=10)
        self.label3 = ctk.CTkLabel
        self.label3.grid(column=1, row=2, pady=10, padx=10)
        self.label4 = ctk.CTkLabel
        self.label4.grid(column=1, row=3, pady=10, padx=10)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        self.label1.config(text=usuario.nome)
        self.label2.config(text=usuario.edad)
        self.label3.config(text=usuario.genero)
        self.label4.config(text=usuario.avatar)
