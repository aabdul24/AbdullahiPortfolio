''' The script below calculates the mortgage payments of the user's loan based 
on the principal amount of the loan, the annual interest rate, mortgage term, and
number of payments per year. The first three functions deal in calculating the 
payments as well as interest. The fourth function deals most of the calculation
using the first three functions, and the last function is argument parser which
takes the arguments to collect the data from the user.
'''

import sys
import argparse

def min_payment(principal, annual_interest_rate, mortgage = 30, payments = 12):
    c = annual_interest_rate / payments
    r = c + 1
    n = payments * mortgage
    minpayment = (principal * c * (r ** n)) / ((r ** n) - 1)
    return(minpayment)

''' The function above calculates the minimum monthly payment of the loan

Args:
    principal: total balance of the loan, annual_interest_rate: percentage
    of interest per year, mortgage: years of mortgage payment, payments: 
    amount of payments per year.

Returns
    minpayment: the minimum mortgage payment per month.
'''


def interest_due(balance, annual_interest_rate, payments=12):
    c = annual_interest_rate / payments
    next_interest = balance * c
    return(next_interest)

''' This function calculates the amount of interest remaining after payment

Args:
    balance: remaining balance of mortgage, annual_interest_rate: percentage
    of interest for the year, payments: amount of payments in the year.
Returns:
    Amount of interest remaining. 
'''

def remaining_payments(balance, annual_interest_rate, payment_amount, payments=12):
    counter = 0
    while balance > 0:
        only_interest = interest_due(balance, annual_interest_rate, payments)
        balance_pay = payment_amount - only_interest
        balance = balance - balance_pay
        counter += 1
    return(counter)
'''This function calculates the remaining monthly payments left on the mortgage.

Args: 
    payment_amount: amount of monthly payments remaining.

Returns: 
    Number of months of payment remaining.
'''

def main(principal, annual_interest_rate, mortgage = 30, payments = 12, target_payment = None):
    min_pay = min_payment(principal, annual_interest_rate, mortgage, payments)
    if target_payment is None:
        target_payment = min_pay
    if target_payment < min_pay:
        print("Your target payment is less than the minimum payment for this mortage.")
    else:
        rem_pay = remaining_payments(principal, annual_interest_rate, target_payment, payments)
        print("If you make payments of $", target_payment, "you will pay off the mortgage in", rem_pay, "payments.")

''' Main function. Calculates target payment using minimum payments and remaining
    payments in mortgage.

Args:
    target_payment: targeted monthly payment to finish mortgage in 'remaining_payments'
    months. Default value of None.
Returns:
    remaining payments as well as target payments.
'''

def parse_args(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("MortgageAmount", type=float, help = "The total amount of your mortgage.")
    parser.add_argument("AnnualInterestRate", type=float)
    parser.add_argument("-MortgageTerm", type=int, default = 30)
    parser.add_argument("-Payments", type=int, default = 12)
    parser.add_argument("-TargetPayment", type=int)
    args = parser.parse_args(arguments)
    return args

''' 

Argument parser.

'''

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.MortgageAmount, args.AnnualInterestRate, args.MortgageTerm, args.Payments, args.TargetPayment)

     


    





    
    




