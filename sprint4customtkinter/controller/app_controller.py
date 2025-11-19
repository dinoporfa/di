from model import usuario_model
from view import main_view

class AppController:
    def __init__(self, app):
        self.view = main_view.MainView
        self.model = usuario_model.Usuario

        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar(self.model.Usuario)
        self.view.actualizar_lista_usuarios(self.view, usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        self.view.mostrar_detalles_usuario(self.view, indice)