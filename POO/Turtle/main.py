import turtle
from prettytable import PrettyTable

ivancho = turtle.Turtle()
print(ivancho)
ivancho.shape("turtle")
ivancho.color("red")
ivancho.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)

# All rows at once
cities = PrettyTable()
cities.field_names = ["City Name", "Area", "Population", "Annual Rainfall"]
cities.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
cities.align = "l"
print(cities)