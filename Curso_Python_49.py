# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:59:44 2022

@author: LALO
"""

#49)Expresiones regulares .split() .sub()

import re

texto =  'Aquellos que no conocen la historia estan condenados a repetirla - Edmund Burke'

resultado = re.split(' ', texto) #guarda todo menos lo que pongan entre comillas
print(resultado)

resultado = re.split(' ', texto, 4)#maxsplit al encontrar la cuarta cooincidencia para y lo demas lo deja en un solo string
print(resultado)

resultado = re.sub(' ', '-', texto) #sustituye el primer valor con el segundo
print(resultado)

resultado = re.sub(' ', '---', texto)
print(resultado)

resultado = re.sub(' ', '---', texto,4) #Limita las veces que se sustituye el valor
print(resultado)