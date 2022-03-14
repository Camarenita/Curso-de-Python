# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:54:42 2022

@author: LALO
"""

#37)Clases y Objetos

class Naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = 'Negro'
    color2 = 'Rojo'
    motores = 4
    activada = False
    compueta_principal = False
    sistema_defensa = True
    autodestruccion = False
    
    def encender(self):
        self.activada = True
        
    def apagar(self):
        self.activada = False
        
    def abrir_compuerta(self):
        self.compueta_principal = True
        
    def cerrar_compuerta(self):
        self.compueta_principal = False
        
    def  desactivar_defensas(self):
        self.sistema_defensa = False
        
    def  activar_defensas(self):
        self.sistema_defensa = True
        
    def activar_autodestruccion(self):
        self.autodestruccion = True
        print('Protocolo de autodestruccion activado...')
        
    def estado_motores(self):
        if(self.activada):
            return 'Motores trabajando al 100%'
        else:
            return 'Motores apagados'
    
    def estado_compuerta(self):
        if (self.compueta_principal):
            return 'La compuerta esta abierta'
        else:
            return 'La compuerta esta cerrada'
        
    def estado_defensa(self):
        if(self.sistema_defensa):
            return 'El sistema de defensa esta activado'
        else:
            return 'Peligro! El sistema de defensa esta desactivado'
        
#Creando el primer objeto de naves

nave1 = Naves()

#Comandos al objeto

#Encender
nave1.encender()

#Estado de los motores
print(nave1.estado_motores())

#Apagar 
nave1.apagar()

#Actualizacion de estado de los motores
print(nave1.estado_motores())

#Abre la compuerta
nave1.abrir_compuerta()

#Estado de la compuerta
print(nave1.estado_compuerta())

#Cierra la compuerta
nave1.cerrar_compuerta()

#Actualizacion de estado de la compuerta
print(nave1.estado_compuerta())

#Estado de las defensas
print(nave1.estado_defensa())

#Desactiva las defensas 
nave1.desactivar_defensas()

#Actualizacion de estado de las defensas
print(nave1.estado_defensa())

#Ejecuta la autodestruccion de la nave
nave1.activar_autodestruccion()