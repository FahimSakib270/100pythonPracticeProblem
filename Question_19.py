# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
number = input("Enter a number ")

numLen = len(number)

numberInInt = int(number)
total = 0

for i in number:
    total += int(i)**numLen

if total==numberInInt:
    print("ArmStrong")
else:
    print("No")