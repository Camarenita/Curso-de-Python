# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:01:35 2022

@author: LALO
"""

#50)Expresiones regulares

#Secuencias especiales
#\A	Devuelve una coincidencia si los caracteres especificados se encuentran al principio de la cadena.	"\ABienvenidos"
#\b	Devuelve una coincidencia si los caracteres especificados se encuentran al principio o al final de una palabra.	"Bienvenidos\b"
#\B	Devuelve una coincidencia si los caracteres especificados se encuentran entre una palabra, pero no al principio o al final.	"veni\B"
#\d	Devuelve una coincidencia si el string contiene dígitos del 0 al 9.	"\d"
#\D	Devuelve una coincidencia si en el string no hay ningún dígito.	"\D"
#\s	Devuelve una coincidencia si en el string hay al menos un espacio en blanco.	"\s"
#\S	Devuelve una coincidencia si en el string no hay ningún espacio en blanco.	"\S"
#\w	Devuelve una coincidencia si el string contiene cualquier carácter de la a a la z, dígitos del 0 al 9 o la barra baja "_"	"mundo$"
#\W	Devuelve una coincidencia si el string no contiene cualquier carácter de la letra a a la z.	"es*"
#\Z	Devuelve una coincidencia si los carácteres especificados están al final del string.	"fácil\Z"


import re

texto = 'siete septimos son siete septimas mas de los que tienes 7'

resultado = re.findall('\Asiete', texto)
print(resultado)

resultado = re.findall('\Ason', texto)
print(resultado)

resultado = re.findall('\D', texto)
print(resultado)

#Metacaracteres
#[]	Un conjunto de caracteres.	"[a-z]"
#{}	Especifican un número determinado de resultados. En el ejemplo el {2} representa dos letras o.	"zo{2}lógico"
#()	Agrupan patrones.	
#\	Se utiliza para especificar una secuencia especial.	"\A"
#|	Se utiliza para especificar que encuentre un resultado u otro.	"par|impar"
#.	Caracter comodin, reemplaza cualquier caracter.	"programa..ón fác.l"
#^	Comienza con lo que le escribas.	"^hola"
#$	Termina con lo que le escribas.	"mundo$"
#*	Ninguno o más resultados.	"es*"
#+	Uno o más resultados.	"es+"

resultado = re.findall('sep..mos', texto)
print(resultado)

resultado = re.findall('septimos|septimas|siete|adsja', texto)
print(resultado)

resultado = re.findall('[a-p]', texto)
print(resultado)