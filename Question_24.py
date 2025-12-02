# Write a program that can multiply 2 numbers provided by the user without using the * operator

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = 0
for _ in range(abs(num2)):
    result += abs(num1)

if (num1 < 0) != (num2 < 0):  
    result = -result

print(f"{num1} × {num2} = {result}")