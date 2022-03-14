# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:59:20 2022

@author: LALO
"""

#47)Expresiones regulares .search()

import re

texto = 'Bienvenidos al infierno'

busqueda = re.search('i', texto)
print(busqueda)
busqueda = re.search('b', texto)
print(busqueda)
busqueda = re.search('Bienvenidos', texto)
print(busqueda)
busqueda = re.search('Bienbenidos', texto)
print(busqueda)
busqueda = re.search('Bienvenidos al infierno', texto)
print(busqueda)