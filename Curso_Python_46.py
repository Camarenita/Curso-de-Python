# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:58:54 2022

@author: LALO
"""

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

import datetime
import locale

locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now()

print(fecha.strftime('%A'))
print(fecha.strftime('%H'))
print(fecha.strftime('%M'))

fecha = datetime.datetime(1998,9,30)

print(fecha.strftime('%Y'))