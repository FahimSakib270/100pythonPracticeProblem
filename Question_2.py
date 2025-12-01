# Write a program that will convert celsius value to fahrenheit

# c/5 = f-32/9;  f = (9c/5)+32

userInput = float(input("Enter a number - "))

fahrenheit = ((9*userInput)/5) + 32

print(f"converted fahrenheit value is {fahrenheit: .2f}")