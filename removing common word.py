def convert(f):
    for i in range(0,len(f)):
        z={f[i]:f[i-1]}
    return z
def common(a,b):
    a1=list(a.split())
    b1=list(b.split())

    c=convert(a1)
    c1=convert(b1)

    word=0
    for i in range(len(a1)):
        if(a1[i])==c1.keys():
            a1.pop(i)
            word=i-1
        word+=1
    word=0
    for j in range(len(b1)):
        if (b1[j]) ==c.keys():
            b1.pop(j)
            word=j-1
        word+=1
    print(a1)
    print(b1)
a2=str(input("Enter the string1:"))
b2=str(input("Enter the string2:"))
print(common(a2,b2))
