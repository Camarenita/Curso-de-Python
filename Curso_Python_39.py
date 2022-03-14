# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:55:01 2022

@author: LALO
"""

#39)Cambiar valores de objetos

class Usuarios2:
    def __init__(self,nombre,edad): #El self puede ser cambiado por cualquier otro nombre
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios2('Julian', 56)
usuario1.muestra_datos()

usuario1.edad = 65
usuario1.muestra_datos()