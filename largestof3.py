number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 and number1 > number3:
    print(number1, "is the greatest number.")
elif number2 > number1 and number2 > number3:
    print(number2, "is the greatest number.")
else:
    print(number3, "is the greatest number.")


# shorthands
if(True):   print("Done")
print("left") if(True) else print("right")      # works like ternery operator in c/c++