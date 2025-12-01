# User will input (2numbers).Write a program to swap the numbers

userInput1 = int(input("Enter 1st num: "))
userInput2 = int(input("Enter 2nd num: "))

print(f"before swaping number one is {userInput1} and number two is {userInput2}")

# temp = userInput1
# userInput1 = userInput2
# userInput2 = temp

# print(f"after swaping number one is {userInput1} and number two is {userInput2}")


userInput1,userInput2 = userInput2,userInput1

print(f"after swaping number one is {userInput1} and number two is {userInput2}")
