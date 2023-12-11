print('Loan Questions: Rate(1 - 10) ')
print()
# How large is the loan?
loan_size = int(input('How large is the loan? '))
# How good is your credit history?
cred_hist = int(input('How good is your credit history? '))
# How high is your income?
income = int(input('How high is your income? '))
# How large is your down payment?
payment = int(input('How large is your down payment? '))

grantLoan = False

if loan_size >= 5:
    if cred_hist >= 7 and income >= 7:
        grantLoan = True
        if payment >= 5:
            grantLoan = True
        else:
            grantLoan = False
    else:
        grantLoan = False
elif loan_size < 5:
    if cred_hist < 4:
        grantLoan = False
    else:
        if income >= 7 and payment >= 7:
            grantLoan = True
        elif income >= 4 and payment >= 4:
            grantLoan = True
        else:
            grantLoan = False

if grantLoan:
    print('Your loan is granted')
else:
    print('Your loan is not granted.')