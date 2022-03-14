# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:58:47 2022

@author: LALO
"""

#45)Modulo Datetime

import datetime

fecha = datetime.datetime.now()

print(fecha)

fecha = datetime.datetime(2020,9,29,10,50,45)

print(fecha)

fecha = datetime.datetime.now()

print('Año',fecha.year)
print('Mes',fecha.month)
print('Día',fecha.day)