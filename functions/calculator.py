from art import logo
print(logo)

# Functions
def add(n1, n2):
    #docstring
    """Take 2 numbers and return the sum"""
    return n1 + n2

def subtract(n1, n2):
    #docstring
    """Take 2 numbers and return the substract"""
    return n1 - n2

def multiply(n1, n2):
    #docstring
    """Take 2 numbers and return the multiply"""
    return n1 * n2

def divide(n1, n2):
    #docstring
    """Take 2 numbers and return the divide"""
    return n1 / n2

# Dictionary to store operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = True

    while should_continue:
        number1 = float(input("What is the first number: "))
        number2 = float(input("What is the second number: "))
        
        print("Operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")
        if operation_symbol in operations:
            calculation_function = operations[operation_symbol]
            print(calculation_function)
            result = calculation_function(number1, number2)
            print(result)
            print(f"{number1} {operation_symbol} {number2} = {result}")
        else:
            print("Invalid operation. Please try again.")
            continue

        if input("Do you want to perform another calculation? Type 'yes' to continue or 'no' to exit: ").lower() != 'yes':
            should_continue = False
            print("Goodbye!")

# def calculator():
#     should_continue = True

#     while should_continue:
#         number1 = float(input("What is the first number: "))
#         number2 = float(input("What is the second number: "))
        
#         print("Operations:")
#         for symbol in operations:
#             print(symbol)

#         operation_symbol = input("Pick an operation from the line above: ")
#         if operation_symbol == "+":
#             result = add(number1, number2)
#             print(f"{number1} {operation_symbol} {number2} = {result}")
#         elif operation_symbol == "-":
#             result = subtract(number1, number2)
#             print(f"{number1} {operation_symbol} {number2} = {result}")
#         elif operation_symbol == "*":
#             result = multiply(number1, number2)
#             print(f"{number1} {operation_symbol} {number2} = {result}")
#         elif operation_symbol == "/":
#             result = divide(number1, number2)
#             print(f"{number1} {operation_symbol} {number2} = {result}")
#         else:
#             print("Invalid operation. Please try again.")
#             continue

#         if input("Do you want to perform another calculation? Type 'yes' to continue or 'no' to exit: ").lower() != 'yes':
#             should_continue = False
#             print("Goodbye!")

calculator()