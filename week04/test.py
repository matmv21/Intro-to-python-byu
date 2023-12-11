# number = 0

# Keep looping as long as the number is less than 10
# while number < 10:
#     number = int(input("What is the number? "))

# print("Finished with the loop")

# -----------------------------------------------------------------
# number = int(input('Please type a positive number: '))

# while number < 0:
#     print('Sorry, that is a negative number. Please try again.')
#     number = int(input('Please type a positive number: '))

# print(f'The number is: {number}')

#------------------------------------------------------------------
# answer = str(input('May I have a piece of candy? '))

# while answer.lower() != 'yes':
#     answer = str(input('May I have a piece of candy? '))

# print('Thank you.')

#------------------------------------------------------------------
# items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

# for item in items:
#     print(f"The item is: {item}")

#------------------------------------------------------------------
#LOOP FOR EACH
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in range(10):
#     print(number)

#------------------------------------------------------------------
#LOOP FOR EACH
# for i in range(5):
#     print(i)
#
# for i in range(5):
#     print(i)
#     for j in range(10, 13):
#         print(f"--{j}")
#------------------------------------------------------------------
#LOOPING THROUGH STRINGS
# first_name = "Brigham"
# for letter in first_name:
#     print(f"The letter is: {letter}")
#------------------------------------------------------------------
# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     print(str(index) + ' - ' + word[index])

# ANOTHER WAY
# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")
#------------------------------------------------------------------
# LETTER COUNT
# dog_name = input("What is your dog's name? ")
# letter_count = len(dog_name)

# print(f"Your dog's name has {letter_count} letters")
#------------------------------------------------------------------
# word = "book"
# number_of_letters = len(word) # Notice this can now work for any string

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")