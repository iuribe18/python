programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again."
                          }
## Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Imprimir el valor del diccionario dada su key
print(f"Key: 'Bug' Value: '{programming_dictionary["Bug"]}'")

# Add new item to the dictionary
programming_dictionary["Variable"] = "A storage location in programming that holds data which can be changed during program execution."

# Imprimir todo el diccionario
print("\n",programming_dictionary)

# Imprimir el diccionario por medio de un for
print("\nfor: ")
for clave, valor in programming_dictionary.items():
    print(f'{clave}: {valor}')

print("\nElementos del diccionario: ")
# Imprimir todos los elementos del diccionario
for x in programming_dictionary:
    print(x)
    print(programming_dictionary[x])

# Imprimir solo las claves del diccionario
print("\nkey: ")
for clave in programming_dictionary.keys():
    print(clave)

print("\nvalues: ")
# Imprimir solo los valores del diccionario
for valor in programming_dictionary.values():
    print(valor)