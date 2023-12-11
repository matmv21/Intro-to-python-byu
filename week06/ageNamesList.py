people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 100
youngest_name = ""
age = 1

for line in people:
    person = line.split(" ")
    person_name = person[0]
    age = int(person[1])

    
    if age < youngest_age:
        youngest_age = age
        youngest_name = person_name

    print(f"{person_name} - {age}")
print(f"The youngest is {youngest_age} and his/her name is {youngest_name}")