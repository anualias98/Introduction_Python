num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))
num3 = int(input("Enter 3rd number :"))
if (num1 > num2) and (num1 > num3):
    if num2>num3:
        print(num2," is second largest number")
    else:
        print(num3, " is 2nd largest number")
elif (num2 > num1) and (num2 > num3):
    if num1>num3:
        print(num1," is second largest number")
    else:
        print(num3," is 2nd largest number")
elif num3>num1 and num3>num2:
    if num1>num2:
        print(num1, " is 2nd largest number")
    else:
        print(num2," is second largest number")