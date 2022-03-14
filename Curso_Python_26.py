# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:47:06 2022

@author: LALO
"""

#26)Tips para condicionales 

x = 100 #Se ve mas visible
y=200

print('Se ejecuta el if') if x > y else print('Se ejecuta el else') #En una sola linea solo para una instruccion

x = 100
y = 200
z = 300

if x < y and z > y:
    print('Se cumplen las condiciones')
else:
    print('No se cumple una o ninguna de las condiciones')
    
    
if x < y or z > y:
    print('Se cumplen las condiciones')
else:
    print('No se cumple ninguna de las condiciones')
    
if x < y: #Causa error sin el pass
    pass