"""
Descripción del problema
Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena
Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.

Función requerida
Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
Nombre de la función: contar_caracteres_repetidos
Parámetros
Nombre: cadena
Tipo: str
Descripción: La cadena que se debe revisar
Tipo del retorno: int
Descipción del retorno: La cantidad de caracteres diferentes que aparecen repetidos en la cadena
"""
import collections
def contar_caracteres_repetidos(cadena: str)->int:
    contador = collections.Counter(cadena)
    print(contador)
    suma = 0
    contar = 0
    for i, j in contador.items():
        if j >= 2:
            suma = suma + j
            contar = contar + 1
    return contar

if __name__ == '__main__':
    #contar_caracteres_repetidos('fresas y bananas')
    c = contar_caracteres_repetidos("fresas y bananas")
    print(c)