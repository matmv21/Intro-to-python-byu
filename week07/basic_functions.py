def display_regular(phrase):
    string = phrase
    return print(string)

def display_uppercase(phrase):
    string = phrase.upper()
    return print(string)

def display_lowercase(phrase):
    string = phrase.lower()
    return print(string)

phrase = str(input('What is your message? '))
display_regular(phrase)
display_uppercase(phrase)
display_lowercase(phrase)

###############################
# def display_numbers(x, y):

#     print(x)

# x = 3
# y = 4

# display_numbers(y,x)

###############################
# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# display_numbers(x, y)

# print(x)

###############################
# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# print(display_numbers(x, y))

###############################
# def display_numbers(x, y):
#     return 10

# x = 3
# y = 4
# x = display_numbers(x, y)

# print(x)