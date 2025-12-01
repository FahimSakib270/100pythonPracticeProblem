# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num1 = input("Enter ")

reversed1 = num1[::-1]

originalNum = int(num1)
reversedNum = int(reversed1)

if originalNum == reversedNum:
    print("true")

print(f"Original number {originalNum}")
print(f"reversed Number {reversed}")