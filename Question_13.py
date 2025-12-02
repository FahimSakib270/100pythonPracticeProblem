userInput = int(input("Enter the number: "))

if userInput == 0:
    print("0 is divisible by both 3 and 6.")
elif userInput % 6 == 0: 
    print(f"{userInput} is divisible by both 3 and 6.")
elif userInput % 3 == 0:
    print(f"{userInput} is divisible by 3 but not by 6.")
else:
    print(f"{userInput} is not divisible by 3 or 6.")