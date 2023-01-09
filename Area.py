print("Area calculator")
def square():
    a=float(input("Enter measure of a side:"))
    area=a*a
    print("Area of square is ",area)
def circle():
    r=float(input("Enter radius of circle:"))
    pie=3.14
    area=pie*r*r
    print("Area of circle  is ",area)
def rectangle():
    l=float(input("Enter length of rectangle:"))
    b= float(input("Enter breadth of rectangle:"))
    area=l*b
    print("Area of rectangle is ",area)
print("Select a shape")
print("1.Square\n2.Circle\n3.Rectangle\n")
c=int(input("Select your choice"))
if c==1:
    square()
elif c==2:
    circle()
elif c==3:
    rectangle()
else:
    print("Invalid choice")