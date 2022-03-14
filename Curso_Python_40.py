# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:56:36 2022

@author: LALO
"""

#40)Clases vacias y eliminar objetos

class nombreClase(): #Puedes quitar los parentesis 
    pass

class Usuarios3:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios3('Enrique', 28)

print(usuario1.nombre, usuario1.edad)

del usuario1.edad #Elimina la edad
del usuario1 #Elimina el objeto usuario 1