
def maxOf3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

print("The maximum of all numbers is: ", maxOf3(n1,n2,n3))
