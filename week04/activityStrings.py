#letter = input('What is your favorite letter? ')

word = 'Commitment'
word_count = len(word)

# CAPTALIZING
# for letter in range(word_count):
#     if word[letter] == 'm':
#         print(word[letter].upper(), end="")
#     else:
#         print(word[letter].lower(), end="")

# HIDING IT
for letter in range(len(word.lower())):
    if word[letter] == 'm':
        print('_', end="")
    else:
        print(word[letter].lower(), end="")