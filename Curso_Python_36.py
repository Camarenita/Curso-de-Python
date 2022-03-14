# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:54:29 2022

@author: LALO
"""

#36)Diccionarios arbitrarios

def colores(color1,color2,color3,color4):
    print('Este es el color: '+color1+'.')

def colores2(**kwargs):
    print('Este es el color: '+kwargs['color1']+'.')

colores(color1='rojo', color2='azul', color3='verde', color4='amarillo')
colores2(color1='naranja', color2='azul', color3='verde', color4='amarillo')

def suma(x,y):
    return x + y

total = suma(10,10)
print(total)

def resta(x,y):
    return x - y

total = resta(10,5)
print(total)

def mul(x,y):
    return x * y

total = mul(10,10)
print(total)

def div(x,y):
    return x / y

total = div(10,10)
print(total)

def nohacenada():
    pass

def colores3(color='rojo'):
    print('Mi color favorito es: '+color)
    
colores3('azul')
colores3()
colores3('verde')