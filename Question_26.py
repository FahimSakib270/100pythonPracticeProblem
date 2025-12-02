# Write a program that can find the factorial of a given number provided by the user.

num = int(input("Enter a number "))
factorial = 1

for i in range(1,num+1):
    factorial *=i

print(factorial)