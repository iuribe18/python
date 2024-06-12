print("Hello future Python Programmer!")
print("Hello", "future", "Python", "Programmer!")
print("Hello! \"Python\" is cool")

print("Hello!", end="")
# print string "Hello!" without add un salto de línea al final. El argumento end="" especifica que el carácter al final de la cadena impresa debe ser una cadena vacía en lugar del carácter de nueva línea predeterminado.
print("Python is a great language")

print("Hello", end="!")
print("Python is a great language")

# Another keyword argument is sep. This keyword allows you to control how Python separates the outputted arguments, which is just a space by default.
print("Hello", "future", "Python", "Programmer!", sep="-")
print(1, 2, 3, 4, sep='#', end='&')
print("My age is: " + "25")