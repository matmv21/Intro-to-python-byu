# Welcome to the word guessing game!

# Your hint is: _ _ _ _ _ _ 
# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? moroni
# Your hint is: M O _ o _ i 
# What is your guess? hhhhhh
# Your hint is: h h h h h H 
# What is your guess? mosiah  
# Congratulations! You guessed it!
# It took you 4 guesses.

word = 'Shape'
word_size = len(word)
count_guesses = 1
i = 0

print('Welcome the Word Guessing Game!')
print('Your hint is? _ _ _ _ _')
guess = input('What is your guess? ')

if len(guess) == word_size:
    while answer.lower() != 'no':
        if guess.lower() == word.lower():
            for letter in range(len(guess)):
                # Exact position
                if guess[letter].lower() == word[letter].lower():
                    print(f'{guess[letter]}, end=""')
                else:

    answer = input('Do you want to play again? ')
else:
    print('Sorry, the guess must have the same number of letters as the secret word.')

# if word_user.lower() == word.lower():
#     print("You guessed it!\nThe word is '{word}'")
# else:
#     print("It starts with an 's'. Try again.")