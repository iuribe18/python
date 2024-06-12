## Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
# Write a function that will work with the following line of code to add the entry for Brazil to the travel_log.
# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

# Input: Brazil, 5, ["Sao Paulo", "Rio de Janeiro"]
# Output: 
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.

# country = input() # Add country name
country = "Brazil"
#visits = int(input()) # Number of visits
visits = 2
# list_of_cities = eval(input()) # create list from formatted string
list_of_cities = ["Sao Paulo", "Rio de Janeiro"]
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Write the function that will allow new countries to be added to the travel_log. 
def add_new_country(country, visits, cities):
    new_entry = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_entry)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")