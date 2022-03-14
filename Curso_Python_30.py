# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:48:57 2022

@author: LALO
"""

#30)Bucle for range

for x in range(10):
    print(x)
    
for x in range(5,10):
    print(x)
    
for x in range(5,25,2):
    print(x)
    
print('Lista de numeros:\n')

numeros = [2,4,8,16,32,64,128]

for x in range(len(numeros)):
    print('Numero de operacion ->',x,' Multiplicacion ->',numeros[x],'Resultado: ->',numeros[x]*numeros[x])
       
for x in range(10):
    print(x)
else:
    print('Se acabo el bucle for...')
    
num1 = ['1','2','3','4','5']
num2 = '0'
num3 = '0'

for x in num1:
    for y in num2:
        print(x + y)

for x in num1:
    for y in num2:
        for z in num3:
            print(x + y + z)