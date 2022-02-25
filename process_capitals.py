# Author: Mohamad Almoussa
# course: CSC 352/552 Advanced Python

# This project prompt to user to enter the name of a country or a US state and the displays the capital of
# country/state on a generated map.

from mapit import display_on_map

# Dictionaries containing the latitude and longitude locations of all major world-wide cities.
file1 = open('country_capital_locations.csv')
country_capital_locations = {}
for i in file1:
    i = i.split(",")
    if i[0] == 'Country' or i[1] == 'Capital' or i[2] == 'Latitude' or i[3] == 'Longitude':
        continue
    country_capital_locations[i[0]] = i[1], float(i[2]), float(i[3])

file2 = open('state_capital_locations.csv')
state_capital_locations = {}
for j in file2:
    j = j.split(",")
    if j[0] == 'name' or j[1] == 'description' or j[2] == 'latitude' or j[3] == 'longitude':
        continue
    state_capital_locations[j[0]] = j[1], float(j[2]), float(j[3])

print(state_capital_locations)
print("Process Capitals...")
while True:
    name = input("Enter a country or state name (exit to quit): ")
    if name.lower().title() == 'Exit':
        break
    if name.lower().title() not in country_capital_locations and name.lower().title() not in state_capital_locations:
        print("Not found error ")
    else:
        if name.lower().title() not in state_capital_locations:
            print("Capital of " + name.title() + " is", country_capital_locations[name.lower().title()][0])
            display_on_map(country_capital_locations[name.lower().title()][0],
                           country_capital_locations[name.lower().title()][1],
                           country_capital_locations[name.lower().title()][2])
        else:
            print("Capital of " + name.title() + " is", state_capital_locations[name.lower().title()][0])
            display_on_map(state_capital_locations[name.lower().title()][0],
                           state_capital_locations[name.lower().title()][1],
                           state_capital_locations[name.lower().title()][2])
print("Exitted!")






