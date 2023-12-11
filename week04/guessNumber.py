import random

answer = 'yes'

while answer.lower() == 'yes':
    magic_number = random.randint(1, 10)
    count = 1
    # magic_number = int(input('Pick the magic number: '))
    number = int(input('guess the number: '))

    while number != magic_number:
        count = count + 1
        if number > magic_number:
            print('Lower')
            number = int(input('guess the number: '))
        elif number < magic_number:
            print('Higher')
            number = int(input('guess the number: '))
    else:
        print(f'You guessed it!\nYou tried {count} time(s).')
        print(answer)
        answer = str(input('Do you want to play again? '))