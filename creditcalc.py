import argparse
import sys
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")


args = parser.parse_args()

arguments = sys.argv


if not args.interest:
    print("Incorrect parameters (no interest)")
elif args.type != "annuity" and args.type != "diff" and not args.type:
    print("Incorrect parameters (type incorrect)")
elif len(arguments) < 5:
    print("Incorrect parameters (number of arguments)")
elif args.type =="diff" and args.payment:
        print("Incorrect parameters (diff with payment)")
elif args.interest and float(args.interest)<0:
    print("Incorrect parameters (negative)")
elif args.payment and int(args.payment)<0:
    print("Incorrect parameters (negative)")
elif args.principal and int(args.principal)<0:
    print("Incorrect parameters (negative)")
elif args.periods and int(args.periods)<0:
    print("Incorrect parameters (negative)")
else:
    if args.type == "diff":
        interest = float(args.interest)
        adj_interest = (interest/100)/12
        periods = int(args.periods)
        loan_principal = int(args.principal)
        sum_payments = 0
        for i in range(1, periods + 1):
            differentiated_payment = loan_principal/periods + adj_interest * (loan_principal - ((loan_principal * (i - 1))/ periods))
            print(f"Month {i}: payment is", math.ceil(differentiated_payment))
            sum_payments += math.ceil(differentiated_payment)
        overpayment = sum_payments - loan_principal
        print("Overpayment =", overpayment)
    else:
        if not args.periods:
            interest = float(args.interest)
            adj_interest = (interest/100)/12
            loan_principal = int(args.principal)
            monthly_payment = int(args.payment)
            total_months = math.ceil(math.log((monthly_payment / (monthly_payment - adj_interest * loan_principal)),(adj_interest + 1)))
            years = total_months // 12
            months = total_months % 12
            if months == 0:
                if years == 1:
                    print(f"It will take {years} year to repay this loan!")
                else: 
                    print(f"It will take {years} years to repay this loan!")
            elif years == 0:
                if months == 1:
                    print("It will take {months} month to repay this loan!")
                else:
                    print("It will take {months} months to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")    
            sum_payments = monthly_payment * total_months
            overpayment = sum_payments - loan_principal
            print("Overpayment=", math.ceil(overpayment))
        elif not args.principal:
            interest = float(args.interest)
            adj_interest = (interest/100)/12
            periods = int(args.periods)
            monthly_payment = int(args.payment)
            denominator = adj_interest * pow((1 + adj_interest), periods) / (pow((1 + adj_interest), periods) - 1)
            loan_principal = monthly_payment / denominator
            print(f"Your loan principal = {round(loan_principal)}!")
            sum_payments = monthly_payment * periods
            overpayment = sum_payments - loan_principal
            print("Overpayment=", math.ceil(overpayment))
        elif not args.payment:
            interest = float(args.interest)
            adj_interest = (interest/100)/12
            periods = int(args.periods)
            loan_principal = int(args.principal)
            annuity = math.ceil(loan_principal * (adj_interest * pow((1 + adj_interest), periods) / (pow((1 + adj_interest), periods) - 1)))
            print(f"Your annuity payment = {annuity}!")
            sum_payments = annuity*periods
            overpayment = sum_payments - loan_principal
            print("Overpayment=", math.ceil(overpayment))
        