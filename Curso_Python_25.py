# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:46:56 2022

@author: LALO
"""

#25)Multiples condiciones IF

print('Saludos guerrero, Que deseas comprar?\n\n'+
      'Items disponibles:\n\n'+
      'Espadas:\n\n'+
      '\t1.- Espada Nivel 1: 150 monedas de oro\n'+
      '\t2.- Espada Nivel 2: 1200 monedas de oro\n\n'+
      'Escudos:\n\n'+
      '\t3.- Escudo Nivel 1: 100 monedas de oro\n'+
      '\t4.- Escudo Nivel 2: 750 monedas de oro\n\n')

comprar = [1]
dinero = 1500

espadalvl1 = 150
espadalvl2 = 1200

escudolvl1 = 100
escudolvl2 = 750

if 0 in comprar or comprar == []:
    print('Especifica un numero entre 1 y 4')
    
if 1 in comprar:
    dinero = dinero - espadalvl1
    
if 2 in comprar:
    dinero = dinero - espadalvl2
    
if 3 in comprar:
    dinero = dinero - escudolvl1

if 4 in comprar:
    dinero = dinero - escudolvl2
    
else:
    print('Especifica un numero entre 1 y 4')

if dinero < 0:
    print('No te ajusta el diinero')
    
if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print('Te queda '+str(dinero)+' monedas de oro.')
    print('Se agrego el objeto a tu inventario')