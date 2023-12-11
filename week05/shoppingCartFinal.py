# SHOOPING CART PROGRAM
shopping_cart = []
price_item = []
action = 0
item = ''

while action != 5:
    print('\nWelcome to the Shopping Cart Program!')
    print(f'{shopping_cart}')
    print('Please select one of the following:')
    print(
        '1. Add item\n' + #OK
        '2. View cart\n' + #OK
        '3. Remove item\n' +
        '4. Compute total\n' +
        '5. Quit\n' #OK
    )
    action = int(input('Please enter an action: '))
    
    #ADD AN ITEM TO THE LIST
    if action == 1:
        item = (input('What item would you like to add? '))
        price = float(input(f'What is the price for {item}? '))
        if len(shopping_cart) == 0:
            shopping_cart.append(item)
            price_item.append(price)
        else:
            for i in range(len(shopping_cart)):
                if shopping_cart[i].lower() == item.lower():
                    print(f'{item} already exists in the list.')
            shopping_cart.append(item)
            price_item.append(price)

    #VIEWING THE CART LIST  
    elif action == 2:
        if len(shopping_cart) == 0:
            print('The list still empty, try adding somthing to the list.')
        else:
            print('The contents of the shopping cart are:')
            for i in range(len(shopping_cart)):
                formatted_price = ["%.2f" % elem for elem in price_item]
                print(f'{shopping_cart[i]} - ${formatted_price[i]}')

    #REMOVING AN ITEM OF THE LIST
    elif action == 3:
        if len(shopping_cart) == 0:
            print('The list still empty, try adding something to the list.')
        else:
            item = int(input('Which item do you want to remove? '))
            if shopping_cart[item]:
                shopping_cart.pop(item)
                price_item.pop(item)
                print(f'Item number {item} removed.')
            else:
                print('Sorry, that is not a valid item number.')

    #COMPUTING THE TOTAL AMOUNT
    elif action == 4:
        print(f'The total price of the items in the shopping cart is ${sum(price_item)}')

    #TREATING INVALID OPTIONS
    elif action > 5:
        print('Choose a valid option please!\nChoose options 1, 2, 3, 4, or 5.')
else:
    print('Thank you. Goodbye.')
    exit()