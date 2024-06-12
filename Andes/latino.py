"""
Descripción del problema
El Pig Latin es un lenguaje construido a partir de la transformación de palabras en inglés. 
Aunque se desconoce el origen de dicho lenguaje, este es mencionado en al menos dos documentos del siglo XIX, lo cual sugiere que ha existido por más de cien años.

Las siguientes son las reglas que se usan para traducir del inglés al Pig Latin:

Si una palabra empieza por una consonante, todas las letras del inicio de la palabra, hasta la primera vocal, se eliminan y luego se agregan al final de la palabra, seguidas de “ay”. 
Por ejemplo, “computer” se traduce a “omputercay” y “think” se traduce a “inkthay”.

Si una palabra inicia por vocal, se agrega “way” al final de la palabra. 
Por ejemplo, “algorithm” se traduce a “algorithmway” y “office” se convierte en “officeway”.
Si una palabra no tiene vocales (por ejemplo "my"), entonces no se cambia de ninguna forma.
Cree una función que reciba como parámetro un texto (conformado por una o más palabras), y retorne la traducción de dicho texto a Pig Latin. 
Puede asumir que el texto ingresado por el usuario consiste solamente de palabras en minúscula y separadas por espacios.

Función requerida
Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales
Nombre de la función: traducir_a_pig_latin
Parámetros:
Nombre:	texto
Tipo: str	
Descripción: Texto (cadena de caracteres) a traducir al Pig Latin. Consiste solamente de palabras en minúscula, separadas por espacios
Tipo del retorno: str
Descipción del retorno: Texto con las palabras de la cadena original traducidas a Pig Latin, separadas por espacios
"""

# def es_vocal(cadena: str) -> bool:
#     vocal = True
#     if cadena[0] == 'a' or cadena[0] == 'e' or cadena[0] == 'i' or cadena[0] == 'o' or cadena[0] == 'u':
#         vocal = True
#     else:
#         vocal = False
#     return vocal

def traducir_a_pig_latin(texto: str) ->str:

    # Convertir texto a palabras
    texto = texto.split()

    pig_latin = []
    for palabra in texto:
        # Recorrer por palabras
        vocales = 0
        
        # Contar vocales
        for j in palabra:
            if j[0] == 'a' or j[0] == 'e' or j[0] == 'i' or j[0] == 'o' or j[0] == 'u':
                vocales = vocales + 1

        if vocales == 0:
            # Insertar palabra en la lista
            pig_latin.append(palabra)
        elif palabra[0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i' or palabra[0] == 'o' or palabra[0] == 'u':
            pig_latin.append(palabra + "way")
        elif not (palabra[0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i' or palabra[0] == 'o' or palabra[0] == 'u') and (palabra[1] == 'a' or palabra[1] == 'e' or palabra[1] == 'i' or palabra[1] == 'o' or palabra[1] == 'u'):
            pig_latin.append(palabra[1:len(palabra)] + palabra[0:1] + "ay")
        elif not (palabra[0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i' or palabra[0] == 'o' or palabra[0] == 'u') and not (palabra[1] == 'a' or palabra[1] == 'e' or palabra[1] == 'i' or palabra[1] == 'o' or palabra[1] == 'u'):
            pig_latin.append(palabra[2:len(palabra)] + palabra[0:2] + "ay")
    return " ".join(pig_latin)   

if __name__ == '__main__':
    # El texto se convierte a minuscula
    texto = (input("Escriba Texto: ")).lower()
    #texto_separado = separar_texto(cadena)
    #print(texto_separado)
    pig_latin = traducir_a_pig_latin(texto)
    print(pig_latin)