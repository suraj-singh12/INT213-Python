# find the oldest person of 4 
p1 = int(input("Person1 Enter age: "))
p2 = int(input("Person2 Enter age: "))
p3 = int(input("Person3 Enter age: "))
p4 = int(input("Person4 Enter age: "))
if p1 > p2 and p1 > p3 and p1 > p4:
    print("Person 1 is oldest")
elif p2 > p1 and p2 > p3 and p2 > p4:
    print("Person 2 is oldest")
elif p3 > p1 and p3 > p2 and p3 > p4:
    print("Person 3 is oldest")
else:
    print("Person 4 is oldest")
