#program to find factorial of the number#

a=int(input("enter the number:"))
fact =1
for k in range(1,a+1):
    fact=fact*k
print("the factorial of",a,"is:",fact)
