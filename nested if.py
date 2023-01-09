a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number:"))
c=input("enter your choice:1.2,3,4")
if c=="1":
    sum=a+b
    print(sum)
    if c=="rose":
        print("equals")
    else:
        print("not equals")
elif c=="2":
    sub=a-b
    print(sub)
elif c=="3":
    mul=a-b
    print(mul)
elif c == "4":
    div= a - b
    print(div)
else:
    print("invalid")


# check a number positive,negative or zero
x=int(input("Enter number:"))
if x>0:
    print("x is positive")
    if x==100:
        print("equals")
    else:
        print("not equals")

elif x<0:
    print("x is negative")
else:
    print("x is zero")