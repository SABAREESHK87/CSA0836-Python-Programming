a=str(input("enter the grade of the employee:"))
b=int(input("enter the salary of the employee:"))
b1=b*0.05
b2=b*0.10
b3=b*0.02
if(len(a)==1):
    if(a=='A')and(b<=10000):
        print("salary:",b)
        print("bonus:",b1+b3)
        print("total salary:",b+b1+b3)
    elif(a=='B')and(b<=10000):
        print("salary:",b)
        print("bonus:",b2+b3)
        print("total salary:",b+b2+b3)
    elif(a=='A'):
        print("salary:",b)
        print("bonus:",b1+b3)
        print("total salary:",b+b1)
    elif(a=='B'):
        print("salary:",b)
        print("bonus:",b2+b3)
        print("total salary:",b+b2)
