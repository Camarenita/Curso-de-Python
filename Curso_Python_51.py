# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:01:46 2022

@author: LALO
"""

#51)Manejo de excepciones


variable = 'Correcto.'

try:
    print(variable)
    print(variables)

except:
    print('Hay un error')
    
    
reinicio = True

while reinicio:
    try:
        num1 = int(input('Introducir un numero para multiplicar: '))
        num2 = int(input('Introducir otro numero para multiplicar: '))
    except ValueError:
        print('Ese no es un numero. Vuelve a intentarlo')
    else:
        print('El resultado es:', num1*num2)
    finally:
        pregunta = input('Quieres seguir? introduce S/N:\n')
    if pregunta == 'N':
        reinicio = False
    else:
        print('De acuerdo, vamos a seguir multiplicando')