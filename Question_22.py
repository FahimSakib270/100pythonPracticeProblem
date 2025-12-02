"""Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
"""

heads = int(input("Total heads: "))
legs = int(input("Total legs: "))

dogs = (legs - 2*heads)/2
chickens = heads - dogs

print(f"total number of dogs {dogs} and total number chickens are {chickens}")