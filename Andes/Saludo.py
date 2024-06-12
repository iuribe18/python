# Descripción del problema
# Cree una función que reciba un nombre y un entero, y retorne la cadena 'Hola' seguida del nombre recibido por parámetro, pero con la letra 'o' repetida tantas veces como indique el entero recibido, así como la letra 'a' la mitad de las veces que la 'o' (si la mitad no es exacta, se debe tomar la parte entera)
# Por ejemplo, si se reciben como parámetros 'Egan' y 5, la cadena a retornar será 'Hooooolaa Egan'
# Función requerida
# Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
# Nombre de la función:	saludar_repetidas_veces
# Parámetros
# Nombre: Nombre a incluir en el saludo	
# tipo: str	
# Veces: int
# Descripción: Cantidad de veces a repetir las letras
# Tipo del retorno str	
# Descipción del retorno: Cadena con el saludo con letras repetidas


def saludar_repetidas_veces(nombre, veces):
    Hola = 'Hola'
    o = Hola[1] * veces
    a = veces // 2
    a = Hola[3] * a
    mensaje = 'H' + o + 'l' + a
    return mensaje

if __name__ == '__main__':
    nombre = input("Dime tu Nombre: ")
    mensaje = saludar_repetidas_veces(nombre, 5)
    print(mensaje + ' ' + nombre)