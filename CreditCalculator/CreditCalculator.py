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

# CreditCalculator 3
import math
from math import ceil
text = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
if text == "n":
    p = int(input("Enter the loan principal: "))
    m = int(input("Enter the monthly payment: "))
    l = float(input("Enter the loan interest: "))
    i = l / (12 * 100)
    n = math.ceil(math.log(float(m) / (float(m) - i * float(p)), i + 1))
    o = divmod(n, 12)
    if n > 12:
        print("It will take {} years and {} months to repay this loan!".format(o[0], o[1]))
    elif n == 12:
        print("It will take {} years to repay this loan!".format(o[0]))
    else:
        print("It will take {} months to repay this loan!".format(o[1]))
elif text == "a":
    pr = int(input("Enter the loan principal: "))
    pe = int(input("Enter the number of periods: "))
    int = float(input("Enter the loan interest: "))
    i = int / (12 * 100)
    y = math.ceil(pr * (i * ((1 + i) ** pe)) / (((1 + i) ** pe) - 1))
    print("Your monthly payment = {}!".format(y))
elif text == "p":
    y = float(input("Enter the annuity payment: "))
    pe = int(input("Enter the number of periods: "))
    int = float(input("Enter the loan interest: "))
    i = int / (12 * 100)
    p = y / (i*(1+i)**pe)/(((1+i)*pe) - 1)
    finish = round(y / ((i * math.pow(1 + i, pe)) / (math.pow(1 + i, pe) - 1)))
    print("Your loan principal = {}!".format(finish))
