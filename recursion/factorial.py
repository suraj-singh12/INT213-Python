# factorial

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
number = int(input("Enter number: "))   
fact = factorial(number)
print("Factorial of", number , "is:", fact)