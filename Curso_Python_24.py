# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:46:43 2022

@author: LALO
"""

#24)Comprobar datos en listas y en tuplas

navegadores = ['chrome','firefox','opera','microsoft edge']
print('opera' in navegadores)
print('safari' in navegadores)

entrada = input('Introduce un navegador  ')

if entrada in navegadores:
    print("El navegador esta en la lista")
else:
    print('El navegador no esta en la lista')