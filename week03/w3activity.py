a = int(input('integer 1: '))
b = int(input('integer 2: '))

if a > b:
    print('The first number is greater')
else:
    print('The first number is not greater')

if a == b:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if b > a:
    print('The second number is greater')
else:
    print('The second number is not greater')

print()
animal = str(input('What is your favorite animal? '))
my_favorite_animal = 'dog'

if animal.lower() == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That's not my favorite animal.")