# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:59:31 2022

@author: LALO
"""

#48)Expresiones regulares .findall()

import re

texto = 'tres tristes tigres comen trigo en un trigal'

busqueda = re.findall('e', texto)
print(busqueda)

busqueda = re.findall('es', texto)
print(busqueda)

busqueda = re.findall('cuatro', texto)
print(busqueda)