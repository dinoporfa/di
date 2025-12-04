import random

class JuegoTopo:
   def __init__(self, root):
       self.root = root

       self.total_intentos = 10
       self.num_celdas = 9
       self.intentos_restantes = 10
       self.puntos = 0
       self.celda_topo = 0

   def get_puntos(self):
       return self.puntos

   def get_intentos_restantes(self):
       return self.intentos_restantes

   def nueva_partida(self):
       self.puntos = 0
       self.intentos_restantes = self.total_intentos
       self.generar_una_celda()

   def generar_una_celda(self):
       self.celda_topo = random.randint(0, self.num_celdas - 1)

   def provar_celda(self, indice: int) -> dict:
       self.intentos_restantes = self.intentos_restantes - 1
       if indice == self.celda_topo:
           self.puntos = self.puntos + 1
           acierto = True
       else:
           acierto = False
       if self.intentos_restantes == 0:
           self.nueva_partida()
           fin = True
       else:
           self.intentos_restantes = self.intentos_restantes - 1
           self.celda_topo = random.randint(0, self.num_celdas - 1)
           fin = False
       return {'acierto': acierto, 'fin': fin}