# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: 
# 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock
# 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock
# Examples
# s = '12:01:00PM' Return '12:01:00'
# s = '12:01:00AM' Return '00:01:00'

import math
import os
import random
import re
import sys

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# Steps:

# 1. Identificar la parte AM/PM: Verifica si el tiempo proporcionado es AM o PM
# 2. Convertir la hora:
    # Si es AM, convierte la hora a 00 si es 12 y mantenla igual si es cualquier otra hora.
    # Si es PM, convierte la hora a 12 si es 12 y añade 12 a cualquier otra hora para obtener el formato de 24 horas.
# 3. Conservar los minutos y segundos: Estos permanecen iguales.

def timeConversion(s):
    # Extraemos los últimos dos caracteres para saber si es AM o PM
    period = s[-2:]
    periodo = s[8:10]
    # s = '12:01:00AM'
    # start = 8: Comienza en el índice 8 (valor A).
    # stop = 10: Termina antes del índice 10 (Incluir el último valor).
    print(period)
    print(periodo)
    # Extraemos la hora, los minutos y los segundos
    hours = int(s[:2])
    minutes_seconds = s[2:-2]

    if period == "AM":
        if hours == 12:
            # Si es medianoche, convertimos a 00
            hours = 0
    else:  # PM
        if hours != 12:
            # Si no es mediodía, sumamos 12 para convertir a formato 24 horas
            hours += 12

    # Devolvemos el tiempo en formato de 24 horas, asegurándonos de que la hora tenga dos dígitos
    return f"{hours:02}{minutes_seconds}"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Digite la Hora: ")
    result = timeConversion(s)
    print(result)
    #fptr.write(result + '\n')
    #fptr.close()