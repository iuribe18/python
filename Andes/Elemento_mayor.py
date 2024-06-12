"""
Descripción del problema
En este ejercicio se quiere encontrar el mayor número en una lista de enteros positivos.
Usted debe construir una función que retorne el número mayor que se encuentre en la lista. 
En caso de que la lista esté vacía, se debe retornar -1.

Función requerida
Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
Nombre de la función: encontrar_mayor
Parámetros
Nombre: entrada
Tipo: list
Descripción: lista de números que se desea buscar
Tipo del retorno: int
Descipción del retorno: El número más grande en la lista, si está vacía -1
"""

def encontrar_mayor():
    #lista = [10, 9, 6, 12, 8, 6, 7]
    lista = []
    elementos = len(lista)
    
    if elementos == 0:
        print(-1)
    else:
        print('Elementos de la lista:', lista)
        #Ordenar lista
        lista.sort()
        #Lista Invertida
        lista.reverse()
        mayor = lista[0]
        print('El mayor Número de la lista es:', mayor)

if __name__ == '__main__':
    encontrar_mayor()