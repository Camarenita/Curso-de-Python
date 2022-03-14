# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:48:25 2022

@author: LALO
"""

#29)Bucle FOR

for x in 'Python':
    print(x)
    
cursos = ['Java','C++','C','Python']
 
for x in cursos:
     print(x)
     
for x in cursos:
    if x == 'C++':
        continue
    if x == 'C':
        break
    print(x)
    
for x in []:
    pass