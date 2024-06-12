from collections import Counter

print("Anagrama")
first_word = input("Primera Palabra: ")
second_word = input("Segunda Palabra: ")

# Contamos las letras en cada palabra
# contador_palabra1 = Counter(first_word)
# contador_palabra2 = Counter(second_word)

# if contador_palabra1 == contador_palabra2:
#     print(f"{first_word} y {second_word} es un Anagrama")
# else:
#     print(f"{first_word} y {second_word} NO es un Anagrama")

def contar_letras(palabra):
    contador = {}
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

contador_palabra1 = contar_letras(first_word)
contador_palabra2 = contar_letras(second_word)

if contador_palabra1 == contador_palabra2:
    print(f"{first_word} y {second_word} es un Anagrama")
else:
    print(f"{first_word} y {second_word} NO es un Anagrama")

print(f"Contador de letras en '{first_word}': {contador_palabra1}")
print(f"Contador de letras en '{second_word}': {contador_palabra2}")