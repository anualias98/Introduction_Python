#variables
#to store data
a=10
b="Hello world"
print(a)
print(b)
#condition using if /else
x=12
y=5
if x<y:
    print("yes")
else:
    print("no")
#type
x=45
print(type(x))
y="anu"
print(type(y))
#casting
b=float(78)
print(b)
#multiple variables
x,y,z=1,2,3
print(x)
print(z)
a,b,c=1,"apple",23.4
print(type(b),type(a),type(c))
# print(type(c))
# print(type(a))
fruits=["apple","orange","grape"]
x,y,z=fruits
print(x)
a=b="rose"
print(a)
print(b)
#global variables
x=23
def test():
    print(str(x) + " is a number")#concantenation
test()
y="awesome"
def myfun():
    y="easy"
    print("python is " + y)
myfun()
print("python is " + y)
