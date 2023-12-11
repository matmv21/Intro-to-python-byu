numbers = []
num = 1

while num != 0:
        num = int(input('Enter a number: '))
        if num != 0:
            numbers.append(int(num))
else:
    #CORE REQUIREMENTS
    print('Itens of the list')
    print(numbers)
    print('SUM function')
    print(sum(numbers))
    print('AVERAGE of the list')
    print(sum(numbers) / len(numbers))
    print('LARGEST number')
    print(max(numbers))

    #STRETCH CHALLENGE
    print('SMALLEST positive number')
    print(min([i for i in numbers if i > 0]))
    print('SORT the list')
    print(sorted(numbers))