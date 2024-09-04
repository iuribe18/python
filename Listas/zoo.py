""" Lists Assignment
Create a list of 5 animals called zoo
Delete the animal at the 3rd index.
Append a new animal at the end of the list
Delete the animal at the beginning of the list.
Print all the animals
Print only the first 3 animals"""

zoo = ["donkey", "bee", "dog", "cat", "caterpillar"]
print(zoo)
for x in zoo:
    print(x)
# Delete the animal at the 3rd index
zoo.pop(2)
print(zoo)
# Append a new animal at the end of the list
zoo.append("zebra")
print(zoo)
# Print only the first 3 animals
print(zoo[0:3])