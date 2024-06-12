"""
Descripción del problema
En este ejercicio se quiere sumar todos los números de una lista que están en posiciones pares. 
Recuerde que las posiciones de las listas empiezan en 0 y van hasta n - 1, donde n es el tamaño de la lista.
Se garantiza que todos los números de la lista son enteros

Función requerida
Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
Nombre de la función: sumar_pares
Parámetros
Nombre: numeros
Tipo: list
Descripción: La lista con los números a sumar
Tipo del retorno: int
Descipción del retorno: La suma de los números de la lista que están en posiciones pares
"""

def sumar_pares(lista):
    suma = 0   
    # i = indice
    # j = valor
    # Usando enumerate
    # for i, j in enumerate(lista):
    #     if i % 2 == 0:
    #         print(suma)
    #         #print('Indice: ', i)
    #         #print('Valor: ', j)
    #         suma = suma + j
    # return suma
    
    # Usando
    for i in range(0, len(lista)):
        if i % 2 == 0:
            print(suma)
            suma = suma + lista[i]
    return suma

if __name__ == '__main__':
    print(sumar_pares(lista = [10, 9, 6, 12, 8, 6, 7]))