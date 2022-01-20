# CreditCalculator 1
principal = "loan principal: 1000"
month_1 = "Month 1: repaid 250"
month_2 = "Month 2: repaid 250"
month_3 = "Month 3: repaid 500"
repaid = "the loan has been repaid!"

print("principal")
print("month_1")
print("month_2")
print("month_3")
print("repaid")

# CreditCalculator 2
import math
print("Enter the loan principal:")
t = float(input("> "))
print("""
What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:""")
c = input("> ")
if c == "m":
    print("Enter the monthly payment:")
    o = int(input("> "))
    n = math.ceil(t / o)
    print("It will take " + str(n) + " months to repay the loan")
if c == "p":
    print("Enter the number of months:")
    n = int(input("> "))
    o = math.ceil(t / n)
    l = t - (n - 1) * o
    if l == o:
        print("Your monthly payment  " + str(o))
    else:
        print("Your monthly payment  " + str(o) + " and the lasy payment = " + str(l) + ".")
else:
    print("No correct!")


