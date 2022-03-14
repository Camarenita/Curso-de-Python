# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:51:09 2022

@author: LALO
"""

#27)Bucle while

x = 1

while x <= 10:
    print(x)
    x += 1
    
frase = 'Lo que escribas lo repito: '
frase += '\nIntroduce el comando "salir" para finalizar el proframa.\n'

mensaje = ''

while mensaje != 'salir':
    mensaje = input(frase)
    print (mensaje)
    
print('Has salido del bucle')