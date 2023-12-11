word = 'shape'
word_size = len(word)
count_guesses = 1
answer = 'yes'
i = 0
hint = '_ _ _ _ _'
print('Welcome the Word Guessing Game!\n')
while answer.lower() != 'n':
    guess = str(input('What is your guess? '))
    print('Your hint is: {hint}', end="")
    hint = ''
    if len(guess) == word_size:
        for i in range(len(guess)):
            if word[i] == guess[i]:
                print(f'{guess[i].upper()}', end="")
            for j in range(len(guess)):
                if word[i] == guess[j]:
                    print(f'{guess[j].lower()}', end="")
                else:
                    print('_', end="")
    else:
        print('Sorry, the guess must have the same number of letters as the secret word.')
else:
    answer = input('\nDo you want to play again? (y/n): ')


# if len(word_user) == word_size:
#     while word_user.lower() != word.lower():
#         print('Your guess was not correct.')
#         word_user = input('What is your guess? ')
#         count_guesses = count_guesses + 1
#     print('Congratulations! You guessed it!')
#     print(f'It took you {count_guesses} guesses.')
#     answer = 'no'
# else:
#     print(f'Your guess must have {word_size} caracters.')
