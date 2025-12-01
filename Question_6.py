# Write a program that will tell whether the number entered by the user is odd or even.
userInput = int(input("Enter a number "))
# if userInput%2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("Even" if userInput%2==0 else "Odd")