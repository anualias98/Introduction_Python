p1=int(input("Enter your age:"))
p2=int(input("Enter your age:"))
p3=int(input("Enter your age:"))
if p1>p2 & p1>p3:
    oldest=p1
elif p2>p3 & p2>p1:
      oldest=p2
elif p3>p1 & p3>p2:
      oldest=p3
if p1<p2 & p1<p3:
    youngest=p1
elif p2<p1 & p2<p3:
    youngest=p2
else:
    youngest=p3
    print(str(oldest) + " is oldest ")
    print(str(youngest) + " is youngest ")
