# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:53:18 2022

@author: LALO
"""

#33)Diccionarios Metodos

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

print(len(teclado1) + len(teclado2))

teclado1.pop('Categoria')
del teclado1['Precio']
print(teclado1)
teclado1.clear()
print(teclado1)
del teclado1

teclado2['Color'] = 'Negro'
print(teclado2)

tecladoCopia = teclado2.copy()
print(tecladoCopia)
tecladoCopia2 = dict(teclado2)
print(tecladoCopia2)

teclado1 = dict(Categoria = 'Teclados',
                Modelo = 'HyperX Alloy FPS Pro',
                Precio = '89,99',
                ID = '001')
print(teclado1)

teclado3 = ('Categoria','Modelo','Precio')
vacia = 'Valor vacio'

teclado3 = dict.fromkeys(teclado3,vacia)
print(teclado3)

vistaTeclado = teclado1.keys()
print(vistaTeclado)

teclado1.update({'Color': 'Negro'})
print(teclado1)

if 'ID' in teclado1:
    print('El producto tiene un ID especifico')
else:
    print('El producto no tiene un ID especifico')
    
if 'ID' in teclado2:
    print('El producto tiene un ID especifico')
else:
    print('El producto no tiene un ID especifico')

teclados = {
    "teclado1" : {
        'Categoria': 'Teclados',
        'Modelo': 'HyperX Alloy FPS Pro',
        'Precio': '89,99',
        'ID': '001'
        },
    "teclado2" : {
        'Categoria': 'Teclados',
        'Modelo': 'Corsair K55 RGB',
        'Precio': '59,99'
        }
    }
print(teclados)
print(len(teclados))