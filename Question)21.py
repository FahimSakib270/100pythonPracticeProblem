# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

def cm_to_feet():
    cm = float(input("Enter length in centimeters: "))
    feet = cm / 30.48
    print(f"{cm} cm = {feet:.2f} feet\n")
    return feet

def km_to_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km / 1.609
    print(f"{km} km = {miles:.2f} miles\n")
    return miles

def usd_to_inr():
    
    usd = float(input("Enter amount in USD: "))
    inr = usd * 83.0  
    print(f"${usd:.2f} USD = ₹{inr:.2f} INR\n")
    return inr

def main():
    while True:
        print("===== CONVERSION MENU =====")
        print("1. Centimeters to Feet")
        print("2. Kilometers to Miles")
        print("3. USD to INR")
        print("4. Exit")
        print("===========================")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            cm_to_feet()
        elif choice == '2':
            km_to_miles()
        elif choice == '3':
            usd_to_inr()
        elif choice == '4':
            print("Thank you for using the converter. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()