# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:56:45 2022

@author: LALO
"""

#41)Herencias de clases

class Usuarios3:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)

class Usuarios_premium(Usuarios3):
    pass

usuario2 = Usuarios_premium('Pepe', 45)
usuario2.muestra_datos()