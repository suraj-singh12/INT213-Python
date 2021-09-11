# check if the nubmer entered is divisible by 2 and 3 both

number = int(input("Enter the number: "))
if number % 2 == 0 and number %3 == 0:
    print("Divisible by 2 and 3 both")
else:
    print("Not divisible by both 2 and 3")