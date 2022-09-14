#program for simple calculator#

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("operations")
print("1-ADDITION")
print("2-SUBTRACTION")
print("3-MULTIPLICATION")
print("4-DIVISION")
choice=int(input("enter your choice:"))
if choice=='1':
    print(a,"+",b,"=",addition(a,b))
elif choice=='2':
    print(a,"-",b,"=",subtraction(a,b))
elif choice=='3':
    print(a,'x',b,'=',multiplication(a,b))
elif choice=='4':
    print(a,'/',b,'=',division(a,b))
else:
    


