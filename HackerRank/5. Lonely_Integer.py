# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example
# a = [1,2,3,4,1,2,3]
# The unique element is 4.

import math
import os
import random
import re
import sys

# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    result = 0
    # Iteramos a través de la lista y aplicamos XOR entre los elementos
    for number in a:
        result ^= number
    return result

if __name__ == '__main__':
    # Inserta directamente el arreglo de números
    # a = [1, 2, 3, 4, 1, 2, 3]  # Aquí puedes cambiar el arreglo con los números que desees
    
    # Solicitar la longitud del arreglo
    n = int(input("Ingrese la longitud del arreglo: ").strip())
    
    # Crear una lista vacía para almacenar los elementos
    a = []
    
    # Solicitar al usuario que ingrese los elementos del arreglo
    for i in range(n):
        element = int(input(f"Ingrese el elemento {i+1}: ").strip())
        a.append(element)

    # Llamar a la función lonelyinteger con el arreglo ingresado
    result = lonelyinteger(a)

    # Imprimir el resultado
    print(f"El elemento único es: {result}")