import math
# core assigment
print('1 .Please enter the following information: ')
squareSide = input('What is the length of a side of the square? ')
squareArea = float(squareSide) ** 2
print(f'The area of the square is: {(squareArea)}' )
rectangleLength = input('What is the length of rectangle?: ')
rectangleWidth = input('What is the width of the rectangle?: ')
rectangleArea = float(rectangleLength) * float(rectangleWidth)
print(f'The area of the rectangle is: {(rectangleArea)}' )
circleRadius = input('What is the radius of the circle?: ')
circleArea = (float(circleRadius) ** 2) * 3.14
print(f'The area of the circle is: {circleArea: .1f}' )

#stretch 1
print('1 .Please enter the following information: ')
squareSide = input('What is the length of a side of the square? ')
squareArea = float(squareSide) ** 2
print(f'The area of the square is: {(squareArea)}' )
rectangleLength = input('What is the length of rectangle?: ')
rectangleWidth = input('What is the width of the rectangle?: ')
rectangleArea = float(rectangleLength) * float(rectangleWidth)
print(f'The area of the rectangle is: {(rectangleArea)}' )
circleRadius = input('What is the radius of the circle?: ')
circleArea = (float(circleRadius) ** 2) * math.pi
print(f'The area of the circle is: {circleArea: .1f}' )

# #stretch 2
print('\n\n\n 2. Please enter the following information: ')
lenght = input('What is the length you want to calculate? ')
squareArea = float(lenght) ** 2
circleArea = (float(lenght) ** 2) * math.pi
cubeVolume = float(lenght) ** 3
sphereVolume = 4/3 * math.pi * (float(lenght) ** 3)
print(f'The area of the square is: {squareArea: .1f}' )
print(f'The area of the circle is: {circleArea: .1f}' )
print(f'The volume of the cube is: {cubeVolume: .1f}' )
print(f'The volume of the sphere is: {sphereVolume: .1f}' )

#stretch 3
print('1 .Please enter the following information: ')
squareSide = input('What is the length, in centimeters, of a side of the square? ')
squareArea = float(squareSide) ** 2
print(f'The area of the square, in cm², is: {(squareArea)}')
print(f'The area of the square, in m², is: {(squareArea)/10000}')
rectangleLength = input('What is the length, in centimeters, of rectangle?: ')
rectangleWidth = input('What is the width, in centimeters, of the rectangle?: ')
rectangleArea = float(rectangleLength) * float(rectangleWidth)
print(f'The area of the rectangle, in cm², is: {(rectangleArea)}')
print(f'The area of the rectangle, in m², is: {(rectangleArea)/10000}')
circleRadius = input('What is the radius, in centimeters, of the circle?: ')
circleArea = (float(circleRadius) ** 2) * math.pi
print(f'The area of the circle, in cm², is: {(circleArea)}')
print(f'The area of the circle, in m², is: {(circleArea)/10000}')

