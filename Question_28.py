# Write a program to print whether a given number is prime number or not


def checkPrime(num):
    if num <= 1:
        return "Not a prime number"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a prime number"
    
    return "Prime number"

print(f"1: {checkPrime(1)}")
print(f"2: {checkPrime(2)}")
print(f"3: {checkPrime(3)}")
print(f"4: {checkPrime(4)}")
print(f"5: {checkPrime(5)}")
print(f"6: {checkPrime(6)}")
print(f"7: {checkPrime(7)}")
print(f"13: {checkPrime(13)}")
print(f"17: {checkPrime(17)}")
print(f"25: {checkPrime(25)}")