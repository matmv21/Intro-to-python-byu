import math

def compute_area_square(side):
    area = float(side * side)
    return area

def compute_area_rectangle(width, height):
    area = float(width * height)
    return area

def compute_area_circle(radius):
    area = float(math.pi * (radius**2))
    return area

answer = ""

while answer.lower() != 'quit':
    print("SHAPES:")
    print("Square\nRectangle\nCircle\nQuit")
    answer = str(input("What area do you want to compute? "))
    
    if answer.lower() == 'square':
        side = float(input('Insert a value for the side: '))
        print(f'Square Area: {compute_area_square(side)}')
    elif answer.lower() == 'rectangle':
        width = float(input('Insert a value for the width: '))
        height = float(input('Insert a value for the height: '))
        print(f'Rectangle Area: {compute_area_rectangle(width, height)}')
    elif answer.lower() == 'circle':
        radius = float(input('Insert a value for the radius: '))
        print(f'Circle Area: {compute_area_circle(radius)}')
    elif answer.lower() == 'quit':
        exit()
    else:
        print("Choose a valid option!")