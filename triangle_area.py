side1 = float(input("Enter side a: "))
side2 = float(input("Enter side b: "))
side3 = float(input("Enter side c: "))

s = (side1 + side2 + side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

print("Area of triangle is: {:.3f}".format(area))

