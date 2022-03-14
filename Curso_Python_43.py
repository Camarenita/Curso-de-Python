# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:58:31 2022

@author: LALO
"""

#43)Globales, locales y funciones anidades

def funcion1():
    variable1 = 'variable dentro de la funcion'
    print(variable1)
    
    def funcion2():
        variable1 = 'He cambiado el valor de la funcion'
        print(variable1)
        
    funcion2()
    
funcion1()

variable2 = 'Variable fuera de la funcion'

def funcion3():
    variable2 = 'Variable dentro de la funcion'
    print(variable2)

funcion3()
print(variable2)

num1 = 50
def funcion4():
    global num1
    num1 = 10000
    
funcion4()
print(num1)