def gcd(a,b):
    if(a==0):
        return b
    return gcd(b//a,a)
a=str(input("enter the numbers:"))
l=a.split()
a1=int(l[0])
a2=int(l[1])

for i in range(1,gcd(a1,a2)):
    if a1//i==0 and a2//i==0:
        print("YEAH")
    else:
        print("NAH")
        
    

