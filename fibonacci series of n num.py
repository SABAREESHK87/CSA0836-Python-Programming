#program to find fibonacci series of given number#

a=int(input("enter the limit:"))
b,c=0,1
print("fibonacci series:",b,c,end=" ")
for j in range(2,a):
    d=b+c
    b=c
    c=d
    print(d,end=" ")

print()
