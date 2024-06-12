# Order items
fruits = ["pear", "strawberry", "pineapple", "cherry", "apple"]

for fruit in fruits:
    print(fruit)
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
usa_states = ["California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan", "Delaware", "Arizona"]
print(usa_states[0])

# If I wrote -1 or -2, starts counting from the end of the list.
print(fruits[-1]) #apple
fruits[0] = "Pear"
print(fruits)

# add an item to the end of the list
usa_states.append("Utah")
print(usa_states)

## Operations
# list.count(x) Return the number of times x appears in the list
fruits.count("apple")

# list.extend(iterable) Extend the list by appending all the items from the iterable
fruits.extend(["orange", "banana"])
print(fruits)

# Nested List
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

## Instructions
# You are going to write a program that calculates the average student height from a List of heights.
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# Input 1: 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
# Output: total height = 857, number of students = 5, average height = 171

# Input a Python list of student heights
# students = int(input("Cuantos estudiantes hay en el curso: "))
# heights = []  # Lista vacía para almacenar las estaturas
# total_height = 0
# for i in range(students):
#     height = int(input(f"Introduce la estatura del estudiante {i + 1}: "))
#     heights.append(height)
#     total_height += height
#     average_height = round(total_height/students)
#     round(average_height, 0)
# print(f"total height: {total_height}")
# print(f"average height: {average_height}")


## Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Input: 78 65 89 86 55 91 64 89
# Output: The highest score in the class is: 91
students = int(input("Cuantos estudiantes hay en el curso: "))
scores = []  # Lista vacía para almacenar las notas
highest_score = 0
for i in range(students):
    score = int(input(f"Introduce la nota del estudiante {i + 1}: "))
    scores.append(score)
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")