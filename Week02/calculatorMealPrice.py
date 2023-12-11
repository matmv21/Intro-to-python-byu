# ENTERING THE DATA IN THE VARIABLES
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
sales_tx_rate = float(input("What is the sales tax rate? "))

# MAKING THE CALCULATIONS AND PRINTING THE RESULTS
print()
# Subtotal Calculation
subtotal = (child_meal * num_children) + (adult_meal * num_adults)
print(f"Subtotal: ${subtotal: .2f}")

# Sales Tax Calculation
sales_tax = subtotal * (sales_tx_rate/100)
print(f"Sales Tax: ${sales_tax: .2f}")
total_price = subtotal + sales_tax
print(f"Total Price: ${total_price: .2f}")

print()
# Payment Calculation
payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total_price
print(f'Change: ${change: .2f}')