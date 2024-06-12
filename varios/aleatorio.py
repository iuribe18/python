import random

# Generates a random number between i and j
i = 100
j = 200
random_integer = random.randint(i, j)
print(random_integer)

# Returns the next random floating point number between [0.0 to 1.0)
random_float = random.random()
print(random_float * 5)