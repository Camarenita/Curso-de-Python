# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:58:22 2022

@author: LALO
"""

#42)Heredar propiedades

class Usuarios4:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios4('Enrique', 28)

print(usuario1.nombre, usuario1.edad)

class Usuarios_premium2(Usuarios4):
    def __init__(self, nombre, edad, instagram):
        Usuarios4.__init__(self, nombre, edad)
        self.instagram = instagram
        
    def muestr_datos_premium(self):
        print('El nombre de usuario es: '+self.nombre, 'y tiene', self.edad, 'años. Su Instagram es:',self.instagram)
        
usuario2 = Usuarios_premium2('Elvira', 23, 'elvi_23')

usuario2.muestr_datos_premium()