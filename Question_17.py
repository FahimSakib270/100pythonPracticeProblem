# Write a program that will take three digits from the user and add the square of each digit.
number = input("Enter a three-digit number: ")
total = 0

for digit in number:
    total += int(digit) ** 2

print(total)