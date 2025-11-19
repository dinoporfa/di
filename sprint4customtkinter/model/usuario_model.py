class Usuario:
    nombre = ""
    edad = 0
    genero = ""
    avatar = 0
    def __init__(self, root):
        self.root = root
        self.usuarios = []

        self.cargar_datos_exemplo()

    def cargar_datos_exemplo(self):
        self.nombre = "pablo"
        self.edad = 20
        self.genero = "masculino"
        self.usuarios.append(self.nombre)
        self.usuarios.append(self.edad)
        self.usuarios.append(self.genero)
        self.usuarios.append(self.avatar)

        self.nombre = "alejandro"
        self.edad = 20
        self.genero = "outro"
        self.usuarios.append(self.nombre)
        self.usuarios.append(self.edad)
        self.usuarios.append(self.genero)
        self.usuarios.append(self.avatar)

    def listar(self):
        for usuario in self.usuarios:
            print(usuario)
