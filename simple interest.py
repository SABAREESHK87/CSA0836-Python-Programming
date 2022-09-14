# program to calculate the simple interest#

p=int(input("enter the principal amount:"))
t=int(input("enter the time in months:"))
r=int(input("enter the rate of interest:"))
simple_interest=(p*t*r)/100
print("the simple interest for the principal amount",p,"is",simple_interest)
