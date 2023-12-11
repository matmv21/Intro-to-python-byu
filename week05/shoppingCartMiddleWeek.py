# SHOOPING CART PROGRAM
shopping_cart = []
action = 0
item = ''

while action != 5:
    print('\nWelcome to the Shopping Cart Program!')
    print(f'{shopping_cart}')
    print('Please select one of the following:')
    print(
        '1. Add item\n' +
        '2. View cart\n' +
        '3. Remove item\n' +
        '4. Compute total\n' +
        '5. Quit\n'
    )
    action = int(input('Please enter an action: '))
    if action == 1:
        item = (input('What item would you like to add? '))
        print()
        if len(shopping_cart) == 0:
            shopping_cart.append(item)
        else:
            for i in range(len(shopping_cart)):
                if shopping_cart[i].lower() == item.lower():
                    print(f'{item} already exists in the list.')
            shopping_cart.append(item)
                
    elif action == 2:
        print('The contents of the shopping cart are:')
        if len(shopping_cart) == 0:
            print('The list still empty, try adding somthing to the list.')
        else:
            for i in range(len(shopping_cart)):
                print(shopping_cart[i])

    elif action == 3 or action == 4:
        print('Choose a valid option please!\nFor now choose options 1, 2 or 5.')
else:
    print('Thank you. Goodbye.')
    exit()