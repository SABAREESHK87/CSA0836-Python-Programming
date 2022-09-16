def peak(k,l):
    if(l==1):
        return 0
    if(k[0]>=k[1]):
        return 0
    if(k[l-1]>=k[l-2]):
        return n-1
    for i in range(1,l-1):
        if(k[i]>=k[i-1])and(k[i]>=k[i+1]):
            return k[i]

a=[]
b=int(input("enter the limit:"))
for i in range(0,b):
    c=int(input("enter the element:"))
    a.append(c)
print(a)
x=len(a)
print("peak value:",peak(a,x))
