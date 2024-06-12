import random
from art import logo, vs
from data import data

def format_data(account):
    """Format the account data into printable format """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers_count, b_followers_count):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers_count > b_followers_count:
        return guess == "A"
    else:
        return guess == "B"

# Print the logo
# print(logo)
# score = 0
# game_should_continue = True

# while game_should_continue:
#     # Generate a random account from the data
#     elemento_a = random.choice(data)
#     elemento_b = random.choice(data)
#     # Make sure elements are different
#     while elemento_a == elemento_b:
#         elemento_b = random.choice(data)
#     print(f"Compare A: {format_data(elemento_a)}.")
#     print(vs)
#     print(f"Compare B: {format_data(elemento_b)}.")
#     # Solicitar al usuario que elija quién tiene más seguidores
#     guess = input("Who has more followers? Type 'A' or 'B': ").upper()

#     # Get follower count of each account 
#     a_follower_count = elemento_a["follower_count"]
#     b_follower_count = elemento_b["follower_count"]

#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     # Give user feedback on their guess
#     # Score keeping
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score: {score}.")
#     else:
#         game_should_continue = False
#         print(f"Sorry, that's wrong. Final score: {score}")

## Version 2
# Print the logo
print(logo)
score = 0
game_should_continue = True
# Generate a random account from the data
elemento_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the data
    elemento_a = elemento_b
    elemento_b = random.choice(data)
    # Make sure elements are different
    while elemento_a == elemento_b:
        elemento_b = random.choice(data)
    print(f"Compare A: {format_data(elemento_a)}.")
    print(vs)
    print(f"Compare B: {format_data(elemento_b)}.")
    # Solicitar al usuario que elija quién tiene más seguidores
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Get follower count of each account 
    a_follower_count = elemento_a["follower_count"]
    b_follower_count = elemento_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")