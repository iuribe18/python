import pandas

data = pandas.read_csv("Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"]) # Gray Squirrels
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"]) # Gray Squirrels
black_squirrels = len(data[data["Primary Fur Color"] == "Black"]) # Black Squirrels
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

## Create a DataFrame Scratch
# data_dict = {
#     "colors": ["grey", "red", "black"],
#     "scores": [grey_squirrels, red_squirrels, black_squirrels]
# }
# datos = pandas.DataFrame(data_dict)
# print(datos)
# datos.to_csv("colors.csv")

data_dict = data.to_dict()  # Convert a DataFrame to a Dictionary
print(data_dict)

# temp_list = data["temp"].to_list()  # Convert a Series to a List
# print(temp_list)
# print(len(temp_list))

# ## Get data in columns
# # Average
# temp_average = data["temp"].mean()
# print(temp_average)

# # Maximun
# temp_max = data["temp"].max()
# print(temp_max)
# condition = data.condition
# print(condition)

# ## Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == temp_max])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# # Create a DataFrame Scratch
# data_dict = {
#     "students": ["Ivancho", "Nana", "Negra", "Santi"],
#     "scores": [76, 77, 80, 90]
# }
# datos = pandas.DataFrame(data_dict)
# print(datos)
# datos.to_csv("students.csv")