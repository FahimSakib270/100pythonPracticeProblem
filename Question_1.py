# User will input (3ages).Find the oldest one

num1 = int(input("Enter age -"))
num2 = int(input("Enter age -"))
num3 = int(input("Enter age -"))

# if num1>=num2 and num1>=num3:
#     print(f"{num1} is the oldest")
# elif num2>=num3:
#     print(f"{num2} is the oldest")
# else:
#     print(f"{num3} is the oldest")

oldest = max(num1,num2,num3)
print(f"{oldest} is the oldest")