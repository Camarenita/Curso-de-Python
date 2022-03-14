# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:52:23 2022

@author: LALO
"""

#31)Diccionarios I

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

consulta = teclado1['Modelo'],teclado1['Precio'],teclado2['Modelo'],teclado2['Precio']
print(consulta)

muestraTeclado = dict(teclado1)
print(muestraTeclado)