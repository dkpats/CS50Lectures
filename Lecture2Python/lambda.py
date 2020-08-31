
people = [
    {"name":"Legolas","weapon":"bow"},
    {"name":"Aragorn","weapon":"sword"},
    {"name":"Gimli", "weapon":"axe"},
    {"name":"Pippin","weapon":"rock"}
]

print(people)

sorter = input("Enter weapon or name: ")

people.sort(key=lambda person: person[sorter])

print(people)