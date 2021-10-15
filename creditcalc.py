from math import log, pow, ceil
import argparse

#
# choice = input('What do you want to calculate?\n'
#                'type "n" for number of monthly payments,\n'
#                'type "a" for annuity monthly payment amount,\n'
#                'type "p" for loan principal:\n')
# if choice == 'n':
#     principal = float(input("Enter the loan principal:\n"))
#     payment = int(input("Enter the monthly payment:\n"))
#     loan_interest = float(input("Enter the loan interest:\n"))
#     i = loan_interest / 1200
#     n = ceil(log((payment / (payment - i * principal)), 1 + i))
#     years = n // 12
#     start = "It will take"
#     str_years = f"{years} years"
#     str_months = ""
#     end = "to repay this loan!"
#     if n % 12:
#         months = n - years * 12
#         if months > 1:
#             str_months = f"and {months} months"
#         else:
#             str_months = f"and {months} month"
#         if n < 12:
#             str_years = ""
#     if years == 1:
#         str_years = f"{years} year"
#     print(f"{start} {str_years} {str_months} {end}")
# elif choice == "a":
#     principal = float(input("Enter the loan principal:\n"))
#     n = int(input("Enter the number of periods:\n"))
#     loan_interest = float(input("Enter the loan interest:\n"))
#     i = loan_interest / 1200
#     payment = ceil(principal * ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)))
#     print(f"Your monthly payment = {payment}!")
# elif choice == "p":
#     payment = float(input("Enter the annuity payment:\n"))
#     n = int(input("Enter the number of periods:\n"))
#     loan_interest = float(input("Enter the loan interest:\n"))
#     i = loan_interest / 1200
#     principal = round(payment / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)), 0)
#     print(f"Your loan principal = {principal}!")

parser = argparse.ArgumentParser()
parser.add_argument("--type", default="")
parser.add_argument("--principal", default=0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0)
parser.add_argument("--payment", default=0)
args = parser.parse_args()
type = args.type
principal = int(args.principal)
periods = int(args.periods)
payment = int(args.payment)
interest = float(args.interest)

interest /= 1200
if type == "diff" and principal > 0 and periods > 0 and interest > 0:
    result = 0
    for i in range(periods):
        temp = principal - principal * i / periods
        D = ceil(principal / periods + interest * temp)
        result += D
        print(f"Month {i+1}: payment is {D}")
    print(f"\nOverpayment = {result - principal}")
elif type == "annuity" and principal > 0 and periods > 0 and interest > 0:
    payment = ceil(principal * ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1)))
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {payment * periods - principal}")
elif type == "annuity" and payment > 0 and periods > 0 and interest > 0:
    principal = int(round(payment / ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1)), 0))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {payment * periods - principal}")
elif type == "annuity" and principal > 0 and payment > 0 and interest > 0:
    periods = ceil(log((payment / (payment - interest * principal)), 1 + interest))
    years = periods // 12
    start = "It will take"
    str_years = f"{years} years"
    str_months = ""
    end = "to repay this loan!"
    if periods % 12:
        months = periods - years * 12
        if months > 1:
            str_months = f"and {months} months"
        else:
            str_months = f"and {months} month"
        if periods < 12:
            str_years = ""
    if years == 1:
        str_years = f"{years} year"
    print(f"{start} {str_years} {str_months} {end}")
    print(f"Overpayment = {payment * periods - principal}")
else:
    print("Incorrect parameters")
