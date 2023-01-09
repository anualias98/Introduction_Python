# task 1
name=input("Enter your name:")
salary=int(input("Enter your salary:"))
years=int(input("Enter your experience:"))
if years > 5:
    bonus=salary+5/100
    print(name + " your salary is ",bonus)
else:
    print("your salary is ",salary)
