# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

principle = int(input("Enter principle "))
rateOfInterest = int(input("Enter rate of interest "))
time = int(input("Enter time "))

simpleInterest = (principle*rateOfInterest*time)/100

print(simpleInterest)