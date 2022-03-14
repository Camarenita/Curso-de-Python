# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:48:18 2022

@author: LALO
"""

#28)Bucle while como salir y continuar

x = 1

while x < 10:
    print(x)
    if x==5:
        print('x = 5')
        break
    x += 1
    
    
while x <= 10:
    print(x)
    x += 1
else:
    print('Se ha terminado el bucle')
    
while x <= 15:
    x += 1
    if x == 12 or x == 14:
        continue
    print(x)