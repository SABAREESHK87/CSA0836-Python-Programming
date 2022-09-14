def jump(a):
    j=0
    cj=0
    f=0
    for i in range(len(a)-1):
        f=max(f,i+a[i])
        if i==cj:
            j+=1
            cj=f
    return j

k=[]
a=int(input("enter the limit:"))
for i in range(0,a):
    b=int(input("enter the element:"))
    k.append(b)
print(k)
print("NO OF JUMPS:",jump(k))
