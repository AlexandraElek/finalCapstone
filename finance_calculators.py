
# This is a calculator that helps users calculate their investment or home loan repayments
import math
user_choice = (input('''Welcome to the financial calculator!
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:
''').lower())

# Calculation of the investment based on the user's input
# The result is rounded to two decimal places
if user_choice == 'investment':
    print('Please enter only numbers for the following:')
    deposit = float(input('Amount of your deposit:\n'))
    interest_rate = float(input('Interest rate (as a percentage):\n'))
    years_of_invest = float(input('Number of years of investment:\n'))
    interest = (input("Now enter the interest type you want to calculate by typing 'simple' or 'compound':\n").lower())
    if interest == 'simple':
        simple_earnings = deposit * (1 + interest_rate / 100 * years_of_invest)
        rounded_simple_earnings = round(simple_earnings,2)
        print(f'The total amount is £{rounded_simple_earnings}')
    elif interest == 'compound':
        compound_earnings = deposit * math.pow((1 + interest_rate / 100),years_of_invest)
        rounded_compound_earnings = round(compound_earnings,2)
        print(f'The total amount is £{rounded_compound_earnings}')
    else:
        print("Invalid user input! You can only choose between 'simple' and 'compound'.")

# Calculation of the home loan repayments based on the user's input
# The result is rounded to two decimal places
elif user_choice == 'bond':
    print('Please enter only numbers for the following:')
    house_value = float(input('The present value of the house:\n'))
    interest_rate = float(input('Interest rate (as a percentage):\n'))
    months_of_bond = float(input('The time required for repayment in months:\n'))
    repayment = (interest_rate/(100 * 12) * house_value) / (1 - (1 + interest_rate/(100 * 12)) ** (-months_of_bond))
    rounded_repayment = round(repayment,2)
    print(f'You will have to repay £{rounded_repayment} each months.')

else:
    print("Invalid user input! You can only choose between 'investment' and 'bond'.")