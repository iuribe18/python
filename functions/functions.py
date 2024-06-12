def greet():
    print("Hello")
    print("Good Morning")
    print("What about the weather")

# Function with 1 parameter
def greet_with_name(name):
    # name is a parameter
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    print(f"What about the weather {name}")

# Function with 2 parameters
def greet_with(name, location):
    # name is a parameter
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    # location is a parameter
    print(f"Are you from {location}?")

greet()

# Ivancho is an argument
greet_with_name("Ivancho")

# Ivancho is an argument, Bucaramanga is another argument
# Positional arguments are the ones that are passed in the order they are defined in the function
greet_with("Ivancho", "Bucaramanga")

# Function with keywords arguments
greet_with(location = "Medellin", name= "Charlie")