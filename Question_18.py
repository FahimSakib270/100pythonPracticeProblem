# Write a program that will check whether the number is armstrong number or not.

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