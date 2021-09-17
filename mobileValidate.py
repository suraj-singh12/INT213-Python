mobile = input("Enter mobile no(without country code): ")
if len(mobile) == 10 and mobile.isdigit() == True:
    print("Validation Success !!")
else:
    print("Validation Failed !!")