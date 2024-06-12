"""
Descripción del problema
Jorge tiene un Refugio de perros el cual hará un evento de adopción. 
Para esto, debe separar los animales en diferentes habitaciones, con ayuda de un diccionario que tiene en su oficina. 
Este diccionario tiene como llaves los nombres de los animales, y como valores la edad de cada uno. 
Puesto que los animales estarán separados por edad para el evento de adopción, Jorge necesita una manera rápida de saber el nombre de los animales que deben estar juntos.
Cree una función que reciba un diccionario animales y dos enteros minimo y maximo, y que retorne una lista de cadenas que contenga los nombres de los animales que tengan estrictamente menos edad que maximo y edad mayor o igual que minimo.
Los nombres de los perros, deben estar ordenados alfabéticamente.
Si no hay animales en el diccionario, retorne una lista vacía

Función requerida
Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
Nombre de la función: separar_por_edad
Parámetros:
Nombre:	animales
Tipo: dict	
Descripción: Diccionario cuyas llaves son los nombres de las mascotas y sus valores la edad de cada una
Nombre: minimo	
Tipo: int	
Descripción: Edad mínima de los animales para esta habitación
Nombre: maximo	
Tipo: int
Descripción: Edad máxima de los animales para esta habitación
"""
import operator
def separar_por_edad(animales, minimo, maximo):
    animal = []
    animales_ordenados = sorted(animales.items(), key = operator.itemgetter(0))

    for nombre, edad in animales_ordenados:
        if edad >= minimo and edad < maximo:
            animal.append(nombre)
    return animal

if __name__ == '__main__':
    Animales = {'rufo': 7, 'oddie': 2, 'max': 1, 'bacan': 3, 'firulais': 3, 'mateo': 2, 'lucas': 2, 'poty': 4}
    minimo = int(input("Minimo: "))
    maximo = int(input("Maximo: "))
    animales = separar_por_edad(Animales, minimo, maximo)
    print(animales)