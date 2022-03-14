# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:52:33 2022

@author: LALO
"""

#32)Diccionarios con bucle for

teclado1 = {
    'Categoria': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }
teclado2 = {
    'Categoria': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
    }

consulta = teclado1.get('Modelo'),teclado1['Precio'],teclado2['Modelo'],teclado2['Precio']
print(consulta)

teclado1['Precio'] = '85'
print(teclado1.get('Precio'))

for x in teclado2:
    print(x)
    
for x in teclado2:
    print(teclado2[x])
    
for x in teclado2.values():
    print(x)

for x,y in teclado2.items():
    print(x,y)