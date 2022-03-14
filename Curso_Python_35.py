# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:54:15 2022

@author: LALO
"""

#35)Argumentos arbitrarios

def alumnos(*args): #Cualquier nombre y ahi se guardaran las variables que mandes
    print('El ultimo alumno es: ' + args[-1] + ' el primero es: ' + args[0])

alumnos('Julia','Pedro','Francisco','Eduardo')

def alumnos_profesores(profesor,sustituto, *args):
    print('Profesor: '+profesor)
    print('Sustituto: '+sustituto)
    for x in args:
        print('Alumno: '+x)
        
lista_alumnos = ('Julia','Pedro','Francisco','Eduardo')
alumnos_profesores('Antonio', 'Amador', *lista_alumnos)