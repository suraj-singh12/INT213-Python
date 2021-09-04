# accept percentage from user, and display its grade 
percentage = int(input("Enter your percentage: "))

if percentage > 80:
    print("A+")
elif percentage > 60:
    print("A")
elif percentage > 50:
    print("B+")
elif percentage > 45:
    print("B")
elif percentage > 25:
    print("C")
else:
    print("D")
    