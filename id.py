x = 4
y = 4
# is        is one of the two identity operators
print(x is y)

# id() prints memory address of the value being pointed to by the object
print(id(x))
print(id(y))

x = 4/2
y = 8/4

print(x is y)
print(id(x))
print(id(y))

x = [1,2,3]
y = [1,2,3]
print(id(x))
print(id(y))
print(x is y)

y = x
print(x is y)



x1 = -6
y1 = -6
print(x1 is y1)
print(id(x1))
print(id(y1))
print(x1 is y1)