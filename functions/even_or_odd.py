
# function to check if the number is even or odd
def isEven(num):
    if num % 2 == 0:
        return True
    return False

number = int(input("Enter the number: "))
print(isEven(number))