import customtkinter as ctk

class VistaJuego:
   def __init__(self, master):
       self.master = master
       super().__init__(master)
       self.on_celda_pulsada = None
       self.on_nueva_partida = None
       self.on_salir = None
       self.botones = []

       self.titulo = ctk.CTkLabel
       self.titulo.grid(column=0, row=0)
       self.puntos = ctk.CTkLabel
       self.puntos.grid(column=1, row=0)
       self.intentos = ctk.CTkLabel
       self.intentos.grid(column=2, row=0)
       self.mensajes = ctk.CTkLabel
       self.mensajes.grid(column=3, row=0)
       self.frame = ctk.CTkFrame
       self.frame.grid(column=1, row=0)