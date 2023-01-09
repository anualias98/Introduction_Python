
def sum():
    sum=x+y
    print(sum)
def sub():
    sub=x-y
    print(sub)
def mul():
    mul=x*y
    print(mul)
def div():
    div=(x/y)
    print(div)
x=int(input("Enter 1st number:"))
y=int(input("Eter 2nd number:"))
z=input("Enter the choice 1,2,3,4:")
if z=="1":
    add()
elif z=="2":
     sub()
elif z=="3":
     mul()
elif z=="4":
     div()
else:
    print("invalid choice")