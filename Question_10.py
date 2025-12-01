# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

costPrice = int(input("Enter buying price "))
sellingPrice = int(input("Enter selling price "))

if costPrice>sellingPrice:
    print("loss")
elif sellingPrice>costPrice :
    print("profit")
else:
    print("No Profit No Loss")