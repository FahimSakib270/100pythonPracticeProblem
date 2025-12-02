"""Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< 30%)(0-1lakh print k).
"""

salary = int(input("Enter your salary: "))

HRA = 10 / 100
DA = 5 / 100
PF = 3 / 100

hra_amt = salary * HRA
da_amt = salary * DA
pf_amt = salary * PF
total_deductions = hra_amt + da_amt + pf_amt

tax = 0
if salary <= 100000:
    tax = 0
elif 500000 <= salary <= 1000000:
    tax = salary * 0.10   
elif 1100000 <= salary <= 2000000:
    tax = salary * 0.20   
elif salary > 2000000:
    tax = salary * 0.30    
else:  
    tax = 0

in_hand = salary - total_deductions - tax


if salary <= 100000:
    print("k")
else:
    print(f"In-hand salary: ₹{in_hand:,.2f}")
    