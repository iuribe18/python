import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100: ")

# Choosing a random number between 1 and 100
number = random.randint(1, 100)


# Function to choose difficulty level
def level():
    """ Choose a difficulty level for the game """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number")
    return attempts

def check_answer(guess, attempts):
    """ Check the user's guess and return the number of attempts remaining """
    if guess == number:
        print("You got it!")
        return 0
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high.")
        return attempts - 1

# Call the level function to set the attempts
attempts = level()

# Let the user guess a number
is_game_over = False
while not is_game_over:
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You got it!")
        print(f"The answer was {number}")
        is_game_over = True
    else:
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {number}")
            is_game_over = True
        elif guess < number:
            print("Too low.")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif guess > number:
            print("Too high.")
            print(f"You have {attempts} attempts remaining to guess the number")