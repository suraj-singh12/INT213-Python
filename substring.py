
s = input("Enter a string: ")
sub = input("Enter substring to be capitalized: ")

if sub in s:
    s = s.replace(sub,sub.capitalize())
    print(s)
else:
    print("Ops!", sub, "not found in", s)