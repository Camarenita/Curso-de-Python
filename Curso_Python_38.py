# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:54:49 2022

@author: LALO
"""

#38)Metodo __init__

class Usuarios():
    
    def __init__(self,nombre,pin):
        self.nombre = nombre
        self.pin = pin
        
    def saludo(self):
        print('Saludos '+self.nombre+'. Iniciaste sesion correctamente')
        
    def despedida(self):
        print(self.nombre + ', cerraste sesion')
        
usuario1 = Usuarios('Toni', '1234')
usuario2 = Usuarios('Julia', '1452')

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()