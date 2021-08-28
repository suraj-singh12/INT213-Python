# nested if-else

number = int(input("Enter a number; "))

if number > 5:
    print("greater than 5")
    if number > 10:
        print("greater than 10 too.")
    else:
        print("smaller than 10 but")
elif number < 5:
    print("smaller than 5")
    if number < 0:
        print("It's negative number.")
    elif number == 0:
        print("This is 0")
    else:
        print("This is greater than 0 but")
else:
    print("You entered 5 !!")
print("Job done !!")