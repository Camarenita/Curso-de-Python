# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:58:38 2022

@author: LALO
"""

#44)Importar modulos y funciones lambda

import math

def area(radio):
    resultado = round(math.pi * radio * radio, 2)
    print(resultado)
    
area(2)

area = lambda radio: round(math.pi * radio * radio, 2)

print(area(2))