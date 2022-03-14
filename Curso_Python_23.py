# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:46:34 2022

@author: LALO
"""

#23)Condicional Elif
    
edad = int(input('Cual es tu edad?\n'))

if edad <= 0:
    print('No puedes tener esa edad')

elif edad >= 1 and edad <= 17:
    print('Eres menor de edad')
    
elif edad <=100:
    print('Eres mayor de edad')
    
else:
    print('Edad no valida')