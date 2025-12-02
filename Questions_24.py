"""Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.
"""

userInput = int(input("Enter a number "))

total = 0

for i in range(0,userInput+1):
    total += i

print(total)