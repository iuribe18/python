"""Descripción del problema
En muchos países, la altura de una persona se mide en pies y pulgadas.
Cree una función que reciba como parámetro el número de pies y el número de pulgadas que componen la altura de una persona, y retorne la altura en metros (redondeada a dos decimales).

Recuerde que:
1 pie = 12 pulgadas
1 pulgada = 2,54 centímetros
"""


def altura(pies, pulgadas):
    pies = float(pies)
    pulgadas = float(pulgadas)
    altura = (((pies * 12) + pulgadas) *2.54)/100
    altura = round(altura, 2)
    #dolares = str(dolares)
    print("Usted mide", altura, " metros")
    return altura
    
pies = input("Por Favor Digita tu Altura en Pies: ")
pies = float(pies)
pulgadas = input("Por Favor Digita tu Altura en Pulgadas: ")
pulgadas = float(pulgadas)

longitud = altura(pies, pulgadas)
print(longitud)