# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:03:45 2022

@author: LALO
"""
#Curso de python

#2)Variables
mensaje = 'Bienvenido al curso de Python'

mensaje = 100

print(mensaje)

#3)Strings

texto = 'Esto es un "string"'

print(texto)


#4)Concatenar strings

primerapalabra = 'Hola'
segundapalabra = 'Que tal?'
todo = primerapalabra+' '+segundapalabra+'.'

print(todo)
print('Hola '+'Que tal?'+'.')


#5)Metodos .lower .upper .title

msj = "pAlabRas eN "

print(msj.title()+'Mayusculas Iniciales')

msj = msj.lower()

print(msj+'minusculas')

print(msj.upper()+'MAYUSCULAS TODAS')


#6)Saltos de linea y tabulaciones

print('Hola que tal')
print('Soy Lalo')
print('Mucho gusto')#Sin saltos de linea


print('\tHola que tal\nSoy Lalo\nMucho gusto')#Con saltos de linea 


#7)Operaciones
suma = 6+2
resta = 6-2
mult = 6*2
div = 6/2


print(suma)
print(resta)
print(mult)
print(div)
print(suma, resta, mult, div)

#8)Exponenciales

elvd = 2**2

print(elvd)

#9)Decimales y round

num1 = 4.1845
num2 = 15.25

res = num1+num2

print(res)
print(round(res,2))


#10)Listas/Arrays

smrtph = ['Xiaomi','Samsung','IPhone']

print(smrtph)
print(smrtph[1])

#11)Posiciones negativas
paises = ['Afganistán','Albania','Alemania','Argentina','Bahamas','Brasil','México','Japón','Italia','Estados Unidos','España','Nueva Zelanda ','Perú','Filipinas','Sudáfrica','Uruguay','Rusia','Portugal','Indonesia','Haití','Colombia','Canadá','Catar','Suiza','Francia','Corea del Sur','Noruega','Jamaica','China']
print('El ulimo numero de la lista es: ' + paises[-1])
print('El penulimo numero de la lista es: ' + paises[-2])

#12)Eliminar elementos del()
hw = ['CPU','RAM','Hard Drive']

del hw[0]
print(hw)

#13)Eliminar elementos .remove

hw = ['CPU','RAM','Hard Drive']

hw.remove('RAM')
print(hw)

#14)Eliminar elementos .pop

colores = ['rojo','azul','verde','amarillo','naranja']

guardar = colores.pop(1)
print(colores)
print(colores[1])
print('El color eliminado y guardado es: ' + guardar)


#15)Agregar elementos al final de la lista .append

colores = ['rojo','azul','verde','amarillo','naranja']

colores.append('violeta')
print(colores)


#16)Agregar elementos donde sea .insert(posicion,objeto)

colores = ['rojo','azul','verde','amarillo','naranja']

colores.insert(4, 'violeta')
colores.insert(-1, 'blanco')
print(colores)


#17)Ordenar listas .sort

colores = ['rojo','azul','verde','amarillo','naranja']

colores.sort()
print(colores)
colores.sort(reverse=True)
print(colores)
print(sorted(colores))
print(colores)

#18)Contar elementos de una lista

paises = ['Afganistán','Albania','Alemania','Argentina','Bahamas','Brasil','México','Japón','Italia','Estados Unidos','España','Nueva Zelanda ','Perú','Filipinas','Sudáfrica','Uruguay','Rusia','Portugal','Indonesia','Haití','Colombia','Canadá','Catar','Suiza','Francia','Corea del Sur','Noruega','Jamaica','China']

print(len(paises))


#19)Tuplas (igual que las listas solo que no pueden variar)

lista = [25,15,'azul','verde','amarillo','naranja']

tupla = ('rojo','azul','verde','amarillo','naranja') #No puede variar

print(lista)
print(tupla)
print(tupla[2])
print(lista[4],lista[0]+lista[1])

#tupla[1] = 'violeta' (no se puede)


#20)Transformar listas y tuplas

lista = [25,15,'azul','verde','amarillo','naranja']

tupla = ('rojo','azul','verde','amarillo','naranja')

lista = tuple(lista)

tupla = list(tupla)

print(lista)
print(tupla)


#21)Condicional IF
num1 = 20
num2 = 10


if num1 == num2:
    print('Son iguales')
    
if num1 != num2:
    print('Son diferentes')


#22)Condicional if else

edad = 18

if edad >= 18:
    print('Puedes acceder')
else:
    print('No puedes acceder')
    
    
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
    
    
#24)Comprobar datos en listas y en tuplas

navegadores = ['chrome','firefox','opera','microsoft edge']
print('opera' in navegadores)
print('safari' in navegadores)

entrada = input('Introduce un navegador  ')

if entrada in navegadores:
    print("El navegador esta en la lista")
else:
    print('El navegador no esta en la lista')


#25)Multiples condiciones IF

print('Saludos guerrero, Que deseas comprar?\n\n'+
      'Items disponibles:\n\n'+
      'Espadas:\n\n'+
      '\t1.- Espada Nivel 1: 150 monedas de oro\n'+
      '\t2.- Espada Nivel 2: 1200 monedas de oro\n\n'+
      'Escudos:\n\n'+
      '\t3.- Escudo Nivel 1: 100 monedas de oro\n'+
      '\t4.- Escudo Nivel 2: 750 monedas de oro\n\n')

comprar = [1]
dinero = 1500

espadalvl1 = 150
espadalvl2 = 1200

escudolvl1 = 100
escudolvl2 = 750

if 0 in comprar or comprar == []:
    print('Especifica un numero entre 1 y 4')
    
if 1 in comprar:
    dinero = dinero - espadalvl1
    
if 2 in comprar:
    dinero = dinero - espadalvl2
    
if 3 in comprar:
    dinero = dinero - escudolvl1

if 4 in comprar:
    dinero = dinero - escudolvl2
    
else:
    print('Especifica un numero entre 1 y 4')

if dinero < 0:
    print('No te ajusta el diinero')
    
if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print('Te queda '+str(dinero)+' monedas de oro.')
    print('Se agrego el objeto a tu inventario')
    
    
#26)Tips para condicionales 

x = 100 #Se ve mas visible
y=200

print('Se ejecuta el if') if x > y else print('Se ejecuta el else') #En una sola linea solo para una instruccion

x = 100
y = 200
z = 300

if x < y and z > y:
    print('Se cumplen las condiciones')
else:
    print('No se cumple una o ninguna de las condiciones')
    
    
if x < y or z > y:
    print('Se cumplen las condiciones')
else:
    print('No se cumple ninguna de las condiciones')
    
if x < y: #Causa error sin el pass
    pass

#27)Bucle while

x = 1

while x <= 10:
    print(x)
    x += 1
    
frase = 'Lo que escribas lo repito: '
frase += '\nIntroduce el comando "salir" para finalizar el proframa.\n'

mensaje = ''

while mensaje != 'salir':
    mensaje = input(frase)
    print (mensaje)
    
print('Has salido del bucle')

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
            
#31)Diccionarios I

teclado1 = {
    'Categoria': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }
teclado2 = {
    'Categoria': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
    }

consulta = teclado1['Modelo'],teclado1['Precio'],teclado2['Modelo'],teclado2['Precio']
print(consulta)

muestraTeclado = dict(teclado1)
print(muestraTeclado)

#32)Diccionarios con bucle for

teclado1 = {
    'Categoria': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }
teclado2 = {
    'Categoria': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
    }

consulta = teclado1.get('Modelo'),teclado1['Precio'],teclado2['Modelo'],teclado2['Precio']
print(consulta)

teclado1['Precio'] = '85'
print(teclado1.get('Precio'))

for x in teclado2:
    print(x)
    
for x in teclado2:
    print(teclado2[x])
    
for x in teclado2.values():
    print(x)

for x,y in teclado2.items():
    print(x,y)
    
#33)Diccionarios Metodos

teclado1 = {
    'Categoria': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }
teclado2 = {
    'Categoria': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
    }

print(len(teclado1) + len(teclado2))

teclado1.pop('Categoria')
del teclado1['Precio']
print(teclado1)
teclado1.clear()
print(teclado1)
del teclado1

teclado2['Color'] = 'Negro'
print(teclado2)

tecladoCopia = teclado2.copy()
print(tecladoCopia)
tecladoCopia2 = dict(teclado2)
print(tecladoCopia2)

teclado1 = dict(Categoria = 'Teclados',
                Modelo = 'HyperX Alloy FPS Pro',
                Precio = '89,99',
                ID = '001')
print(teclado1)

teclado3 = ('Categoria','Modelo','Precio')
vacia = 'Valor vacio'

teclado3 = dict.fromkeys(teclado3,vacia)
print(teclado3)

vistaTeclado = teclado1.keys()
print(vistaTeclado)

teclado1.update({'Color': 'Negro'})
print(teclado1)

if 'ID' in teclado1:
    print('El producto tiene un ID especifico')
else:
    print('El producto no tiene un ID especifico')
    
if 'ID' in teclado2:
    print('El producto tiene un ID especifico')
else:
    print('El producto no tiene un ID especifico')

teclados = {
    "teclado1" : {
        'Categoria': 'Teclados',
        'Modelo': 'HyperX Alloy FPS Pro',
        'Precio': '89,99',
        'ID': '001'
        },
    "teclado2" : {
        'Categoria': 'Teclados',
        'Modelo': 'Corsair K55 RGB',
        'Precio': '59,99'
        }
    }
print(teclados)
print(len(teclados))

#34)Funciones

def saluda():
    print('Bienvenidos')
    
saluda()

print('La familia Simpson\n')

def familiaS(nombre,parentesco):
    print(nombre + ' Simpson ' + parentesco)

familiaS('Homero','Padre')
familiaS('Marge','Madre')
familiaS('Lisa','Hija')
familiaS('Bart','Hijo')
familiaS('Maggie','Hija')


#35)Argumentos arbitrarios

def alumnos(*args): #Cualquier nombre y ahi se guardaran las variables que mandes
    print('El ultimo alumno es: ' + args[-1] + ' el primero es: ' + args[0])

alumnos('Julia','Pedro','Francisco','Eduardo')

def alumnos_profesores(profesor,sustituto, *args):
    print('Profesor: '+profesor)
    print('Sustituto: '+sustituto)
    for x in args:
        print('Alumno: '+x)
        
lista_alumnos = ('Julia','Pedro','Francisco','Eduardo')
alumnos_profesores('Antonio', 'Amador', *lista_alumnos)


#36)Diccionarios arbitrarios

def colores(color1,color2,color3,color4):
    print('Este es el color: '+color1+'.')

def colores2(**kwargs):
    print('Este es el color: '+kwargs['color1']+'.')

colores(color1='rojo', color2='azul', color3='verde', color4='amarillo')
colores2(color1='naranja', color2='azul', color3='verde', color4='amarillo')

def suma(x,y):
    return x + y

total = suma(10,10)
print(total)

def resta(x,y):
    return x - y

total = resta(10,5)
print(total)

def mul(x,y):
    return x * y

total = mul(10,10)
print(total)

def div(x,y):
    return x / y

total = div(10,10)
print(total)

def nohacenada():
    pass

def colores3(color='rojo'):
    print('Mi color favorito es: '+color)
    
colores3('azul')
colores3()
colores3('verde')


#37)Clases y Objetos

class Naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = 'Negro'
    color2 = 'Rojo'
    motores = 4
    activada = False
    compueta_principal = False
    sistema_defensa = True
    autodestruccion = False
    
    def encender(self):
        self.activada = True
        
    def apagar(self):
        self.activada = False
        
    def abrir_compuerta(self):
        self.compueta_principal = True
        
    def cerrar_compuerta(self):
        self.compueta_principal = False
        
    def  desactivar_defensas(self):
        self.sistema_defensa = False
        
    def  activar_defensas(self):
        self.sistema_defensa = True
        
    def activar_autodestruccion(self):
        self.autodestruccion = True
        print('Protocolo de autodestruccion activado...')
        
    def estado_motores(self):
        if(self.activada):
            return 'Motores trabajando al 100%'
        else:
            return 'Motores apagados'
    
    def estado_compuerta(self):
        if (self.compueta_principal):
            return 'La compuerta esta abierta'
        else:
            return 'La compuerta esta cerrada'
        
    def estado_defensa(self):
        if(self.sistema_defensa):
            return 'El sistema de defensa esta activado'
        else:
            return 'Peligro! El sistema de defensa esta desactivado'
        
#Creando el primer objeto de naves

nave1 = Naves()

#Comandos al objeto

#Encender
nave1.encender()

#Estado de los motores
print(nave1.estado_motores())

#Apagar 
nave1.apagar()

#Actualizacion de estado de los motores
print(nave1.estado_motores())

#Abre la compuerta
nave1.abrir_compuerta()

#Estado de la compuerta
print(nave1.estado_compuerta())

#Cierra la compuerta
nave1.cerrar_compuerta()

#Actualizacion de estado de la compuerta
print(nave1.estado_compuerta())

#Estado de las defensas
print(nave1.estado_defensa())

#Desactiva las defensas 
nave1.desactivar_defensas()

#Actualizacion de estado de las defensas
print(nave1.estado_defensa())

#Ejecuta la autodestruccion de la nave
nave1.activar_autodestruccion()

#38)Metodo __init__

class Usuarios():
    
    def __init__(self,nombre,pin):
        self.nombre = nombre
        self.pin = pin
        
    def saludo(self):
        print('Saludos '+self.nombre+'. Iniciaste sesion correctamente')
        
    def despedida(self):
        print(self.nombre + ', cerraste sesion')
        
usuario1 = Usuarios('Toni', '1234')
usuario2 = Usuarios('Julia', '1452')

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()

#39)Cambiar valores de objetos

class Usuarios2:
    def __init__(self,nombre,edad): #El self puede ser cambiado por cualquier otro nombre
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios2('Julian', 56)
usuario1.muestra_datos()

usuario1.edad = 65
usuario1.muestra_datos()


#40)Clases vacias y eliminar objetos

class nombreClase(): #Puedes quitar los parentesis 
    pass

class Usuarios3:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios3('Enrique', 28)

print(usuario1.nombre, usuario1.edad)

del usuario1.edad #Elimina la edad
del usuario1 #Elimina el objeto usuario 1

#41)Herencias de clases

class Usuarios_premium(Usuarios3):
    pass

usuario2 = Usuarios_premium('Pepe', 45)
usuario2.muestra_datos()

#42)Heredar propiedades

class Usuarios4:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print('El nombre del usuario es '+self.nombre, self.edad)
        
usuario1 = Usuarios4('Enrique', 28)

print(usuario1.nombre, usuario1.edad)

class Usuarios_premium2(Usuarios4):
    def __init__(self, nombre, edad, instagram):
        Usuarios4.__init__(self, nombre, edad)
        self.instagram = instagram
        
    def muestr_datos_premium(self):
        print('El nombre de usuario es: '+self.nombre, 'y tiene', self.edad, 'años. Su Instagram es:',self.instagram)
        
usuario2 = Usuarios_premium2('Elvira', 23, 'elvi_23')

usuario2.muestr_datos_premium()


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

#44)Importar modulos y funciones lambda

import math

def area(radio):
    resultado = round(math.pi * radio * radio, 2)
    print(resultado)
    
area(2)

area = lambda radio: round(math.pi * radio * radio, 2)

print(area(2))


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


#46)Metodo STRFTIME

#%d - Día del mes / 01 - 32
#%a - Día de la semana (corto) / mi
#%A - Día de la semana (entero) / miércoles
#%w - Día de la semana (número) / 0-6
#%b - Mes (corto) / mar.
#%B - Mes (entero) / marzo
#%m - Número del mes / 01-12
#%y - Año (corto) / 20
#%Y - Año (entero) / 2020
#%H - Hora / 00 - 23
#%I - Hora / 00 - 12
#%p - AM - PM
#%M - Minutos / 00 - 59
#%S - Segundos / 00 - 59
#%f - Microsegundos / 000000 - 999999
#%j - Día del año / 001 - 366
#%U - Número de semana del año (D) / 00 - 53
#%W - Número de semana del año (L) / 00 - 53
#%Z - Zona horaria / UTC
#%c - Fecha y hora local (entera) / 18/03/20020 15:10:39
#%x - Fecha local / 18/03/20020
#%X - Hora local / 15:10:39

#import datetime
import locale

locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now()

print(fecha.strftime('%A'))
print(fecha.strftime('%H'))
print(fecha.strftime('%M'))

fecha = datetime.datetime(1998,9,30)

print(fecha.strftime('%Y'))


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


#48)Expresiones regulares .findall()

#import re

texto = 'tres tristes tigres comen trigo en un trigal'

busqueda = re.findall('e', texto)
print(busqueda)

busqueda = re.findall('es', texto)
print(busqueda)

busqueda = re.findall('cuatro', texto)
print(busqueda)


#49)Expresiones regulares .split() .sub()

#import re

texto =  'Aquellos que no conocen la historia estan condenados a repetirla - Edmund Burke'

resultado = re.split(' ', texto) #guarda todo menos lo que pongan entre comillas
print(resultado)

resultado = re.split(' ', texto, 4)#maxsplit al encontrar la cuarta cooincidencia para y lo demas lo deja en un solo string
print(resultado)

resultado = re.sub(' ', '-', texto) #sustituye el primer valor con el segundo
print(resultado)

resultado = re.sub(' ', '---', texto)
print(resultado)

resultado = re.sub(' ', '---', texto,4) #Limita las veces que se sustituye el valor
print(resultado)


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


#import re

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