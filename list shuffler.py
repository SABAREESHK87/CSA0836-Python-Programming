def shuffler(k,k1):
    k=list(set(k))
    k1=list(set(k1))
    k2=[]
    for i in k1:
        if i not in k:
            k2.append(i)
    for j in k:
        if j not in k1 and j not in k2:
            k2.append(j)
    k2.sort()
    return k2

a=[]
a1=int(input("enter the element limit of a:"))
for i in range(0,a1):
    a2=int(input("enter the element:"))
    a.append(a2)
print(a)
b=[]
b1=int(input("enter the element limit of b:"))
for k in range(0,b1):
    b2=int(input("enter the element:"))
    b.append(b2)
print(b)
print("shuffled output:",shuffler(a,b))
