import random
from hangman_word import word_list
from hangman_art import stages, logo

import os
def clear():
    os.system('cls')

# Select a random word
end_of_game = False
# Step 1, generate a ramdom word for a list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
# Print the random word
# print(f"La palabra aleatoria es: {chosen_word}")

# Print the word with "_" instead of letters
display = []
for _ in range(word_length):
    display += "_"

print(logo)
while not end_of_game:
    guess = input("Guess a Letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    # Verificar si la letra está en la palabra
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose...!!!")
    if "_" not in display:
        end_of_game = True
        print("You Win...!!!")
    print(stages[lives])

#     # Actualizar los espacios en blanco con la letra adivinada
#     for i, letra in enumerate(palabra_aleatoria):
#         if letra == guess:
#             espacios_blancos[i] = guess

# # Unir la lista actualizada en una cadena separada por espacios
# espacios_blancos_str = " ".join(espacios_blancos)
# print(espacios_blancos_str)

# import random
# import string

# def generar_palabra_aleatoria(longitud):
#     letras = string.ascii_lowercase
#     return ''.join(random.choice(letras) for i in range(longitud))

# # Generar una palabra aleatoria de 8 letras
# palabra_aleatoria = generar_palabra_aleatoria(8)

# print(f"La palabra aleatoria generada es: {palabra_aleatoria}")