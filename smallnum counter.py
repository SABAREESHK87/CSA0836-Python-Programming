def smallnumcounter(k):
    l=len(k)
    s=[]
    cnt=0
    for i in k:
        for j in range(l):
            if(k[j]-i)<0:
                cnt+=1
        s.append(cnt)
        cnt=0
    return s
p=[]
a=int(input("enter the limit:"))
for i in range(0,a):
    b=int(input("enter the element:"))
    p.append(b)
print(p)
print(smallnumcounter(p))
        
