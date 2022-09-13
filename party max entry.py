E=[]
L=[]
T=int(input("Range T:"))
for i in range(T):
    e=int(input("ENTRY:"))
    E.append(e)
for k in range(T):
    l=int(input("leave:"))
    L.append(l)
Sum=0
m=0
for i in range(T):
    Sum+=E[i]-L[i]
    m=max(Sum,m)
print("max members leaved in instance",m)
    
