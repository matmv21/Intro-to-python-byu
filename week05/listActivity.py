# friends = []
# name = ''

# while name != 'end':
#     name = str(input('Type a name of a friend: '))
#     if name != 'end':
#         friends.append(str(name))

# print("Your friends are:")
# for name in friends:
#     print(name)

# #WORKING WITH NUMBERS
# receipts = [12.24, 18.50, 4.99, 21.75]

# running_total = 0

# for receipt in receipts:
#     running_total = running_total + receipt

# # for receipt in receipts:
# #     # Note the use of the += operator here
# #     running_total += receipt

# # Display the total
# print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48

#LIST USIN INDEX
# first = the_list[0] # gets the first item
# second = the_list[1] # gets the second item

# index = int(input("Which index would you like to get? "))
# user_choice = the_list[index] # gets the item at the index the user typed


# names = []
# numbers = []

# # ...
# # Code here that populates the two lists
# names.append('Mateus')
# names.append('Marcos')
# names.append('Cintia')
# names.append('Edemilton')
# names.append('William')

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# numbers.append(5)
# # ...

# for i in range(len(names)):
#     name = names[i]
#     number = numbers[i]

#     print(f"{name} - {number}")


shopping_items = []
item = ''
print('Please enter the items of the shopping list (type: quit to finish):')
while item.lower() != 'quit':
    item = str(input('Item: '))
    if item.lower() != 'quit':
        shopping_items.append(str(item))
else:
    print('The shopping list is:')
    for i in range(len(shopping_items)):
        i = i
        print(f'{i} - {shopping_items[i]}')

choice = int(input('Which item would you like to change? '))
newItem = str(input('What is the new item? '))

print('The new shopping list is:')
for i in range(len(shopping_items)):
    if i == choice:
        shopping_items[i] = newItem
    i = i
    print(f'{i} - {shopping_items[i]}')