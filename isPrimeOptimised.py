'''
    Program to check if the entered number is prime or not.
'''


# checks if the number is prime; returns true if yes, else false
# it is an optimised approach
def isPrime(n):
    if n <= 1:              # if number is <= 1; it is not prime
        return False
    if n == 2 or n == 3:        # if number is 2 or 3, it is prime
        return True
    if n % 2 == 0 or n % 3 == 0:    # if number is not 2 or 3 but is divisible by 2 or 3; it is not prime
        return False
    
    i = 5               # if number is not any of the above cases, 
                        # then start dividing it by prime numbers, and see if it is divisible, if yes, then it is non-prime
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    # if number is not divisible by the above range of mumbers, then it's prime so return true
    return True

# main function
def main():
    number = int(input("Enter a number: "))
    ans = isPrime(number)
    if ans == True:
        print("Yes", number, "is Prime.")
    else:
        print("No", number, "is NOT Prime.")


if __name__ == "__main__":
    main()