
#sum of n natural numbers
# n=10
# def sum():
#     sum = ((n * (n + 1) / 2))
#     print("sum of n natural numbers is " + str(sum))
# sum()



num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
check=int(input("Enter your selection"))
if check==1:
    result=num1+num2
    print( "sum = ",result)
elif check==2:
    result = num1 - num2
    print("diff = ", result)
elif check==3:
    result = num1 * num2
    print("product = ", result)
elif check==4:
    result = num1 / num2
    print("result = ", result)
else:
    print("You enter a invalid number")




