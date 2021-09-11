# check if the entered number is prime or not

number = int(input("Enter number: "))

if number <= 1:
    print("NOT Prime")
    quit()

i = 2
while i*i <= number:
    if number % i == 0:
        print("NOT Prime")
        break
    i += 1
else:
    print("Prime")